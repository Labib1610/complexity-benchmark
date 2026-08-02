#!/usr/bin/env python3
"""Deliberately naive solution for family 01 / criterion 1 (3-coloring).

This is the file-mandated naive: plain recursive backtracking that tries every
vertex x every color, with only the *basic conflict check* against already-
coloured neighbours, no ordering heuristic and no bitsets. It is essentially the
same shape as the reference (3^n with minimal pruning) -- which is the point:
family 01's reference is itself naive backtracking, so this measures how narrow
the P-vs-NPC window is when the reference and a naive solution share a shape.
"""
import sys


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx + 1]); idx += 2
        adj[u].append(v)
        adj[v].append(u)

    color = [0] * (n + 1)
    sys.setrecursionlimit(1 << 20)

    def bt(v):
        if v > n:
            return True
        for c in (1, 2, 3):
            ok = True
            for u in adj[v]:
                if color[u] == c:
                    ok = False
                    break
            if ok:
                color[v] = c
                if bt(v + 1):
                    return True
                color[v] = 0
        return False

    if bt(1):
        print("YES")
        print(*color[1:n + 1])
    else:
        print("NO")


main()
