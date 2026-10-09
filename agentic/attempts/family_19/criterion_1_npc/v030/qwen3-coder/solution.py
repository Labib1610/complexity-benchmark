from collections import defaultdict, deque
import sys

def solve():
    n, m, k = map(int, input().split())
    
    requests = []
    for _ in range(k):
        s, t, d = map(int, input().split())
        requests.append((s, t, d))
    
    edges = []
    edge_dict = {}
    for i in range(m):
        u, v, c = map(int, input().split())
        edges.append((u, v, c))
        edge_dict[(u, v)] = i
    
    # Build graph for flow calculations
    graph = [[] for _ in range(n+1)]
    for i, (u, v, c) in enumerate(edges):
        graph[u].append((v, c, i))
        graph[v].append((u, c, i))  # Add reverse edge for residual graph
    
    def bfs_flow(source, sink, capacity):
        parent = [-1] * (n + 1)
        visited = [False] * (n + 1)
        queue = deque([source])
        visited[source] = True
        
        while queue:
            u = queue.popleft()
            for v, cap, idx in graph[u]:
                if not visited[v] and capacity[idx] > 0:
                    visited[v] = True
                    parent[v] = u
                    queue.append(v)
                    if v == sink:
                        return parent
        return None
    
    def max_flow(source, sink, demand):
        # Initialize capacities
        capacity = [edges[i][2] for i in range(m)]
        flows = [[0] * m for _ in range(k)]
        
        # Try to satisfy each request
        for req_idx, (s, t, d) in enumerate(requests):
            # We need to find a way to send 'd' units from s to t
            # This is essentially solving a multi-commodity flow problem
            # But we'll use a simpler approach: for each request, find a path and try to allocate
            
            # Since this is complex, let's model it as a min-cost max-flow or just path finding
            # For each request, we need to find a flow of 'd' units from s to t
            
            # Let's build a residual graph and try to push flow
            local_flow = [0] * m
            remaining = d
            
            while remaining > 0:
                # Find augmenting path using BFS
                parent = [-1] * (n + 1)
                visited = [False] * (n + 1)
                queue = deque([s])
                visited[s] = True
                
                found_path = False
                while queue and not found_path:
                    u = queue.popleft()
                    for v, cap, edge_idx in graph[u]:
                        if not visited[v] and capacity[edge_idx] - local_flow[edge_idx] > 0:
                            visited[v] = True
                            parent[v] = (u, edge_idx)
                            queue.append(v)
                            if v == t:
                                found_path = True
                                break
                
                if not found_path:
                    return None, None  # Cannot satisfy this request
                
                # Find bottleneck capacity along the path
                path_flow = remaining
                current = t
                path_edges = []
                while current != s:
                    prev_node, edge_idx = parent[current]
                    path_edges.append(edge_idx)
                    path_flow = min(path_flow, capacity[edge_idx] - local_flow[edge_idx])
                    current = prev_node
                
                # Update local flow
                for edge_idx in path_edges:
                    local_flow[edge_idx] += path_flow
                
                remaining -= path_flow
            
            flows[req_idx] = local_flow[:]
            # Update global capacity
            for i in range(m):
                capacity[i] -= local_flow[i]
                
                if capacity[i] < 0:
                    return None, None
        
        return "YES", flows
    
    # Simpler approach: solve each request independently with shared capacity constraints
    # This is a multi-commodity flow problem which is NP-hard in general
    # But since constraints are small, we can try a greedy approach
    
    # Let's try to solve it by modeling it properly
    # For each request, we need to find a flow that satisfies conservation laws
    
    def solve_request(req_idx):
        s, t, d = requests[req_idx]
        
        # Create a local flow network for this request
        # We'll use a simple path-based approach
        local_capacity = [edges[i][2] for i in range(m)]
        # Subtract flows already allocated
        for r in range(req_idx):
            for i in range(m):
                local_capacity[i] -= result_flows[r][i]
                if local_capacity[i] < 0:
                    return None
        
        # Now find d paths from s to t using available capacity
        flow_allocation = [0] * m
        remaining = d
        
        while remaining > 0:
            # Find shortest path with available capacity
            parent = [-1] * (n + 1)
            visited = [False] * (n + 1)
            edge_used = [-1] * (n + 1)
            queue = deque([s])
            visited[s] = True
            
            path_found = False
            while queue:
                u = queue.popleft()
                if u == t:
                    path_found = True
                    break
                for v, cap, edge_idx in graph[u]:
                    if not visited[v] and local_capacity[edge_idx] - flow_allocation[edge_idx] > 0:
                        visited[v] = True
                        parent[v] = u
                        edge_used[v] = edge_idx
                        queue.append(v)
            
            if not path_found:
                return None  # No path found
            
            # Reconstruct path and find bottleneck
            path = []
            current = t
            while current != s:
                path.append(edge_used[current])
                current = parent[current]
            
            # Allocate one unit of flow
            for edge_idx in path:
                flow_allocation[edge_idx] += 1
            remaining -= 1
        
        return flow_allocation
    
    # Try to solve sequentially
    result_flows = []
    total_capacity = [edges[i][2] for i in range(m)]
    
    for req_idx in range(k):
        s, t, d = requests[req_idx]
        
        # Create residual capacity considering previous allocations
        residual_capacity = total_capacity[:]
        for prev_req in range(req_idx):
            for i in range(m):
                residual_capacity[i] -= result_flows[prev_req][i]
        
        # Solve this request with residual capacity
        # Use max-flow algorithm
        # Build a flow network for this single request with current residual capacities
        
        # For simplicity, let's use Ford-Fulkerson
        local_flow = [0] * m
        remaining = d
        
        while remaining > 0:
            # Find augmenting path
            parent = [-1] * (n + 1)
            visited = [False] * (n + 1)
            edge_to = [-1] * (n + 1)
            queue = deque([s])
            visited[s] = True
            
            sink_reached = False
            while queue:
                u = queue.popleft()
                for v, _, edge_idx in graph[u]:
                    if not visited[v] and residual_capacity[edge_idx] - local_flow[edge_idx] > 0:
                        visited[v] = True
                        parent[v] = u
                        edge_to[v] = edge_idx
                        queue.append(v)
                        if v == t:
                            sink_reached = True
                            break
                if sink_reached:
                    break
            
            if not sink_reached:
                print("NO")
                return
            
            # Push one unit of flow
            current = t
            while current != s:
                edge_idx = edge_to[current]
                local_flow[edge_idx] += 1
                current = parent[current]
            
            remaining -= 1
        
        result_flows.append(local_flow)
    
    print("YES")
    for flow in result_flows:
        print(*flow)

solve()