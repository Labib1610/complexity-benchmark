#!/usr/bin/env python3
"""Seeded, deterministic input generators for family 09 (clique / independent set).

Usage:
    python tools/gen_family_09.py --criterion 1 --n 40 --k 13 --seed 4 --has_clique yes
    python tools/gen_family_09.py --criterion 2 --nA 600 --seed 3 --mode hard
    python tools/gen_family_09.py --criterion 3 --n 30 --m 200 --seed 5
"""
import argparse
import random


# --- criterion 1: k-clique decision (B&B vs C(n,k) subsets) ---------------------
def gen_clique(n, k, seed, p=0.5, has_clique=True):
    """Random graph G(n, p). has_clique=True plants a k-clique on the HIGHEST-indexed
    vertices (so the C(n,k) subset baseline, iterating lexicographically, reaches the
    one good group last), keeping k above the ~2*log2(n) natural max clique so the
    planted clique is the only one. has_clique=False leaves it random at p=0.5 with k
    just above the max clique -> NO, forcing exhaustive refutation."""
    rng = random.Random(seed * 1_000_003 + 11)
    adj = [[False] * (n + 1) for _ in range(n + 1)]
    edges = []

    def add(u, v):
        if not adj[u][v]:
            adj[u][v] = adj[v][u] = True
            edges.append((u, v))

    clique_verts = set(range(n - k + 1, n + 1)) if has_clique else set()
    for u in range(1, n + 1):
        for v in range(u + 1, n + 1):
            if u in clique_verts and v in clique_verts:
                add(u, v)                      # planted clique edge
            elif rng.random() < p:
                add(u, v)
    rng.shuffle(edges)
    lines = [f"{n} {len(edges)} {k}"]
    lines += [f"{u} {v}" for (u, v) in edges]
    return "\n".join(lines) + "\n"


# --- criterion 2: bipartite independent set = (nA+nB) - max matching ------------
def gen_bipartite_is(nA, nB, m, seed, mode="hard"):
    """mode='hard' -> lower-triangular staircase (A-user i connects to B-users 1..i),
    forcing Kuhn's O(V*E) long augmenting chains while Hopcroft-Karp stays O(E*sqrt V).
    mode='empty' -> no edges (independent set = nA+nB). mode='random' -> random edges."""
    rng = random.Random(seed * 2_000_003 + 7)
    edges = []
    if mode == "hard":
        for a in range(1, nA + 1):
            for b in range(1, a + 1):
                if b <= nB:
                    edges.append((a, b))
        rng.shuffle(edges)
    elif mode == "empty":
        edges = []
    else:
        seen = set(); want = min(m, nA * nB); att = 0
        while len(edges) < want and att < 40 * want + 500:
            att += 1
            e = (rng.randint(1, nA), rng.randint(1, nB))
            if e in seen:
                continue
            seen.add(e); edges.append(e)
    lines = [f"{nA} {nB} {len(edges)}"]
    lines += [f"{a} {b}" for (a, b) in edges]
    return "\n".join(lines) + "\n"


# --- criterion 3: oversized request (r > n) -------------------------------------
def gen_oversize_request(n, m, seed):
    """Random dense graph on n users, request r = n + 1 (> n, so the answer is NO).
    A baseline that searches subsets for an r-clique (ignoring the pigeonhole) explores
    exponentially and TLEs; the reference is O(1)."""
    rng = random.Random(seed * 3_000_003 + 5)
    r = n + 1
    seen = set(); edges = []
    want = min(m, n * (n - 1) // 2)
    att = 0
    while len(edges) < want and att < 40 * want + 500:
        att += 1
        u = rng.randint(1, n); v = rng.randint(1, n)
        if u == v:
            continue
        e = (min(u, v), max(u, v))
        if e in seen:
            continue
        seen.add(e); edges.append(e)
    rng.shuffle(edges)
    lines = [f"{n} {len(edges)} {r}"]
    lines += [f"{u} {v}" for (u, v) in edges]
    return "\n".join(lines) + "\n"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--criterion", type=int, required=True, choices=[1, 2, 3])
    p.add_argument("--n", type=int, default=0)
    p.add_argument("--k", type=int, default=0)
    p.add_argument("--m", type=int, default=0)
    p.add_argument("--nA", type=int, default=0)
    p.add_argument("--nB", type=int, default=0)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--p", type=float, default=0.5)
    p.add_argument("--has_clique", default="yes")
    p.add_argument("--mode", default="hard")
    args = p.parse_args()

    if args.criterion == 1:
        out = gen_clique(args.n, args.k, args.seed, p=args.p,
                         has_clique=(args.has_clique.lower() in ("yes", "y", "1", "true")))
    elif args.criterion == 2:
        out = gen_bipartite_is(args.nA, args.nB, args.m, args.seed, mode=args.mode)
    else:
        out = gen_oversize_request(args.n, args.m, args.seed)

    import sys
    sys.stdout.write(out)


if __name__ == "__main__":
    main()
