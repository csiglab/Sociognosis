#!/usr/bin/env python3
"""
Minimal sync server for the Sociognosis Editor.

A single instance serves every dataset found under the docs root
(one directory per dataset under <docs-root>/data/, e.g. prd and idx),
exposes a small graph API, and persists nodes to a CouchDB database
(one document per node). A mirror copy of each dataset is also written
to disk so the read-only viewers (index.html) keep working.

API (all same origin):

    GET  /api/graph?dataset=prd      -> nodes array for a dataset
    POST /api/graph/save             -> upsert {nodes:[...], dataset} into CouchDB
    POST /api/layout/recompute       -> regenerate layout.json (?dataset= optional)
    GET  /api/health                 -> service + CouchDB status

Usage:

    # Serves both docs/prd/edit.html and docs/idx/edit.html from one server:
    python sync.py \
        --docs-root docs \
        --couch-url http://localhost:5984 \
        --couch-db sociognosis

    # Legacy single-dataset mode still works:
    python sync.py --data-file docs/data/prd/data.json

In the editor's Settings -> "Backend Sync" -> "Backend Save URL", enter:

    http://localhost:8000/api/graph/save
"""

import argparse
import base64
import json
import os
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
from functools import partial
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

SAVE_ENDPOINT = "/api/graph/save"
LOAD_ENDPOINT = "/api/graph"
HEALTH_ENDPOINT = "/api/health"
LAYOUT_RECOMPUTE_ENDPOINT = "/api/layout/recompute"


class CouchError(Exception):
    """Raised on CouchDB HTTP failures; carries the status code and body."""

    def __init__(self, status, body):
        super().__init__(f"CouchDB HTTP {status}: {body!r}")
        self.status = status
        self.body = body


class CouchClient:
    """Minimal stdlib-only CouchDB client (one dataset <-> many node docs).

    Each graph node is stored as its own CouchDB document. Because a single
    CouchDB database may hold several datasets (e.g. 'prd' and 'idx'), document
    ids are namespaced: '{dataset}:{node_id}'. The node's logical 'id' field is
    preserved verbatim inside each document.
    """

    def __init__(self, base_url, db, user=None, password=None, timeout=30):
        self.base_url = base_url.rstrip("/")
        self.db = db
        self.timeout = timeout
        self._auth = None
        if user and password:
            token = base64.b64encode(
                f"{user}:{password}".encode("utf-8")
            ).decode("ascii")
            self._auth = "Basic " + token

    # ------------------------------------------------------------------
    # Low-level transport
    # ------------------------------------------------------------------
    def _request(self, method, url, body=None):
        data = None
        headers = {"Accept": "application/json"}
        if self._auth:
            headers["Authorization"] = self._auth
        if body is not None:
            data = json.dumps(body).encode("utf-8")
            headers["Content-Type"] = "application/json"

        req = urllib.request.Request(
            url,
            data=data,
            method=method,
            headers=headers,
        )
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                raw = resp.read()
                return json.loads(raw.decode("utf-8")) if raw else None
        except urllib.error.HTTPError as exc:
            raise CouchError(exc.code, exc.read())
        except urllib.error.URLError as exc:
            raise CouchError(0, str(exc).encode("utf-8"))

    # ------------------------------------------------------------------
    # Database lifecycle
    # ------------------------------------------------------------------
    def db_info(self):
        return self._request("GET", f"{self.base_url}/{self.db}")

    def ensure_db(self):
        """Create the database if it does not exist. Returns True if created."""
        url = f"{self.base_url}/{self.db}"
        try:
            self._request("GET", url)
            return False
        except CouchError as exc:
            if exc.status != 404:
                raise
            self._request("PUT", url)
            return True

    # ------------------------------------------------------------------
    # Dataset read / write
    # ------------------------------------------------------------------
    def get_dataset(self, dataset):
        """Return all node docs for a dataset as a list (node fields only)."""
        startkey = urllib.parse.quote(json.dumps(f"{dataset}:"))
        endkey = urllib.parse.quote(json.dumps(f"{dataset}:\ufff0"))
        url = (
            f"{self.base_url}/{self.db}/_all_docs"
            f"?include_docs=true&startkey={startkey}&endkey={endkey}"
        )
        result = self._request("GET", url)
        nodes = []
        for row in result.get("rows", []):
            doc = row.get("doc")
            if not doc:
                continue
            if str(doc.get("_id", "")).startswith("_design"):
                continue
            doc.pop("_rev", None)
            doc.pop("_id", None)
            nodes.append(doc)
        return nodes

    def _revs(self, dataset, ids):
        """Map 'dataset:node_id' -> current CouchDB rev (for clean upserts)."""
        if not ids:
            return {}
        keys = [f"{dataset}:{i}" for i in ids]
        url = f"{self.base_url}/{self.db}/_all_docs"
        result = self._request("POST", url, {"keys": keys})
        revs = {}
        for row in result.get("rows", []):
            key = row.get("key")
            value = row.get("value") or {}
            if key and value.get("rev"):
                revs[key] = value["rev"]
        return revs

    def bulk_upsert(self, dataset, nodes):
        """Upsert a list of node dicts. Returns the number written."""
        valid = [n for n in nodes if isinstance(n, dict) and n.get("id")]
        if not valid:
            return 0

        revs = self._revs(dataset, [n["id"] for n in valid])

        docs = []
        for node in valid:
            doc = dict(node)  # keeps the node's logical 'id' field verbatim
            couch_id = f"{dataset}:{node['id']}"
            doc["_id"] = couch_id
            if couch_id in revs:
                doc["_rev"] = revs[couch_id]
            docs.append(doc)

        url = f"{self.base_url}/{self.db}/_bulk_docs"
        outcomes = self._request("POST", url, {"docs": docs})

        saved = 0
        for res in outcomes:
            if res.get("ok"):
                saved += 1
        return saved


