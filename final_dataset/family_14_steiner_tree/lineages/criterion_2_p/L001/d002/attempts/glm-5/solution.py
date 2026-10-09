import sys
from collections import deque

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    primary = set()
    for i in range(t):
        primary.add(int(input_data[idx])); idx += 1
    
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
    
    # BFS to build parent relationships
    parent = [0] * (n + 1)
    parent_edge = [-1] * (n + 1)
    visited = [False] * (n + 1)
    order = []
    
    root = 1
    visited[root] = True
    q = deque([root])
    parent[root] = 0
    
    while q:
        u = q.popleft()
        order.append(u)
        for v, w, eid in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                parent_edge[v] = eid
                q.append(v)
    
    # Count primaries in each subtree
    subtree_primary = [0] * (n + 1)
    for u in reversed(order):
        if u in primary:
            subtree_primary[u] += 1
        if parent[u] != 0:
            subtree_primary[parent[u]] += subtree_primary[u]
    
    total_cost = 0
    for u in order:
        if u == root:
            continue
        cnt = subtree_primary[u]
        # Edge is needed if cnt >= 1 and (t - cnt) >= 1
        if cnt >= 1 and (t - cnt) >= 1:
            eid = parent_edge[u]
            total_cost += edges[eid][2]
    
    print(total_cost)

solve()