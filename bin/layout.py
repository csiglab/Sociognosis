#!/usr/bin/env python3
"""
Sociognosis graph layout pre-computer (Python port).

Produces layout.json : { "<id>": [x, y], ... }

The sociogenesis graph is overwhelmingly DISCONNECTED (isolated nodes plus a
small number of tiny connected components), so a global O(N^2) force simulation
is both expensive and pointless. Instead:

  1. Place every node on a sunflower (phyllotaxis) spiral -> even, dense,
     overlap-free fill, O(N), deterministic.
  2. For each connected component (size >= 2), run a tiny Fruchterman-Reingold
     layout in a local subspace and anchor it at the centroid of the
     component's spiral slot, so each small cluster reads as a unit without
     disturbing the global packing.

Usage:
    python bin/layout.py \\
        --data-file docs/data/idx/data.json \\
        --layout-file docs/data/idx/layout.json

Defaults resolve relative to the repository root (parent of bin/).
"""

import argparse
import json
import math
import os
import random
import sys
import tempfile
from pathlib import Path

GOLDEN_ANGLE = math.pi * (3.0 - math.sqrt(5.0))

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DATA = ROOT / "docs" / "data" / "idx" / "data.json"
DEFAULT_LAYOUT = ROOT / "docs" / "data" / "idx" / "layout.json"

SPACING = 60.0  # approximate nearest-neighbour distance on the spiral


def load_data(path):
    with open(path, "r", encoding="utf-8") as fh:
        data = json.load(fh)
    if not isinstance(data, list):
        raise ValueError(f"{path} is not a JSON array")
    return data


def build_edges(data, id_set):
    """Undirected edge list from relationships, restricted to ids that exist."""
    edges = []
    for d in data:
        s = d.get("id") if isinstance(d, dict) else None
        if s not in id_set:
            continue
        for r in d.get("relationships") or []:
            if not isinstance(r, dict):
                continue
            t = r.get("targetNodeId")
            if t and t in id_set and t != s:
                edges.append((s, t))
    return edges


def components_of(ids, edges, id_index):
    """Union-find over ids -> list of components (each a list of ids)."""
    parent = list(range(len(ids)))

    def find(x):
        root = x
        while parent[root] != root:
            root = parent[root]
        while parent[x] != root:
            parent[x], x = root, parent[x]
        return root

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb

    for s, t in edges:
        union(id_index[s], id_index[t])

    groups = {}
    for i in range(len(ids)):
        groups.setdefault(find(i), []).append(ids[i])
    return list(groups.values())


def sunflower(i, n, radius):
    r = radius * math.sqrt((i + 0.5) / n)
    theta = i * GOLDEN_ANGLE
    return (r * math.cos(theta), r * math.sin(theta))


def fr_layout(members, edge_pairs, iters, width, height, rng):
    """Fruchterman-Reingold on a small set of points. Fine for tiny components."""
    m = len(members)
    k = math.sqrt((width * height) / max(1, m)) * 0.6
    pos = [[rng.uniform(-w2, w2) for w2 in (width / 2, height / 2)] for _ in range(m)]
    temp = width * 0.25
    for _ in range(iters):
        disp = [[0.0, 0.0] for _ in range(m)]
        for i in range(m):
            xi, yi = pos[i]
            for j in range(i + 1, m):
                dx = xi - pos[j][0]
                dy = yi - pos[j][1]
                d2 = dx * dx + dy * dy
                if d2 < 1e-6:
                    dx = rng.uniform(-1e-3, 1e-3)
                    dy = rng.uniform(-1e-3, 1e-3)
                    d2 = dx * dx + dy * dy
                d = math.sqrt(d2)
                f = (k * k) / d
                disp[i][0] += (dx / d) * f
                disp[i][1] += (dy / d) * f
                disp[j][0] -= (dx / d) * f
                disp[j][1] -= (dy / d) * f
        for a, b in edge_pairs:
            dx = pos[a][0] - pos[b][0]
            dy = pos[a][1] - pos[b][1]
            d = max(1e-6, math.sqrt(dx * dx + dy * dy))
            f = (d * d) / k
            disp[a][0] -= (dx / d) * f
            disp[a][1] -= (dy / d) * f
            disp[b][0] += (dx / d) * f
            disp[b][1] += (dy / d) * f
        for i in range(m):
            dx, dy = disp[i]
            d = max(1e-6, math.sqrt(dx * dx + dy * dy))
            lim = min(d, temp)
            pos[i][0] += (dx / d) * lim
            pos[i][1] += (dy / d) * lim
        temp = max(1e-3, temp * 0.96)
    return pos


