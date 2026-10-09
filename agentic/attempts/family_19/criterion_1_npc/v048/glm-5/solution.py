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
    
    classifications = []
    for _ in range(k):
        s = int(next(it))
        t = int(next(it))
        d = int(next(it))
        classifications.append((s, t, d))
    
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        cap = int(next(it))
        edges.append((u, v, cap))
    
    # Build graph for max flow
    # Nodes: 1..n for offices, source = 0, sink = n+1
    # Edges: source -> origins, destinations -> sink, and all courier routes
    N = n + 2
    source = 0
    sink = n + 1
    adj = [[] for _ in range(N)]
    edge_list = []
    
    def add_edge(u, v, cap):
        idx = len(edge_list)
        edge_list.append([u, v, cap, 0])  # forward edge
        edge_list.append([v, u, 0, 0])    # reverse edge
        adj[u].append(idx)
        adj[v].append(idx ^ 1)
    
    total_demand = 0
    for s, t, d in classifications:
        add_edge(source, s, d)
        add_edge(t, sink, d)
        total_demand += d
    
    for u, v, cap in edges:
        add_edge(u, v, cap)
    
    # Dinic's algorithm
    level = [0] * N
    ptr = [0] * N
    
    def bfs():
        for i in range(N):
            level[i] = -1
        q = deque([source])
        level[source] = 0
        while q:
            u = q.popleft()
            for idx in adj[u]:
                v = edge_list[idx][1]
                if edge_list[idx][2] > 0 and level[v] == -1:
                    level[v] = level[u] + 1
                    q.append(v)
        return level[sink] != -1
    
    def dfs(u, flow):
        if u == sink:
            return flow
        while ptr[u] < len(adj[u]):
            idx = adj[u][ptr[u]]
            v = edge_list[idx][1]
            if edge_list[idx][2] > 0 and level[v] == level[u] + 1:
                pushed = dfs(v, min(flow, edge_list[idx][2]))
                if pushed > 0:
                    edge_list[idx][2] -= pushed
                    edge_list[idx ^ 1][2] += pushed
                    return pushed
            ptr[u] += 1
        return 0
    
    max_flow = 0
    while bfs():
        ptr = [0] * N
        while True:
            pushed = dfs(source, float('inf'))
            if pushed == 0:
                break
            max_flow += pushed
    
    if max_flow != total_demand:
        print("NO")
        return
    
    # Decompose flow for each classification
    # For each classification, we need to find paths from s to t
    # We'll use the flow network and decompose
    
    # Build adjacency for decomposition
    # For each edge in original graph (courier routes), we have flow
    # edge_list[2*i] is the forward edge for courier route i (i from 0 to m-1)
    # The edges for source->s and t->sink are at indices 0, 2, 4, ... for k classifications
    
    # First, let's build a graph for each classification
    # We need to find paths from s_i to t_i
    
    # For each classification, we'll find augmenting paths in the residual graph
    # But we need to track which classification uses which edge
    
    # Let's use a different approach: for each classification, find paths
    # using the flow that was assigned
    
    # We'll use the flow values on edges
    # For courier route i (input order), the forward edge is at index 2*(2*k + i) = 4*k + 2*i
    # Wait, let's recalculate:
    # For each classification: 2 edges (source->s, t->sink), so 2*k edges added
    # Then for each courier route: 1 edge added
    # So courier route i (0-indexed) has forward edge at index 2*(2*k + i) = 4*k + 2*i
    
    # Actually, add_edge adds 2 entries to edge_list per call
    # So for classification j (0-indexed):
    #   add_edge(source, s_j, d_j) -> indices 4*j, 4*j+1
    #   add_edge(t_j, sink, d_j) -> indices 4*j+2, 4*j+3
    # For courier route i (0-indexed):
    #   add_edge(u_i, v_i, cap_i) -> indices 4*k + 2*i, 4*k + 2*i + 1
    
    # The flow on edge idx is edge_list[idx^1][2] (the reverse edge's capacity)
    
    # For decomposition, we'll process each classification
    # For classification j, we need to send d_j units from s_j to t_j
    # We'll find paths using DFS on the flow network
    
    result = [[0] * m for _ in range(k)]
    
    # Build adjacency list for courier routes (for efficient traversal)
    # adj_courier[u] = list of (v, edge_idx_in_input, flow_available)
    adj_courier = [[] for _ in range(n + 1)]
    for i in range(m):
        u, v, _ = edges[i]
        edge_idx = 4 * k + 2 * i
        flow = edge_list[edge_idx ^ 1][2]  # flow = reverse edge capacity
        if flow > 0:
            adj_courier[u].append((v, i, flow))
    
    # For each classification, decompose flow
    for j in range(k):
        s, t, d = classifications[j]
        remaining = d
        
        # We'll use DFS to find paths from s to t
        # We need to track which edges we use and how much
        
        while remaining > 0:
            # Find a path from s to t using DFS
            parent = [(-1, -1, -1)] * (n + 1)  # (prev_node, edge_input_idx, flow_used)
            stack = [s]
            parent[s] = (s, -1, -1)
            found = False
            
            while stack and not found:
                u = stack.pop()
                for v, edge_idx_input, flow_avail in adj_courier[u]:
                    if flow_avail > 0 and parent[v][0] == -1:
                        parent[v] = (u, edge_idx_input, flow_avail)
                        if v == t:
                            found = True
                            break
                        stack.append(v)
            
            if not found:
                # Should not happen if flow is valid
                print("NO")
                return
            
            # Find the bottleneck on this path
            path = []
            v = t
            bottleneck = float('inf')
            while v != s:
                u, edge_idx_input, flow_avail = parent[v]
                path.append((u, v, edge_idx_input))
                bottleneck = min(bottleneck, flow_avail)
                v = u
            
            bottleneck = min(bottleneck, remaining)
            
            # Update the result and flow
            v = t
            while v != s:
                u, edge_idx_input, _ = parent[v]
                result[j][edge_idx_input] += bottleneck
                # Update the flow in adj_courier
                for idx, (vv, ei, f) in enumerate(adj_courier[u]):
                    if vv == v and ei == edge_idx_input:
                        adj_courier[u][idx] = (vv, ei, f - bottleneck)
                        break
                v = u
            
            remaining -= bottleneck
    
    print("YES")
    for row in result:
        print(' '.join(map(str, row)))

solve()