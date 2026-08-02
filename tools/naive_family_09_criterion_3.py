#!/usr/bin/env python3
"""Realistic baseline for family 09 / criterion 3 (oversized request, r > n).

A solution that does NOT apply the pigeonhole shortcut (r > n -> impossible) and
instead searches for a tight-knit group (clique) of size r by extending cliques
vertex by vertex. Since r > n it can never reach size r, so it explores every clique
in the graph -- exponentially many in a dense graph -- and TLEs. The reference is O(1).
"""
import sys


def main():
    sys.setrecursionlimit(100000)
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    r = int(data[idx]); idx += 1
    adj = [set() for _ in range(n + 1)]
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx + 1]); idx += 2
        adj[u].add(v); adj[v].add(u)

    found = [False]

    def extend(size, candidates):
        if found[0]:
            return
        if size == r:
            found[0] = True
            return
        for i, v in enumerate(candidates):
            nxt = [u for u in candidates[i + 1:] if u in adj[v]]
            extend(size + 1, nxt)

    extend(0, list(range(1, n + 1)))       # explores every clique; never reaches r > n

    sys.stdout.write("NO\n")


main()
