import sys
from sys import setrecursionlimit

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    primary = list(map(int, input().split()))
    is_primary = [False] * (n + 1)
    for p in primary:
        is_primary[p] = True
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    parent = [0] * (n + 1)
    parent_weight = [0] * (n + 1)
    order = []
    stack = [1]
    parent[1] = -1
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if parent[v] == 0 and v != parent[1]:
                parent[v] = u
                parent_weight[v] = w
                stack.append(v)
    
    count = [1 if is_primary[u] else 0 for u in range(n + 1)]
    total = 0
    for u in reversed(order):
        p = parent[u]
        if p != -1:
            if count[u] > 0:
                total += parent_weight[u]
            count[p] += count[u]
    
    print(total)

solve()