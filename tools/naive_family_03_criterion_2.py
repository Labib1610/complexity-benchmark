#!/usr/bin/env python3
"""Realistic baseline for family 03 / criterion 2 (unique topological order).

Correct but inefficient: the same Kahn-style logic as the reference, except that at
every step it RESCANS all n vertices to find the in-degree-0 set instead of keeping
a queue. That is O(n^2) rather than O(n+m) -- the obvious solution a model writes
without realising the queue matters. It produces the identical output to the
reference, but TLEs at n ~ 2e5.
"""
import sys


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    adj = [[] for _ in range(n + 1)]
    indeg = [0] * (n + 1)
    edge_set = set()
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx + 1]); idx += 2
        adj[u].append(v); indeg[v] += 1; edge_set.add((u, v))

    removed = [False] * (n + 1)
    order = []
    for _ in range(n):
        # O(n) full scan for in-degree-0 vertices, every step -> O(n^2) overall
        zeros = [v for v in range(1, n + 1) if not removed[v] and indeg[v] == 0]
        if len(zeros) != 1:
            print("NO"); return
        v = zeros[0]
        order.append(v); removed[v] = True
        for u in adj[v]:
            indeg[u] -= 1

    for i in range(n - 1):
        if (order[i], order[i + 1]) not in edge_set:
            print("NO"); return

    print("YES")
    print(' '.join(map(str, order)))


main()
