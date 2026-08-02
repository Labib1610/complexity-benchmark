#!/usr/bin/env python3
"""Seeded, deterministic input generators for family 03 (Hamiltonian path / routing).

Usage:
    python tools/gen_family_03.py --criterion 1 --n 16 --m 60 --seed 4 --path no
    python tools/gen_family_03.py --criterion 2 --n 100000 --seed 3 --unique yes
    python tools/gen_family_03.py --criterion 3 --n 100000 --m 200000 --seed 5 --iso high

Output is stdout in the exact format each statement specifies (1-indexed vertices).
"""
import argparse
import random


# --- criterion 1: Hamiltonian path (undirected) -----------------------------
def gen_ham(n, m, seed, has_path=None):
    """General undirected graph.

    has_path=False -> a DENSE, well-connected graph with NO Hamiltonian path:
        an unbalanced complete-ish bipartition (parts differ by >=2, so no Ham path
        exists) with many cross edges. Naive DFS backtracking explores an enormous
        number of alternating partial paths before failing -- the expensive case.
    has_path=True  -> plant a Hamiltonian path over a random permutation, plus extra
        random edges. Guaranteed YES.
    has_path=None  -> plain random G(n, m).
    """
    rng = random.Random(seed * 1_000_003 + 17)
    max_edges = n * (n - 1) // 2
    m = min(m, max_edges) if m else 0

    if has_path is False:
        # unbalanced bipartition: smaller side a, larger side b = n-a, with b-a >= 2
        a = (n - 2) // 2
        if a < 1:
            a = 1
        verts = list(range(1, n + 1))
        rng.shuffle(verts)
        A = set(verts[:a])
        B = set(verts[a:])                       # |B| - |A| >= 2  -> no Hamiltonian path
        cross = [(u, v) for u in A for v in B]
        rng.shuffle(cross)
        cap = len(cross)
        want = min(m if m else cap, cap)         # default: take all cross edges (densest)
        edges = cross[:want]

    elif has_path is True:
        perm = list(range(1, n + 1))
        rng.shuffle(perm)
        seen = set()
        edges = []
        for i in range(n - 1):
            u, v = perm[i], perm[i + 1]
            e = (min(u, v), max(u, v))
            seen.add(e); edges.append(e)         # the planted Hamiltonian path
        # extra random edges up to m
        want = min(m if m else len(edges), max_edges)
        attempts = 0
        while len(edges) < want and attempts < 60 * want + 500:
            attempts += 1
            u = rng.randint(1, n); v = rng.randint(1, n)
            if u == v:
                continue
            e = (min(u, v), max(u, v))
            if e in seen:
                continue
            seen.add(e); edges.append(e)

    else:
        seen = set(); edges = []
        attempts = 0
        want = min(m, max_edges)
        while len(edges) < want and attempts < 60 * want + 500:
            attempts += 1
            u = rng.randint(1, n); v = rng.randint(1, n)
            if u == v:
                continue
            e = (min(u, v), max(u, v))
            if e in seen:
                continue
            seen.add(e); edges.append(e)

    edges = [(min(u, v), max(u, v)) for (u, v) in edges]
    rng.shuffle(edges)
    lines = [f"{n} {len(edges)}"]
    lines += [f"{u} {v}" for (u, v) in edges]
    return "\n".join(lines) + "\n"


