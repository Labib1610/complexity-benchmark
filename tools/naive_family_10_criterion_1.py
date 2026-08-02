#!/usr/bin/env python3
"""Realistic baseline for family 10 / criterion 1 (dominating set decision).

Try every combination of k locations and check that every location is covered (itself
or a neighbour has a sensor), using closed-neighbourhood bitsets, early exit on the
first dominating set. Natural without the set-cover branch-and-bound. Costs O(C(n,k)),
so raising n while keeping k near the true minimum dominating set makes it explode; the
B&B reference prunes heavily.
"""
import sys
import itertools


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    k = int(data[idx]); idx += 1
    nb = [1 << v for v in range(n)]
    for _ in range(m):
        u = int(data[idx]) - 1; v = int(data[idx + 1]) - 1; idx += 2
        nb[u] |= (1 << v); nb[v] |= (1 << u)

    full = (1 << n) - 1
    for combo in itertools.combinations(range(n), k):
        cov = 0
        for v in combo:
            cov |= nb[v]
        if cov == full:
            sys.stdout.write("YES\n")
            sys.stdout.write(" ".join(str(v + 1) for v in combo) + "\n")
            return
    sys.stdout.write("NO\n")


main()
