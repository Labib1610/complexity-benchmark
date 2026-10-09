from collections import defaultdict, deque

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    m = int(data[idx+1])
    idx += 3
    
    s = int(data[idx])
    t = int(data[idx+1])
    d = int(data[idx+2])
    idx += 3
    
    edges = []
    graph = defaultdict(list)
    capacity = []
    
    for i in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        cap = int(data[idx+2])
        idx += 3
        edges.append((u, v))
        graph[u].append((v, i))
        graph[v].append((u, i))
        capacity.append(cap)
    
    # We will model this as a max-flow problem
    # Build a flow network with source 's' and sink 't'
    # Nodes are numbered 1..n
    # We'll use Ford-Fulkerson with BFS (Edmonds-Karp)
    
    # But we need to check if we can send exactly 'd' units
    # So we'll compute max flow and see if it >= d
    
    # Actually, let's build residual graph and run max flow
    # But since we want exactly d, we can also do it directly
    
    # Let's model it as min-cost max-flow, but since all costs are 0,
    # it's just max-flow. We just need to check if max flow >= d
    
    # But actually, we can formulate it as a circulation problem with demands
    # Or even simpler, just max flow from s to t with edge capacities
    
    # Let's implement Edmonds-Karp
    
    def bfs(residual_graph, s, t, parent):
        visited = [False] * (n + 1)
        queue = deque([s])
        visited[s] = True
        
        while queue:
            u = queue.popleft()
            
            for v, edge_idx in residual_graph[u]:
                if not visited[v] and residual_graph[u][residual_graph[u].index((v, edge_idx))][1] > 0:
                    visited[v] = True
                    parent[v] = (u, edge_idx)
                    queue.append(v)
                    if v == t:
                        return True
        return False
    
    # Build residual graph
    res_graph = [[] for _ in range(n + 1)]
    forward_edges = {}
    backward_edges = {}
    
    for i in range(m):
        u, v = edges[i]
        cap = capacity[i]
        # Add forward edge
        res_graph[u].append((v, cap, i))  # (to, capacity, original_index)
        forward_edges[(u, v, i)] = len(res_graph[u]) - 1
        # Add backward edge with 0 capacity
        res_graph[v].append((u, 0, i))
        backward_edges[(v, u, i)] = len(res_graph[v]) - 1
    
    # To make indexing easier, let's store the residual graph differently
    # Let's use adjacency list with edge indices
    
    # Actually, let's rebuild with proper structure
    res_cap = [0] * (2 * m)  # forward and backward edges
    edge_info = []  # (from, to, original_index, is_forward)
    
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        u, v = edges[i]
        cap = capacity[i]
        # Forward edge
        adj[u].append((v, len(edge_info)))
        edge_info.append((u, v, i, True))
        res_cap[len(edge_info) - 1] = cap
        # Backward edge
        adj[v].append((u, len(edge_info)))
        edge_info.append((v, u, i, False))
        res_cap[len(edge_info) - 1] = 0
    
    parent = [-1] * (n + 1)
    
    def bfs_flow():
        visited = [False] * (n + 1)
        queue = deque([s])
        visited[s] = True
        parent = [-1] * (n + 1)
        
        while queue:
            u = queue.popleft()
            for v, edge_idx in adj[u]:
                if not visited[v] and res_cap[edge_idx] > 0:
                    visited[v] = True
                    parent[v] = (u, edge_idx)
                    queue.append(v)
                    if v == t:
                        return parent
        return None
    
    max_flow = 0
    flow_on_edge = [0] * m
    
    while True:
        parent_info = bfs_flow()
        if parent_info is None or parent_info[t] == -1:
            break
            
        # Find minimum capacity along the path
        path_flow = float('inf')
        curr = t
        path_edges = []
        while curr != s:
            prev, edge_idx = parent_info[curr]
            path_flow = min(path_flow, res_cap[edge_idx])
            path_edges.append((edge_idx, prev, curr))
            curr = prev
            
        # Update residual capacities
        for edge_idx, _, _ in path_edges:
            res_cap[edge_idx] -= path_flow
            # Find the reverse edge index
            # This is tricky; let's find a better way
            
        # Update flows
        curr = t
        while curr != s:
            prev, edge_idx = parent_info[curr]
            from_node, to_node, orig_idx, is_forward = edge_info[edge_idx]
            if is_forward:
                flow_on_edge[orig_idx] += path_flow
            else:
                flow_on_edge[orig_idx] -= path_flow
            curr = prev
            
        max_flow += path_flow
        if max_flow >= d:
            break
    
    if max_flow < d:
        print("NO")
        return
    
    # Now we have a flow of at least d, we need exactly d
    # If max_flow > d, we need to reduce the flow by (max_flow - d)
    # But the problem asks for any valid allocation, so we can just output the flow
    
    # However, we might have floating point issues or over-flowed
    # Since we're dealing with integers, let's scale down if needed
    
    # Actually, let's re-run max flow with capacity scaling to get exactly d
    # Or we can just take the first d units of flow
    
    # Let's restart with a cleaner implementation
    
    pass
    

def solve_clean():
    import sys
    from collections import deque
    
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    m = int(data[idx+1])
    idx += 3
    
    s = int(data[idx])
    t = int(data[idx+1])
    d = int(data[idx+2])
    idx += 3
    
    edges = []
    capacity = []
    
    for i in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        cap = int(data[idx+2])
        idx += 3
        edges.append((u, v))
        capacity.append(cap)
    
    # Max flow implementation
    # Build adjacency list with edge indices
    adj = [[] for _ in range(n + 1)]  # adj[u] = [(v, edge_idx), ...]
    edge_list = []  # Store (from, to, capacity, flow)
    
    for i in range(m):
        u, v = edges[i]
        cap = capacity[i]
        # Forward edge
        adj[u].append(len(edge_list))
        edge_list.append([u, v, cap, 0])
        # Backward edge
        adj[v].append(len(edge_list))
        edge_list.append([v, u, 0, 0])
    
    def bfs():
        parent = [-1] * (n + 1)
        visited = [False] * (n + 1)
        q = deque([s])
        visited[s] = True
        
        while q:
            u = q.popleft()
            for edge_idx in adj[u]:
                v = edge_list[edge_idx][1]
                cap, flow = edge_list[edge_idx][2], edge_list[edge_idx][3]
                if not visited[v] and cap > flow:
                    visited[v] = True
                    parent[v] = (u, edge_idx)
                    q.append(v)
                    if v == t:
                        return parent
        return None
    
    # Run Ford-Fulkerson
    total_flow = 0
    while total_flow < d:
        parent = bfs()
        if parent is None or parent[t] == -1:
            break
            
        # Find bottleneck
        path_flow = d - total_flow
        curr = t
        while curr != s:
            prev, edge_idx = parent[curr]
            cap, flow = edge_list[edge_idx][2], edge_list[edge_idx][3]
            path_flow = min(path_flow, cap - flow)
            curr = prev
            
        # Update flows
        curr = t
        while curr != s:
            prev, edge_idx = parent[curr]
            edge_list[edge_idx][3] += path_flow
            # Backward edge is edge_idx ^ 1
            edge_list[edge_idx ^ 1][3] -= path_flow
            curr = prev
            
        total_flow += path_flow
    
    if total_flow < d:
        print("NO")
        return
        
    # Extract flow on original edges
    result = []
    for i in range(0, len(edge_list), 2):
        result.append(str(edge_list[i][3]))
        
    print("YES")
    print(" ".join(result))

solve_clean()