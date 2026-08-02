#!/usr/bin/env python3
"""Seeded, deterministic input generators for family 08 (vertex cover).

Usage:
    python tools/gen_family_08.py --criterion 1 --k 12 --seed 4 --coverable yes
    python tools/gen_family_08.py --criterion 2 --nA 600 --seed 3 --mode hard
    python tools/gen_family_08.py --criterion 3 --n 100000 --m 200000 --k 25 --seed 5
"""
import argparse
import random


# --- criterion 1: vertex cover decision (2^k branching vs C(n,k) subsets) -------
def gen_vc(k, seed, coverable=True, pad=0):
    """A graph built from disjoint P3 paths (leaf - center - leaf). Each P3 has a
    UNIQUE minimum cover of size 1 (its center), so a graph of t disjoint P3s has a
    unique minimum vertex cover of size t (all the centers). The centers are given the
    HIGHEST indices, so the C(n,k) subset baseline (iterating combinations in
    lexicographic order) reaches the one good cover last and must enumerate almost
    everything, while the 2^k bounded-search reference finds it quickly.

    coverable=True  -> t=k P3s, budget k: feasible (YES), unique cover = the k centers.
    coverable=False -> t=k+1 P3s, budget k: infeasible (NO), forces exhaustive search.
    pad -> extra isolated junctions (inflate n -> larger C(n,k), slower baseline).
    """
    rng = random.Random(seed * 1_000_003 + 11)
    t = k if coverable else k + 1
    n = 2 * t + t + pad                     # 2t leaves + t centers + padding
    leaves = list(range(1, 2 * t + 1))
    centers = list(range(2 * t + pad + 1, 2 * t + pad + t + 1))  # highest indices
    edges = []
    for i in range(t):
        c = centers[i]
        edges.append((leaves[2 * i], c))
        edges.append((leaves[2 * i + 1], c))
    rng.shuffle(edges)
    lines = [f"{n} {len(edges)} {k}"]
    lines += [f"{u} {v}" for (u, v) in edges]
    return "\n".join(lines) + "\n"


# --- criterion 2: bipartite vertex cover = max matching (König) -----------------
def gen_bipartite_vc(nA, nB, m, seed, mode="hard"):
    """mode='hard' -> a lower-triangular 'staircase' (west i connects to east 1..i):
    forces Kuhn's augmenting-path matcher into long chains ~O(V*E) while Hopcroft-Karp
    stays O(E*sqrt V). mode='random' -> random bipartite edges."""
    rng = random.Random(seed * 2_000_003 + 7)
    edges = []
    if mode == "hard":
        for a in range(1, nA + 1):
            for b in range(1, a + 1):
                if b <= nB:
                    edges.append((a, b))
        rng.shuffle(edges)
    else:
        seen = set()
        want = min(m, nA * nB)
        att = 0
        while len(edges) < want and att < 40 * want + 500:
            att += 1
            e = (rng.randint(1, nA), rng.randint(1, nB))
            if e in seen:
                continue
            seen.add(e); edges.append(e)
    lines = [f"{nA} {nB} {len(edges)}"]
    lines += [f"{a} {b}" for (a, b) in edges]
    return "\n".join(lines) + "\n"


# --- criterion 3: too many corridors (planted large matching) -------------------
def gen_big_matching(n, m, k, seed):
    """A graph with a planted matching of at least k+1 disjoint edges (so no cover of
    size k exists), padded with extra random edges up to m. The reference greedily
    collects k+1 disjoint edges in O(m); a baseline that first searches for a size-k
    cover (2^k bounded search) TLEs."""
    rng = random.Random(seed * 3_000_003 + 5)
    edges = []
    seen = set()
    # planted matching: (1,2),(3,4),...  -> at least k+1 disjoint edges
    need = k + 1
    for i in range(need):
        u = 2 * i + 1; v = 2 * i + 2
        if v > n:
            break
        edges.append((u, v)); seen.add((u, v))
    # extra random edges up to m
    att = 0
    while len(edges) < m and att < 40 * m + 500:
        att += 1
        u = rng.randint(1, n); v = rng.randint(1, n)
        if u == v:
            continue
        e = (min(u, v), max(u, v))
        if e in seen:
            continue
        seen.add(e); edges.append(e)
    rng.shuffle(edges)
    lines = [f"{n} {len(edges)} {k}"]
    lines += [f"{u} {v}" for (u, v) in edges]
    return "\n".join(lines) + "\n"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--criterion", type=int, required=True, choices=[1, 2, 3])
    p.add_argument("--k", type=int, default=0)
    p.add_argument("--n", type=int, default=0)
    p.add_argument("--m", type=int, default=0)
    p.add_argument("--nA", type=int, default=0)
    p.add_argument("--nB", type=int, default=0)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--coverable", default="yes")
    p.add_argument("--pad", type=int, default=0)
    p.add_argument("--mode", default="hard")
    args = p.parse_args()

    if args.criterion == 1:
        out = gen_vc(args.k, args.seed,
                     coverable=(args.coverable.lower() in ("yes", "y", "1", "true")), pad=args.pad)
    elif args.criterion == 2:
        out = gen_bipartite_vc(args.nA, args.nB, args.m, args.seed, mode=args.mode)
    else:
        out = gen_big_matching(args.n, args.m, args.k, args.seed)

    import sys
    sys.stdout.write(out)


if __name__ == "__main__":
    main()
