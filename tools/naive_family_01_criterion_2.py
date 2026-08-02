#!/usr/bin/env python3
"""Deliberately naive (correct but inefficient) solution for family 01 / crit 2.

2-colouring is polynomial, but a weak solution can still be far too slow. This one
never builds an adjacency list: to find a vertex's neighbours during BFS it
linearly re-scans the whole edge list every time, giving O(n * m) behaviour. It is
correct, but times out at n, m ~ 2e5 while the reference's O(n+m) BFS is instant.
(A literal n x n adjacency matrix would simply run out of memory at this size.)
"""
import sys
from collections import deque


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    E = []
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx + 1]); idx += 2
        E.append((u, v))

    color = [0] * (n + 1)
    for start in range(1, n + 1):
        if color[start]:
            continue
        color[start] = 1
        q = deque([start])
        while q:
            x = q.popleft()
            # naive neighbour lookup: rescan every edge
            for (a, b) in E:
                if a == x:
                    w = b
                elif b == x:
                    w = a
                else:
                    continue
                if color[w] == 0:
                    color[w] = 3 - color[x]
                    q.append(w)
                elif color[w] == color[x]:
                    print("NO")
                    return

    print("YES")
    print(*color[1:n + 1])


main()
