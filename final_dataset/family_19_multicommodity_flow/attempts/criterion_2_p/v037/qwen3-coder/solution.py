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
    
    s = int(data[idx])
    idx += 1
    t = int(data[idx])
    idx += 1
    d = int(data[idx])
    idx += 1
    
    edges = []
    edge_info = []
    graph = defaultdict(list)
    capacity = []
    
    for i in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        w = int(data[idx])
        idx += 1
        edges.append((u, v))
        edge_info.append((u, v, w))
        graph[u].append((v, i))
        graph[v].append((u, i))
        capacity.append(w)
    
    # Build the network flow graph
    # We'll use Ford-Fulkerson with BFS (Edmonds-Karp)
    
    # Create adjacency list for residual graph
    adj = [[] for _ in range(n+1)]
    for i in range(m):
        u, v = edges[i]
        adj[u].append(i)
        adj[v].append(i)
    
    def bfs(source, sink, cap, flow):
        parent = [-1] * (n + 1)
        parent_edge = [-1] * (n + 1)
        visited = [False] * (n + 1)
        queue = deque([source])
        visited[source] = True
        
        while queue:
            u = queue.popleft()
            if u == sink:
                break
            for e_idx in adj[u]:
                u_e, v_e, _ = edge_info[e_idx]
                residual_capacity = cap[e_idx] - flow[e_idx]
                # Check if this edge is in the correct direction
                if u_e == u and residual_capacity > 0 and not visited[v_e]:
                    visited[v_e] = True
                    parent[v_e] = u
                    parent_edge[v_e] = e_idx
                    queue.append(v_e)
                elif v_e == u and flow[e_idx] > 0 and not visited[u_e]:
                    visited[u_e] = True
                    parent[u_e] = u
                    parent_edge[u_e] = e_idx
                    queue.append(u_e)
        
        if not visited[sink]:
            return None
        
        # Find minimum residual capacity along the path
        path_flow = float('inf')
        s_node = sink
        while s_node != source:
            e_idx = parent_edge[s_node]
            u_e, v_e, _ = edge_info[e_idx]
            if v_e == s_node:
                # Forward edge
                path_flow = min(path_flow, cap[e_idx] - flow[e_idx])
            else:
                # Backward edge
                path_flow = min(path_flow, flow[e_idx])
            s_node = parent[s_node]
        
        # Update residual capacities
        s_node = sink
        while s_node != source:
            e_idx = parent_edge[s_node]
            u_e, v_e, _ = edge_info[e_idx]
            if v_e == s_node:
                # Forward edge
                flow[e_idx] += path_flow
            else:
                # Backward edge
                flow[e_idx] -= path_flow
            s_node = parent[s_node]
        
        return path_flow
    
    # Max flow algorithm
    flow = [0] * m
    max_flow = 0
    
    while True:
        path_flow = bfs(s, t, capacity, flow)
        if path_flow is None:
            break
        max_flow += path_flow
        if max_flow >= d:
            break
    
    if max_flow < d:
        print("NO")
        return
    
    # Now we need to find a feasible flow of exactly d
    # We can scale down if max_flow > d
    if max_flow > d:
        # This shouldn't happen in our implementation since we stop when we reach d
        # But let's handle it anyway
        pass
    
    # Check if we can send exactly d units
    # Let's re-run with a modified approach to get exactly d
    
    # Reset flow
    flow = [0] * m
    
    # Send flow until we reach exactly d
    sent = 0
    while sent < d:
        path_flow = bfs(s, t, capacity, flow)
        if path_flow is None:
            print("NO")
            return
        if sent + path_flow > d:
            # Send only what's needed
            diff = d - sent
            # We need to adjust the last augmenting path
            # This is complex, so let's use a different approach
            
            # Let's find a path and send exactly the remaining amount
            parent = [-1] * (n + 1)
            parent_edge = [-1] * (n + 1)
            visited = [False] * (n + 1)
            queue = deque([s])
            visited[s] = True
            
            found = False
            while queue:
                u = queue.popleft()
                if u == t:
                    found = True
                    break
                for e_idx in adj[u]:
                    u_e, v_e, _ = edge_info[e_idx]
                    residual_capacity = capacity[e_idx] - flow[e_idx]
                    # Check if this edge is in the correct direction
                    if u_e == u and residual_capacity > 0 and not visited[v_e]:
                        visited[v_e] = True
                        parent[v_e] = u
                        parent_edge[v_e] = e_idx
                        queue.append(v_e)
            
            if not found:
                print("NO")
                return
                
            # Find the minimum residual capacity along this path
            min_cap = float('inf')
            s_node = t
            path_edges = []
            while s_node != s:
                e_idx = parent_edge[s_node]
                path_edges.append(e_idx)
                u_e, v_e, _ = edge_info[e_idx]
                if v_e == s_node:
                    # Forward edge
                    min_cap = min(min_cap, capacity[e_idx] - flow[e_idx])
                else:
                    # Backward edge
                    min_cap = min(min_cap, flow[e_idx])
                s_node = parent[s_node]
            
            # Send exactly what's needed
            to_send = d - sent
            for e_idx in path_edges:
                u_e, v_e, _ = edge_info[e_idx]
                if v_e == parent[u_e]:  # Forward edge in path
                    flow[e_idx] += to_send
                else:  # Backward edge in path
                    flow[e_idx] -= to_send
            sent = d
        else:
            sent += path_flow
    
    print("YES")
    print(' '.join(map(str, flow)))

solve()