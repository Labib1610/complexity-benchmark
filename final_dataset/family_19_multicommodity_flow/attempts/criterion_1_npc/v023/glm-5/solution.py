import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    freqs = []
    for _ in range(k):
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        d = int(next(it))
        freqs.append((s, t, d))
    
    edges = []
    adj = [[] for _ in range(n)]
    for i in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        c = int(next(it))
        edges.append((u, v, c))
        adj[u].append((v, i))
    
    # Build flow network
    # Nodes: 0..n-1 are original nodes
    # Node n is super source, node n+1 is super sink
    N = n + 2
    source = n
    sink = n + 1
    
    # Capacity matrix
    cap = [[0] * N for _ in range(N)]
    
    # Add edges from super source to each origin
    for s, t, d in freqs:
        cap[source][s] += d
    
    # Add edges from each destination to super sink
    for s, t, d in freqs:
        cap[t][sink] += d
    
    # Add conduit edges
    for u, v, c in edges:
        cap[u][v] += c
    
    # Dinic's algorithm
    level = [0] * N
    ptr = [0] * N
    
    def bfs():
        for i in range(N):
            level[i] = -1
        level[source] = 0
        q = deque([source])
        while q:
            u = q.popleft()
            for v in range(N):
                if level[v] == -1 and cap[u][v] > 0:
                    level[v] = level[u] + 1
                    q.append(v)
        return level[sink] != -1
    
    def dfs(u, flow):
        if u == sink:
            return flow
        for i in range(ptr[u], N):
            v = i
            if level[v] == level[u] + 1 and cap[u][v] > 0:
                pushed = dfs(v, min(flow, cap[u][v]))
                if pushed > 0:
                    cap[u][v] -= pushed
                    cap[v][u] += pushed
                    return pushed
            ptr[u] += 1
        return 0
    
    total_demand = sum(d for _, _, d in freqs)
    total_flow = 0
    
    while bfs():
        ptr = [0] * N
        while True:
            pushed = dfs(source, float('inf'))
            if pushed == 0:
                break
            total_flow += pushed
    
    if total_flow != total_demand:
        print("NO")
        return
    
    # Extract flow on each edge for each frequency
    # We need to decompose the flow
    
    # Build adjacency list for flow decomposition
    flow_adj = [[] for _ in range(n)]
    for i, (u, v, c) in enumerate(edges):
        # Original capacity was c, current capacity is cap[u][v]
        # So flow used is c - cap[u][v]
        flow_used = c - cap[u][v]
        if flow_used > 0:
            flow_adj[u].append((v, i, flow_used))
    
    # For each frequency, find paths from s to t
    result = [[0] * m for _ in range(k)]
    
    for freq_idx, (s, t, d) in enumerate(freqs):
        remaining = d
        while remaining > 0:
            # Find a path from s to t using BFS
            parent = [-1] * n
            parent_edge = [-1] * n
            q = deque([s])
            parent[s] = s
            while q and parent[t] == -1:
                u = q.popleft()
                for v, edge_idx, flow in flow_adj[u]:
                    if parent[v] == -1 and flow > 0:
                        parent[v] = u
                        parent_edge[v] = edge_idx
                        q.append(v)
            
            if parent[t] == -1:
                # Should not happen if flow is valid
                print("NO")
                return
            
            # Find minimum flow along path
            path_flow = remaining
            v = t
            while v != s:
                u = parent[v]
                edge_idx = parent_edge[v]
                for i, (nv, ni, nf) in enumerate(flow_adj[u]):
                    if ni == edge_idx:
                        path_flow = min(path_flow, nf)
                        break
                v = u
            
            # Update flow and result
            v = t
            while v != s:
                u = parent[v]
                edge_idx = parent_edge[v]
                result[freq_idx][edge_idx] += path_flow
                for i, (nv, ni, nf) in enumerate(flow_adj[u]):
                    if ni == edge_idx:
                        flow_adj[u][i] = (nv, ni, nf - path_flow)
                        break
                v = u
            
            remaining -= path_flow
    
    print("YES")
    for row in result:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    solve()