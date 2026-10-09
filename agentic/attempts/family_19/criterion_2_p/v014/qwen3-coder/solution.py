from collections import defaultdict, deque

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    n = int(data[index])
    m = int(data[index+1])
    index += 3  # skip the '1'
    
    s = int(data[index])
    t = int(data[index+1])
    d = int(data[index+2])
    index += 3
    
    edges = []
    graph = defaultdict(list)
    capacity = {}
    
    for i in range(m):
        u = int(data[index])
        v = int(data[index+1])
        cap = int(data[index+2])
        index += 3
        edges.append((u, v, cap))
        graph[u].append((v, i))
        graph[v].append((u, i))  # For residual graph
        capacity[i] = cap
    
    # We need to find a flow of value d from s to t
    # Build a flow network and use Ford-Fulkerson with BFS (Edmonds-Karp)
    
    # Edge indices: 0 to m-1 for original edges, m to 2m-1 for reverse edges
    # But we'll use adjacency list with edge IDs and track flow separately
    
    # Let's build the graph properly for max flow
    # Each edge has a forward and backward edge
    adj = [[] for _ in range(n+1)]
    edge_list = []  # To store (from, to, capacity, reverse_index)
    
    edge_index_map = {}  # Maps original edge index to forward edge index in edge_list
    
    for i in range(m):
        u, v, cap = edges[i]
        # Forward edge
        fwd_idx = len(edge_list)
        edge_list.append((u, v, cap, fwd_idx + 1))
        adj[u].append(fwd_idx)
        edge_index_map[i] = fwd_idx
        
        # Backward edge
        bwd_idx = len(edge_list)
        edge_list.append((v, u, 0, fwd_idx))
        adj[v].append(bwd_idx)
    
    def bfs(source, sink, parent_edge):
        visited = [False] * (n + 1)
        queue = deque([source])
        visited[source] = True
        
        while queue:
            u = queue.popleft()
            
            for edge_idx in adj[u]:
                to, _, cap, rev_idx = edge_list[edge_idx]
                if not visited[to] and cap > 0:
                    visited[to] = True
                    parent_edge[to] = edge_idx
                    if to == sink:
                        return True
                    queue.append(to)
        
        return False
    
    def edmonds_karp(source, sink):
        parent_edge = [-1] * (n + 1)
        max_flow = 0
        flows = [0] * m  # To store final flow values for original edges
        
        while True:
            if not bfs(source, sink, parent_edge):
                break
            
            # Find minimum capacity along the path
            path_flow = float('inf')
            s_node = sink
            path_edges = []
            
            while s_node != source:
                edge_idx = parent_edge[s_node]
                path_edges.append(edge_idx)
                from_node, to_node, cap, rev_idx = edge_list[edge_idx]
                path_flow = min(path_flow, cap)
                s_node = from_node if from_node != s_node else to_node
                
                # Reconstruct path backwards
                found = False
                for prev_edge in adj[from_node]:
                    if edge_list[prev_edge][1] == s_node and edge_list[prev_edge][0] == from_node:
                        s_node = from_node
                        found = True
                        break
                        
                if not found:
                    temp = s_node
                    s_node = from_node
                    if s_node == source:
                        break
            
            # Reconstruct path correctly
            current = sink
            path_edges = []
            while current != source:
                edge_idx = parent_edge[current]
                from_node, to_node, cap, rev_idx = edge_list[edge_idx]
                path_flow = min(path_flow, cap)
                path_edges.append(edge_idx)
                # Find previous node
                current = from_node
            
            if path_flow == float('inf'):
                break
                
            # Update residual capacities and augment the flow
            for edge_idx in path_edges:
                from_node, to_node, cap, rev_idx = edge_list[edge_idx]
                edge_list[edge_idx] = (from_node, to_node, cap - path_flow, rev_idx)
                # Update reverse edge
                r_from, r_to, r_cap, r_rev = edge_list[rev_idx]
                edge_list[rev_idx] = (r_from, r_to, r_cap + path_flow, r_rev)
            
            max_flow += path_flow
            
            if max_flow >= d:
                break
        
        # If max_flow < d, then impossible
        if max_flow < d:
            return False, None
        
        # Extract flows for original edges
        result_flows = [0] * m
        for i in range(m):
            fwd_edge_idx = edge_index_map[i]
            u, v, orig_cap, rev_idx = edge_list[fwd_edge_idx]
            # Original capacity was edges[i][2]
            # Current capacity is edge_list[fwd_edge_idx][2]
            # Flow is orig_cap - current_capacity
            initial_capacity = edges[i][2]
            current_capacity = edge_list[fwd_edge_idx][2]
            flow_val = initial_capacity - current_capacity
            result_flows[i] = flow_val
        
        return True, result_flows
    
    # Run max flow with demand d
    possible, flows = edmonds_karp(s, t)
    
    if not possible or sum(flows) < d:  # Check if achieved flow meets demand
        # Actually, let's reframe: we want a flow of exactly d
        # So we check if max flow >= d
        # But we also need to make sure we can send exactly d
        # Let's run max flow and see if we get at least d
        # Then extract the actual flow sent
        
        # Recompute using proper method
        # Since Edmonds-Karp finds maximum flow, if it's less than d, impossible
        # Otherwise, we can take a subset of the flow to make it exactly d
        
        # But our implementation above should work
        # Let's fix it properly
        
        # Reset and do it right
        pass  # We already did it
    
    if possible and sum(f) >= d for some interpretation, but let's redo cleanly
    
    # Let's implement a cleaner version
    
    # Build flow network
    # Nodes: 1 to n
    # Edges: given edges with capacities
    # Find max flow from s to t, check if >= d
    
    # Use adjacency list representation
    adj.clear()
    adj.extend([[] for _ in range(n+1)])
    edge_list.clear()
    edge_index_map.clear()
    
    for i in range(m):
        u, v, cap = edges[i]
        # Forward edge
        fwd_idx = len(edge_list)
        edge_list.append((u, v, cap, fwd_idx + 1))
        adj[u].append(fwd_idx)
        edge_index_map[i] = fwd_idx
        
        # Backward edge
        bwd_idx = len(edge_list)
        edge_list.append((v, u, 0, fwd_idx))
        adj[v].append(bwd_idx)
    
    def max_flow(source, sink, target_flow):
        parent_edge = [-1] * (n + 1)
        total_flow = 0
        flows = [0] * m
        
        while total_flow < target_flow:
            # BFS to find augmenting path
            visited = [False] * (n + 1)
            queue = deque([source])
            visited[source] = True
            parent_edge = [-1] * (n + 1)
            
            while queue:
                u = queue.popleft()
                if u == sink:
                    break
                    
                for edge_idx in adj[u]:
                    to, _, cap, rev_idx = edge_list[edge_idx]
                    if not visited[to] and cap > 0:
                        visited[to] = True
                        parent_edge[to] = edge_idx
                        queue.append(to)
            
            if not visited[sink]:
                break  # No more augmenting paths
            
            # Find bottleneck capacity
            path_flow = float('inf')
            current = sink
            path_edges = []
            
            while current != source:
                edge_idx = parent_edge[current]
                path_edges.append(edge_idx)
                from_node, to_node, cap, rev_idx = edge_list[edge_idx]
                path_flow = min(path_flow, cap)
                current = from_node
            
            # Limit path_flow so that total_flow doesn't exceed target_flow
            path_flow = min(path_flow, target_flow - total_flow)
            
            # Update residual graph
            for edge_idx in path_edges:
                from_node, to_node, cap, rev_idx = edge_list[edge_idx]
                edge_list[edge_idx] = (from_node, to_node, cap - path_flow, rev_idx)
                r_from, r_to, r_cap, r_rev = edge_list[rev_idx]
                edge_list[rev_idx] = (r_from, r_to, r_cap + path_flow, r_rev)
            
            total_flow += path_flow
        
        # Extract flows
        result_flows = [0] * m
        for i in range(m):
            fwd_edge_idx = edge_index_map[i]
            initial_capacity = edges[i][2]
            current_capacity = edge_list[fwd_edge_idx][2]
            flow_val = initial_capacity - current_capacity
            result_flows[i] = flow_val
            
        return total_flow >= target_flow, result_flows
    
    possible, flows = max_flow(s, t, d)
    
    if possible:
        print("YES")
        print(' '.join(map(str, flows)))
    else:
        print("NO")

solve()