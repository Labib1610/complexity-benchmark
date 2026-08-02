#!/usr/bin/env python3
"""Realistic baseline for family 10 / criterion 2 (minimum dominating set on a tree).

A solution that does NOT recognise the tree structure and searches for the minimum
dominating set by trying sets of increasing size (all C(n,size) subsets, checking
domination). This is exponential; on any tree whose minimum dominating set exceeds a
handful (paths, balanced, random) it never gets past size ~3 before the C(n,size)
enumeration explodes, so it TLEs, while the O(n) iterative tree DP is instant.
"""
import sys
import itertools


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    nb = [set([v]) for v in range(n + 1)]      # closed neighbourhoods (1-indexed)
    for _ in range(n - 1):
        c = int(data[idx]); p = int(data[idx + 1]); idx += 2
        nb[c].add(p); nb[p].add(c)

    verts = range(1, n + 1)
    for size in range(0, n + 1):
        for combo in itertools.combinations(verts, size):
            covered = set()
            for v in combo:
                covered |= nb[v]
            if len(covered) == n:
                print(size); return


main()
