import sys
from collections import deque

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
    edges = []
    for i in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        w = int(input_data[idx]); idx += 1
        adj[u].append((v, w, i))
        adj[v].append((u, w, i))
        edges.append((u, v, w))
    
    if t <= 1:
        print(0)
        return
    
    parent = [0] * (n + 1)
    parent_edge = [-1] * (n + 1)
    order = []
    visited = [False] * (n + 1)
    
    root = 1
    visited[root] = True
    parent[root] = 0
    queue = deque([root])
    while queue:
        u = queue.popleft()
        order.append(u)
        for v, w, eid in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                parent_edge[v] = eid
                queue.append(v)
    
    has_target = [False] * (n + 1)
    for node in targets:
        has_target[node] = True
    
    for u in reversed(order):
        p = parent[u]
        if p != 0 and has_target[u]:
            has_target[p] = True
    
    total = 0
    for u in range(2, n + 1):
        if has_target[u]:
            eid = parent_edge[u]
            total += edges[eid][2]
    
    print(total)

solve()