def compute_layout(data):
    """Return {id: [x, y]} for every node in data."""
    ids = []
    id_index = {}
    seen = set()
    for d in data:
        if not isinstance(d, dict):
            continue
        nid = d.get("id")
        if not nid or nid in seen:
            continue
        seen.add(nid)
        id_index[nid] = len(ids)
        ids.append(nid)

    n = len(ids)
    if n == 0:
        return {}

    edges = build_edges(data, seen)

    # Adjacency for fast component BFS is unnecessary: union-find already gives
    # components. Re-derive per-component edge index pairs from the global list.
    comps = components_of(ids, edges, id_index)

    disk_radius = SPACING * math.sqrt(n / math.pi)
    out = {}

    # 1. Base positions: sunflower spiral for every node (overlap-free, even).
    base = [sunflower(i, n, disk_radius) for i in range(n)]

    # 2. Tighten connected components locally.
    rng = random.Random(123456789)
    for comp in comps:
        if len(comp) < 2:
            continue
        local_idx = {nid: k for k, nid in enumerate(comp)}
        members = comp
        size = len(members)
        comp_set = set(comp)
        edge_pairs = []
        for s, t in edges:
            if s in comp_set and t in comp_set:
                edge_pairs.append((local_idx[s], local_idx[t]))

        local_span = max(40.0, SPACING * 0.9 * math.sqrt(size))
        pos = fr_layout(members, edge_pairs, 350, local_span, local_span, rng)

        # Anchor at the centroid of the component's spiral slots.
        cx = sum(base[id_index[nid]][0] for nid in members) / size
        cy = sum(base[id_index[nid]][1] for nid in members) / size

        # Scale local coords to a footprint smaller than SPACING so the cluster
        # stays tight at its slot without invading neighbours.
        max_r = max((math.hypot(p[0], p[1]) for p in pos), default=0.0)
        target_r = min(SPACING * 0.45, local_span / 2)
        scale = (target_r / max_r) if max_r > 1e-6 else 1.0

        for k, nid in enumerate(members):
            out[nid] = [cx + pos[k][0] * scale, cy + pos[k][1] * scale]

    # 3. Isolated nodes keep their sunflower slot.
    for i, nid in enumerate(ids):
        if nid not in out:
            out[nid] = [base[i][0], base[i][1]]

    return out


def write_layout_atomically(layout, layout_path):
    """Write layout.json atomically (temp file + os.replace), mirroring sync.py."""
    layout_path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_path = tempfile.mkstemp(suffix=".tmp", dir=str(layout_path.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            json.dump(layout, fh, ensure_ascii=False, separators=(",", ":"))
        os.replace(tmp_path, layout_path)
        os.chmod(layout_path, 0o644)
    except Exception:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise


def recompute(data_file, layout_file):
    """Load data_file, compute layout, write layout_file atomically.

    Returns (node_count, elapsed_seconds). Used by sync.py after each save.
    """
    import time

    start = time.time()
    data = load_data(data_file)
    layout = compute_layout(data)
    write_layout_atomically(layout, Path(layout_file))
    return len(layout), time.time() - start


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="layout.py",
        description="Pre-compute Sociognosis graph layout (sunflower + per-component FR).",
    )
    parser.add_argument("--data-file", default=str(DEFAULT_DATA), help="Path to data.json.")
    parser.add_argument(
        "--layout-file",
        default=str(DEFAULT_LAYOUT),
        help="Path to write layout.json (default: sibling of data file).",
    )
    args = parser.parse_args(argv)

    data_file = Path(args.data_file).resolve()
    layout_file = Path(args.layout_file).resolve()

    node_count, elapsed = recompute(data_file, layout_file)
    size_kb = layout_file.stat().st_size / 1024
    print(
        f"layout: {node_count} nodes -> {layout_file} "
        f"({size_kb:.1f} KB) in {elapsed * 1000:.0f} ms",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
