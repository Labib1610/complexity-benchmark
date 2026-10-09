import sys
from sys import setrecursionlimit

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    targets = set()
    for i in range(t):
        targets.add(int(input_data[idx])); idx += 1
    
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        w = int(input_data[idx]); idx += 1
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    if t <= 1:
        print(0)
        return
    
    root = next(iter(targets))
    
    # Iterative DFS
    parent = [0] * (n + 1)
    parent_edge_w = [0] * (n + 1)
    order = []
    visited = [False] * (n + 1)
    stack = [root]
    visited[root] = True
    parent[root] = 0
    
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                parent_edge_w[v] = w
                stack.append(v)
    
    cnt = [0] * (n + 1)
    for v in targets:
        cnt[v] = 1
    
    # Process in reverse order (bottom-up)
    for u in reversed(order):
        if parent[u] != 0:
            cnt[parent[u]] += cnt[u]
    
    total = 0
    for u in range(1, n + 1):
        if parent[u] != 0:
            c = cnt[u]
            if 1 <= c <= t - 1:
                total += parent_edge_w[u]
    
    print(total)

solve()