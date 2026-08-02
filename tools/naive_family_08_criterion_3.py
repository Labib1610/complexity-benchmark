#!/usr/bin/env python3
"""Realistic baseline for family 08 / criterion 3 (too many corridors).

A solution that does NOT reason via the matching lower bound and instead first tries to
FIND a vertex cover of size k (the same 2^k bounded search the criterion-1 reference
uses), only afterwards -- once it has convinced itself none exists -- emitting k+1
independent corridors. Because the layout contains k+1 disjoint corridors, no size-k
cover exists, so the bounded search explores 2^k nodes and TLEs; the reference's greedy
O(m) matching is instant.
"""
import sys


def main():
    sys.setrecursionlimit(100000)
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    k = int(data[idx]); idx += 1
    edges = []
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx + 1]); idx += 2
        edges.append((u, v))

    in_cover = [False] * (n + 1)

    def first_uncovered():
        for (u, v) in edges:
            if not in_cover[u] and not in_cover[v]:
                return (u, v)
        return None

    def solve(budget):
        e = first_uncovered()
        if e is None:
            return True
        if budget == 0:
            return False
        u, v = e
        for w in (u, v):
            in_cover[w] = True
            if solve(budget - 1):
                return True
            in_cover[w] = False
        return False

    solve(k)                              # exhaustive attempt: no size-k cover exists

    # only now emit the certificate: k+1 pairwise independent corridors
    used = [False] * (n + 1)
    picked = []
    for (u, v) in edges:
        if not used[u] and not used[v]:
            used[u] = used[v] = True
            picked.append((u, v))
            if len(picked) == k + 1:
                break
    sys.stdout.write("\n".join(f"{u} {v}" for (u, v) in picked) + "\n")


main()
