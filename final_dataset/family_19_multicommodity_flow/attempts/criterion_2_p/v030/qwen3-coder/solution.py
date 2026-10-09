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
    indeg = defaultdict(int)
    outdeg = defaultdict(int)
    
    limits = []
    edge_map = {}
    
    for i in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        limit = int(data[idx])
        idx += 1
        
        edges.append((u, v, limit))
        edge_map[(u, v, i)] = len(limits)
        limits.append(limit)
        graph[u].append((v, i))
        outdeg[u] += 1
        indeg[v] += 1
    
    # Build network flow graph
    # Nodes: 0 to n+1
    # 0: source, n+1: sink
    # 1 to n: facilities
    # n+2 to n+1+m: edge variables
    
    # But we'll model it as min-cost max-flow or just use max-flow with constraints
    # We'll create a flow network where:
    # - Each edge has capacity = limit
    # - Each intermediate node (not s,t) has flow conservation
    # - Node s has net flow out of d
    # - Node t has net flow in of d
    
    # Let's use a standard approach: build constraint matrix and use simplex or check feasibility
    # But since this is a programming contest, let's try to model it as a max-flow problem
    
    # However, since we need EXACTLY d flow, we can model it as:
    # - Source connects to s with capacity d
    # - t connects to sink with capacity d
    # - All other nodes have demand 0 (flow conservation)
    # - Each edge has capacity limits[i]
    
    # But actually, we want to find a feasible flow where:
    # For node s: out_flow - in_flow = d
    # For node t: in_flow - out_flow = d
    # For others: in_flow = out_flow
    
    # This is a circulation problem with demands.
    # Convert to max-flow:
    # - Add edge t -> s with capacity d (to return flow)
    # - Now all nodes have balance 0
    # - Edge capacities are original limits
    # - Find a feasible flow
    
    # But we want to find a feasible solution, not necessarily maximum.
    # So we can add a super-source and super-sink:
    # - Connect super-source to s with capacity d
    # - Connect t to super-sink with capacity d
    # - Solve max-flow = d
    
    # Let's implement Ford-Fulkerson or Dinic's algorithm
    
    # Number of nodes: 0..n (facilities), n+1 (super-source), n+2 (super-sink)
    SOURCE = n + 1
    SINK = n + 2
    EDGE_START = n + 3
    EDGE_END = n + 2 + m
    
    # Total nodes: 0..n+2+m
    total_nodes = n + 3 + m
    
    # Build adjacency list for residual graph
    res_graph = [[] for _ in range(total_nodes)]
    
    # Add edges with capacities
    edge_ids = []  # To track original edges
    
    # Original edges
    for i in range(m):
        u, v, limit = edges[i]
        # Forward edge: u -> v, capacity limit
        # Backward edge: v -> u, capacity 0 initially
        res_graph[u].append([v, limit, len(res_graph[v]), True, i])  # [to, cap, rev_index, is_real_edge, id]
        res_graph[v].append([u, 0, len(res_graph[u]) - 1, False, -1])
        edge_ids.append(len(res_graph[u]) - 1)  # index of backward edge in u's list
    
    # Connect super-source to s with capacity d
    res_graph[SOURCE].append([s, d, len(res_graph[s]), True, -2])
    res_graph[s].append([SOURCE, 0, len(res_graph[SOURCE]) - 1, False, -1])
    
    # Connect t to super-sink with capacity d
    res_graph[t].append([SINK, d, len(res_graph[SINK]), True, -2])
    res_graph[SINK].append([t, 0, len(res_graph[t]) - 1, False, -1])
    
    def bfs():
        parent = [-1] * total_nodes
        parent_edge = [-1] * total_nodes
        q = deque()
        q.append(SOURCE)
        parent[SOURCE] = SOURCE
        while q:
            u = q.popleft()
            for i, (v, cap, rev_idx, is_real, eid) in enumerate(res_graph[u]):
                if parent[v] == -1 and cap > 0:
                    parent[v] = u
                    parent_edge[v] = i
                    if v == SINK:
                        return parent, parent_edge
                    q.append(v)
        return parent, parent_edge
    
    def edmonds_karp():
        max_flow = 0
        while True:
            parent, parent_edge = bfs()
            if parent[SINK] == -1:
                break
            # Find minimum capacity along the path
            path_flow = float('inf')
            s_node = SINK
            while s_node != SOURCE:
                u = parent[s_node]
                edge_idx = parent_edge[s_node]
                path_flow = min(path_flow, res_graph[u][edge_idx][1])
                s_node = u
            
            # Update residual capacities
            s_node = SINK
            while s_node != SOURCE:
                u = parent[s_node]
                edge_idx = parent_edge[s_node]
                # Decrease forward edge
                res_graph[u][edge_idx][1] -= path_flow
                # Increase backward edge
                rev_idx = res_graph[u][edge_idx][2]
                res_graph[s_node][rev_idx][1] += path_flow
                s_node = u
            
            max_flow += path_flow
        return max_flow
    
    flow_value = edmonds_karp()
    
    if flow_value < d:
        print("NO")
        return
    
    # Extract flow values for original edges
    flow_values = [0] * m
    for i in range(m):
        u, v, limit = edges[i]
        # The backward edge in v's list corresponds to the forward edge u->v
        # We stored the index of the backward edge in u's list in edge_ids[i]
        # Actually, let's restructure this more clearly
        pass
    
    # Let's rebuild with clearer indexing
    # Rebuild residual graph with explicit tracking
    res_graph = [[] for _ in range(total_nodes)]
    edge_flows = [0] * m  # To store final flows
    
    # Re-add edges with proper indexing
    edge_info = []  # List of (from, to, capacity, flow_index)
    
    for i in range(m):
        u, v, limit = edges[i]
        # Forward: u -> v
        res_graph[u].append([v, limit, 0, len(res_graph[v]), i])  # [to, cap, flow, rev_index, id]
        # Backward: v -> u
        res_graph[v].append([u, 0, 0, len(res_graph[u]) - 1, -1])
        edge_info.append((u, v, limit, i))
    
    # Super source to s
    res_graph[SOURCE].append([s, d, 0, len(res_graph[s]), -2])
    res_graph[s].append([SOURCE, 0, 0, len(res_graph[SOURCE]) - 1, -1])
    
    # t to super sink
    res_graph[t].append([SINK, d, 0, len(res_graph[SINK]), -2])
    res_graph[SINK].append([t, 0, 0, len(res_graph[t]) - 1, -1])
    
    def bfs():
        parent = [-1] * total_nodes
        parent_edge = [-1] * total_nodes
        q = deque()
        q.append(SOURCE)
        parent[SOURCE] = SOURCE
        while q:
            u = q.popleft()
            for i, edge in enumerate(res_graph[u]):
                v, cap, flow, rev_idx, eid = edge
                if parent[v] == -1 and cap > flow:
                    parent[v] = u
                    parent_edge[v] = i
                    if v == SINK:
                        return parent, parent_edge
                    q.append(v)
        return parent, parent_edge
    
    def edmonds_karp_v2():
        while True:
            parent, parent_edge = bfs()
            if parent[SINK] == -1:
                break
            path_flow = float('inf')
            s_node = SINK
            path_edges = []
            while s_node != SOURCE:
                u = parent[s_node]
                edge_idx = parent_edge[s_node]
                u_edge = res_graph[u][edge_idx]
                path_flow = min(path_flow, u_edge[1] - u_edge[2])  # cap - flow
                path_edges.append((u, edge_idx))
                s_node = u
            
            for u, edge_idx in path_edges:
                res_graph[u][edge_idx][2] += path_flow  # increase flow
                v, _, _, rev_idx, _ = res_graph[u][edge_idx]
                res_graph[v][rev_idx][2] -= path_flow  # decrease reverse flow (which means increase in original)
        
        # Extract flows for original edges
        result = [0] * m
        for i in range(m):
            u, v, limit, idx = edge_info[i]
            # Find the edge u->v in res_graph[u]
            for edge in res_graph[u]:
                if edge[0] == v:
                    result[idx] = edge[2]  # flow
                    break
        return result
    
    # Actually, let's simplify and just reimplement cleanly
    
    class FlowNetwork:
        def __init__(self, vertices):
            self.V = vertices
            self.graph = defaultdict(lambda: defaultdict(int))  # adj list with capacities
        
        def add_edge(self, u, v, cap):
            self.graph[u][v] = cap
            self.graph[v][u] = 0  # reverse edge starts with 0 capacity
        
        def bfs(self, source, sink, parent):
            visited = [False] * self.V
            queue = deque([source])
            visited[source] = True
            parent[source] = -1
            
            while queue:
                u = queue.popleft()
                for v in self.graph[u]:
                    if not visited[v] and self.graph[u][v] > 0:
                        queue.append(v)
                        visited[v] = True
                        parent[v] = u
                        if v == sink:
                            return True
            return False
        
        def ford_fulkerson(self, source, sink):
            parent = [-1] * self.V
            max_flow = 0
            
            while self.bfs(source, sink, parent):
                path_flow = float('inf')
                s = sink
                while s != source:
                    u = parent[s]
                    path_flow = min(path_flow, self.graph[u][s])
                    s = u
                
                # update residual capacities
                v = sink
                while v != source:
                    u = parent[v]
                    self.graph[u][v] -= path_flow
                    self.graph[v][u] += path_flow
                    v = parent[v]
                
                max_flow += path_flow
            
            return max_flow
    
    # Create flow network
    fn = FlowNetwork(n + 3 + m)
    SOURCE_NODE = n + 1
    SINK_NODE = n + 2
    
    # Map edges to nodes for flow extraction
    edge_to_node = {}  # map edge index to intermediate node
    node_to_edge = {}  # map intermediate node to edge index
    
    current_node = n + 3
    edge_flows_final = [0] * m
    
    # For each edge (u,v,limit), we create an intermediate node to control flow
    # But simpler approach: just model the original problem directly
    
    # Let's think differently. Model as circulation with demands:
    # - Each edge has 0 <= f_i <= limit_i
    # - For each node: sum(in_flows) - sum(out_flows) = demand
    # - demand[s] = -d, demand[t] = d, others = 0
    # This is equivalent to a max-flow with source connected to s (capacity d) 
    # and t connected to sink (capacity d)
    
    # Number nodes 0 to n-1 (original), n (source), n+1 (sink)
    # But in our case, facilities are numbered from 1 to n typically.
    # From input, s and t are facility numbers (1-based). Convert to 0-based.
    
    # Actually, let's read the problem again.
    # Facilities are numbered from 1 to n.
    # But in our implementation, let's keep them as is and add two extra nodes.
    
    # Total nodes: 0 to n+1 where 0 and n+1 are super-source/sink
    # Or just use n and n+1 as super-source/sink
    
    # Let's redefine:
    SUPER_SOURCE = 0
    SUPER_SINK = n + 1
    # Facilities are 1 to n
    
    fn = FlowNetwork(n + 2)  # nodes 0 to n+1
    
    # Connect super-source to s
    fn.add_edge(SUPER_SOURCE, s, d)
    
    # Connect t to super-sink
    fn.add_edge(t, SUPER_SINK, d)
    
    # Add original edges
    for u, v, limit in edges:
        fn.add_edge(u, v, limit)
    
    # Run max flow
    flow_val = fn.ford_fulkerson(SUPER_SOURCE, SUPER_SINK)
    
    if flow_val < d:
        print("NO")
        return
    
    # Need to extract the actual flow values on original edges
    # The flow on edge (u,v) is the amount of flow pushed from u to v
    # which is initial capacity - residual capacity
    
    # We need to track original capacities
    original_caps = {}
    for u, v, limit in edges:
        original_caps[(u, v)] = limit
    
    # After running Ford-Fulkerson, the residual graph contains the flows
    # Flow on (u,v) = original_cap - residual_cap
    flows = []
    for u, v, limit in edges:
        # Flow = original capacity - residual capacity
        flow = original_caps.get((u, v), 0) - fn.graph[u][v]
        flows.append(flow)
    
    print("YES")
    print(' '.join(map(str, flows)))

solve()