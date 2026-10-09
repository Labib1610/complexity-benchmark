import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    try:
        n = int(next(it))
        m = int(next(it))
        k = int(next(it))
    except StopIteration:
        return

    operations = []
    for _ in range(k):
        s = int(next(it))
        t = int(next(it))
        d = int(next(it))
        operations.append((s, t, d))

    edges = []
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        u = int(next(it))
        v = int(next(it))
        cap = int(next(it))
        edges.append((u, v, cap))
        adj[u].append((v, i))

    # Build flow network
    # Nodes: 1..n for units, plus source and sink
    # We'll use 0-indexed nodes internally for the flow graph
    # Unit i -> node i-1 (0 to n-1)
    # Source -> node n, Sink -> node n+1
    N_nodes = n + 2
    S = n
    T = n + 1
    
    # Edge structure: to, capacity, flow, rev_index
    graph = [[] for _ in range(N_nodes)]
    edge_info = [] # (u, v, cap, edge_idx_in_u, edge_idx_in_v)
    
    def add_edge(u, v, cap):
        # u, v are 0-indexed node indices
        u_idx = len(graph[u])
        v_idx = len(graph[v])
        graph[u].append([v, cap, 0, v_idx])
        graph[v].append([u, 0, 0, u_idx])
        edge_info.append((u, v, cap, u_idx))

    # Add unit-unit edges (channels)
    for u, v, cap in edges:
        add_edge(u - 1, v - 1, cap)
    
    # Add source/sink edges for operations
    for s, t, d in operations:
        add_edge(S, s - 1, d)
        add_edge(t - 1, T, d)

    # Dinic's algorithm
    level = [0] * N_nodes
    ptr = [0] * N_nodes
    
    def bfs():
        for i in range(N_nodes):
            level[i] = -1
        queue = deque([S])
        level[S] = 0
        while queue:
            u = queue.popleft()
            for v, cap, flow, rev in graph[u]:
                if cap - flow > 0 and level[v] == -1:
                    level[v] = level[u] + 1
                    queue.append(v)
        return level[T] != -1

    def dfs(u, pushed):
        if pushed == 0 or u == T:
            return pushed
        for i in range(ptr[u], len(graph[u])):
            ptr[u] = i
            v, cap, flow, rev = graph[u][i]
            if level[v] == level[u] + 1 and cap - flow > 0:
                tr = dfs(v, min(pushed, cap - flow))
                if tr:
                    graph[u][i][2] += tr
                    graph[v][rev][2] -= tr
                    return tr
        return 0

    total_flow = 0
    while bfs():
        ptr = [0] * N_nodes
        while True:
            pushed = dfs(S, float('inf'))
            if not pushed:
                break
            total_flow += pushed

    # Check if all demands are satisfied
    total_demand = sum(d for _, _, d in operations)
    if total_flow != total_demand:
        print("NO")
        return

    print("YES")
    # Extract flows for each operation
    # The first k*2 edges added after channels are the source/sink edges
    # They are added in order: op0_s, op0_t, op1_s, op1_t, ...
    # So edge_info[m + 2*i] corresponds to operation i source edge
    
    results = []
    for i in range(k):
        # Index in edge_info for the source edge of operation i
        # Channels: 0 to m-1
        # Op edges start at m
        # Op i source edge is at m + 2*i
        # Op i sink edge is at m + 2*i + 1 (we don't need its flow, just checking)
        
        # We need to find flow on channel edges for this operation
        # This requires decomposing the flow.
        # Greedy decomposition:
        # For each operation, push flow from s to t using available flow on edges.
        
        s, t, d = operations[i]
        s -= 1
        t -= 1
        
        # Create residual graph view for this operation's flow decomposition
        # We can only use edges that have flow > 0
        # And we track how much of that flow belongs to this operation
        
        # We'll do a DFS to find paths
        # To avoid re-scanning edges, we can use ptr like in Dinic
        
        # Copy current flow state for modification during decomposition
        # We need to subtract flow as we assign it to operations
        # But since we just need to output, we can do it one by one
        # and subtract from the graph's flow values.
        
        op_flow = [0] * m
        remaining_d = d
        
        # We use a simple DFS to find paths from s to t
        # using edges with flow > 0.
        # Note: The graph edges are: graph[u][idx] = [v, cap, flow, rev_idx]
        
        # We need to be careful: graph is modified in-place.
        # We will subtract the flow we use.
        
        while remaining_d > 0:
            # Find a path from s to t
            parent = [-1] * N_nodes
            parent_edge = [-1] * N_nodes
            q = deque([s])
            parent[s] = s # Mark as visited
            
            found = False
            while q:
                u = q.popleft()
                if u == t:
                    found = True
                    break
                
                # Iterate edges to find residual flow (flow > 0)
                # Note: for unit-unit edges, we check graph[u][idx][2] (flow)
                # For source/sink edges, we should not traverse them for decomposition
                # Source edges: from S. Sink edges: to T.
                # We should not enter S or T during decomposition from s to t.
                
                for idx, edge in enumerate(graph[u]):
                    v, cap, flow, rev = edge
                    # We can use this edge if it has flow > 0
                    # And we should not go into S or T
                    # And we should not use the source/sink edges of other operations
                    # Actually, the source/sink edges are connected to S and T.
                    # If we start at s (which is connected to S), we might accidentally go to S.
                    # But S is only connected to sources. So from s, we won't go to S (no edge s->S).
                    # However, we might reach t, which is connected to T.
                    # We should stop at t.
                    
                    if flow > 0 and parent[v] == -1:
                        # Check if this is a valid edge to use
                        # We should not use the edges connected to S or T
                        # Edges connected to S: (S, s_i). We are at s_i, we don't go to S.
                        # Edges connected to T: (t_i, T). We are at t_i, we might go to T.
                        # We should stop at t, not go to T.
                        if v == T: continue # Don't go into global sink
                        if v == S: continue # Don't go into global source
                        
                        # Also, we should not use other operations' source/sink edges
                        # But those are only connected to S and T.
                        # So avoiding S and T is sufficient.
                        
                        parent[v] = u
                        parent_edge[v] = idx
                        q.append(v)
            
            if not found:
                # Should not happen if flow is valid
                # But if it does, we can't satisfy this operation
                # This indicates an issue with the flow or decomposition logic
                # For now, print error or handle gracefully
                # Given the problem guarantees, this should be reachable
                # but if not, we have a problem.
                # Let's assume valid flow always decomposable.
                break
            
            # Reconstruct path and find bottleneck
            path_flow = remaining_d
            curr = t
            path_edges = []
            while curr != s:
                u = parent[curr]
                idx = parent_edge[curr]
                edge = graph[u][idx]
                path_flow = min(path_flow, edge[2])
                path_edges.append((u, idx))
                curr = u
            
            # Apply flow
            path_flow = min(path_flow, remaining_d)
            for u, idx in path_edges:
                edge = graph[u][idx]
                edge[2] -= path_flow
                # Update reverse edge
                v = edge[0]
                rev_idx = edge[3]
                graph[v][rev_idx][2] += path_flow
                
                # If this is a channel edge, record it
                # Channel edges are the first m edges added.
                # We need to map (u, idx) to channel index.
                # We can use edge_info.
                # edge_info stores (u, v, cap, u_idx) for each edge added.
                # We need to find which channel this edge corresponds to.
                # Since we might have multiple edges between same u,v (parallel channels),
                # we need to identify the specific edge.
                
                # We can iterate edge_info to find a match.
                # This is O(m) per edge, which might be slow.
                # Optimization: precompute a map from (u, u_idx) to channel index.
                pass
            
            # To correctly identify channel indices, we need the map.
            # Let's build it before the loop.
            pass
        
    # Re-structure: Build map first, then decompose.
    
    # Map: (u, u_edge_idx) -> channel_index
    edge_to_channel = {}
    for i, (u, v, cap, u_idx) in enumerate(edge_info[:m]):
        edge_to_channel[(u, u_idx)] = i

    results = [[0]*m for _ in range(k)]
    
    for i in range(k):
        s, t, d = operations[i]
        s -= 1
        t -= 1
        
        remaining_d = d
        
        while remaining_d > 0:
            parent = [-1] * N_nodes
            parent_edge = [-1] * N_nodes
            q = deque([s])
            parent[s] = s
            
            found_t = False
            while q:
                u = q.popleft()
                if u == t:
                    found_t = True
                    break
                
                for idx, edge in enumerate(graph[u]):
                    v, cap, flow, rev = edge
                    if flow > 0 and parent[v] == -1:
                        if v == S or v == T: continue
                        parent[v] = u
                        parent_edge[v] = idx
                        q.append(v)
            
            if not found_t:
                break
            
            # Reconstruct
            path_flow = remaining_d
            curr = t
            path_nodes = []
            while curr != s:
                u = parent[curr]
                idx = parent_edge[curr]
                edge = graph[u][idx]
                path_flow = min(path_flow, edge[2])
                path_nodes.append((u, idx))
                curr = u
            
            path_flow = min(path_flow, remaining_d)
            remaining_d -= path_flow
            
            for u, idx in path_nodes:
                edge = graph[u][idx]
                edge[2] -= path_flow
                v = edge[0]
                rev_idx = edge[3]
                graph[v][rev_idx][2] += path_flow
                
                if (u, idx) in edge_to_channel:
                    ch_idx = edge_to_channel[(u, idx)]
                    results[i][ch_idx] += path_flow

    for row in results:
        print(' '.join(map(str, row)))

if __name__ == '__main__':
    solve()