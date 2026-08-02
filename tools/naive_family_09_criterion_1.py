#!/usr/bin/env python3
"""Realistic baseline for family 09 / criterion 1 (k-clique decision).

Try every combination of k users and check that all pairs are friends (early exit on
the first non-edge). This is the natural solution without the Bron-Kerbosch / bitset
branch-and-bound insight. It costs O(C(n,k) * k^2); raising n while keeping k near the
true max clique makes it explode, whereas the bitset B&B reference prunes heavily.
"""
import sys
import itertools


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    k = int(data[idx]); idx += 1
    adj = [set() for _ in range(n + 1)]
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx + 1]); idx += 2
        adj[u].add(v); adj[v].add(u)

    for combo in itertools.combinations(range(1, n + 1), k):
        ok = True
        for i in range(k):
            ai = adj[combo[i]]
            for j in range(i + 1, k):
                if combo[j] not in ai:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            sys.stdout.write("YES\n")
            sys.stdout.write(" ".join(map(str, combo)) + "\n")
            return
    sys.stdout.write("NO\n")


main()
