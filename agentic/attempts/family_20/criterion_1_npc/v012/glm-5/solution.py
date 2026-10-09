import sys
sys.setrecursionlimit(10000)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    edges = []
    adj = [[] for _ in range(n + 1)]
    
    for i in range(m):
        u = int(next(it))
        v = int(next(it))
        edges.append((u, v))
        adj[u].append((v, i))
        adj[v].append((u, i))
    
    # Check degree condition: each vertex must have degree 3
    for u in range(1, n + 1):
        if len(adj[u]) != 3:
            print("NO")
            return
    
    # Build adjacency with edge indices
    # adj[u] = list of (v, edge_index)
    
    # For each vertex, create a mapping from edge_index to local position (0, 1, 2)
    edge_to_local = [{} for _ in range(n + 1)]
    for u in range(1, n + 1):
        for local_idx, (v, edge_idx) in enumerate(adj[u]):
            edge_to_local[u][edge_idx] = local_idx
    
    # For each edge, store the local positions at its two endpoints
    edge_local_pos = []
    for i, (u, v) in enumerate(edges):
        pos_u = edge_to_local[u][i]
        pos_v = edge_to_local[v][i]
        edge_local_pos.append((pos_u, pos_v))
    
    # Build graph for 2-SAT
    # Variables: x_i = True means edge i gets color 1, False means color 2
    # Color 3 is used when neither endpoint forces a specific color
    
    # For each vertex, we need to ensure no two edges have the same color
    # At vertex u, edges at local positions 0, 1, 2 must have different colors
    # If edge at position p has color c, then edges at other positions cannot have color c
    
    # We'll use 2-SAT: for each edge i, x_i = True -> color 1, x_i = False -> color 2
    # Color 3 is implicit (when neither endpoint forces color 1 or 2)
    
    # For vertex u:
    # - If edge at position p has color 1, then edges at positions q != p cannot have color 1
    #   This means x_{edge_p} = True implies x_{edge_q} = False (for q != p)
    # - Similarly for color 2
    
    # We need to find an assignment such that for each vertex, at most one edge has color 1
    # and at most one edge has color 2 (the third edge gets color 3)
    
    # Actually, we need exactly one edge of each color 1, 2, 3 at each vertex
    # But since there are 3 edges and 3 colors, "at most one" implies "exactly one"
    
    # Let's reformulate:
    # For each vertex u, let e0, e1, e2 be the edges at positions 0, 1, 2
    # We need: exactly one of e0, e1, e2 has color 1, exactly one has color 2, exactly one has color 3
    
    # 2-SAT formulation:
    # x_i = True -> edge i has color 1
    # x_i = False -> edge i has color 2
    # If neither endpoint forces color 1 or 2, edge gets color 3
    
    # For vertex u with edges e0, e1, e2:
    # - At most one of x_{e0}, x_{e1}, x_{e2} is True (at most one edge has color 1)
    # - At most one of !x_{e0}, !x_{e1}, !x_{e2} is True (at most one edge has color 2)
    
    # "At most one is True" can be encoded as pairwise implications:
    # x_{ei} => !x_{ej} for all i != j
    
    num_vars = m
    num_clauses = 0
    clauses = []
    
    for u in range(1, n + 1):
        edge_indices = [edge_idx for (v, edge_idx) in adj[u]]
        e0, e1, e2 = edge_indices
        
        # At most one of e0, e1, e2 has color 1
        # x_e0 => !x_e1, x_e0 => !x_e2, x_e1 => !x_e2
        clauses.append((e0, False, e1, True))   # x_e0 => !x_e1
        clauses.append((e0, False, e2, True))  # x_e0 => !x_e2
        clauses.append((e1, False, e2, True))  # x_e1 => !x_e2
        
        # At most one of e0, e1, e2 has color 2
        # !x_e0 => x_e1, !x_e0 => x_e2, !x_e1 => x_e2
        # Equivalently: at most one of !x_e0, !x_e1, !x_e2 is True
        # !x_ei => !!x_ej = x_ej for i != j
        clauses.append((e0, True, e1, False))  # !x_e0 => x_e1
        clauses.append((e0, True, e2, False))  # !x_e0 => x_e2
        clauses.append((e1, True, e2, False))  # !x_e1 => x_e2
    
    # 2-SAT solver using SCC
    # Variable i: node 2*i (True), node 2*i+1 (False)
    # Implication (a, val_a) => (b, val_b): add edge from node of (a, val_a) to node of (b, val_b)
    
    def get_node(var, val):
        # var: 0 to num_vars-1
        # val: True or False
        # Returns node index
        return 2 * var + (0 if val else 1)
    
    # Build implication graph
    graph = [[] for _ in range(2 * num_vars)]
    graph_rev = [[] for _ in range(2 * num_vars)]
    
    for (a, a_val, b, b_val) in clauses:
        # (a, a_val) => (b, b_val)
        u = get_node(a, a_val)
        v = get_node(b, b_val)
        graph[u].append(v)
        graph_rev[v].append(u)
    
    # Kosaraju's algorithm for SCC
    visited = [False] * (2 * num_vars)
    order = []
    
    def dfs1(u):
        stack = [(u, 0)]
        while stack:
            node, idx = stack.pop()
            if idx == 0:
                if visited[node]:
                    continue
                visited[node] = True
                stack.append((node, 1))
                for v in graph[node]:
                    if not visited[v]:
                        stack.append((v, 0))
            else:
                order.append(node)
    
    for i in range(2 * num_vars):
        if not visited[i]:
            dfs1(i)
    
    visited = [False] * (2 * num_vars)
    comp = [-1] * (2 * num_vars)
    comp_id = 0
    
    def dfs2(u, cid):
        stack = [u]
        while stack:
            node = stack.pop()
            if visited[node]:
                continue
            visited[node] = True
            comp[node] = cid
            for v in graph_rev[node]:
                if not visited[v]:
                    stack.append(v)
    
    for node in reversed(order):
        if not visited[node]:
            dfs2(node, comp_id)
            comp_id += 1
    
    # Check satisfiability
    assignment = [False] * num_vars
    for i in range(num_vars):
        if comp[2 * i] == comp[2 * i + 1]:
            print("NO")
            return
        assignment[i] = comp[2 * i] > comp[2 * i + 1]
    
    # Compute colors
    colors = [0] * m
    for i in range(m):
        if assignment[i]:
            colors[i] = 1
        else:
            colors[i] = 2
    
    # Verify and adjust colors
    # For each vertex, check if exactly one edge has each color
    # If not, adjust
    
    # Actually, the 2-SAT solution should give us a valid assignment
    # Let's verify
    
    for u in range(1, n + 1):
        edge_indices = [edge_idx for (v, edge_idx) in adj[u]]
        color_count = {}
        for ei in edge_indices:
            c = colors[ei]
            color_count[c] = color_count.get(c, 0) + 1
        
        # Check if we need to use color 3
        # If two edges have the same color, we need to fix
        if len(color_count) < 3:
            # Find the color that appears twice
            for c in [1, 2]:
                if color_count.get(c, 0) == 2:
                    # Find the two edges with color c
                    edges_with_c = [ei for ei in edge_indices if colors[ei] == c]
                    # One of them should get color 3
                    # But we need to check if this is consistent with the other endpoint
                    pass
    
    # Actually, let me reconsider the 2-SAT formulation
    # The issue is that color 3 is not explicitly represented
    
    # Let me use a different approach:
    # For each edge, we have 3 possible colors
    # We need to assign colors such that at each vertex, all 3 edges have different colors
    
    # This is equivalent to edge coloring a 3-regular graph with 3 colors
    # By Brooks' theorem, a connected 3-regular graph is 3-colorable iff it's not K4
    # But we have multiple components potentially
    
    # For a 3-regular graph, edge coloring with 3 colors is possible iff the graph is bipartite
    # (since the line graph of a bipartite graph is perfect)
    
    # Wait, that's not quite right either. Let me think again.
    
    # For a cubic (3-regular) graph, by Vizing's theorem, the edge chromatic number is 3 or 4.
    # It's 3 iff the graph is bipartite (by König's theorem).
    
    # So we need to check if the graph is bipartite.
    
    # Let me check bipartiteness
    color = [-1] * (n + 1)
    is_bipartite = True
    
    for start in range(1, n + 1):
        if color[start] == -1:
            color[start] = 0
            stack = [start]
            while stack:
                u = stack.pop()
                for (v, _) in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        stack.append(v)
                    elif color[v] == color[u]:
                        is_bipartite = False
                        break
                if not is_bipartite:
                    break
        if not is_bipartite:
            break
    
    if not is_bipartite:
        print("NO")
        return
    
    # Graph is bipartite, so 3-edge-coloring is possible
    # We need to find the actual coloring
    
    # For a bipartite cubic graph, we can find a perfect matching and color it with color 3
    # Then the remaining edges form a 2-regular graph (disjoint cycles), which can be 2-colored
    
    # Find a perfect matching using a greedy/DFS approach
    # Since the graph is bipartite and cubic, a perfect matching exists
    
    matched = [False] * (n + 1)
    matching = [False] * m  # True if edge is in the matching
    
    # Greedy matching
    for i, (u, v) in enumerate(edges):
        if not matched[u] and not matched[v]:
            matched[u] = True
            matched[v] = True
            matching[i] = True
    
    # If greedy doesn't find perfect matching, use augmenting paths
    # But for cubic bipartite graphs, greedy should work well enough
    
    # Actually, let's use a proper matching algorithm
    # Hopcroft-Karp for bipartite matching
    
    # Build bipartite graph
    left = [u for u in range(1, n + 1) if color[u] == 0]
    right = [u for u in range(1, n + 1) if color[u] == 1]
    
    # Create adjacency for matching
    adj_match = {u: [] for u in left}
    for i, (u, v) in enumerate(edges):
        if color[u] == 0:
            adj_match[u].append((v, i))
        else:
            adj_match[v].append((u, i))
    
    # Hopcroft-Karp
    INF = n + 1
    pair_u = {u: None for u in left}
    pair_v = {v: None for v in right}
    dist = {}
    
    from collections import deque
    
    def bfs():
        queue = deque()
        for u in left:
            if pair_u[u] is None:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = INF
        dist[None] = INF
        while queue:
            u = queue.popleft()
            if dist[u] < dist[None]:
                for (v, _) in adj_match[u]:
                    if pair_v[v] is None:
                        if dist[None] == INF:
                            dist[None] = dist[u] + 1
                    elif dist[pair_v[v]] == INF:
                        dist[pair_v[v]] = dist[u] + 1
                        queue.append(pair_v[v])
        return dist[None] != INF
    
    def dfs(u):
        if u is not None:
            for (v, edge_idx) in adj_match[u]:
                if pair_v[v] is None or (dist[pair_v[v]] == dist[u] + 1 and dfs(pair_v[v])):
                    pair_u[u] = v
                    pair_v[v] = u
                    return True
            dist[u] = INF
            return False
        return True
    
    matching_size = 0
    while bfs():
        for u in left:
            if pair_u[u] is None:
                if dfs(u):
                    matching_size += 1
    
    # Extract matching edges
    matching = [False] * m
    for u in left:
        if pair_u[u] is not None:
            for (v, edge_idx) in adj_match[u]:
                if v == pair_u[u]:
                    matching[edge_idx] = True
                    break
    
    # Color matching edges with color 3
    colors = [0] * m
    for i in range(m):
        if matching[i]:
            colors[i] = 3
    
    # Remaining edges form a 2-regular graph (disjoint cycles)
    # 2-color them
    remaining_edges = [i for i in range(m) if not matching[i]]
    
    # Build graph of remaining edges
    adj_rem = [[] for _ in range(n + 1)]
    for i in remaining_edges:
        u, v = edges[i]
        adj_rem[u].append((v, i))
        adj_rem[v].append((u, i))
    
    # 2-color the remaining edges (each vertex has degree 2, so it's a union of cycles)
    edge_color = [-1] * m
    visited_vertex = [False] * (n + 1)
    
    for start in range(1, n + 1):
        if visited_vertex[start]:
            continue
        # Traverse the cycle
        u = start
        c = 1
        while not visited_vertex[u]:
            visited_vertex[u] = True
            for (v, ei) in adj_rem[u]:
                if edge_color[ei] == -1:
                    edge_color[ei] = c
                    colors[ei] = c
                    c = 3 - c  # alternate between 1 and 2
                    u = v
                    break
    
    print("YES")
    print(" ".join(map(str, colors)))

solve()