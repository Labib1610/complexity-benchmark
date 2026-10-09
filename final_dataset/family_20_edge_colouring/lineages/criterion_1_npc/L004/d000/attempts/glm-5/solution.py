import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n)]
    edges = []
    for i in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        edges.append((u, v))
        adj[u].append((v, i))
        adj[v].append((u, i))
    
    # Check if graph is 3-regular
    for i in range(n):
        if len(adj[i]) != 3:
            print("NO")
            return
    
    # Find cycles using DFS
    visited = [False] * n
    cycles = []
    
    for start in range(n):
        if visited[start]:
            continue
        
        # BFS to find cycle
        parent = [-1] * n
        parent_edge = [-1] * n
        q = deque([start])
        visited[start] = True
        cycle_edges = []
        found = False
        
        while q and not found:
            u = q.popleft()
            for v, e in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    parent_edge[v] = e
                    q.append(v)
                elif v != parent[u]:
                    # Found cycle: v -> ... -> u -> v
                    # Trace back from u to v
                    cycle_edges.append(e)
                    curr = u
                    while curr != v:
                        cycle_edges.append(parent_edge[curr])
                        curr = parent[curr]
                    found = True
                    break
        
        if cycle_edges:
            cycles.append(cycle_edges)
    
    # Assign colors
    ans = [0] * m
    used = [False] * m
    
    for cycle in cycles:
        # Alternate between 1 and 2
        for idx, e in enumerate(cycle):
            if not used[e]:
                ans[e] = 1 if idx % 2 == 0 else 2
                used[e] = True
    
    # Fill remaining edges with 3
    for i in range(m):
        if ans[i] == 0:
            ans[i] = 3
    
    # Verify solution
    for u in range(n):
        colors = set()
        for v, e in adj[u]:
            colors.add(ans[e])
        if len(colors) != 3:
            print("NO")
            return
    
    print("YES")
    print(' '.join(map(str, ans)))

solve()