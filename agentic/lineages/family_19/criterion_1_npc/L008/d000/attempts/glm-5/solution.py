import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    tasks = []
    for _ in range(k):
        s = int(next(it))
        t = int(next(it))
        d = int(next(it))
        tasks.append((s, t, d))
    
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        cap = int(next(it))
        edges.append((u, v, cap))
    
    # Build flow network
    # Nodes: 0 is super source, 1..n are routers, n+1..n+k are task sinks, n+k+1 is super sink
    # Actually, let's use: super source = 0, routers = 1..n, task sinks = n+1..n+k, super sink = n+k+1
    # But we need intermediate nodes for each task at each router for flow conservation
    # Better approach: create a node for each (router, task) pair
    # Node (r, i) for router r and task i
    # Total nodes: n * k + 2 (super source and super sink)
    
    # Let's use a different encoding:
    # Node id = r * k + i for router r (0-indexed) and task i (0-indexed)
    # Plus super source = n*k and super sink = n*k + 1
    
    N = n * k + 2
    source = n * k
    sink = n * k + 1
    
    adj = [[] for _ in range(N)]
    
    def add_edge(u, v, cap):
        adj[u].append([v, cap, len(adj[v])])
        adj[v].append([u, 0, len(adj[u]) - 1])
    
    # Add edges for each task
    for i, (s, t, d) in enumerate(tasks):
        s -= 1  # 0-indexed
        t -= 1
        # Super source to task's source router
        add_edge(source, s * k + i, d)
        # Task's destination router to super sink
        add_edge(t * k + i, sink, d)
    
    # Add edges between routers for each task
    for j, (u, v, cap) in enumerate(edges):
        u -= 1  # 0-indexed
        v -= 1
        for i in range(k):
            # Edge from (u, i) to (v, i) with capacity cap (shared)
            # But we need to share capacity across tasks...
            # This is the tricky part - we need to split the capacity
            
            # Actually, we need to model this differently
            # For each physical link, we need to split its capacity among tasks
            # Let's create an intermediate node for each link
            pass
    
    # Let me reconsider the approach
    # We need: for each physical link (u, v, cap), the sum of flows from all tasks on this link <= cap
    # 
    # Approach: For each physical link, create an intermediate node
    # Node structure:
    # - Super source (0)
    # - For each task i and router r: node (r, i)
    # - For each link j: intermediate node link_j
    # - Super sink
    
    # Actually, let's use a cleaner approach:
    # Nodes: 
    # - Super source = 0
    # - For each task i and router r: node id = 1 + i * n + r (1-indexed routers)
    # - For each link j: intermediate node
    # - Super sink
    
    # Simpler: 
    # For each link j from u to v with capacity cap:
    #   Create intermediate node L_j
    #   For each task i: edge from (u, i) to L_j with capacity cap
    #   Edge from L_j to all (v, i) with capacity cap
    # This doesn't work because we need to split cap among tasks
    
    # Correct approach using flow splitting:
    # For link j from u to v with capacity cap:
    #   Create intermediate node L_j
    #   For each task i: edge from (u, i) to L_j with capacity cap (or infinity)
    #   Edge from L_j to (v, i) with capacity cap (or infinity)
    #   But we need to limit total flow through L_j to cap
    #   Solution: edge from L_j_in to L_j_out with capacity cap
    
    # Let me restart with a cleaner node numbering:
    # Nodes:
    # - Super source: 0
    # - Task-router nodes: 1 to n*k (node (r, i) = 1 + r-1 + (i-1)*n)
    # - Link intermediate nodes: n*k + 1 to n*k + m
    # - Super sink: n*k + m + 1
    
    # Hmm, this is getting complex. Let me use a simpler approach.
    
    # Alternative: Use the standard multi-commodity flow formulation
    # but with edge capacity constraints
    
    # Actually, the key insight is:
    # For each link (u, v, cap), we need to split cap among k tasks
    # We can model this by creating a "link node" that has capacity cap
    
    # Final approach:
    # Nodes:
    # - Super source: 0
    # - For each router r and task i: node id = 1 + (r-1) + (i-1)*n
    # - For each link j: intermediate node pair (in, out) with capacity cap between them
    # - Super sink: last node
    
    # Let's implement this carefully
    
    # Node numbering:
    # Super source = 0
    # Router-task nodes: for router r (1..n) and task i (0..k-1): node = 1 + (r-1) + i*n
    # Link intermediate nodes: for link j (0..m-1): node = 1 + n*k + j
    # Super sink = 1 + n*k + m
    
    N = 1 + n * k + m + 1
    source = 0
    sink = N - 1
    
    adj = [[] for _ in range(N)]
    
    def add_edge(u, v, cap):
        adj[u].append([v, cap, len(adj[v])])
        adj[v].append([u, 0, len(adj[u]) - 1])
    
    # For each task, add source and sink edges
    for i, (s, t, d) in enumerate(tasks):
        # Source router node for task i
        src_node = 1 + (s - 1) + i * n
        # Sink router node for task i
        dst_node = 1 + (t - 1) + i * n
        add_edge(source, src_node, d)
        add_edge(dst_node, sink, d)
    
    # For each link, create intermediate node and edges
    link_nodes = []
    for j, (u, v, cap) in enumerate(edges):
        # Link intermediate node
        link_node = 1 + n * k + j
        link_nodes.append(link_node)
        
        # Capacity limiting edge (link_node to a virtual out node, or just use link_node)
        # Actually, we need: flow from (u, i) -> link_node -> (v, i) for each task i
        # And total flow through link_node <= cap
        
        # Create a capacity-limiting structure:
        # For each task i: edge from (u, i) to link_node with capacity cap
        # Edge from link_node to (v, i) with capacity cap
        # But this doesn't limit total flow...
        
        # Correct: create two nodes per link, with capacity cap between them
        # link_in -> link_out with capacity cap
        # For each task i: (u, i) -> link_in, link_out -> (v, i)
        
        # Let me adjust node numbering:
        pass
    
    # Let me restart with correct node numbering
    # Nodes:
    # - Super source: 0
    # - Router-task nodes: for router r (0..n-1) and task i (0..k-1): node = 1 + r + i*n
    # - Link in nodes: for link j (0..m-1): node = 1 + n*k + j
    # - Link out nodes: for link j (0..m-1): node = 1 + n*k + m + j
    # - Super sink: 1 + n*k + 2*m
    
    N = 1 + n * k + 2 * m + 1
    source = 0
    sink = N - 1
    
    adj = [[] for _ in range(N)]
    
    def add_edge(u, v, cap):
        adj[u].append([v, cap, len(adj[v])])
        adj[v].append([u, 0, len(adj[u]) - 1])
    
    # For each task, add source and sink edges
    for i, (s, t, d) in enumerate(tasks):
        src_node = 1 + (s - 1) + i * n
        dst_node = 1 + (t - 1) + i * n
        add_edge(source, src_node, d)
        add_edge(dst_node, sink, d)
    
    # For each link, create intermediate nodes and edges
    for j, (u, v, cap) in enumerate(edges):
        link_in = 1 + n * k + j
        link_out = 1 + n * k + m + j
        
        # Capacity limiting edge
        add_edge(link_in, link_out, cap)
        
        # For each task, connect router to link_in and link_out to router
        for i in range(k):
            # From (u, i) to link_in
            router_u_node = 1 + (u - 1) + i * n
            add_edge(router_u_node, link_in, cap)  # capacity can be cap or d_i
            
            # From link_out to (v, i)
            router_v_node = 1 + (v - 1) + i * n
            add_edge(link_out, router_v_node, cap)
    
    # Now run max flow
    total_demand = sum(d for _, _, d in tasks)
    
    def max_flow(s, t):
        flow = 0
        while True:
            # BFS to find augmenting path
            parent = [-1] * N
            parent_edge = [-1] * N
            q = [s]
            parent[s] = s
            for u in q:
                if u == t:
                    break
                for idx, (v, cap, rev) in enumerate(adj[u]):
                    if parent[v] == -1 and cap > 0:
                        parent[v] = u
                        parent_edge[v] = idx
                        q.append(v)
            
            if parent[t] == -1:
                break
            
            # Find bottleneck
            path_flow = float('inf')
            v = t
            while v != s:
                u = parent[v]
                idx = parent_edge[v]
                path_flow = min(path_flow, adj[u][idx][1])
                v = u
            
            # Augment
            v = t
            while v != s:
                u = parent[v]
                idx = parent_edge[v]
                adj[u][idx][1] -= path_flow
                rev = adj[u][idx][2]
                adj[v][rev][1] += path_flow
                v = u
            
            flow += path_flow
        
        return flow
    
    flow = max_flow(source, sink)
    
    if flow != total_demand:
        print("NO")
        return
    
    print("YES")
    
    # Extract flow on each link for each task
    for i in range(k):
        result = []
        for j, (u, v, cap) in enumerate(edges):
            link_in = 1 + n * k + j
            router_u_node = 1 + (u - 1) + i * n
            
            # Find flow on edge from router_u_node to link_in
            f = 0
            for idx, (to, cap_rem, rev) in enumerate(adj[router_u_node]):
                if to == link_in:
                    # Original capacity was cap, remaining is cap_rem
                    # Flow = original_cap - cap_rem
                    original_cap = cap  # This might not be exact if we used different capacity
                    f = original_cap - cap_rem
                    break
            result.append(f)
        print(' '.join(map(str, result)))

solve()