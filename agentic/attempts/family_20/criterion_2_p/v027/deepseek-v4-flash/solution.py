import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    nL, nR, m = map(int, input().split())
    edges = []
    adj = [[] for _ in range(nL + nR + 2)]
    for i in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
        adj[u].append(i)
        adj[nL + v].append(i)

    max_deg = 0
    deg = [0] * (nL + nR + 2)
    for u, v in edges:
        deg[u] += 1
        deg[nL + v] += 1
    max_deg = max(deg)

    color = [0] * m
    # Greedy edge coloring
    # For each edge, find free color at both endpoints
    used_u = [set() for _ in range(nL + nR + 2)]
    for i in range(m):
        u, v = edges[i]
        right = nL + v
        c = 1
        while c in used_u[u] or c in used_u[right]:
            c += 1
        color[i] = c
        used_u[u].add(c)
        used_u[right].add(c)

    print("YES")
    print(" ".join(map(str, color)))

if __name__ == "__main__":
    solve()