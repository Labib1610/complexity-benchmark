import sys
from collections import deque

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    B = int(input_data[idx]); idx += 1
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        adj[u].append(v)
        adj[v].append(u)
    
    edges = []
    for i in range(1, n + 1):
        for j in adj[i]:
            if i < j:
                edges.append((i, j))
    
    def cost(perm):
        pos = [0] * (n + 1)
        for i in range(n):
            pos[perm[i]] = i + 1
        return sum(abs(pos[u] - pos[v]) for u, v in edges)
    
    best_perm = None
    best_cost = float('inf')
    
    # Try BFS from low-degree nodes
    degrees = [len(adj[i]) for i in range(n + 1)]
    sorted_nodes = sorted(range(1, n + 1), key=lambda x: degrees[x])
    
    starts = sorted_nodes[:min(8, n)]
    
    for s in starts:
        visited = [False] * (n + 1)
        perm = []
        q = deque([s])
        visited[s] = True
        while q:
            u = q.popleft()
            perm.append(u)
            nbrs = sorted(adj[u], key=lambda x: degrees[x])
            for v in nbrs:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
        c = cost(perm)
        if c < best_cost:
            best_cost = c
            best_perm = perm
    
    # Try degree-sorted order
    perm = sorted(range(1, n + 1), key=lambda x: degrees[x])
    c = cost(perm)
    if c < best_cost:
        best_cost = c
        best_perm = perm
    
    # Try reverse degree-sorted
    perm = sorted(range(1, n + 1), key=lambda x: -degrees[x])
    c = cost(perm)
    if c < best_cost:
        best_cost = c
        best_perm = perm
    
    if best_cost <= B:
        print("YES")
        print(' '.join(map(str, best_perm)))
    else:
        print("NO")

solve()