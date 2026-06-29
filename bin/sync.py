#!/usr/bin/env python3
"""
Minimal sync server for the Sociognosis Editor.

Serves static files from the root directory inferred from the data file
and persists JSON sync POST requests to that data file.

Usage:

    python sync.py \
        --data-file docs/data/index/data.json

In the editor's Settings → "Backend Sync" → "Backend Save URL", enter:

    http://localhost:8000/api/graph/save
"""

import argparse
import json
import os
import sys
import tempfile
import time
from functools import partial
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

SAVE_ENDPOINT = "/api/graph/save"
HEALTH_ENDPOINT = "/api/health"
LAYOUT_RECOMPUTE_ENDPOINT = "/api/layout/recompute"


class SyncHandler(SimpleHTTPRequestHandler):
    """Serves static files and handles graph save requests."""

    data_file = None

    # ------------------------------------------------------------------
    # CORS
    # ------------------------------------------------------------------

    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header(
            "Access-Control-Allow-Methods",
            "GET, POST, OPTIONS",
        )
        self.send_header(
            "Access-Control-Allow-Headers",
            "Content-Type",
        )
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(204)
        self.end_headers()

    # ------------------------------------------------------------------
    # GET
    # ------------------------------------------------------------------

    def do_GET(self):
        path = self.path.split("?", 1)[0]

        if path == HEALTH_ENDPOINT:
            self._handle_health()
            return

        super().do_GET()

    def _handle_health(self):
        exists = self.data_file.exists()

        self._send_json(
            {
                "status": "ok",
                "service": "sociognosis-sync",
                "data_file": str(self.data_file),
                "data_file_exists": exists,
                "data_file_size": (
                    self.data_file.stat().st_size
                    if exists
                    else None
                ),
            }
        )

    # ------------------------------------------------------------------
    # POST
    # ------------------------------------------------------------------

    def do_POST(self):
        path = self.path.split("?", 1)[0]

        if path == SAVE_ENDPOINT:
            self._handle_save()
        elif path == LAYOUT_RECOMPUTE_ENDPOINT:
            self._handle_layout_recompute()
        else:
            self.send_error(404, "Not Found")

    def _handle_save(self):
        try:
            length = int(self.headers.get("Content-Length", 0))
            raw = self.rfile.read(length) if length else b"{}"

            patch = json.loads(raw)
            changed = patch.get("nodes", [])

            if not changed:
                self._send_json({"status": "ok", "saved": 0})
                return

            with open(self.data_file, "r", encoding="utf-8") as fh:
                data = json.load(fh)

            id_index = {
                node["id"]: i
                for i, node in enumerate(data)
                if isinstance(node, dict) and "id" in node
            }

            saved = 0

            for node in changed:
                if not isinstance(node, dict):
                    continue

                node_id = node.get("id")
                if not node_id:
                    continue

                if node_id in id_index:
                    data[id_index[node_id]] = node
                else:
                    id_index[node_id] = len(data)
                    data.append(node)

                saved += 1

            self.data_file.parent.mkdir(
                parents=True,
                exist_ok=True,
            )

            tmp_fd, tmp_path = tempfile.mkstemp(
                suffix=".tmp",
                dir=str(self.data_file.parent),
            )

            try:
                with os.fdopen(
                    tmp_fd,
                    "w",
                    encoding="utf-8",
                ) as fh:
                    json.dump(
                        data,
                        fh,
                        indent=2,
                        ensure_ascii=False,
                    )

                os.replace(tmp_path, self.data_file)
                os.chmod(self.data_file, 0o644) # Only the owner to write (usually safer).

            except Exception:
                try:
                    os.unlink(tmp_path)
                except OSError:
                    pass
                raise

            self._send_json(
                {
                    "status": "ok",
                    "saved": saved,
                    "timestamp": patch.get(
                        "timestamp",
                        "",
                    ),
                }
            )

        except json.JSONDecodeError as exc:
            self._send_json(
                {
                    "status": "error",
                    "message": f"Invalid JSON: {exc}",
                },
                400,
            )

        except Exception as exc:
            self._send_json(
                {
                    "status": "error",
                    "message": str(exc),
                },
                500,
            )

    # ------------------------------------------------------------------
    # Layout recompute endpoint (on demand from the editor)
    # ------------------------------------------------------------------

    def _handle_layout_recompute(self):
        """POST /api/layout/recompute -> regenerate layout.json now.

        Decoupled from save so saves stay fast; the editor calls this
        explicitly (e.g. its "Recompute Layout" button)."""
        try:
            result = self._recompute_layout()
            if "layout_error" in result:
                self._send_json(
                    {"status": "error", "message": result["layout_error"]},
                    500,
                )
            else:
                self._send_json({"status": "ok", **result})
        except Exception as exc:  # pragma: no cover - defensive
            self._send_json(
                {"status": "error", "message": str(exc)},
                500,
            )

    # ------------------------------------------------------------------
    # Layout recompute (triggered after every successful save)
    # ------------------------------------------------------------------

    def _recompute_layout(self):
        """Recompute layout.json (sibling of data file) via bin/layout.py.

        Best-effort: a layout failure is reported, not raised. Returns a dict
        consumed by the save/recompute response handlers.
        """
        layout_file = self.data_file.parent / "layout.json"
        try:
            bin_dir = os.path.dirname(os.path.abspath(__file__))
            if bin_dir not in sys.path:
                sys.path.insert(0, bin_dir)
            import layout as layout_mod  # noqa: E402

            node_count, elapsed = layout_mod.recompute(
                self.data_file,
                layout_file,
            )
            sys.stderr.write(
                f"[sync] layout recomputed: {node_count} nodes "
                f"in {elapsed * 1000:.0f} ms -> {layout_file}\n"
            )
            return {
                "layout": "recomputed",
                "layout_nodes": node_count,
                "layout_ms": int(elapsed * 1000),
            }
        except Exception as exc:  # pragma: no cover - defensive
            sys.stderr.write(f"[sync] layout recompute failed: {exc}\n")
            return {"layout_error": str(exc)}

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    def _send_json(self, obj, code=200):
        body = json.dumps(obj).encode("utf-8")

        self.send_response(code)
        self.send_header(
            "Content-Type",
            "application/json",
        )
        self.send_header(
            "Content-Length",
            str(len(body)),
        )
        self.end_headers()

        self.wfile.write(body)

    def log_message(self, fmt, *args):
        sys.stderr.write(
            f"[sync] {self.address_string()} - {fmt % args}\n"
        )


