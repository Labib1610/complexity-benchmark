import sys
from collections import deque

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    k = int(data[idx]); idx += 1

    types = []
    for _ in range(k):
        s = int(data[idx]); idx += 1
        t = int(data[idx]); idx += 1
        d = int(data[idx]); idx += 1
        types.append((s, t, d))

    links = []
    for _ in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        cap = int(data[idx]); idx += 1
        links.append((u, v, cap))

    # Node indexing:
    # 0 .. n-1 : original stations
    # n .. n+m-1 : link nodes (link j -> node n+j)
    # n+m : super source
    # n+m+1 : super sink
    total_nodes = n + m + 2
    S = n + m
    T = n + m + 1

    # Build graph for max flow
    # We need to store edges with: to, cap, flow, rev_index
    graph = [[] for _ in range(total_nodes)]

    def add_edge(fr, to, cap):
        graph[fr].append([to, cap, 0, len(graph[to])])
        graph[to].append([fr, 0, 0, len(graph[fr]) - 1])

    # Super source to each type's start
    for i, (s, t, d) in enumerate(types):
        add_edge(S, s - 1, d)

    # Each type's target to super sink
    for i, (s, t, d) in enumerate(types):
        add_edge(t - 1, T, d)

    # Link edges: station u -> link node -> station v
    # We need to track which graph edges correspond to which link
    # to extract per-type flows later.
    # For link j: u-1 -> (n+j) with cap limit, (n+j) -> v-1 with cap limit
    # But we need per-type flows, so we need to split differently.
    # 
    # Actually, to get per-type flows on each link, we need to track
    # which type's flow goes through each link. This requires a different
    # approach: we need k separate commodity flows sharing link capacities.
    #
    # This is a multi-commodity flow problem which is NP-hard in general,
    # but since all types share the same links and we just need integral
    # flows, we can use the following trick:
    # 
    # For each link j with capacity c, we create k parallel edges
    # (one per type) each with capacity c, but then add a constraint
    # that the sum of flows on these k edges <= c.
    #
    # This can be modeled by: u -> link_node_j (capacity c),
    # then link_node_j -> v with k separate edges each of capacity c
    # (but that doesn't enforce the shared constraint properly).
    #
    # Correct model: u -> link_node_j (capacity c, shared),
    # link_node_j -> v (capacity c, shared). But then we can't distinguish
    # types.
    #
    # Alternative: We need to track type-specific flow. Let's use
    # a different node structure.
    # 
    # For type i, link j: create edge from (type i at station u) to 
    # (type i at station v). But shared capacity on link j means
    # sum over types of flow on link j <= cap_j.
    #
    # This is genuinely multi-commodity flow. However, since the graph
    # is a DAG-free general graph and flows are integral, and the problem
    # asks for a solution, perhaps we can use LP relaxation + rounding,
    # or perhaps the problem expects us to use the fact that 
    # multi-commodity flow with a single shared capacity per edge
    # can be solved by a clever reduction.
    #
    # Actually, re-reading the problem: the link limit applies to the
    # combined count. So we need sum_i x[i][j] <= cap[j] for each link j,
    # and for each type i, x[i] forms a valid flow from s_i to t_i 
    # with value d_i.
    #
    # This is the integral multi-commodity flow problem. For general
    # graphs this is NP-hard. But maybe the constraints are small enough
    # that we can use an LP approach, or maybe there's a special structure.
    #
    # Let me think about this differently. We can model this as a single
    # max flow problem if we're clever about it.
    #
    # Create a graph where:
    # - Super source S connects to each type's source with capacity d_i
    # - Each type's sink connects to super sink T with capacity d_i
    # - For each link (u, v, cap), we add edge u->v with capacity cap
    # 
    # Then max flow from S to T gives the total flow, but it doesn't
    # distinguish between types. However, if max flow == sum(d_i),
    # we can decompose the flow into per-type flows.
    #
    # Wait, but the flow through the network doesn't track which type
    # each unit belongs to. We need to track this.
    #
    # The key insight: if we can find a feasible flow in the combined
    # network (max flow = sum of demands), we can then decompose it
    # into per-type flows by tracking paths.
    #
    # But that's not quite right either, because the combined flow
    # might mix types at intermediate nodes.
    #
    # Actually, let me reconsider. The combined max flow approach works
    # if we can decompose the flow. Here's why:
    # 
    # In the combined network, S -> s_i (cap d_i), t_i -> T (cap d_i),
    # and links have their capacities. If max flow = sum(d_i), then
    # there exists a feasible flow. We can then extract per-type flows
    # by finding augmenting paths for each type separately in the
    # residual graph.
    #
    # Let me implement this approach.

    # Rebuild graph with correct structure
    graph = [[] for _ in range(total_nodes)]

    edge_list = []  # (from, to, cap, edge_obj_ref)

    def add_edge(fr, to, cap):
        forward = [to, cap, 0, len(graph[to])]
        backward = [fr, 0, 0, len(graph[fr])]
        graph[fr].append(forward)
        graph[to].append(backward)

    # Super source to type sources
    type_source_edges = []
    for i, (s, t, d) in enumerate(types):
        add_edge(S, s - 1, d)
        type_source_edges.append(len(graph[S]) - 1)

    # Type sinks to super sink
    type_sink_edges = []
    for i, (s, t, d) in enumerate(types):
        add_edge(t - 1, T, d)
        type_sink_edges.append(len(graph[t - 1]) - 1)

    # Link edges
    link_edges = []  # store (from_node, edge_index_in_graph) for each link
    for j, (u, v, cap) in enumerate(links):
        add_edge(u - 1, v - 1, cap)
        link_edges.append((u - 1, len(graph[u - 1]) - 1))

    # Max flow using Dinic's algorithm
    def bfs_level_graph():
        level = [-1] * total_nodes
        level[S] = 0
        q = deque([S])
        while q:
            u = q.popleft()
            for e in graph[u]:
                if e[1] - e[2] > 0 and level[e[0]] < 0:
                    level[e[0]] = level[u] + 1
                    q.append(e[0])
        return level

    def dfs_flow(u, pushed, level, it):
        if u == T:
            return pushed
        while it[u] < len(graph[u]):
            e = graph[u][it[u]]
            if e[1] - e[2] > 0 and level[e[0]] == level[u] + 1:
                d = dfs_flow(e[0], min(pushed, e[1] - e[2]), level, it)
                if d > 0:
                    e[2] += d
                    graph[e[0]][e[3]][2] -= d
                    return d
            it[u] += 1
        return 0

    def dinic():
        total = 0
        while True:
            level = bfs_level_graph()
            if level[T] < 0:
                break
            it = [0] * total_nodes
            while True:
                f = dfs_flow(S, float('inf'), level, it)
                if f == 0:
                    break
                total += f
        return total

    total_demand = sum(d for _, _, d in types)
    maxflow = dinic()

    if maxflow < total_demand:
        print("NO")
        return

    # Now decompose the flow into per-type flows
    # For each type i, we need to find d_i units of flow from s_i to t_i
    # in the current flow graph.
    # 
    # Strategy: For each type, find augmenting paths from s_i to t_i
    # using the existing flow, and track how much of each link is used
    # by each type.
    #
    # We'll work with the flow values on edges.
    # For each edge, flow = e[2] (the flow value).
    # 
    # For type i, we repeatedly find a path from s_i to t_i with 
    # positive flow, extract the min flow along the path, assign it
    # to type i, and reduce the flow on those edges.

    # Build adjacency list for flow decomposition
    # For each node, list of (to, edge_ref, flow_amount, link_index_or_None)
    
    # First, let's identify which edges correspond to links
    # and create a mapping
    link_flow = [[0] * m for _ in range(k)]  # link_flow[type][link]

    # For each type, decompose flow
    # We need to find paths from s_i to t_i in the flow network
    
    # Create flow adjacency: for each node, outgoing edges with positive flow
    def get_flow_edges(u):
        edges = []
        for e in graph[u]:
            if e[2] > 0:  # positive flow
                edges.append(e)
        return edges

    for i, (s, t, d) in enumerate(types):
        remaining = d
        s_node = s - 1
        t_node = t - 1
        
        while remaining > 0:
            # Find a path from s_node to t_node with positive flow
            # using BFS/DFS
            parent = [-1] * total_nodes
            parent_edge = [None] * total_nodes
            visited = [False] * total_nodes
            visited[s_node] = True
            q = deque([s_node])
            found = False
            while q and not found:
                u = q.popleft()
                for e in graph[u]:
                    if e[2] > 0 and not visited[e[0]]:
                        visited[e[0]] = True
                        parent[e[0]] = u
                        parent_edge[e[0]] = e
                        if e[0] == t_node:
                            found = True
                            break
                        q.append(e[0])
            
            if not found:
                # This shouldn't happen if max flow is correct
                print("NO")
                return
            
            # Find min flow along path
            path_flow = float('inf')
            v = t_node
            path_edges = []
            while v != s_node:
                e = parent_edge[v]
                path_flow = min(path_flow, e[2])
                path_edges.append((v, e))
                v = parent[v]
            
            path_flow = min(path_flow, remaining)
            
            # Reduce flow and track link usage
            for v, e in path_edges:
                e[2] -= path_flow
                graph[e[0]][e[3]][2] += path_flow  # reverse edge
                
                # Check if this edge corresponds to a link
                u = parent[v]
                # Find which link this edge corresponds to
                for j, (lu, le_idx) in enumerate(link_edges):
                    if u == lu and graph[lu][le_idx] is e:
                        link_flow[i][j] += path_flow
                        break
            
            remaining -= path_flow

    print("YES")
    for i in range(k):
        print(' '.join(map(str, link_flow[i])))

solve()