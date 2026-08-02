#!/usr/bin/env python3
"""Realistic baseline for family 10 / criterion 3 (isolated location, budget k=0).

A solution that does NOT scan degrees and instead tries to actually cover the facility:
it searches for a dominating set of increasing size (all C(n,size) subsets), and only
after that search fails to help does it report the uncovered isolated location. The
search is exponential -> TLEs at scale; the reference's O(n+m) degree scan is instant.
"""
import sys
import itertools


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    k = int(data[idx]); idx += 1
    nb = [set([v]) for v in range(n + 1)]
    deg = [0] * (n + 1)
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx + 1]); idx += 2
        nb[u].add(v); nb[v].add(u); deg[u] += 1; deg[v] += 1

    # wasteful attempt: search for a dominating set by increasing size (exponential)
    for size in range(0, n + 1):
        stop = False
        for combo in itertools.combinations(range(1, n + 1), size):
            covered = set()
            for v in combo:
                covered |= nb[v]
            if len(covered) == n:
                stop = True
                break
        if stop:
            break

    # only now report the smallest location with no links
    for v in range(1, n + 1):
        if deg[v] == 0:
            print(v); return


main()
