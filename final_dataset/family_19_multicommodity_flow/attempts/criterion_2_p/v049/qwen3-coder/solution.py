from collections import defaultdict, deque

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    n = int(data[index])
    index += 1
    m = int(data[index])
    index += 1
    _ = int(data[index])
    index += 1
    
    s = int(data[index])
    index += 1
    t = int(data[index])
    index += 1
    d = int(data[index])
    index += 1
    
    edges = []
    graph = defaultdict(list)
    capacity = []
    
    for i in range(m):
        u = int(data[index])
        index += 1
        v = int(data[index])
        index += 1
        cap = int(data[index])
        index += 1
        edges.append((u, v, cap))
        graph[u].append((v, i, cap))   # node, edge_index, capacity
        graph[v].append((u, i, 0))     # reverse edge with 0 capacity initially
        capacity.append(cap)
    
    # We need to model this as a circulation problem with demands.
    # To do so, we add an edge from t to s with demand d (lower bound d, upper bound d).
    # This ensures that exactly d units flow from s to t.
    # But to convert lower bounds to circulation, we transform the problem.
    
    # However, let's instead use the standard approach:
    # Create super-source S and super-sink T.
    # Connect S to s with capacity d.
    # Connect t to T with capacity d.
    # All original edges have capacities as given.
    # Then find a max flow from S to T. If it's d, then we can satisfy the demand.
    
    # Actually, let's think differently. 
    # We want to send exactly d units from s to t.
    # So we create a flow network:
    # - Add a new source S and sink T
    # - Edge S -> s with capacity d
    # - Edge t -> T with capacity d
    # - Original edges with their capacities
    # Find max flow from S to T. If it's less than d, return NO.
    # Otherwise, extract the flow values.
    
    # Let's assign indices:
    # Nodes: 1 to n, plus S = n+1, T = n+2
    S = n + 1
    T = n + 2
    
    # Build the extended graph for flow
    extended_graph = defaultdict(list)
    edge_list = []  # list of (from, to, capacity, reverse_index)
    
    # Add original edges
    for u, v, cap in edges:
        forward_idx = len(edge_list)
        edge_list.append((u, v, cap, len(extended_graph[v])))
        extended_graph[u].append(forward_idx)
        
        backward_idx = len(edge_list)
        edge_list.append((v, u, 0, len(extended_graph[u]) - 1))
        extended_graph[v].append(backward_idx)
    
    # Add S -> s with capacity d
    forward_idx = len(edge_list)
    edge_list.append((S, s, d, len(extended_graph[s])))
    extended_graph[S].append(forward_idx)
    
    backward_idx = len(edge_list)
    edge_list.append((s, S, 0, len(extended_graph[S]) - 1))
    extended_graph[s].append(backward_idx)
    
    # Add t -> T with capacity d
    forward_idx = len(edge_list)
    edge_list.append((t, T, d, len(extended_graph[T])))
    extended_graph[t].append(forward_idx)
    
    backward_idx = len(edge_list)
    edge_list.append((T, t, 0, len(extended_graph[t]) - 1))
    extended_graph[T].append(backward_idx)
    
    def bfs():
        parent = [-1] * (n + 3)
        parent_edge = [-1] * (n + 3)
        queue = deque([S])
        parent[S] = -2  # Special marker
        
        while queue:
            u = queue.popleft()
            if u == T:
                break
            for e_idx in extended_graph[u]:
                to, _, cap, _ = edge_list[e_idx]
                if parent[to] == -1 and cap > 0:
                    parent[to] = u
                    parent_edge[to] = e_idx
                    queue.append(to)
                    if to == T:
                        break
        return parent, parent_edge
    
    def edmonds_karp():
        flow = [0] * len(edge_list)
        while True:
            parent, parent_edge = bfs()
            if parent[T] == -1:
                break
            
            # Find minimum capacity along the path
            path_flow = float('inf')
            s_ptr = T
            while s_ptr != S:
                e_idx = parent_edge[s_ptr]
                path_flow = min(path_flow, edge_list[e_idx][2])
                s_ptr = parent[s_ptr]
            
            # Update residual capacities
            s_ptr = T
            while s_ptr != S:
                e_idx = parent_edge[s_ptr]
                edge_list[e_idx] = (edge_list[e_idx][0], edge_list[e_idx][1], 
                                    edge_list[e_idx][2] - path_flow, edge_list[e_idx][3])
                
                # Update reverse edge
                rev_idx = e_idx ^ 1
                edge_list[rev_idx] = (edge_list[rev_idx][0], edge_list[rev_idx][1], 
                                      edge_list[rev_idx][2] + path_flow, edge_list[rev_idx][3])
                
                s_ptr = parent[s_ptr]
        
        # Check if max flow is d
        total_flow = 0
        for e_idx in extended_graph[S]:
            total_flow += edge_list[e_idx ^ 1][2]  # Flow on reverse edge
        
        if total_flow < d:
            return None
        
        # Extract flows on original edges
        result = [0] * m
        for i in range(m):
            # The forward edge was at index 2*i in the original list
            # But now we need to map correctly
            # Let's rebuild mapping
            pass
        
        # Let's restructure to keep track of original edge indices
        # Rebuild with proper tracking
        
        # Alternative simpler approach:
        # Since we know the structure, let's just run max flow and check
        
        # But to get the actual flows, we need to track them.
        # Let's redo with explicit flow tracking
        
        pass
    
    # Let's implement a cleaner version
    
    # Map original edges to their indices in edge_list
    edge_map = {}
    new_edge_list = []
    
    # Rebuild with flow tracking
    idx_original_edges = []
    
    extended_graph_clean = defaultdict(list)
    all_edges = []
    
    # Add original edges
    for i, (u, v, cap) in enumerate(edges):
        forward_idx = len(all_edges)
        all_edges.append([u, v, cap, 0])  # [from, to, capacity, flow]
        extended_graph_clean[u].append(len(extended_graph_clean[u]))
        extended_graph_clean[v].append(len(extended_graph_clean[v]))
        idx_original_edges.append(forward_idx)
        
        backward_idx = len(all_edges)
        all_edges.append([v, u, 0, 0])
        
    # Add S->s and t->T
    all_edges.append([S, s, d, 0])
    extended_graph_clean[S].append(len(extended_graph_clean[S]))
    extended_graph_clean[s].append(len(extended_graph_clean[s]))
    
    all_edges.append([t, T, d, 0])
    extended_graph_clean[t].append(len(extended_graph_clean[t]))
    extended_graph_clean[T].append(len(extended_graph_clean[T]))
    
    # This is getting complex. Let's use a known working max-flow implementation.
    
    # For simplicity, let's assume we can use a library or known algorithm.
    # But since we're coding from scratch, let's try a different modeling.
    
    # Model the problem directly as a circulation with demands:
    # - Each normal edge has 0 demand, [0, capacity] flow
    # - Super source connects to s with demand d => edge [d,d]
    # - t connects to super sink with demand d => edge [d,d]
    # - super source connects to super sink with [0, inf] to balance
    
    # But converting to circulation with lower bounds is tricky.
    
    # Simpler: Create flow network:
    # Source connects to s with capacity d
    # t connects to sink with capacity d
    # Max flow should be d
    
    # Implement Dinic's or Edmonds-Karp
    
    # Let's do Edmonds-Karp properly
    
    class FlowNetwork:
        def __init__(self, n_nodes):
            self.n = n_nodes
            self.graph = defaultdict(lambda: defaultdict(int))  # adj matrix like
            self.adj = defaultdict(list)
        
        def add_edge(self, u, v, cap):
            self.graph[u][v] += cap
            if cap > 0 and v not in self.adj[u]:
                self.adj[u].append(v)
            if cap > 0 and u not in self.adj[v]:
                self.adj[v].append(u)
        
        def bfs(self, s, t, parent):
            visited = [False] * (self.n)
            queue = deque([s])
            visited[s] = True
            parent[s] = -1
            
            while queue:
                u = queue.popleft()
                for v in self.adj[u]:
                    if not visited[v] and self.graph[u][v] > 0:
                        queue.append(v)
                        parent[v] = u
                        visited[v] = True
                        if v == t:
                            return True
            return False
        
        def ford_fulkerson(self, source, sink):
            parent = [-1] * (self.n)
            max_flow = 0
            
            while self.bfs(source, sink, parent):
                path_flow = float("Inf")
                s = sink
                while s != source:
                    path_flow = min(path_flow, self.graph[parent[s]][s])
                    s = parent[s]
                
                v = sink
                while v != source:
                    u = parent[v]
                    self.graph[u][v] -= path_flow
                    self.graph[v][u] += path_flow
                    v = parent[v]
                
                max_flow += path_flow
            
            return max_flow
    
    # Now build the network
    fn = FlowNetwork(n + 3)  # 1..n, S=n+1, T=n+2
    S_node = n + 1
    T_node = n + 2
    
    # Add original edges
    for u, v, cap in edges:
        fn.add_edge(u, v, cap)
    
    # Add S -> s and t -> T
    fn.add_edge(S_node, s, d)
    fn.add_edge(t, T_node, d)
    
    max_flow = fn.ford_fulkerson(S_node, T_node)
    
    if max_flow < d:
        print("NO")
        return
    
    # Extract flow values
    flow_values = []
    for u, v, cap in edges:
        # The flow is cap - residual_capacity
        flow = cap - fn.graph[u][v]
        flow_values.append(flow)
    
    print("YES")
    print(" ".join(map(str, flow_values)))

solve()