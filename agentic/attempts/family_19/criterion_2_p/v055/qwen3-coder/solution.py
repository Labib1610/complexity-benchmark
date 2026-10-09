from collections import defaultdict, deque

def solve():
    # Read input
    n, m, _ = map(int, input().split())
    s, t, d = map(int, input().split())
    
    edges = []
    graph = defaultdict(list)
    capacity = []
    
    for i in range(m):
        u, v, cap = map(int, input().split())
        edges.append((u, v))
        graph[u].append((v, i))  # (node, edge_index)
        graph[v].append((u, i))  # For residual graph
        capacity.append(cap)
    
    # We need to find a flow of exactly d from s to t
    # This is a maximum flow problem with exact flow requirement
    
    # Add super source and super sink
    SUPER_SOURCE = 0
    SUPER_SINK = n + 1
    
    # Connect super source to s with capacity d
    # Connect t to super sink with capacity d
    source_edges = []
    sink_edges = []
    
    # Modify graph to include super source and sink
    graph[SUPER_SOURCE].append((s, m))  # Edge index m
    graph[s].append((SUPER_SOURCE, m))  # Reverse edge
    source_edges.append(m)
    
    graph[t].append((SUPER_SINK, m+1))  # Edge index m+1
    graph[SUPER_SINK].append((t, m+1))  # Reverse edge
    sink_edges.append(m+1)
    
    # Extend capacity array
    extended_capacity = capacity[:] + [d, d]
    
    # Add reverse edges for all original edges
    total_edges = m + 2
    for i in range(m):
        u, v = edges[i]
        graph[v].append((u, i + total_edges))  # Reverse edge index
        extended_capacity.append(0)  # Initial flow on reverse edge is 0
    
    total_edges += m
    
    def bfs_find_path():
        # BFS to find augmenting path in residual graph
        visited = [-1] * (n + 2)
        queue = deque([(SUPER_SOURCE, -1, float('inf'))])  # (node, edge_to_node, min_capacity)
        visited[SUPER_SOURCE] = -2  # Special marker for source
        
        while queue:
            current_node, edge_to_current, min_cap = queue.popleft()
            
            if current_node == SUPER_SINK:
                return min_cap, edge_to_current
            
            for neighbor, edge_idx in graph[current_node]:
                if visited[neighbor] == -1 and extended_capacity[edge_idx] > 0:
                    new_min_cap = min(min_cap, extended_capacity[edge_idx])
                    visited[neighbor] = edge_to_current if neighbor != SUPER_SINK else edge_idx
                    queue.append((neighbor, edge_idx, new_min_cap))
        
        return 0, -1
    
    def find_path_edges(target):
        # Reconstruct path from BFS result
        path_edges = []
        current = target
        while current != -2:  # Until we reach SUPER_SOURCE
            if current == -1:
                return []  # No path found
            path_edges.append(current)
            # Find how we got to the node that has this edge
            # This is tricky; let's re-implement BFS properly
            
        return path_edges[::-1]
    
    # Ford-Fulkerson with proper path tracking
    def max_flow():
        flow = [0] * total_edges
        total_flow = 0
        
        while True:
            # BFS to find augmenting path
            parent = [-1] * (n + 2)
            parent_edge = [-1] * (n + 2)
            queue = deque([SUPER_SOURCE])
            parent[SUPER_SOURCE] = -2  # Mark source
            
            while queue:
                current = queue.popleft()
                
                for neighbor, edge_idx in graph[current]:
                    if parent[neighbor] == -1 and extended_capacity[edge_idx] > 0:
                        parent[neighbor] = current
                        parent_edge[neighbor] = edge_idx
                        queue.append(neighbor)
                        
                        if neighbor == SUPER_SINK:
                            break
            
            if parent[SUPER_SINK] == -1:
                break  # No more augmenting paths
                
            # Find minimum capacity along the path
            min_flow = float('inf')
            current = SUPER_SINK
            while parent[current] != -2:  # While not at source
                edge_idx = parent_edge[current]
                min_flow = min(min_flow, extended_capacity[edge_idx])
                current = parent[current]
            
            # Update flows and capacities
            current = SUPER_SINK
            while parent[current] != -2:
                edge_idx = parent_edge[current]
                flow[edge_idx] += min_flow
                extended_capacity[edge_idx] -= min_flow
                # Update reverse edge
                if edge_idx < m + 2:  # Original or added edges
                    reverse_idx = edge_idx + (m if edge_idx < m else -m) if edge_idx < m + 2 + m else edge_idx - m
                    if edge_idx >= m and edge_idx < m + 2:  # Added edges don't have reverse in same way
                        reverse_idx = edge_idx + m if edge_idx < m + 2 else edge_idx - m
                    else:
                        reverse_idx = edge_idx + m if edge_idx < m else edge_idx - m
                else:
                    reverse_idx = edge_idx - m - 2
                
                if edge_idx < m:  # Original forward edge
                    reverse_idx = edge_idx + m + 2
                elif edge_idx >= m + 2 and edge_idx < m + 2 + m:  # Reverse of original
                    reverse_idx = edge_idx - m - 2
                else:
                    # Handle added edges specially
                    if edge_idx == m:  # Super source to s
                        reverse_idx = m + 2 + m  # Will be added later
                    elif edge_idx == m + 1:  # t to super sink
                        reverse_idx = m + 2 + m + 1  # Will be added later
                
                # Simpler approach: just use the known mapping
                if edge_idx < m:  # Original forward edge
                    reverse_idx = m + 2 + edge_idx
                elif edge_idx >= m + 2 and edge_idx < m + 2 + m:  # Reverse of original
                    reverse_idx = edge_idx - m - 2
                elif edge_idx == m:  # Super source to s
                    reverse_idx = m + 2 + m
                elif edge_idx == m + 1:  # t to super sink
                    reverse_idx = m + 2 + m + 1
                
                if reverse_idx < len(extended_capacity):
                    extended_capacity[reverse_idx] += min_flow
                
                current = parent[current]
            
            total_flow += min_flow
        
        return total_flow, flow
    
    # Add reverse edges for the two special edges too
    for i in range(2):
        extended_capacity.append(0)  # Reverse of super edges
    
    total_flow, flow_result = max_flow()
    
    if total_flow != d:
        print("NO")
        return
    
    # Check if flow on super edges is exactly d
    flow_on_source_edge = flow_result[m]  # Flow from super source to s
    flow_on_sink_edge = flow_result[m+1]   # Flow from t to super sink
    
    if flow_on_source_edge != d or flow_on_sink_edge != d:
        print("NO")
        return
    
    # Extract flows on original edges
    result_flows = flow_result[:m]
    
    # Validate that no flow exceeds capacity
    valid = True
    for i in range(m):
        if result_flows[i] > capacity[i] or result_flows[i] < 0:
            valid = False
            break
    
    if not valid:
        print("NO")
        return
    
    # Validate flow conservation at intermediate nodes
    node_balance = [0] * (n + 1)  # Net flow at each node
    
    for i in range(m):
        u, v = edges[i]
        flow_val = result_flows[i]
        node_balance[u] -= flow_val
        node_balance[v] += flow_val
    
    # Check intermediate nodes (not s and not t)
    for node in range(1, n + 1):
        if node != s and node != t:
            if node_balance[node] != 0:
                print("NO")
                return
    
    # Check source and sink balances
    if node_balance[s] != -d or node_balance[t] != d:
        print("NO")
        return
    
    print("YES")
    print(' '.join(map(str, result_flows)))

solve()