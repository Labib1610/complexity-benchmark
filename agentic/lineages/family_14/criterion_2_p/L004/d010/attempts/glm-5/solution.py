import sys
from sys import setrecursionlimit

def solve():
    input = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input[idx]); idx += 1
    m = int(input[idx]); idx += 1
    t = int(input[idx]); idx += 1
    
    priority = [False] * (n + 1)
    for _ in range(t):
        p = int(input[idx]); idx += 1
        priority[p] = True
    
    adj = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u = int(input[idx]); idx += 1
        v = int(input[idx]); idx += 1
        w = int(input[idx]); idx += 1
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    if t <= 1:
        print(0)
        return
    
    sys.setrecursionlimit(400000)
    
    parent = [0] * (n + 1)
    parent_weight = [0] * (n + 1)
    depth = [0] * (n + 1)
    order = []
    
    stack = [(1, 0, 0, 0)]
    while stack:
        u, p, pw, d = stack.pop()
        parent[u] = p
        parent_weight[u] = pw
        depth[u] = d
        order.append(u)
        for v, w in adj[u]:
            if v != p:
                stack.append((v, u, w, d + 1))
    
    cnt = [1 if priority[i] else 0 for i in range(n + 1)]
    
    for u in reversed(order):
        if u != 1:
            cnt[parent[u]] += cnt[u]
    
    total = 0
    for u in range(2, n + 1):
        if cnt[u] > 0 and cnt[u] < t:
            total += parent_weight[u]
    
    print(total)

solve()