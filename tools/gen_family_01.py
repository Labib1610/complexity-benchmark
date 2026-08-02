#!/usr/bin/env python3
"""Seeded, deterministic input generators for family 01 (graph coloring / shifts).

Usage:
    python tools/gen_family_01.py --criterion 1 --n 26 --seed 7 --mode hard
    python tools/gen_family_01.py --criterion 2 --n 100000 --m 200000 --seed 3 --sat yes
    python tools/gen_family_01.py --criterion 3 --n 2000 --m 200000 --seed 5 --plant high

All output goes to stdout in the exact format each statement specifies
(1-indexed vertices, no self-loops, no duplicate edges).
"""
import argparse
import random


def _rand_edges(n, m, rng, forbid=None, allowed_pair=None, k4_free=False):
    """Return up to m distinct undirected edges (u<v) over vertices 1..n.

    forbid: optional set of vertices that must not appear in any edge.
    allowed_pair: optional predicate(u, v) -> bool restricting which edges are allowed.
    k4_free: if True, reject any edge that would complete a 4-clique (K4). This keeps
             refutation of NO instances search-based (no trivial 4-clique witness).
    """
    forbid = forbid or set()
    verts = [v for v in range(1, n + 1) if v not in forbid]
    max_edges = len(verts) * (len(verts) - 1) // 2
    m = min(m, max_edges)
    adj = {v: set() for v in verts}
    seen = set()
    out = []

    def completes_k4(u, v):
        # adding (u,v) completes a K4 iff u and v share two common neighbours a,b
        # that are themselves adjacent (then {u,v,a,b} is a 4-clique).
        common = adj[u] & adj[v]
        for a in common:
            if adj[a] & common:      # some b in common adjacent to a
                return True
        return False

    # Rejection sampling is fine while the graph is sparse (our target ratios are).
    attempts = 0
    limit = 50 * m + 1000
    while len(out) < m and attempts < limit:
        attempts += 1
        u = rng.choice(verts)
        v = rng.choice(verts)
        if u == v:
            continue
        if u > v:
            u, v = v, u
        if (u, v) in seen:
            continue
        if allowed_pair is not None and not allowed_pair(u, v):
            continue
        if k4_free and completes_k4(u, v):
            continue
        seen.add((u, v))
        adj[u].add(v)
        adj[v].add(u)
        out.append((u, v))
    return out


def gen_3col(n, seed, mode="hard", ratio=None, k4_free=False):
    """Criterion 1: n workers, m conflict pairs. Format: 'n m' then m lines 'u v'.

    mode='hard'   -> random graph at edge ratio m/n ~ 2.35 (the random 3-coloring
                     phase transition), where instances force deep backtracking.
    mode='random' -> sparser Erdos-Renyi (ratio ~1.5), usually easily colorable.
    ratio         -> override the edge/vertex ratio (e.g. 2.33 for a hard instance
                     just below the phase transition, favouring a hard YES).
    k4_free       -> forbid any 4-clique, so a NO instance cannot be refuted by
                     spotting a trivial K4 -- refutation must be search-based.
    """
    rng = random.Random(seed * 1_000_003 + 11)
    if ratio is None:
        if mode == "hard":
            ratio = 2.35
        elif mode == "random":
            ratio = 1.5
        else:
            raise ValueError(f"unknown mode {mode!r}")
    m = round(ratio * n)
    edges = _rand_edges(n, m, rng, k4_free=k4_free)
    lines = [f"{n} {len(edges)}"]
    lines += [f"{u} {v}" for (u, v) in edges]
    return "\n".join(lines) + "\n"


