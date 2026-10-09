import sys
from sys import setrecursionlimit

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    
    required = [False] * (n + 1)
    for _ in range(t):
        required[int(next(it))] = True
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    if t <= 1:
        print(0)
        return
    
    setrecursionlimit(300000)
    
    parent = [0] * (n + 1)
    parent_weight = [0] * (n + 1)
    depth = [0] * (n + 1)
    order = [1]
    parent[1] = 0
    
    for u in order:
        for v, w in adj[u]:
            if v != parent[u]:
                parent[v] = u
                parent_weight[v] = w
                depth[v] = depth[u] + 1
                order.append(v)
    
    cnt = [1 if required[i] else 0 for i in range(n + 1)]
    
    for u in reversed(order):
        if u != 1:
            cnt[parent[u]] += cnt[u]
    
    total = 0
    for u in range(2, n + 1):
        if cnt[u] > 0 and cnt[u] < t:
            total += parent_weight[u]
    
    print(total)

solve()