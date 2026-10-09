import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    species = []
    for _ in range(k):
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        d = int(next(it))
        species.append((s, t, d))
    
    edges_input = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        cap = int(next(it))
        edges_input.append((u, v, cap))
    
    # Build flow network
    # Nodes: source (0), sink (1), then for each original node i:
    # node_in = 2 + 2*i, node_out = 2 + 2*i + 1
    # Total nodes: 2 + 2*n
    N = 2 + 2 * n
    source = 0
    sink = 1
    
    graph = [[] for _ in range(N)]
    edge_list = []
    
    def add_edge(u, v, cap):
        graph[u].append(len(edge_list))
        edge_list.append([v, cap, 0])  # forward edge
        graph[v].append(len(edge_list))
        edge_list.append([u, 0, 0])    # reverse edge
    
    # Add edges from source to species starting points
    for idx, (s, t, d) in enumerate(species):
        node_out = 2 + 2*s + 1
        add_edge(source, node_out, d)
    
    # Add edges from species targets to sink
    for idx, (s, t, d) in enumerate(species):
        node_in = 2 + 2*t
        add_edge(node_in, sink, d)
    
    # Add internal edges (in -> out) for each node with infinite capacity
    INF = 10**18
    for i in range(n):
        node_in = 2 + 2*i
        node_out = 2 + 2*i + 1
        add_edge(node_in, node_out, INF)
    
    # Add corridor edges
    for u, v, cap in edges_input:
        u_out = 2 + 2*u + 1
        v_in = 2 + 2*v
        add_edge(u_out, v_in, cap)
    
    # Dinic's algorithm
    level = [0] * N
    ptr = [0] * N
    
    def bfs():
        for i in range(N):
            level[i] = -1
        level[source] = 0
        q = deque([source])
        while q:
            u = q.popleft()
            for eid in graph[u]:
                v, cap, flow = edge_list[eid]
                if cap > flow and level[v] == -1:
                    level[v] = level[u] + 1
                    q.append(v)
        return level[sink] != -1
    
    def dfs(u, pushed):
        if pushed == 0 or u == sink:
            return pushed
        for i in range(ptr[u], len(graph[u])):
            ptr[u] = i
            eid = graph[u][i]
            v, cap, flow = edge_list[eid]
            if level[v] != level[u] + 1:
                continue
            remaining = cap - flow
            tr = dfs(v, min(pushed, remaining))
            if tr > 0:
                edge_list[eid][2] += tr
                edge_list[eid ^ 1][2] -= tr
                return tr
        return 0
    
    total_demand = sum(d for _, _, d in species)
    max_flow = 0
    
    while bfs():
        ptr = [0] * N
        while True:
            pushed = dfs(source, INF)
            if pushed == 0:
                break
            max_flow += pushed
    
    if max_flow != total_demand:
        print("NO")
        return
    
    print("YES")
    
    # Extract flow for each species
    # For each species, we need to find the flow through each corridor
    # We'll use the edge decomposition approach
    
    # First, identify which edges are corridor edges
    # Corridor edges are added after the first k*2 + n edges (source->out, in->sink, internal)
    # Actually, let's track the indices
    
    # Rebuild with tracking
    # Let's re-solve with proper tracking
    
    # Actually, let's use a different approach:
    # For each species, we'll compute the flow through each edge
    
    # We need to decompose the flow into k commodities
    # This is done by finding paths from source to sink for each species
    
    # Let's build the flow graph and decompose
    
    # Build adjacency list for flow decomposition
    adj = [[] for _ in range(N)]
    for u in range(N):
        for eid in graph[u]:
            v, cap, flow = edge_list[eid]
            if eid % 2 == 0:  # forward edge
                adj[u].append((v, eid, flow))
    
    # For each species, find paths and extract flow
    # We need to track which species uses which edge
    
    # Map: for each edge, how much flow from each species
    # But edges are shared, so we need to decompose
    
    # Let's use a greedy approach: for each species, find augmenting paths
    # in the residual graph
    
    # Build residual graph
    residual = [[] for _ in range(N)]
    for u in range(N):
        for eid in graph[u]:
            v, cap, flow = edge_list[eid]
            residual[u].append((v, eid, cap - flow, flow, eid % 2 == 0))
    
    # For each species, we need to route d_i flow from s_i to t_i
    # through the shared edges
    
    # Actually, let's use a simpler approach:
    # We'll compute the flow for each species separately using the max flow solution
    
    # The key insight is that we need to decompose the flow into k paths
    # We'll use the fact that the flow is already computed
    
    # Let's find all paths from source to sink and assign them to species
    
    # First, let's identify which species each path belongs to
    # by looking at the starting node
    
    # Build a mapping from node_out to species index
    node_to_species = {}
    for idx, (s, t, d) in enumerate(species):
        node_out = 2 + 2*s + 1
        if node_out not in node_to_species:
            node_to_species[node_out] = []
        node_to_species[node_out].append(idx)
    
    # Now, let's decompose the flow
    # We'll use DFS to find paths
    
    # For each species, we'll track the flow through each corridor
    species_flow = [[0] * m for _ in range(k)]
    
    # We need to find which corridor edge corresponds to which index
    # Corridor edges are added at the end
    # Let's count: source->out (k edges), in->sink (k edges), internal (n edges)
    # So corridor edges start at index base = 2*k + n
    base = 2 * k + n
    
    # Actually, let's rebuild the edge tracking properly
    # Let's re-run the algorithm with proper edge tracking
    
    # Rebuild the graph with edge tracking
    N2 = 2 + 2 * n
    graph2 = [[] for _ in range(N2)]
    edge_list2 = []
    edge_info = []  # (type, data) where type is 'source', 'sink', 'internal', 'corridor'
    
    def add_edge2(u, v, cap, info):
        graph2[u].append(len(edge_list2))
        edge_list2.append([v, cap, 0])
        edge_info.append(info)
        graph2[v].append(len(edge_list2))
        edge_list2.append([u, 0, 0])
        edge_info.append(None)  # reverse edge has no info
    
    # Add edges
    for idx, (s, t, d) in enumerate(species):
        node_out = 2 + 2*s + 1
        add_edge2(source, node_out, d, ('source', idx))
    
    for idx, (s, t, d) in enumerate(species):
        node_in = 2 + 2*t
        add_edge2(node_in, sink, d, ('sink', idx))
    
    for i in range(n):
        node_in = 2 + 2*i
        node_out = 2 + 2*i + 1
        add_edge2(node_in, node_out, INF, ('internal', i))
    
    corridor_edge_indices = []
    for i, (u, v, cap) in enumerate(edges_input):
        u_out = 2 + 2*u + 1
        v_in = 2 + 2*v
        add_edge2(u_out, v_in, cap, ('corridor', i))
        corridor_edge_indices.append(len(edge_list2) - 2)  # forward edge index
    
    # Run Dinic's again
    level2 = [0] * N2
    ptr2 = [0] * N2
    
    def bfs2():
        for i in range(N2):
            level2[i] = -1
        level2[source] = 0
        q = deque([source])
        while q:
            u = q.popleft()
            for eid in graph2[u]:
                v, cap, flow = edge_list2[eid]
                if cap > flow and level2[v] == -1:
                    level2[v] = level2[u] + 1
                    q.append(v)
        return level2[sink] != -1
    
    def dfs2(u, pushed):
        if pushed == 0 or u == sink:
            return pushed
        for i in range(ptr2[u], len(graph2[u])):
            ptr2[u] = i
            eid = graph2[u][i]
            v, cap, flow = edge_list2[eid]
            if level2[v] != level2[u] + 1:
                continue
            remaining = cap - flow
            tr = dfs2(v, min(pushed, remaining))
            if tr > 0:
                edge_list2[eid][2] += tr
                edge_list2[eid ^ 1][2] -= tr
                return tr
        return 0
    
    max_flow2 = 0
    while bfs2():
        ptr2 = [0] * N2
        while True:
            pushed = dfs2(source, INF)
            if pushed == 0:
                break
            max_flow2 += pushed
    
    # Now decompose the flow
    # For each species, we need to find paths from source to sink
    
    # Build adjacency list for flow decomposition
    adj2 = [[] for _ in range(N2)]
    for u in range(N2):
        for eid in graph2[u]:
            if eid % 2 == 0:  # forward edge
                v, cap, flow = edge_list2[eid]
                if flow > 0:
                    adj2[u].append((v, eid, flow))
    
    # For each species, find paths and extract flow
    species_remaining = [d for _, _, d in species]
    
    # We'll use DFS to find paths for each species
    def find_path_for_species(species_idx, current_flow):
        """Find a path from source to sink for the given species"""
        s, t, d = species[species_idx]
        start_node = 2 + 2*s + 1  # node_out of starting reserve
        end_node = 2 + 2*t        # node_in of target reserve
        
        # We need to find a path from start_node to end_node
        # But the flow goes source -> start_node -> ... -> end_node -> sink
        
        # Let's find paths in the flow graph
        path = []
        visited = [False] * N2
        
        def dfs_path(u, target, min_flow):
            if u == target:
                return True, min_flow
            visited[u] = True
            for i, (v, eid, flow) in enumerate(adj2[u]):
                if visited[v] or flow == 0:
                    continue
                # Check if this edge can be used for this species
                info = edge_info[eid]
                if info is not None:
                    if info[0] == 'source' and info[1] != species_idx:
                        continue
                    if info[0] == 'sink' and info[1] != species_idx:
                        continue
                actual_flow = min(min_flow, flow)
                found, result_flow = dfs_path(v, target, actual_flow)
                if found:
                    path.append((u, v, eid, result_flow))
                    return True, result_flow
            return False, 0
        
        # Find path from start_node to end_node
        found, flow = dfs_path(start_node, end_node, current_flow)
        if found:
            path.reverse()
            return path, flow
        return None, 0
    
    # Process each species
    for species_idx in range(k):
        s, t, d = species[species_idx]
        remaining = d
        
        while remaining > 0:
            path, flow = find_path_for_species(species_idx, remaining)
            if path is None:
                break
            
            # Update the flow on each edge
            for u, v, eid, f in path:
                # Update the flow in adj2
                for i, (vv, eeid, ff) in enumerate(adj2[u]):
                    if eeid == eid:
                        adj2[u][i] = (vv, eeid, ff - f)
                        break
            
            # Extract corridor flows
            for u, v, eid, f in path:
                info = edge_info[eid]
                if info is not None and info[0] == 'corridor':
                    corridor_idx = info[1]
                    species_flow[species_idx][corridor_idx] += f
            
            remaining -= f
    
    # Output the result
    for i in range(k):
        print(' '.join(map(str, species_flow[i])))

solve()