#!/usr/bin/env python3
"""Seeded, deterministic input generators for family 10 (dominating set).

Usage:
    python tools/gen_family_10.py --criterion 1 --k 12 --seed 4 --dominatable yes
    python tools/gen_family_10.py --criterion 2 --n 200000 --seed 3 --shape path
    python tools/gen_family_10.py --criterion 3 --n 100000 --m 200000 --seed 5 --at high
"""
import argparse
import random


# --- criterion 1: dominating set decision (B&B vs C(n,k) subsets) ---------------
def gen_domset(k, seed, dominatable=True, pad=0):
    """Disjoint P3 paths (leaf - center - leaf). A P3 has a UNIQUE minimum dominating
    set of size 1 (its center, which dominates all three); so t disjoint P3s have a
    unique minimum dominating set of size t (all centers). Centers get the HIGHEST
    indices, so the C(n,k) subset baseline reaches the one good set last.

    dominatable=True  -> t=k P3s, budget k: feasible (YES), unique DS = the k centers.
    dominatable=False -> t=k+1 P3s, budget k: infeasible (NO), forces exhaustive search.
    """
    rng = random.Random(seed * 1_000_003 + 11)
    t = k if dominatable else k + 1
    n = 2 * t + t + pad                     # 2t leaves + t centers + padding
    leaves = list(range(1, 2 * t + 1))
    centers = list(range(2 * t + pad + 1, 2 * t + pad + t + 1))
    edges = []
    for i in range(t):
        c = centers[i]
        edges.append((leaves[2 * i], c))
        edges.append((leaves[2 * i + 1], c))
    rng.shuffle(edges)
    lines = [f"{n} {len(edges)} {k}"]
    lines += [f"{u} {v}" for (u, v) in edges]
    return "\n".join(lines) + "\n"


# --- criterion 2: rooted tree (parent list) -------------------------------------
def gen_tree(n, seed, shape="path"):
    """Rooted tree on n nodes (root = 1), printed as n-1 'child parent' links.
    shape: path (deep -> recursive DFS hits the recursion limit), star, balanced
    (complete binary), random."""
    rng = random.Random(seed * 2_000_003 + 7)
    parent = [0] * (n + 1)
    if shape == "path":
        for c in range(2, n + 1):
            parent[c] = c - 1
    elif shape == "star":
        for c in range(2, n + 1):
            parent[c] = 1
    elif shape == "balanced":
        for c in range(2, n + 1):
            parent[c] = c // 2
    else:  # random: each node's parent is a random earlier node
        for c in range(2, n + 1):
            parent[c] = rng.randint(1, c - 1)
    lines = [str(n)]
    lines += [f"{c} {parent[c]}" for c in range(2, n + 1)]
    return "\n".join(lines) + "\n"


# --- criterion 3: isolated location, budget k=0 ---------------------------------
def gen_isolated_k0(n, m, seed, at="high"):
    """General graph with a planted degree-0 location; budget k=0. Every other
    location has an edge, so the isolated one is the unique (smallest) answer.
    at='high' -> isolated at index n; 'low' -> 1; <int> -> that index."""
    rng = random.Random(seed * 3_000_003 + 5)
    if at == "high":
        iso = n
    elif at == "low":
        iso = 1
    else:
        iso = int(at)
    others = [v for v in range(1, n + 1) if v != iso]
    rng.shuffle(others)
    seen = set(); edges = []
    for i in range(len(others) - 1):           # a random path over the others
        u, v = others[i], others[i + 1]
        e = (min(u, v), max(u, v)); seen.add(e); edges.append(e)
    att = 0
    while len(edges) < m and att < 20 * m + 500:
        att += 1
        u = rng.choice(others); v = rng.choice(others)
        if u == v:
            continue
        e = (min(u, v), max(u, v))
        if e in seen:
            continue
        seen.add(e); edges.append(e)
    rng.shuffle(edges)
    lines = [f"{n} {len(edges)} 0"]
    lines += [f"{u} {v}" for (u, v) in edges]
    return "\n".join(lines) + "\n"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--criterion", type=int, required=True, choices=[1, 2, 3])
    p.add_argument("--k", type=int, default=0)
    p.add_argument("--n", type=int, default=0)
    p.add_argument("--m", type=int, default=0)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--dominatable", default="yes")
    p.add_argument("--pad", type=int, default=0)
    p.add_argument("--shape", default="path")
    p.add_argument("--at", default="high")
    args = p.parse_args()

    if args.criterion == 1:
        out = gen_domset(args.k, args.seed,
                         dominatable=(args.dominatable.lower() in ("yes", "y", "1", "true")), pad=args.pad)
    elif args.criterion == 2:
        out = gen_tree(args.n, args.seed, shape=args.shape)
    else:
        out = gen_isolated_k0(args.n, args.m, args.seed, at=args.at)

    import sys
    sys.stdout.write(out)


if __name__ == "__main__":
    main()
