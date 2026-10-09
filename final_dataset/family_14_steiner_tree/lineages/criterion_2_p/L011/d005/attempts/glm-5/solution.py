import sys
from collections import deque

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    critical = set()
    for _ in range(t):
        critical.add(int(input_data[idx])); idx += 1
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        w = int(input_data[idx]); idx += 1
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    root = next(iter(critical))
    
    parent = [0] * (n + 1)
    parent_edge_w = [0] * (n + 1)
    order = []
    visited = [False] * (n + 1)
    visited[root] = True
    queue = deque([root])
    
    while queue:
        u = queue.popleft()
        order.append(u)
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                parent_edge_w[v] = w
                queue.append(v)
    
    has_critical = [False] * (n + 1)
    for c in critical:
        has_critical[c] = True
    
    for u in reversed(order):
        p = parent[u]
        if p != 0 and has_critical[u]:
            has_critical[p] = True
    
    total = 0
    for u in range(1, n + 1):
        if u != root and has_critical[u]:
            total += parent_edge_w[u]
    
    print(total)

solve()