def gen_2col(n, m, seed, satisfiable=True, components=1):
    """Criterion 2: large graph for 2-coloring.

    satisfiable=True  -> genuinely bipartite: split vertices into two sides and add
                         only cross-side edges (odd-cycle free -> YES).
    satisfiable=False -> same, plus a planted triangle (odd cycle) -> NO.
    components>1      -> partition the vertices into that many disjoint bipartite
                         blocks (tests per-component lex-smallest handling).
    """
    rng = random.Random(seed * 2_000_003 + 7)
    # Partition vertices into `components` contiguous blocks; within each block
    # split into side A / side B. Build cross-side edges directly per component
    # (no global rejection sampling, so this scales to n, m ~ 2e5).
    block_size = max(2, n // components)
    comp_A = {}
    comp_B = {}
    comp_ids = []
    for v in range(1, n + 1):
        c = min((v - 1) // block_size, components - 1)
        if c not in comp_A:
            comp_A[c] = []
            comp_B[c] = []
            comp_ids.append(c)
        (comp_A if rng.randint(0, 1) == 0 else comp_B)[c].append(v)

    caps = []
    for c in comp_ids:
        caps.append(len(comp_A[c]) * len(comp_B[c]))
    total_cap = sum(caps) or 1

    # Reserve 3 slots for the planted triangle when building an unsatisfiable
    # instance, so the total edge count never exceeds the requested m.
    budget = m - (0 if satisfiable else 3)
    edges = []
    seen = set()
    for c, cap in zip(comp_ids, caps):
        if cap == 0 or len(edges) >= budget:
            continue
        target = min(cap, round(m * cap / total_cap), budget - len(edges))
        A, B = comp_A[c], comp_B[c]
        got = 0
        attempts = 0
        limit = 20 * target + 50
        while got < target and attempts < limit:
            attempts += 1
            u = rng.choice(A)
            v = rng.choice(B)
            if u > v:
                u, v = v, u
            if (u, v) in seen:
                continue
            seen.add((u, v))
            edges.append((u, v))
            got += 1

    if not satisfiable:
        # Plant a triangle 1-2-3 (odd cycle) to force a NO regardless of the rest.
        for (u, v) in [(1, 2), (2, 3), (1, 3)]:
            if (u, v) not in seen:
                seen.add((u, v))
                edges.append((u, v))

    rng.shuffle(edges)
    lines = [f"{n} {len(edges)}"]
    lines += [f"{u} {v}" for (u, v) in edges]
    return "\n".join(lines) + "\n"


def gen_triangle(n, m, seed, plant="low"):
    """Criterion 3: graph guaranteed to contain exactly one triangle.

    The base graph is bipartite (hence triangle-free); the planted trio are isolated
    from the base (their only edges are the three triangle edges), so the planted
    triangle is the unique -- and therefore lexicographically smallest -- triangle.

    plant='low'  -> triangle at low indices (e.g. near 1 2 3).
    plant='high' -> triangle at high indices, so a solution that prints the first
                    triangle it stumbles on (not the smallest) still finds it, but a
                    correct solution must confirm it is the smallest.
    """
    rng = random.Random(seed * 3_000_003 + 5)
    if plant == "low":
        a, b, c = 1, 2, 3
    elif plant == "high":
        a, b, c = n - 2, n - 1, n
    else:
        raise ValueError(f"unknown plant {plant!r}")
    trio = {a, b, c}

    # Bipartite base over the remaining vertices (triangle-free).
    side = [rng.randint(0, 1) for _ in range(n + 1)]

    def cross_ok(u, v):
        return side[u] != side[v]

    base = _rand_edges(n, m - 3, rng, forbid=trio, allowed_pair=cross_ok)
    edges = base + [(a, b), (a, c), (b, c)]
    rng.shuffle(edges)
    lines = [f"{n} {len(edges)}"]
    lines += [f"{u} {v}" for (u, v) in edges]
    return "\n".join(lines) + "\n"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--criterion", type=int, required=True, choices=[1, 2, 3])
    p.add_argument("--n", type=int, required=True)
    p.add_argument("--m", type=int, default=0)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--mode", default="hard")            # criterion 1
    p.add_argument("--ratio", type=float, default=None)  # criterion 1: override m/n
    p.add_argument("--k4free", action="store_true")      # criterion 1: forbid 4-cliques
    p.add_argument("--sat", default="yes")              # criterion 2: yes/no
    p.add_argument("--components", type=int, default=1)  # criterion 2
    p.add_argument("--plant", default="low")            # criterion 3: low/high
    args = p.parse_args()

    if args.criterion == 1:
        out = gen_3col(args.n, args.seed, mode=args.mode, ratio=args.ratio, k4_free=args.k4free)
    elif args.criterion == 2:
        out = gen_2col(args.n, args.m, args.seed,
                       satisfiable=(args.sat.lower() in ("yes", "y", "true", "1")),
                       components=args.components)
    else:
        out = gen_triangle(args.n, args.m, args.seed, plant=args.plant)

    import sys
    sys.stdout.write(out)


if __name__ == "__main__":
    main()