# --- criterion 2: unique topological order (DAG) ----------------------------
def gen_dag_unique(n, seed, unique=True, ratio=2):
    """Directed acyclic graph.

    unique=True  -> a UNIQUE topological order that is also a Hamiltonian path:
        pick a random permutation p; add the chain p[0]->p[1]->...->p[n-1] (forces the
        order and connects consecutive pairs) plus extra forward edges p[i]->p[j] (i<j).
        Kahn sees exactly one in-degree-0 vertex at every step -> YES, order = p.
    unique=False -> NOT uniquely ordered: drop one chain link so two vertices are
        simultaneously in-degree-0 at some step -> Kahn reports NO.
    All edges go forward in p, so the graph is acyclic by construction.
    """
    rng = random.Random(seed * 2_000_003 + 7)
    p = list(range(1, n + 1))
    rng.shuffle(p)
    pos = {v: i for i, v in enumerate(p)}
    seen = set()
    edges = []
    # chain
    for i in range(n - 1):
        e = (p[i], p[i + 1]); seen.add(e); edges.append(e)
    if not unique and n >= 3:
        # remove a middle chain link -> p[k] and p[k+1] both become sources later,
        # breaking uniqueness (two in-degree-0 at once) -> NO
        k = rng.randint(0, n - 2)
        drop = (p[k], p[k + 1])
        edges = [e for e in edges if e != drop]
        seen.discard(drop)
    # extra forward edges up to ratio*n, capped at the statement's m bound (2e5)
    want = min(ratio * n, n * (n - 1) // 2, 200_000)
    attempts = 0
    while len(edges) < want and attempts < 60 * want + 500:
        attempts += 1
        i = rng.randint(0, n - 1); j = rng.randint(0, n - 1)
        if i >= j:
            continue
        e = (p[i], p[j])                          # always forward in p -> acyclic
        if e in seen:
            continue
        seen.add(e); edges.append(e)
    rng.shuffle(edges)
    lines = [f"{n} {len(edges)}"]
    lines += [f"{u} {v}" for (u, v) in edges]
    return "\n".join(lines) + "\n"


# --- criterion 3: planted isolated vertex -----------------------------------
def gen_isolated(n, m, seed, iso="high", iso2=-1):
    """Undirected graph with planted degree-0 vertex/vertices; every other vertex has
    >=1 edge. The answer is the SMALLEST isolated index.

    iso='high' -> isolated vertex at index n (a scan-from-1 solution must go all the
                  way to the end; a report-first-nonsmallest solution fails).
    iso='low'  -> isolated vertex at index 1.
    iso=<int>  -> isolated at that index.
    iso2=<int> -> plant a SECOND isolated vertex here (>0). With two isolated vertices
                  the correct answer is min(iso_at, iso2), so a solution that returns
                  a non-smallest isolated vertex (e.g. the last one found) is wrong.
    """
    rng = random.Random(seed * 3_000_003 + 5)
    if iso == "high":
        iso_at = n
    elif iso == "low":
        iso_at = 1
    else:
        iso_at = int(iso)
    isolated = {iso_at}
    if iso2 and iso2 > 0:
        isolated.add(int(iso2))
    others = [v for v in range(1, n + 1) if v not in isolated]
    # connect the others as a random path first (guarantees every other vertex has an
    # edge and the non-isolated part is one connected component), then add random edges.
    rng.shuffle(others)
    seen = set(); edges = []
    for i in range(len(others) - 1):
        u, v = others[i], others[i + 1]
        e = (min(u, v), max(u, v)); seen.add(e); edges.append(e)
    max_edges = (n - 1) * (n - 2) // 2            # among the non-isolated vertices
    want = min(m, max_edges)
    attempts = 0
    while len(edges) < want and attempts < 20 * want + 500:
        attempts += 1
        u = rng.choice(others); v = rng.choice(others)
        if u == v:
            continue
        e = (min(u, v), max(u, v))
        if e in seen:
            continue
        seen.add(e); edges.append(e)
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
    p.add_argument("--path", default="")           # criterion 1: yes / no / (blank=random)
    p.add_argument("--unique", default="yes")       # criterion 2: yes / no
    p.add_argument("--iso", default="high")         # criterion 3: high / low / <int>
    p.add_argument("--iso2", type=int, default=-1)   # criterion 3: optional 2nd isolated vertex
    args = p.parse_args()

    if args.criterion == 1:
        hp = {"yes": True, "no": False, "": None}[args.path]
        out = gen_ham(args.n, args.m, args.seed, has_path=hp)
    elif args.criterion == 2:
        out = gen_dag_unique(args.n, args.seed,
                             unique=(args.unique.lower() in ("yes", "y", "true", "1")))
    else:
        out = gen_isolated(args.n, args.m, args.seed, iso=args.iso, iso2=args.iso2)

    import sys
    sys.stdout.write(out)


if __name__ == "__main__":
    main()
