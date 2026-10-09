from collections import defaultdict, deque

def solve():
    n, m, _ = map(int, input().split())
    s, t, d = map(int, input().split())
    
    edges = []
    graph = defaultdict(list)
    capacity = []
    
    for i in range(m):
        u, v, cap = map(int, input().split())
        edges.append((u, v))
        graph[u].append((v, i, cap))  # (to_node, edge_index, capacity)
        graph[v].append((u, i, 0))    # reverse edge with 0 capacity
        capacity.append(cap)
    
    # We need to model this as a circulation problem with supply/demand
    # Node s has supply +d, node t has demand +d, others have supply 0
    
    # Add super source and super sink
    SUPER_SOURCE = 0
    SUPER_SINK = n + 1
    
    # Connect super source to s with capacity d
    graph[SUPER_SOURCE].append((s, m, d))
    graph[s].append((SUPER_SOURCE, m, 0))
    
    # Connect t to super sink with capacity d
    graph[t].append((SUPER_SINK, m+1, d))
    graph[SUPER_SINK].append((t, m+1, 0))
    
    # For each intermediate node (not s and not t), add edge from super_sink to node with capacity infinity
    # and from node to super_source with capacity infinity to enforce flow conservation
    for node in range(1, n+1):
        if node != s and node != t:
            # These edges ensure flow conservation at intermediate nodes
            # But actually, in a circulation problem, we want the net flow at each intermediate node to be 0
            # So we don't need to add extra edges; the flow conservation is inherent in max flow formulation
            
            # Actually, let's think differently. 
            # We want: 
            # - Net flow out of s = d  => s has supply d
            # - Net flow into t = d   => t has demand d  
            # - Net flow at other nodes = 0 => flow conservation
            pass
    
    # Now run max flow from SUPER_SOURCE to SUPER_SINK
    # Edge indices: 0 to m-1 are original edges, m and m+1 are the new edges
    
    def bfs():
        parent = [-1] * (n + 2)  # Nodes 1..n, plus 0 (SUPER_SOURCE) and n+1 (SUPER_SINK)
        parent_edge = [-1] * (n + 2)
        visited = [False] * (n + 2)
        queue = deque([SUPER_SOURCE])
        visited[SUPER_SOURCE] = True
        
        while queue:
            u = queue.popleft()
            
            for v, edge_idx, cap in graph[u]:
                if not visited[v] and cap > 0:
                    visited[v] = True
                    parent[v] = u
                    parent_edge[v] = edge_idx
                    queue.append(v)
                    if v == SUPER_SINK:
                        return parent, parent_edge
        return None, None
    
    # Initialize flow
    flow = [0] * (m + 2)  # flow[i] is the flow on edge i
    
    # Max flow algorithm
    while True:
        parent, parent_edge = bfs()
        if parent is None:
            break
            
        # Find minimum capacity along the path
        min_cap = float('inf')
        curr = SUPER_SINK
        while curr != SUPER_SOURCE:
            prev = parent[curr]
            edge_idx = parent_edge[curr]
            # Find the actual capacity of this edge
            for v, idx, cap in graph[prev]:
                if v == curr and idx == edge_idx:
                    min_cap = min(min_cap, cap)
                    break
            curr = prev
            
        # Update capacities and flows
        curr = SUPER_SINK
        while curr != SUPER_SOURCE:
            prev = parent[curr]
            edge_idx = parent_edge[curr]
            
            # Update forward edge capacity
            for i, (v, idx, cap) in enumerate(graph[prev]):
                if v == curr and idx == edge_idx:
                    graph[prev][i] = (v, idx, cap - min_cap)
                    flow[idx] += min_cap
                    break
                    
            # Update backward edge capacity
            for i, (v, idx, cap) in enumerate(graph[curr]):
                if v == prev and idx == edge_idx:
                    graph[curr][i] = (v, idx, cap + min_cap)
                    flow[idx] -= min_cap
                    break
                    
            curr = prev
    
    # Check if we achieved the required flow
    # Flow through the edge from SUPER_SOURCE to s should be d
    achieved_flow = 0
    for v, edge_idx, cap in graph[SUPER_SOURCE]:
        if v == s:
            # The original capacity was d, current capacity is cap
            # So flow is d - cap
            for orig_v, orig_idx, orig_cap in graph[s]:
                if orig_v == SUPER_SOURCE:
                    achieved_flow = orig_cap - cap
                    break
            break
    
    if achieved_flow < d:
        print("NO")
        return
    
    # Extract the solution
    result = flow[:m]
    print("YES")
    print(*result)

solve()