import sys
from sys import stdin, setrecursionlimit

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    t = int(data[idx]); idx += 1
    
    active = [False] * (n + 1)
    for _ in range(t):
        v = int(data[idx]); idx += 1
        active[v] = True
    
    if t <= 1:
        print(0)
        return
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        w = int(data[idx]); idx += 1
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    setrecursionlimit(1 << 25)
    
    parent = [0] * (n + 1)
    parent_edge = [0] * (n + 1)
    order = []
    stack = [1]
    parent[1] = -1
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if parent[v] == 0:
                parent[v] = u
                parent_edge[v] = w
                stack.append(v)
    
    cnt = [0] * (n + 1)
    for u in reversed(order):
        if active[u]:
            cnt[u] += 1
        p = parent[u]
        if p != -1:
            cnt[p] += cnt[u]
    
    ans = 0
    for u in range(2, n + 1):
        if cnt[u] > 0:
            ans += parent_edge[u]
    
    print(ans)

solve()