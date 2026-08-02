#!/usr/bin/env python3
"""Realistic baseline for family 14 / criterion 1 (Steiner tree).

Enumerate every subset S of the OPTIONAL (relay) sites; for each, take the induced
subgraph on (terminals union S) and compute its MST if it spans all those nodes; the
minimum over all subsets is the exact Steiner tree cost. Natural without Dreyfus-Wagner.
Cost is O(2^(n-t) * m log m): exponential in the number of optional sites, so holding t
small and growing n kills it, while the 3^t reference is unaffected.
"""
import sys
import itertools


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); m = int(data[idx + 1]); t = int(data[idx + 2]); idx += 3
    terminals = [int(data[idx + i]) for i in range(t)]; idx += t
    tset = set(terminals)
    edges = []
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx + 1]); w = int(data[idx + 2]); idx += 3
        edges.append((w, u, v))

    optional = [v for v in range(1, n + 1) if v not in tset]
    best = float("inf")

    def mst_cost(nodeset):
        parent = {x: x for x in nodeset}

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]; x = parent[x]
            return x
        total = 0; used = 0
        for w, u, v in edges:                        # edges are given sorted below
            if u in nodeset and v in nodeset:
                ru, rv = find(u), find(v)
                if ru != rv:
                    parent[ru] = rv; total += w; used += 1
        return total if used == len(nodeset) - 1 else None

    edges.sort()
    for r in range(len(optional) + 1):
        for S in itertools.combinations(optional, r):
            c = mst_cost(tset | set(S))
            if c is not None and c < best:
                best = c

    print(best if best != float("inf") else -1)


main()
