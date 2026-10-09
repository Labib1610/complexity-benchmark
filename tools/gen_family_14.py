#!/usr/bin/env python3
"""Seeded, deterministic input generators for family 14 (Steiner tree).

Usage:
    python tools/gen_family_14.py --criterion 1 --n 30 --t 8 --seed 4
    python tools/gen_family_14.py --criterion 2 --n 200000 --m 200000 --seed 3 --equal
    python tools/gen_family_14.py --criterion 3 --n 100000 --m 200000 --t 5 --seed 5 --at high
"""
import argparse
import random


# --- criterion 1: Steiner tree (fix t, grow n = grow optional relays) -----------
def gen_steiner(n, t, seed):
    """t required terminals (ids 1..t) and n-t optional relays. Relays GENUINELY help:
    several relays each offer near-tie cheap routing to all terminals (cheaper than
    connecting terminals directly), so the answer is not just the terminal MST and a
    baseline must enumerate subsets of the n-t relays (2^(n-t)) to find the best. The
    Dreyfus-Wagner reference is 3^t * n (t fixed small). Weights up to 1e6."""
    rng = random.Random(seed * 1_000_003 + 11)
    edges = []
    seen = set()

    def add(u, v, w):
        key = (min(u, v), max(u, v))
        if key not in seen:
            seen.add(key); edges.append((u, v, w))

    # expensive direct terminal-terminal edges (so relays win)
    for a in range(1, t + 1):
        for b in range(a + 1, t + 1):
            add(a, b, rng.randint(800, 1000))
    # several relays, each cheaply reaching all terminals with near-tie costs
    relays = list(range(t + 1, n + 1))
    for r in relays:
        base = rng.randint(30, 60)
        for a in range(1, t + 1):
            add(r, a, base + rng.randint(0, 8))     # near-tie: which relay is best is unclear
    # extra random relay-relay edges (noise / alternative routes)
    for _ in range(2 * len(relays)):
        if len(relays) >= 2:
            u = rng.choice(relays); v = rng.choice(relays)
            if u != v:
                add(u, v, rng.randint(1, 200))
    rng.shuffle(edges)
    lines = [f"{n} {len(edges)} {t}", " ".join(str(i) for i in range(1, t + 1))]
    lines += [f"{u} {v} {w}" for (u, v, w) in edges]
    return "\n".join(lines) + "\n"


# --- criterion 2: MST (connected graph) -----------------------------------------
def gen_tree_steiner(n, t, seed):
    """UNIFIED schema (audit B4): same as criterion 1 (n m t + required sites + weighted edges), but
    the cabling graph is a TREE (m = n-1). Steiner tree on a tree is polynomial (the minimal subtree
    spanning the required sites). t required sites are chosen at random."""
    rng = random.Random(seed * 2_000_003 + 7)
    edges = []
    for c in range(2, n + 1):
        p = rng.randint(1, c - 1)
        w = rng.randint(1, 1_000_000)
        edges.append((p, c, w))
    t = max(1, min(t, n))
    terminals = rng.sample(range(1, n + 1), t)
    rng.shuffle(edges)
    lines = [f"{n} {len(edges)} {t}"]
    lines.append(" ".join(map(str, terminals)))
    lines += [f"{u} {v} {w}" for (u, v, w) in edges]
    return "\n".join(lines) + "\n"


def gen_mst(n, m, seed, equal=False):
    """Connected weighted graph. equal=True -> all edges have the SAME weight (stress
    tie-breaking). Otherwise random weights. A random spanning tree guarantees
    connectivity, then extra random edges up to m."""
    rng = random.Random(seed * 2_000_003 + 7)
    edges = []
    seen = set()
    perm = list(range(1, n + 1)); rng.shuffle(perm)
    W = 7 if equal else None
    for i in range(1, n):                            # random spanning tree -> connected
        u = perm[i]; v = perm[rng.randint(0, i - 1)]
        w = W if equal else rng.randint(1, 1_000_000)
        seen.add((min(u, v), max(u, v))); edges.append((u, v, w))
    att = 0
    while len(edges) < m and att < 40 * m + 500:     # extra random edges
        att += 1
        u = rng.randint(1, n); v = rng.randint(1, n)
        if u == v:
            continue
        key = (min(u, v), max(u, v))
        if key in seen:
            continue
        w = W if equal else rng.randint(1, 1_000_000)
        seen.add(key); edges.append((u, v, w))
    rng.shuffle(edges)
    lines = [f"{n} {len(edges)}"]
    lines += [f"{u} {v} {w}" for (u, v, w) in edges]
    return "\n".join(lines) + "\n"


# --- criterion 3: an isolated required terminal ---------------------------------
def gen_isolated_terminal(n, m, t, seed, at="high"):
    """One required terminal has degree 0 (no cabling option touches it). The answer is
    the smallest such required id. at='high' places it at a high id."""
    rng = random.Random(seed * 3_000_003 + 5)
    if at == "high":
        iso = n                                       # isolated required site at high id
    elif at == "low":
        iso = 1
    else:
        iso = int(at)
    # terminals: iso plus t-1 others (all != iso, since iso is isolated)
    pool = [x for x in range(1, n + 1) if x != iso]
    rng.shuffle(pool)
    terminals = sorted([iso] + pool[:t - 1])
    others = [x for x in range(1, n + 1) if x != iso]
    seen = set(); edges = []
    for i in range(len(others) - 1):                  # connect the non-isolated sites
        u, v = others[i], others[i + 1]
        e = (min(u, v), max(u, v)); seen.add(e); edges.append((u, v, rng.randint(1, 1_000_000)))
    att = 0
    while len(edges) < m and att < 20 * m + 500:
        att += 1
        u = rng.choice(others); v = rng.choice(others)
        if u == v:
            continue
        e = (min(u, v), max(u, v))
        if e in seen:
            continue
        seen.add(e); edges.append((u, v, rng.randint(1, 1_000_000)))
    rng.shuffle(edges)
    lines = [f"{n} {len(edges)} {t}", " ".join(map(str, terminals))]
    lines += [f"{u} {v} {w}" for (u, v, w) in edges]
    return "\n".join(lines) + "\n"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--criterion", type=int, required=True, choices=[1, 2, 3])
    p.add_argument("--n", type=int, required=True)
    p.add_argument("--m", type=int, default=0)
    p.add_argument("--t", type=int, default=8)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--equal", action="store_true")
    p.add_argument("--at", default="high")
    args = p.parse_args()

    if args.criterion == 1:
        out = gen_steiner(args.n, args.t, args.seed)
    elif args.criterion == 2:
        # audit B4: unified schema (n m t + terminals) with a tree-graph promise (Steiner on a tree).
        out = gen_tree_steiner(args.n, args.t, args.seed)
    else:
        out = gen_isolated_terminal(args.n, args.m, args.t, args.seed, at=args.at)

    import sys
    sys.stdout.write(out)


if __name__ == "__main__":
    main()