def main():
    parser = argparse.ArgumentParser(
        prog="sync.py",
        description=(
            "Minimal sync server for the Sociognosis Editor."
        ),
    )

    parser.add_argument(
        "--data-file",
        required=True,
        help="Path to the graph JSON file.",
    )

    parser.add_argument(
        "-p",
        "--port",
        type=int,
        default=8000,
        help="Port to listen on (default: 8000).",
    )

    parser.add_argument(
        "--host",
        default="0.0.0.0",
        help="Host/interface to bind (default: 0.0.0.0).",
    )

    args = parser.parse_args()

    data_file = Path(args.data_file).resolve()

    if not data_file.exists():
        print(
            f"WARNING: data file not found: {data_file}",
            file=sys.stderr,
        )

    # docs/data/index/data.json -> docs/
    root_dir = data_file.parents[2]

    SyncHandler.data_file = data_file

    handler = partial(
        SyncHandler,
        directory=str(root_dir),
    )

    server = HTTPServer(
        (args.host, args.port),
        handler,
    )

    display_host = (
        "localhost"
        if args.host in ("0.0.0.0", "::")
        else args.host
    )

    print("══════════════════════════════════════════════")
    print("  Sociognosis Sync Server")
    print("──────────────────────────────────────────────")
    print(
        f"  Save:    http://{display_host}:{args.port}{SAVE_ENDPOINT}"
    )
    print(
        f"  Layout:  http://{display_host}:{args.port}{LAYOUT_RECOMPUTE_ENDPOINT}"
    )
    print(
        f"  Health:  http://{display_host}:{args.port}{HEALTH_ENDPOINT}"
    )
    print("══════════════════════════════════════════════")
    print()

    try:
        server.serve_forever()

    except KeyboardInterrupt:
        print("\nShutting down...")
        server.shutdown()


if __name__ == "__main__":
    main()