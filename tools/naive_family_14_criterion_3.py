#!/usr/bin/env python3
"""Realistic baseline for family 14 / criterion 3 (an isolated required site).

A solution that does NOT scan degrees and instead tries to actually connect the
required sites -- enumerating subsets of the optional sites and looking for one whose
induced subgraph connects every terminal (the same exponential Steiner attempt as the
criterion-1 baseline). Since one required site is isolated, no subset ever connects them
all, so it explores exponentially -> TLE. Only afterwards does it report the isolated
required site. The reference's O(n+m) degree scan is instant.
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
    deg = [0] * (n + 1)
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx + 1]); idx += 3   # weight unused here
        edges.append((u, v)); deg[u] += 1; deg[v] += 1

    optional = [v for v in range(1, n + 1) if v not in tset]

    def connects_all(nodeset):
        parent = {x: x for x in nodeset}

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]; x = parent[x]
            return x
        for u, v in edges:
            if u in nodeset and v in nodeset:
                parent[find(u)] = find(v)
        roots = {find(x) for x in terminals}
        return len(roots) == 1

    # exhaustive Steiner attempt (never succeeds: a required site is isolated)
    for r in range(len(optional) + 1):
        stop = False
        for S in itertools.combinations(optional, r):
            if connects_all(tset | set(S)):
                stop = True; break
        if stop:
            break

    # only now report the smallest required site with no cabling option touching it
    for site in sorted(terminals):
        if deg[site] == 0:
            print(site); return


main()
