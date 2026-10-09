import sys
from collections import deque

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    _ = int(next(it))  # number of currencies, always 1
    s = int(next(it))
    t = int(next(it))
    d = int(next(it))
    
    edges = []
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        u = int(next(it))
        v = int(next(it))
        limit = int(next(it))
        edges.append((u, v, limit))
        adj[u].append((v, i))
        adj[v].append((u, i))
    
    # Check connectivity using BFS
    visited = [False] * (n + 1)
    q = deque([s])
    visited[s] = True
    while q:
        u = q.popleft()
        for v, i in adj[u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)
    
    if not visited[t]:
        print("NO")
        return
    
    # Build flow network
    # Node indices: 1..n for original nodes, n+1..n+m for edge nodes
    # Edge node i (0-indexed) corresponds to node n+1+i
    N = n + m + 1
    cap = [[0] * (N + 1) for _ in range(N + 1)]
    flow = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Add edges from edge nodes to their endpoints
    for i, (u, v, limit) in enumerate(edges):
        edge_node = n + 1 + i
        cap[edge_node][v] = limit
        cap[u][edge_node] = limit
    
    # Add super source and super sink
    super_source = N
    super_sink = N - 1 if N - 1 != t else N - 2  # This shouldn't happen, just use N
    super_sink = N
    
    # Actually, let's use N+1 as super source/sink
    # Rebuild with proper indexing
    N = n + m
    cap = [[0] * (N + 2) for _ in range(N + 2)]
    flow = [[0] * (N + 2) for _ in range(N + 2)]
    super_source = N + 1
    super_sink = N + 2
    
    for i, (u, v, limit) in enumerate(edges):
        edge_node = n + i + 1
        cap[edge_node][v] = limit
        cap[u][edge_node] = limit
    
    cap[super_source][s] = d
    cap[t][super_sink] = d
    
    # Dinic's algorithm
    level = [0] * (N + 3)
    ptr = [0] * (N + 3)
    
    def bfs():
        for i in range(N + 3):
            level[i] = -1
        level[super_source] = 0
        q = deque([super_source])
        while q:
            u = q.popleft()
            for v in range(1, N + 3):
                if level[v] == -1 and cap[u][v] - flow[u][v] > 0:
                    level[v] = level[u] + 1
                    q.append(v)
        return level[super_sink] != -1
    
    def dfs(u, f):
        if u == super_sink:
            return f
        for v in range(ptr[u], N + 3):
            ptr[u] = v
            if level[v] == level[u] + 1 and cap[u][v] - flow[u][v] > 0:
                pushed = dfs(v, min(f, cap[u][v] - flow[u][v]))
                if pushed > 0:
                    flow[u][v] += pushed
                    flow[v][u] -= pushed
                    return pushed
        return 0
    
    max_flow = 0
    while bfs():
        ptr = [0] * (N + 3)
        while True:
            pushed = dfs(super_source, float('inf'))
            if pushed == 0:
                break
            max_flow += pushed
    
    if max_flow < d:
        print("NO")
        return
    
    print("YES")
    result = []
    for i, (u, v, limit) in enumerate(edges):
        edge_node = n + i + 1
        result.append(str(flow[u][edge_node]))
    print(' '.join(result))

solve()