class SyncHandler(SimpleHTTPRequestHandler):
    """Serves static files and handles graph sync requests.

    A single instance serves every dataset discovered under the docs root
    (one directory per dataset under <docs-root>/data/). Each dataset is
    mirrored to its own data.json so the read-only viewers keep working.
    """

    couch = None                  # CouchClient
    datasets = None               # {dataset_name: Path(data.json)}

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
        params = {}
        if "?" in self.path:
            params = urllib.parse.parse_qs(self.path.split("?", 1)[1])

        if path == HEALTH_ENDPOINT:
            self._handle_health()
            return

        if path == LOAD_ENDPOINT:
            self._handle_graph(params)
            return

        super().do_GET()

    def _default_dataset(self):
        names = sorted(self.datasets or {})
        return names[0] if names else None

    def _handle_graph(self, params):
        """GET /api/graph?dataset=prd|idx -> nodes array from CouchDB."""
        dataset = (params.get("dataset") or [self._default_dataset()])[0]
        if not dataset:
            self._send_json(
                {"status": "error", "message": "No datasets configured."},
                500,
            )
            return
        try:
            nodes = self.couch.get_dataset(dataset)
            self._send_json(nodes)
        except CouchError as exc:
            sys.stderr.write(f"[sync] couch read error: {exc}\n")
            self._send_json(
                {
                    "status": "error",
                    "message": f"CouchDB: {exc}",
                    "dataset": dataset,
                },
                502,
            )

    def _handle_health(self):
        couch_ok = False
        couch_info = None
        try:
            couch_info = self.couch.db_info()
            couch_ok = True
        except Exception as exc:
            couch_info = {"error": str(exc)}

        datasets_info = {}
        for name, path in (self.datasets or {}).items():
            datasets_info[name] = {
                "data_file": str(path),
                "exists": path.exists(),
                "size": path.stat().st_size if path.exists() else None,
            }

        self._send_json(
            {
                "status": "ok" if couch_ok else "degraded",
                "service": "sociognosis-sync",
                "datasets": datasets_info,
                "couchdb": {
                    "url": f"{self.couch.base_url}/{self.couch.db}",
                    "ok": couch_ok,
                    "info": couch_info,
                },
            }
        )

    # ------------------------------------------------------------------
    # POST
    # ------------------------------------------------------------------

    def do_POST(self):
        path = self.path.split("?", 1)[0]
        params = {}
        if "?" in self.path:
            params = urllib.parse.parse_qs(self.path.split("?", 1)[1])

        if path == SAVE_ENDPOINT:
            self._handle_save()
        elif path == LAYOUT_RECOMPUTE_ENDPOINT:
            self._handle_layout_recompute(params)
        else:
            self.send_error(404, "Not Found")

    def _handle_save(self):
        try:
            length = int(self.headers.get("Content-Length", 0))
            raw = self.rfile.read(length) if length else b"{}"

            patch = json.loads(raw)
            changed = patch.get("nodes", [])
            dataset = patch.get("dataset") or self._default_dataset()

            if not changed:
                self._send_json(
                    {"status": "ok", "saved": 0, "dataset": dataset}
                )
                return

            saved = self.couch.bulk_upsert(dataset, changed)

            # Mirror the full dataset to disk so the read-only viewers
            # (index.html) keep working off the static data.json.
            mirrored = False
            data_file = (self.datasets or {}).get(dataset)
            if data_file:
                full = self.couch.get_dataset(dataset)
                self._write_data_file(full, data_file)
                mirrored = True
            else:
                sys.stderr.write(
                    f"[sync] no on-disk mirror for dataset '{dataset}'; "
                    f"saved to CouchDB only.\n"
                )

            self._send_json(
                {
                    "status": "ok",
                    "saved": saved,
                    "timestamp": patch.get("timestamp", ""),
                    "dataset": dataset,
                    "mirrored": mirrored,
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

        except CouchError as exc:
            sys.stderr.write(f"[sync] couch write error: {exc}\n")
            self._send_json(
                {
                    "status": "error",
                    "message": f"CouchDB: {exc}",
                },
                502,
            )

        except Exception as exc:
            self._send_json(
                {
                    "status": "error",
                    "message": str(exc),
                },
                500,
            )

    def _write_data_file(self, data, data_file):
        """Atomically write the full node list to the on-disk mirror."""
        data_file.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        tmp_fd, tmp_path = tempfile.mkstemp(
            suffix=".tmp",
            dir=str(data_file.parent),
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

                os.replace(tmp_path, data_file)
                os.chmod(data_file, 0o644)  # Owner-writable (safer default).

        except Exception:
            try:
                os.unlink(tmp_path)
            except OSError:
                pass
            raise

    # ------------------------------------------------------------------
    # Layout recompute endpoint (on demand from the editor)
    # ------------------------------------------------------------------

    def _handle_layout_recompute(self, params):
        """POST /api/layout/recompute?dataset=prd|idx -> regenerate layout.json.

        If no dataset is given, every known dataset is recomputed. Decoupled
        from save so saves stay fast; the editor calls this explicitly (e.g. its
        "Recompute Layout" button). Datasets without a usable layout are skipped.
        """
        try:
            requested = (params.get("dataset") or [None])[0]
            targets = (
                [requested]
                if requested
                else sorted(self.datasets or {})
            )

            results = {}
            had_error = False
            for name in targets:
                data_file = (self.datasets or {}).get(name)
                if not data_file or not data_file.exists():
                    continue
                res = self._recompute_layout(data_file)
                results[name] = res
                if "layout_error" in res:
                    had_error = True

            status = "error" if had_error else "ok"
            code = 500 if had_error else 200
            self._send_json({"status": status, "datasets": results}, code)
        except Exception as exc:  # pragma: no cover - defensive
            self._send_json(
                {"status": "error", "message": str(exc)},
                500,
            )

    # ------------------------------------------------------------------
    # Layout recompute helper
    # ------------------------------------------------------------------

    def _recompute_layout(self, data_file):
        """Recompute layout.json (sibling of data file) via bin/layout.py.

        Best-effort: a layout failure is reported, not raised. Returns a dict
        consumed by the recompute response handler.
        """
        layout_file = data_file.parent / "layout.json"
        try:
            bin_dir = os.path.dirname(os.path.abspath(__file__))
            if bin_dir not in sys.path:
                sys.path.insert(0, bin_dir)
            import layout as layout_mod  # noqa: E402

            node_count, elapsed = layout_mod.recompute(
                data_file,
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


def maybe_bootstrap(couch, dataset, data_file):
    """Seed CouchDB for a dataset from the on-disk data file if it is empty.

    Lets the editor read through the API immediately, without a manual import
    step, the first time sync.py is pointed at a fresh database.
    """
    try:
        existing = couch.get_dataset(dataset)
    except CouchError as exc:
        sys.stderr.write(
            f"[sync] cannot read dataset '{dataset}' from CouchDB: {exc}\n"
        )
        return

    if existing:
        return

    if not data_file.exists():
        return

    try:
        with open(data_file, "r", encoding="utf-8") as fh:
            seed = json.load(fh)
    except Exception as exc:
        sys.stderr.write(
            f"[sync] cannot read seed file {data_file}: {exc}\n"
        )
        return

    if not isinstance(seed, list):
        return

    nodes = [n for n in seed if isinstance(n, dict) and n.get("id")]
    if not nodes:
        return

    written = couch.bulk_upsert(dataset, nodes)
    sys.stderr.write(
        f"[sync] bootstrapped {written} nodes from {data_file} "
        f"into '{couch.db}:{dataset}'\n"
    )


def discover_datasets(docs_root):
    """Return {dataset_name: Path(data.json)} for <docs_root>/data/*/data.json."""
    docs_root = Path(docs_root)
    data_dir = docs_root / "data"
    datasets = {}
    if data_dir.is_dir():
        for path in sorted(data_dir.glob("*/data.json")):
            datasets[path.parent.name] = path.resolve()
    return datasets


def main():
    parser = argparse.ArgumentParser(
        prog="sync.py",
        description=(
            "Sync server for the Sociognosis Editor. Serves every dataset "
            "under <docs-root>/data/ from a single instance."
        ),
    )

    parser.add_argument(
        "--docs-root",
        default=None,
        help=(
            "Directory served statically and parent of data/<dataset>/. "
            "Defaults to the repo 'docs' dir (or derived from --data-file)."
        ),
    )

    parser.add_argument(
        "--data-file",
        default=None,
        help=(
            "Optional legacy path to a single dataset's data.json. Used to "
            "derive --docs-root; modern usage prefers --docs-root."
        ),
    )

    parser.add_argument(
        "-p",
        "--port",
        type=int,
        default=8001,
        help="Port to listen on (default: 8001).",
    )

    parser.add_argument(
        "--host",
        default="0.0.0.0",
        help="Host/interface to bind (default: 0.0.0.0).",
    )

    parser.add_argument(
        "--couch-url",
        default="http://localhost:5984",
        help="CouchDB base URL (default: http://localhost:5984).",
    )

    parser.add_argument(
        "--couch-db",
        default="sociognosis",
        help="CouchDB database name (default: sociognosis).",
    )

    parser.add_argument(
        "--couch-user",
        default=None,
        help="CouchDB user (optional).",
    )

    parser.add_argument(
        "--couch-password",
        default=None,
        help="CouchDB password (optional).",
    )

    args = parser.parse_args()

    # Resolve the docs root (the static-serving directory).
    if args.docs_root:
        docs_root = Path(args.docs_root).resolve()
    elif args.data_file:
        # docs/data/<dataset>/data.json -> docs
        docs_root = Path(args.data_file).resolve().parents[2]
    else:
        # Default: <repo>/docs (bin/ is a sibling of docs/).
        docs_root = (Path(__file__).resolve().parent.parent / "docs").resolve()

    if not docs_root.is_dir():
        print(
            f"ERROR: docs root not found: {docs_root}",
            file=sys.stderr,
        )
        sys.exit(1)

    datasets = discover_datasets(docs_root)

    # Legacy --data-file: make sure that specific dataset is included even if
    # it lives outside the discovered tree.
    if args.data_file:
        df = Path(args.data_file).resolve()
        datasets.setdefault(df.parent.name, df)

    if not datasets:
        print(
            f"WARNING: no datasets found under {docs_root}/data/*/data.json",
            file=sys.stderr,
        )

    couch = CouchClient(
        args.couch_url,
        args.couch_db,
        user=args.couch_user,
        password=args.couch_password,
    )

    try:
        created = couch.ensure_db()
        if created:
            print(
                f"[sync] created CouchDB database '{args.couch_db}'",
                file=sys.stderr,
            )
    except CouchError as exc:
        print(
            f"ERROR: cannot reach CouchDB at {args.couch_url}: {exc}",
            file=sys.stderr,
        )
        sys.exit(1)

    for name, data_file in datasets.items():
        maybe_bootstrap(couch, name, data_file)

    SyncHandler.couch = couch
    SyncHandler.datasets = datasets

    handler = partial(
        SyncHandler,
        directory=str(docs_root),
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

    ds_list = ", ".join(sorted(datasets)) or "(none)"

    print("══════════════════════════════════════════════")
    print("  Sociognosis Sync Server")
    print("──────────────────────────────────────────────")
    print(f"  Datasets: {ds_list}  (CouchDB: {args.couch_db})")
    print(f"  Root:     {docs_root}")
    for name in sorted(datasets):
        print(
            f"  Load:    http://{display_host}:{args.port}{LOAD_ENDPOINT}?dataset={name}"
        )
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
