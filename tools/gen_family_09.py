#!/usr/bin/env python3
"""Seeded, deterministic input generators for family 09 (independent set).

REBUILT per the audit (MD files/COMPLEXITY_BENCHMARK_AUDIT.md), blockers B4/B5/B6:

  * The family is UNIFIED on one task -- INDEPENDENT SET (decide whether a set of exactly k
    pairwise-non-adjacent vertices exists, and report one) -- with ONE input schema across all three
    criteria (audit B4). Previously criterion 1 was clique, criterion 2 was maximum independent set
    on a bipartite graph (a different task/output), and criterion 3 was a clique decision. The one
    documented switch between A and B is now the graph class: general (NPC) vs bipartite (P).
  * Criterion 3 (INFEASIBLE) is REDESIGNED as an infeasibility-CERTIFICATE task (B5): every instance
    has no independent set of size k for a checkable reason (k > n, or the graph is complete so the
    max independent set is 1), and the model must output the certificate, not a constant "NO".
  * Every case computes its ground truth here and uses a distinct seed, so k is always correct and
    no inputs collide (B6).

Unified schema (all three): line 1 = "n m k", then m lines "u v" (1-based, u != v).

Usage:
    python tools/gen_family_09.py --criterion 1 --n 40 --seed 4 --kind no
    python tools/gen_family_09.py --criterion 2 --n 400 --seed 3 --kind yes
    python tools/gen_family_09.py --criterion 3 --n 30 --seed 5 --kind complete
"""
import argparse
import random
import sys


def _popcount(x):
    return bin(x).count("1")


def _max_clique_size(n, adjbits):
    """Max clique size in a bitset graph (n <= ~46) via branch-and-bound."""
    best = 0

    def expand(Rsize, P):
        nonlocal best
        if P == 0:
            if Rsize > best:
                best = Rsize
            return
        if Rsize + _popcount(P) <= best:
            return
        Pp = P
        while Pp:
            if Rsize + _popcount(P) <= best:
                return
            v = (Pp & -Pp).bit_length() - 1
            Pp &= Pp - 1
            P &= ~(1 << v)
            expand(Rsize + 1, P & adjbits[v])

    expand(0, (1 << n) - 1)
    return best


def _complement_adj(n, edges):
    """Bitset adjacency of the COMPLEMENT graph (max clique here == max independent set in G)."""
    full = [((1 << n) - 1) ^ (1 << i) for i in range(n)]  # everyone except self
    adjG = [0] * n
    for (u, v) in edges:
        adjG[u - 1] |= (1 << (v - 1))
        adjG[v - 1] |= (1 << (u - 1))
    return [full[i] & ~adjG[i] for i in range(n)]


def _max_independent_set_size(n, edges):
    return _max_clique_size(n, _complement_adj(n, edges))


def _emit(n, edges, k):
    lines = [f"{n} {len(edges)} {k}"]
    lines += [f"{u} {v}" for (u, v) in edges]
    return "\n".join(lines) + "\n"


