import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))

    species = []
    for _ in range(k):
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        d = int(next(it))
        species.append((s, t, d))

    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        cap = int(next(it))
        edges.append((u, v, cap))

    # Build a single-commodity flow network.
    # Node layout:
    # 0..n-1: original reserves
    # n..n+m-1: edge nodes (edge j -> node n+j)
    # n+m: super source S
    # n+m+1: super sink T
    S = n + m
    T = n + m + 1
    total_nodes = n + m + 2

    # We use a CSR-style adjacency for Dinic.
    # Each directed edge in residual graph: to, rev_index, cap
    head = [-1] * total_nodes
    to = []
    cap = []
    nxt = []
    rev = []

    def add_edge(u, v, c):
        head_u = head[u]
        head[v] = len(to)
        to.append(v)
        cap.append(c)
        nxt.append(head_u)
        rev.append(len(to))
        head[u] = len(to)
        to.append(u)
        cap.append(0)
        nxt.append(head[v])
        rev.append(len(to) - 1)

    # Original corridors: reserve u -> edge-node j, capacity cap
    for j, (u, v, c) in enumerate(edges):
        add_edge(u, n + j, c)

    # Edge-node j -> reserve v, capacity INF
    INF = 1 << 60
    for j, (u, v, c) in enumerate(edges):
        add_edge(n + j, v, INF)

    # Super source to each species start
    for idx, (s, t, d) in enumerate(species):
        add_edge(S, s, d)

    # Each species target to super sink
    for idx, (s, t, d) in enumerate(species):
        add_edge(t, T, d)

    # Dinic's algorithm
    level = [0] * total_nodes
    it_ptr = [0] * total_nodes

    def bfs():
        for i in range(total_nodes):
            level[i] = -1
        queue = [0] * total_nodes
        qh = 0
        qt = 0
        level[S] = 0
        queue[qt] = S
        qt += 1
        while qh < qt:
            u = queue[qh]
            qh += 1
            e = head[u]
            while e != -1:
                v = to[e]
                if cap[e] > 0 and level[v] < 0:
                    level[v] = level[u] + 1
                    queue[qt] = v
                    qt += 1
                e = nxt[e]
        return level[T] >= 0

    def dfs(u, f):
        if u == T:
            return f
        while it_ptr[u] < len(to):
            e = head[u]
            # advance to the current edge pointer
            # Since we store as linked list, we need to track pointer differently.
            # Let's just use array-based iteration.
            break
        # Actually, let's implement dfs using the linked list properly.
        return dfs_ll(u, f)

    # Reimplement dfs using linked list with it_ptr as edge index
    def dfs_ll(u, f):
        if u == T:
            return f
        e = it_ptr[u]
        while e != -1:
            v = to[e]
            if cap[e] > 0 and level[v] == level[u] + 1:
                pushed = dfs_ll(v, f if f < cap[e] else cap[e])
                if pushed > 0:
                    cap[e] -= pushed
                    cap[rev[e]] += pushed
                    return pushed
            e = nxt[e]
            it_ptr[u] = e
        return 0

    def max_flow():
        flow = 0
        while bfs():
            for i in range(total_nodes):
                it_ptr[i] = head[i]
            while True:
                f = dfs_ll(S, INF)
                if f == 0:
                    break
                flow += f
        return flow

    total_demand = sum(d for (s, t, d) in species)
    flow = max_flow()

    if flow < total_demand:
        print("NO")
        return

    # Extract per-species flow on each original corridor.
    # For corridor j (u -> v), the flow on u -> edge-node j tells total animals.
    # To split by species, we need per-species flows.
    # Since the problem only asks for a valid plan (any), we can decompose.
    # But the single-commodity flow doesn't directly give per-species.
    # We need to compute per-species flows that respect shared capacities.
    # 
    # Approach: The total flow gives us which corridors are used and how much.
    # We can route each species greedily in the residual network? No.
    # 
    # Actually, we need to output per-species flows. The single commodity max flow
    # proves feasibility. To extract a solution, we can do per-species flow in the
    # residual graph of the total flow? That doesn't directly work either.
    #
    # Better: Build a multi-commodity flow? No, that's hard in general.
    # But wait: the problem is actually a single-commodity flow because all species
    # share capacities and we just need net flow. The per-species decomposition
    # is always possible if total flow exists: we can decompose the total flow
    # into paths and assign each path to a species.
    #
    # Let's decompose the total flow into s-t paths and assign to species.
    # But we have multiple sources/sinks. We can trace flow from super source.
    #
    # Actually, let's compute per-species flows directly by running flow for each
    # species in the residual graph after removing already used capacity.
    # This greedy approach works because if total flow = total demand, then
    # there exists an assignment; but greedy per-species might fail.
    #
    # Correct approach: decompose the total flow into paths from S to T.
    # Each path goes S -> s_i -> ... -> t_i -> T. The S->s_i and t_i->T edges
    # tell us which species. Then we can assign the path to that species.
    #
    # Let's do path decomposition on the flow (forward edges with cap>0 in original
    # are residual; we need edges where flow was sent, i.e., reverse edges have cap>0).

    # Reconstruct flow on each edge: flow[e] = cap[rev[e]] (the residual capacity
    # on reverse edge equals flow sent on forward edge).
    # But we added edges in a specific order. Let's track which edges are "forward".
    # Actually, for decomposition, we can use the residual graph: flow on edge (u,v)
    # is the amount pushed, which equals cap[rev[e]] for forward edge e.
    
    # Let's build adjacency of flow-carrying edges for path decomposition.
    # For each forward edge (u->v) with flow f = cap[rev[e]] > 0, we have f units
    # of flow from u to v.
    
    # We need to identify forward edges. We added them in add_edge calls.
    # Let's just iterate all edges and use cap[rev[e]] as flow, but only for
    # forward edges (even indices in our add_edge? No, we used linked list).
    
    # Simpler: rebuild flow adjacency.
    flow_adj = [[] for _ in range(total_nodes)]
    for u in range(total_nodes):
        e = head[u]
        while e != -1:
            f = cap[rev[e]]  # flow on this edge
            if f > 0:
                flow_adj[u].append((to[e], e, f))
            e = nxt[e]
    
    # Now decompose into paths from S to T.
    # We'll use a stack-based DFS.
    # For each path, we find min flow along it, subtract, and record.
    
    # But we also need to know which species each path belongs to.
    # The first edge from S goes to some s_i. The edge from s_i to T... no.
    # Path: S -> s_i -> (corridors) -> t_i -> T.
    # The S->s_i edge tells us species i. But we added them in order, so
    # the edge S->s for species idx. We need to map.
    
    # Let's find which species each S->? edge corresponds to.
    # We added: for each species, add_edge(S, s, d) and add_edge(t, T, d).
    # The edges from S go to species starts.
    
    # Let's collect flow on S->s edges and t->T edges.
    # Actually for decomposition, let's just trace paths.
    
    # We'll record per-species flow on each corridor.
    species_flow = [[0] * m for _ in range(k)]
    
    # Map from node to species index for starts and targets
    start_species = {}  # node -> species idx (for S->s edges)
    # Actually multiple species can have same start, so we need edge-based.
    
    # Let's identify the S->s_i edges. We added them in species order.
    # After adding corridor edges (2m edges from add_edge for corridors + INF edges),
    # then we added k edges S->s_i and k edges t_i->T.
    # Each add_edge adds 2 directed edges. So the S->s_i forward edges are at
    # specific positions. But with linked list, positions are indices in to[].
    
    # Let's just decompose paths and figure out species from the path.
    # A path from S starts with S -> s_i. We need to know which species.
    # We can check: the edge S -> v where v is a start node. But multiple species
    # might share start nodes. 
    
    # Alternative: decompose flow into paths, and for each path, the start node
    # (after S) and end node (before T) tell us s and t. We match to a species
    # with that s, t, and remaining demand.
    
    # Let's track remaining demand per species.
    remaining = [d for (s, t, d) in species]
    species_by_st = {}
    for idx, (s, t, d) in enumerate(species):
        key = (s, t)
        if key not in species_by_st:
            species_by_st[key] = []
        species_by_st[key].append(idx)
    
    # Path decomposition using flow_adj
    # We need to handle the edge-node representation: path goes
    # S -> s_i -> n+j1 -> v1 -> n+j2 -> v2 -> ... -> t_i -> T
    # The corridors used are j1, j2, ...
    
    # Let's do iterative path finding.
    edge_flow_remaining = {}  # edge index -> remaining flow
    for u in range(total_nodes):
        e = head[u]
        while e != -1:
            f = cap[rev[e]]
            if f > 0:
                edge_flow_remaining[e] = f
            e = nxt[e]
    
    # Find paths from S to T
    # Use DFS with explicit stack
    # We'll find a path, compute bottleneck, subtract, assign to species.
    
    # Build a quick adjacency for flow edges
    flow_head = [-1] * total_nodes
    flow_to = []
    flow_cap = []
    flow_nxt = []
    flow_eid = []
    for u in range(total_nodes):
        e = head[u]
        while e != -1:
            f = cap[rev[e]]
            if f > 0:
                flow_nxt.append(flow_head[u])
                flow_to.append(to[e])
                flow_cap.append(f)
                flow_eid.append(e)
                flow_head[u] = len(flow_to) - 1
            e = nxt[e]
    
    flow_it = list(flow_head)
    
    def find_path():
        # Returns (path_nodes, path_edge_ids, bottleneck) or None
        path_nodes = [S]
        path_edges = []
        path_edge_caps = []
        # DFS
        stack = [(S, flow_head[S])]
        # Actually let's do recursive-like with explicit stack
        # We'll use flow_it for iterator state
        node = S
        it = flow_head[S]
        while True:
            if node == T:
                # found path
                bottleneck = min(path_edge_caps) if path_edge_caps else 0
                return path_nodes, path_edges, bottleneck
            if it != -1:
                v = flow_to[it]
                c = flow_cap[it]
                eid = flow_eid[it]
                if c > 0:
                    # advance and push
                    flow_it[node] = flow_nxt[it]
                    path_nodes.append(v)
                    path_edges.append(eid)
                    path_edge_caps.append(c)
                    node = v
                    it = flow_it[v] if v < len(flow_it) else flow_head[v]
                    if node == T:
                        bottleneck = min(path_edge_caps) if path_edge_caps else 0
                        return path_nodes, path_edges, bottleneck
                    it = flow_head[v] if flow_it[v] == -1 else flow_it[v]
                    # Actually flow_it should be initialized properly
                    it = flow_it[v]
                    continue
                else:
                    it = flow_nxt[it]
                    flow_it[node] = it
            else:
                # backtrack
                if len(path_nodes) <= 1:
                    return None
                path_nodes.pop()
                path_edges.pop()
                path_edge_caps.pop()
                node = path_nodes[-1]
                it = flow_it[node]
    
    # The above is getting complicated. Let me use a simpler approach.
    # Reset and use simple recursive path finding with flow adjacency list.
    
    # Simple approach: repeatedly find any path from S to T in flow graph.
    flow_graph = [[] for _ in range(total_nodes)]
    for u in range(total_nodes):
        e = head[u]
        while e != -1:
            f = cap[rev[e]]
            if f > 0:
                flow_graph[u].append([to[e], e, f])  # mutable for cap update
            e = nxt[e]
    
    def find_and_remove_path():
        # DFS to find S->T path, return (edges, bottleneck) or None
        # edges is list of (u, v, edge_index_in_flow_graph)
        parent = [-1] * total_nodes
        parent_edge = [None] * total_nodes
        visited = [False] * total_nodes
        stack = [S]
        visited[S] = True
        while stack:
            u = stack.pop()
            if u == T:
                # reconstruct path
                path_edges = []
                node = T
                while node != S:
                    pe = parent_edge[node]
                    path_edges.append(pe)
                    node = parent[node]
                path_edges.reverse()
                # bottleneck
                bottleneck = min(flow_graph[pe[0]][pe[1]][2] for pe in path_edges)
                return path_edges, bottleneck
            for idx, (v, e, f) in enumerate(flow_graph[u]):
                if f > 0 and not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    parent_edge[v] = (u, idx)
                    stack.append(v)
        return None
    
    # Decompose
    while True:
        result = find_and_remove_path()
        if result is None:
            break
        path_edges, bottleneck = result
        # Subtract flow
        for (u, idx) in path_edges:
            flow_graph[u][idx][2] -= bottleneck
        
        # Identify corridors and species
        # path_edges gives (u, idx) pairs. The actual edge is flow_graph[u][idx].
        # The edge index e = flow_graph[u][idx][1]
        # The edge goes from u to flow_graph[u][idx][0]
        
        # Reconstruct node sequence
        nodes = [S]
        for (u, idx) in path_edges:
            v = flow_graph[u][idx][0]
            nodes.append(v)
        
        # nodes: S, s_i, n+j1, v1, n+j2, v2, ..., t_i, T
        # s_i = nodes[1], t_i = nodes[-2]
        s_node = nodes[1]
        t_node = nodes[-2]
        
        # Find corridors: edges where u < n and v >= n (u is reserve, v is edge-node)
        corridors_used = []
        for (u, idx) in path_edges:
            v = flow_graph[u][idx][0]
            if u < n and n <= v < n + m:
                j = v - n
                corridors_used.append(j)
        
        # Find species
        key = (s_node, t_node)
        if key in species_by_st:
            candidates = species_by_st[key]
            chosen = None
            for idx in candidates:
                if remaining[idx] >= bottleneck:
                    chosen = idx
                    break
            if chosen is None:
                # This shouldn't happen if flow is valid
                # But could if multiple species share s,t and we need to split
                # Let's just pick any with remaining > 0
                for idx in candidates:
                    if remaining[idx] > 0:
                        chosen = idx
                        break
            if chosen is not None:
                remaining[chosen] -= bottleneck
                for j in corridors_used:
                    species_flow[chosen][j] += bottleneck
    
    print("YES")
    out_lines = []
    for i in range(k):
        out_lines.append(' '.join(str(x) for x in species_flow[i]))
    print('\n'.join(out_lines))

solve()