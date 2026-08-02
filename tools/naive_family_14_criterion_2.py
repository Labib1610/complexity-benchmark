#!/usr/bin/env python3
"""Realistic baseline for family 14 / criterion 2 (MST).

Prim's algorithm WITHOUT a priority queue: each of the n steps scans all vertices to
find the minimum key. That is O(n^2), so it TLEs at n = 2e5, while the O(m log m)
Kruskal reference is fast.
"""
import sys


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); m = int(data[idx + 1]); idx += 2
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx + 1]); w = int(data[idx + 2]); idx += 3
        adj[u].append((v, w)); adj[v].append((u, w))

    INF = float("inf")
    key = [INF] * (n + 1)
    in_mst = [False] * (n + 1)
    key[1] = 0
    total = 0
    for _ in range(n):
        # O(n) linear scan for the minimum-key vertex not yet in the tree -> O(n^2)
        u = -1; best = INF
        for x in range(1, n + 1):
            if not in_mst[x] and key[x] < best:
                best = key[x]; u = x
        if u == -1:
            break
        in_mst[u] = True
        total += key[u]
        for (v, w) in adj[u]:
            if not in_mst[v] and w < key[v]:
                key[v] = w
    print(total)


main()