# --- criterion 1: independent set in a GENERAL graph (NPC) -----------------------
def gen_is_general(n, seed, kind):
    """Random graph. kind='no' uses a dense graph (small max IS) and sets k = maxIS+1 -> no IS of
    size k (exhaustive refutation). kind='yes' plants an independent set on the highest-indexed
    vertices (found last by a C(n,k) subset baseline) and sets k = the true max IS. Ground truth is
    computed by branch-and-bound on the complement, so k is always correct."""
    rng = random.Random(seed * 1_000_003 + 11)
    if kind == "yes":
        t = max(2, n // 3)                     # planted independent-set size
        planted = set(range(n - t + 1, n + 1))
        edges = []
        for u in range(1, n + 1):
            for v in range(u + 1, n + 1):
                if u in planted and v in planted:
                    continue                   # no edge inside the planted IS
                if rng.random() < 0.65:        # dense elsewhere -> max IS stays == t
                    edges.append((u, v))
        rng.shuffle(edges)
        k = _max_independent_set_size(n, edges)
        return _emit(n, edges, k)
    # kind == 'no': dense random graph, k = maxIS + 1
    edges = []
    for u in range(1, n + 1):
        for v in range(u + 1, n + 1):
            if rng.random() < 0.72:
                edges.append((u, v))
    rng.shuffle(edges)
    k = _max_independent_set_size(n, edges) + 1
    return _emit(n, edges, k)


# --- criterion 2: independent set in a BIPARTITE graph (P) -----------------------
def _bip_max_is(nA, nB, adjA):
    """Max IS size of a bipartite graph via Hopcroft-Karp: (nA+nB) - maxMatching (König)."""
    from collections import deque
    INF = float("inf")
    pair_u = [0] * (nA + 1); pair_v = [0] * (nB + 1); dist = [0] * (nA + 1)

    def bfs():
        q = deque()
        for u in range(1, nA + 1):
            if pair_u[u] == 0:
                dist[u] = 0; q.append(u)
            else:
                dist[u] = INF
        found = False
        while q:
            u = q.popleft()
            for v in adjA[u]:
                w = pair_v[v]
                if w == 0:
                    found = True
                elif dist[w] == INF:
                    dist[w] = dist[u] + 1; q.append(w)
        return found

    def dfs(u):
        for v in adjA[u]:
            w = pair_v[v]
            if w == 0 or (dist[w] == dist[u] + 1 and dfs(w)):
                pair_u[u] = v; pair_v[v] = u; return True
        dist[u] = INF; return False

    matching = 0
    while bfs():
        for u in range(1, nA + 1):
            if pair_u[u] == 0 and dfs(u):
                matching += 1
    return (nA + nB) - matching


def gen_is_bipartite(n, seed, kind):
    """Bipartite graph on vertices 1..n split into side A = 1..a and side B = a+1..n, with random
    cross edges. Emitted in the unified schema (the solver 2-colors to recover the bipartition).
    kind='yes' -> k = max IS; kind='no' -> k = max IS + 1."""
    rng = random.Random(seed * 2_000_003 + 7)
    a = max(1, n // 2)
    b = n - a
    edges = []
    adjA = [[] for _ in range(a + 1)]
    seen = set()
    # Keep the graph sparse and within the statement's m <= 400000 bound: a few edges per vertex,
    # which is enough to force a non-trivial matching (so max IS < n) while staying near-linear.
    target_m = min(400_000, a * b, 3 * n + 5)
    att = 0
    while len(edges) < target_m and att < 40 * target_m + 500:
        att += 1
        ua = rng.randint(1, a); vb = rng.randint(1, b)
        if (ua, vb) in seen:
            continue
        seen.add((ua, vb))
        adjA[ua].append(vb)
        edges.append((ua, a + vb))             # global numbering for side B
    max_is = _bip_max_is(a, b, adjA)
    k = max_is if kind == "yes" else max_is + 1
    rng.shuffle(edges)
    return _emit(n, edges, k)


# --- criterion 3: INFEASIBLE independent set with a checkable certificate --------
def gen_infeasible_certificate(n, seed, kind):
    """kind='size' -> k > n (cannot pick k distinct vertices). Certificate: `SIZE`.
       kind='complete' -> the graph is complete (K_n), so the max IS is 1; with k>=2 no IS of size k
       exists. Certificate: `COMPLETE`."""
    rng = random.Random(seed * 3_000_003 + 5)
    if kind == "size":
        # a sparse random graph, but ask for more vertices than exist
        edges = []
        seen = set()
        target_m = min(2 * n, n * (n - 1) // 2)
        att = 0
        while len(edges) < target_m and att < 40 * target_m + 500:
            att += 1
            u = rng.randint(1, n); v = rng.randint(1, n)
            if u == v:
                continue
            e = (min(u, v), max(u, v))
            if e in seen:
                continue
            seen.add(e); edges.append(e)
        k = n + rng.randint(1, 5)
        rng.shuffle(edges)
        return _emit(n, edges, k)
    # kind == 'complete': K_n, ask for an independent set of size k in [2, n]
    edges = [(u, v) for u in range(1, n + 1) for v in range(u + 1, n + 1)]
    k = rng.randint(2, n)
    return _emit(n, edges, k)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--criterion", type=int, required=True, choices=[1, 2, 3])
    p.add_argument("--n", type=int, required=True)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--kind", default="", help="c1/c2: yes|no ; c3: size|complete")
    args = p.parse_args()

    if args.criterion == 1:
        out = gen_is_general(args.n, args.seed, args.kind or "no")
    elif args.criterion == 2:
        out = gen_is_bipartite(args.n, args.seed, args.kind or "yes")
    else:
        out = gen_infeasible_certificate(args.n, args.seed, args.kind or "size")

    sys.stdout.write(out)


if __name__ == "__main__":
    main()
