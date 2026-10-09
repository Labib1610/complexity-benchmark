from collections import defaultdict, deque

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    _ = int(data[idx])
    idx += 1
    
    s = int(data[idx]) - 1  # Convert to 0-based
    idx += 1
    t = int(data[idx]) - 1  # Convert to 0-based
    idx += 1
    d = int(data[idx])
    idx += 1
    
    edges = []
    capacity = []
    graph = defaultdict(list)
    
    for i in range(m):
        u = int(data[idx]) - 1  # Convert to 0-based
        idx += 1
        v = int(data[idx]) - 1  # Convert to 0-based
        idx += 1
        cap = int(data[idx])
        idx += 1
        
        edges.append((u, v))
        capacity.append(cap)
        graph[u].append((v, i, 1))      # forward edge with cost 1
        graph[v].append((u, i, -1))     # backward edge with cost -1
    
    # We need to find a flow of value d from s to t
    # Build residual graph and use Ford-Fulkerson with DFS
    # But since we need to output the actual flow values, let's use a max-flow algorithm
    
    # Let's build the flow network properly
    # Nodes: 0 to n-1
    # Edges: as given, with capacities
    
    # Use Edmonds-Karp (BFS version of Ford-Fulkerson) to find max flow
    # Then check if it's at least d
    
    # But actually, we just need any flow of exactly d
    # So we can set the demand and solve
    
    # Let's model this as a feasible flow problem with demands
    # But since all demands are zero except for source and sink,
    # It's just a standard max flow where we want to send exactly d flow
    
    # We'll use a standard approach:
    # Run max flow, see if it's >= d
    # If yes, then we can extract a flow of exactly d
    
    # Let's implement Ford-Fulkerson with BFS (Edmonds-Karp)
    
    # Build adjacency list with edge indices
    adj = [[] for _ in range(n)]
    for i in range(m):
        u, v = edges[i]
        adj[u].append((v, i, capacity[i]))  # node, edge_id, capacity
        adj[v].append((u, i, 0))            # reverse edge, capacity 0 initially
    
    # But wait, we should track flow separately
    flow = [0] * m
    
    # Actually, let's re-think. We'll run max-flow and see if we get at least d
    # If so, we can scale down or just take any valid flow decomposition of size d
    
    # For simplicity, let's run Ford-Fulkerson directly tracking flows
    
    def bfs_find_path():
        # Find augmenting path using BFS
        parent_edge = [-1] * n
        parent_node = [-1] * n
        visited = [False] * n
        queue = deque()
        queue.append(s)
        visited[s] = True
        
        while queue:
            u = queue.popleft()
            if u == t:
                break
            for v, edge_idx, cap in adj[u]:
                if not visited[v] and cap > 0:
                    visited[v] = True
                    parent_node[v] = u
                    parent_edge[v] = edge_idx
                    queue.append(v)
        
        if not visited[t]:
            return False, []
        
        # Reconstruct path
        path_edges = []
        cur = t
        while cur != s:
            edge_idx = parent_edge[cur]
            prev = parent_node[cur]
            path_edges.append(edge_idx)
            cur = prev
            
        path_edges.reverse()
        return True, path_edges
    
    # Initialize residual capacities
    res_capacity = capacity[:]
    
    total_flow = 0
    while total_flow < d:
        found, path = bfs_find_path()
        if not found:
            break
            
        # Find bottleneck capacity
        bottleneck = float('inf')
        for edge_idx in path:
            u, v = edges[edge_idx]
            # Need to find the right direction in adj[u]
            cap = 0
            for x, idx, c in adj[u]:
                if x == v and idx == edge_idx:
                    cap = c
                    break
            bottleneck = min(bottleneck, cap)
            
        if bottleneck == 0:
            break
            
        # But we want exactly the remaining flow needed
        bottleneck = min(bottleneck, d - total_flow)
        if bottleneck <= 0:
            break
            
        # Update residual capacities and flows
        for edge_idx in path:
            u, v = edges[edge_idx]
            # Forward edge: u -> v
            for i in range(len(adj[u])):
                if adj[u][i][0] == v and adj[u][i][1] == edge_idx:
                    adj[u][i] = (adj[u][i][0], adj[u][i][1], adj[u][i][2] - bottleneck)
                    break
            # Backward edge: v -> u  
            for i in range(len(adj[v])):
                if adj[v][i][0] == u and adj[v][i][1] == edge_idx:
                    adj[v][i] = (adj[v][i][0], adj[v][i][1], adj[v][i][2] + bottleneck)
                    break
                    
        total_flow += bottleneck
        
        # Update our flow tracking
        temp_flow = [0] * m
        # This is getting complex, let's restart with a cleaner implementation
        
    # Cleaner approach: Implement Ford-Fulkerson properly with flow tracking
    
    # Reset everything
    flow = [0] * m
    res_capacity = capacity[:]
    
    # Build proper residual graph representation
    # For each edge i from u to v, we have:
    # - Original edge (u,v) with index i 
    # - Reverse edge (v,u) with index i+m (but we don't actually add these edges, we just track them)
    
    # Actually, let's think differently. 
    # We'll keep track of flow on each original edge
    # And maintain residual capacities implicitly
    
    adj_list = [[] for _ in range(n)]  # (neighbor, edge_index, is_forward)
    for i in range(m):
        u, v = edges[i]
        adj_list[u].append((v, i, True))   # forward edge
        adj_list[v].append((u, i, False))  # backward edge
    
    def find_augmenting_path():
        parent = [-1] * n  # (node, edge_index, direction)
        visited = [False] * n
        queue = deque([s])
        visited[s] = True
        
        while queue:
            u = queue.popleft()
            for v, edge_idx, is_forward in adj_list[u]:
                # Check residual capacity
                residual_cap = 0
                if is_forward:
                    residual_cap = capacity[edge_idx] - flow[edge_idx]
                else:  # backward edge
                    residual_cap = flow[edge_idx]
                    
                if not visited[v] and residual_cap > 0:
                    visited[v] = True
                    parent[v] = (u, edge_idx, is_forward)
                    if v == t:
                        # Found path
                        path = []
                        current = v
                        while parent[current] != -1:
                            prev, e_idx, fwd = parent[current]
                            path.append((e_idx, fwd))
                            current = prev
                        path.reverse()
                        return path
                    queue.append(v)
        
        return None
    
    # Run Ford-Fulkerson
    while True:
        path = find_augmenting_path()
        if path is None:
            break
            
        # Find bottleneck
        bottleneck = d - sum(flow)  # We only want exactly d total
        if bottleneck <= 0:
            break
            
        for edge_idx, is_forward in path:
            if is_forward:
                residual = capacity[edge_idx] - flow[edge_idx]
            else:
                residual = flow[edge_idx]
            bottleneck = min(bottleneck, residual)
            
        if bottleneck <= 0:
            break
            
        # Update flow
        for edge_idx, is_forward in path:
            if is_forward:
                flow[edge_idx] += bottleneck
            else:
                flow[edge_idx] -= bottleneck
    
    # Check if we achieved the desired flow
    # Compute actual flow out of source
    source_out = 0
    for i in range(m):
        if edges[i][0] == s:
            source_out += flow[i]
        elif edges[i][1] == s:
            source_out -= flow[i]
            
    if source_out != d:
        print("NO")
        return
        
    # Also verify flow conservation at all nodes except s,t
    node_flow = [0] * n  # net flow into node
    for i in range(m):
        u, v = edges[i]
        node_flow[v] += flow[i]
        node_flow[u] -= flow[i]
        
    valid = True
    for i in range(n):
        if i != s and i != t:
            if node_flow[i] != 0:
                valid = False
                break
                
    if not valid or node_flow[s] != -d or node_flow[t] != d:
        print("NO")
        return
        
    # Check all flows are within capacity
    for i in range(m):
        if flow[i] < 0 or flow[i] > capacity[i]:
            print("NO")
            return
            
    print("YES")
    print(' '.join(map(str, flow)))

solve()