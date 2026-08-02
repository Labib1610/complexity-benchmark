#!/usr/bin/env python3
"""Realistic baseline for family 08 / criterion 1 (vertex cover decision).

Try every combination of k junctions and check whether it covers all corridors (with
early exit on the first covering set). This is the natural solution when a model does
not know the 2^k bounded-search-tree (FPT) trick. It costs O(C(n,k) * m), so raising n
while keeping k near the true minimum cover makes it explode, whereas the reference's
2^k branching is unaffected.
"""
import sys
import itertools


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    k = int(data[idx]); idx += 1
    edges = []
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx + 1]); idx += 2
        edges.append((u, v))

    for combo in itertools.combinations(range(1, n + 1), k):
        cover = set(combo)
        if all(u in cover or v in cover for (u, v) in edges):
            sys.stdout.write("YES\n")
            sys.stdout.write(" ".join(map(str, combo)) + "\n")
            return
    sys.stdout.write("NO\n")


main()
