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
    graph = defaultdict(list)
    capacity = []
    edge_index = {}
    
    for i in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        w = int(data[idx])
        idx += 1
        
        edges.append((u, v, w))
        graph[u].append((v, i))
        graph[v].append((u, i))
        capacity.append(w)
        edge_index[(u, v)] = i
    
    # Create residual graph for max flow
    # We'll use Ford-Fulkerson with BFS (Edmonds-Karp)
    
    def bfs_flow():
        # Build adjacency list with capacities
        adj = [[] for _ in range(n+1)]
        forward_edges = [{} for _ in range(n+1)]
        backward_edges = [{} for _ in range(n+1)]
        
        edge_ids = []
        
        for i, (u, v, w) in enumerate(edges):
            if w > 0:
                forward_edges[u][v] = forward_edges[u].get(v, 0) + w
                backward_edges[v][u] = backward_edges[v].get(u, 0) + w
                
                if v not in adj[u]:
                    adj[u].append(v)
                if u not in adj[v]:
                    adj[v].append(u)
        
        # Edmonds-Karp implementation
        parent = [-1] * (n+1)
        parent_edge = [-1] * (n+1)
        
        def bfs(source, sink):
            visited = [False] * (n+1)
            queue = deque([source])
            visited[source] = True
            
            while queue:
                u = queue.popleft()
                
                for v in adj[u]:
                    if not visited[v]:
                        # Check forward edge
                        if v in forward_edges[u] and forward_edges[u][v] > 0:
                            parent[v] = u
                            parent_edge[v] = edge_index.get((u,v), -1)
                            if v == sink:
                                return True
                            queue.append(v)
                            visited[v] = True
                        # Check backward edge
                        elif u in backward_edges[v] and backward_edges[v][u] > 0:
                            parent[v] = u
                            parent_edge[v] = edge_index.get((v,u), -1)
                            if v == sink:
                                return True
                            queue.append(v)
                            visited[v] = True
            return False
        
        max_flow = 0
        flow_on_edges = [0] * m
        
        while bfs(s, t):
            path_flow = float('inf')
            v = t
            
            # Find minimum capacity along the path
            while v != s:
                u = parent[v]
                if parent_edge[v] != -1:
                    edge_id = parent_edge[v]
                    if (u, v) in edge_index:
                        path_flow = min(path_flow, forward_edges[u][v])
                    else:
                        path_flow = min(path_flow, backward_edges[v][u])
                v = u
            
            # Update residual capacities and record flows
            v = t
            while v != s:
                u = parent[v]
                if parent_edge[v] != -1:
                    edge_id = parent_edge[v]
                    if (u, v) in edge_index:
                        # Forward edge
                        forward_edges[u][v] -= path_flow
                        if (v, u) not in backward_edges:
                            backward_edges[v][u] = 0
                        backward_edges[v][u] += path_flow
                        flow_on_edges[edge_id] += path_flow
                    else:
                        # Backward edge
                        backward_edges[u][v] -= path_flow
                        if (v, u) not in forward_edges:
                            forward_edges[v][u] = 0
                        forward_edges[v][u] += path_flow
                        flow_on_edges[edge_id] -= path_flow
                v = u
            
            max_flow += path_flow
        
        return max_flow, flow_on_edges
    
    # But we need to handle this differently since we want to send exactly 'd' units
    
    # Let's model this as a max flow problem where we want to send exactly d units
    # If max flow < d, then impossible. Otherwise, we can scale down if needed.
    
    # Actually, let's just run max flow and see if we can get at least d
    
    def max_flow_value(source, sink):
        # Build adjacency with capacities
        fwd_cap = [{} for _ in range(n+1)]
        bwd_cap = [{} for _ in range(n+1)]
        
        for i, (u, v, w) in enumerate(edges):
            if w > 0:
                if v not in fwd_cap[u]:
                    fwd_cap[u][v] = 0
                if u not in bwd_cap[v]:
                    bwd_cap[v][u] = 0
                fwd_cap[u][v] += w
                bwd_cap[v][u] += w
        
        def bfs():
            parent = [-1] * (n+1)
            visited = [False] * (n+1)
            queue = deque([source])
            visited[source] = True
            
            while queue:
                u = queue.popleft()
                for v in fwd_cap[u]:
                    if not visited[v] and fwd_cap[u][v] > 0:
                        parent[v] = u
                        visited[v] = True
                        queue.append(v)
                        if v == sink:
                            return parent
                for v in bwd_cap[u]:  # Backward edges
                    if not visited[v] and bwd_cap[u][v] > 0:
                        parent[v] = u
                        visited[v] = True
                        queue.append(v)
                        if v == sink:
                            return parent
            return None
        
        flow = 0
        while flow < d:
            parent = bfs()
            if parent is None:
                break
            
            # Find bottleneck
            path_flow = float('inf')
            s_node = sink
            path_edges = []
            
            while s_node != source:
                p = parent[s_node]
                if s_node in fwd_cap[p]:
                    path_flow = min(path_flow, fwd_cap[p][s_node])
                    path_edges.append((p, s_node, 'f'))
                else:
                    path_flow = min(path_flow, bwd_cap[s_node][p])
                    path_edges.append((s_node, p, 'b'))
                s_node = p
            
            path_flow = min(path_flow, d - flow)
            
            if path_flow <= 0:
                break
                
            # Update capacities
            s_node = sink
            while s_node != source:
                p = parent[s_node]
                if s_node in fwd_cap[p]:
                    fwd_cap[p][s_node] -= path_flow
                    if p not in bwd_cap[s_node]:
                        bwd_cap[s_node][p] = 0
                    bwd_cap[s_node][p] += path_flow
                else:
                    bwd_cap[s_node][p] -= path_flow
                    if p not in fwd_cap[s_node]:
                        fwd_cap[s_node][p] = 0
                    fwd_cap[s_node][p] += path_flow
                s_node = p
            
            flow += path_flow
        
        return flow
    
    # For getting actual flow values, let's do a proper flow computation
    
    # Use network simplex or just run Ford-Fulkerson properly
    
    # Let's build the flow network properly
    
    def edmonds_karp_max_flow(source, sink):
        # Initialize flow
        flow_values = [0] * m
        
        # Residual graph representation
        fwd_adj = [{} for _ in range(n+1)]   # forward edges
        bwd_adj = [{} for _ in range(n+1)]   # backward edges
        edge_map = {}  # map (u,v) -> index
        
        for i, (u, v, cap) in enumerate(edges):
            if cap > 0:
                if v not in fwd_adj[u]:
                    fwd_adj[u][v] = 0
                if u not in bwd_adj[v]:
                    bwd_adj[v][u] = 0
                fwd_adj[u][v] += cap
                edge_map[(u, v)] = i
        
        def bfs_find_path(src, dst):
            parent = [-1] * (n+1)
            edge_used = [''] * (n+1)  # 'f' for forward, 'b' for backward
            visited = [False] * (n+1)
            q = deque([src])
            visited[src] = True
            
            while q:
                u = q.popleft()
                # Check forward edges
                for v in fwd_adj[u]:
                    if not visited[v] and fwd_adj[u][v] > 0:
                        parent[v] = u
                        edge_used[v] = 'f'
                        if v == dst:
                            return parent, edge_used
                        visited[v] = True
                        q.append(v)
                # Check backward edges
                for v in bwd_adj[u]:
                    if not visited[v] and bwd_adj[u][v] > 0:
                        parent[v] = u
                        edge_used[v] = 'b'
                        if v == dst:
                            return parent, edge_used
                        visited[v] = True
                        q.append(v)
            return None, None
        
        total_flow = 0
        while total_flow < d:
            parent, edge_used = bfs_find_path(source, sink)
            if parent is None:
                break
                
            # Find path flow
            path_flow = float('inf')
            cur = sink
            path = []
            while cur != source:
                prev = parent[cur]
                if edge_used[cur] == 'f':
                    path_flow = min(path_flow, fwd_adj[prev][cur])
                    path.append((prev, cur, 'f'))
                else:  # 'b'
                    path_flow = min(path_flow, bwd_adj[prev][cur])
                    path.append((prev, cur, 'b'))
                cur = prev
            
            path_flow = min(path_flow, d - total_flow)
            if path_flow <= 0:
                break
            
            # Update residual graph
            for u, v, direction in path:
                if direction == 'f':
                    fwd_adj[u][v] -= path_flow
                    if u not in bwd_adj[v]:
                        bwd_adj[v][u] = 0
                    bwd_adj[v][u] += path_flow
                    if (u, v) in edge_map:
                        flow_values[edge_map[(u, v)]] += path_flow
                else:  # 'b'
                    bwd_adj[u][v] -= path_flow
                    if u not in fwd_adj[v]:
                        fwd_adj[v][u] = 0
                    fwd_adj[v][u] += path_flow
                    if (v, u) in edge_map:
                        flow_values[edge_map[(v, u)]] -= path_flow
            
            total_flow += path_flow
        
        return total_flow, flow_values
    
    max_flow_possible, flows = edmonds_karp_max_flow(s, t)
    
    if max_flow_possible >= d:
        # We can send at least d, now adjust to exactly d
        # Since we're sending exactly what we computed, and our algorithm sends exactly d,
        # the flows should already be correct
        
        # Need to ensure we don't exceed capacities
        result_flows = []
        for i in range(m):
            f = flows[i]
            if f < 0:
                f = 0
            elif f > capacity[i]:
                f = capacity[i]
            result_flows.append(int(f))
            
        print("YES")
        print(' '.join(map(str, result_flows)))
    else:
        print("NO")

solve()