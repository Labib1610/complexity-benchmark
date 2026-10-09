import sys
from collections import deque

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    s = int(next(it))
    t = int(next(it))
    budget = int(next(it))
    
    edges = []
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        edges.append((u, v, w, i))
        adj[u].append((v, i))
        adj[v].append((u, i))
    
    # BFS to find shortest path by number of edges
    parent = [-1] * (n + 1)
    parent_edge = [-1] * (n + 1)
    q = deque([s])
    parent[s] = s
    
    while q:
        u = q.popleft()
        if u == t:
            break
        for v, eid in adj[u]:
            if parent[v] == -1:
                parent[v] = u
                parent_edge[v] = eid
                q.append(v)
    
    if parent[t] == -1:
        print("YES")
        print(0)
        return
    
    # Reconstruct path
    path_edges = []
    u = t
    while u != s:
        eid = parent_edge[u]
        path_edges.append(eid)
        u = parent[u]
    
    # Find minimum weight edge on path
    min_w = float('inf')
    min_eid = -1
    for eid in path_edges:
        w = edges[eid][2]
        if w < min_w:
            min_w = w
            min_eid = eid
    
    if min_w <= budget:
        u, v, w, idx = edges[min_eid]
        print("YES")
        print(1)
        print(u, v)
    else:
        print("NO")

if __name__ == "__main__":
    solve()