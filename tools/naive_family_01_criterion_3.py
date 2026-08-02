#!/usr/bin/env python3
"""Deliberately naive solution for family 01 / criterion 3 (triangle certificate).

A plain triple nested loop over all vertex triples, O(n^3), returning the
lexicographically smallest triangle. Correct, but at n=2000 that is 8e9 iterations
and times out, while the reference's bitset search finishes in a fraction of a
second.
"""
import sys


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    adj = [[False] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx + 1]); idx += 2
        adj[u][v] = True
        adj[v][u] = True

    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            for c in range(b + 1, n + 1):
                if adj[a][b] and adj[a][c] and adj[b][c]:
                    print(a, b, c)
                    return


main()
