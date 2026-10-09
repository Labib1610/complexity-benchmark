import sys

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    k = int(input_data[idx]); idx += 1

    resources = []
    for _ in range(k):
        s = int(input_data[idx]) - 1; idx += 1
        t = int(input_data[idx]) - 1; idx += 1
        d = int(input_data[idx]); idx += 1
        resources.append((s, t, d))

    edges = []
    for _ in range(m):
        u = int(input_data[idx]) - 1; idx += 1
        v = int(input_data[idx]) - 1; idx += 1
        cap = int(input_data[idx]); idx += 1
        edges.append((u, v, cap))

    # Build flow network
    # Nodes: 0..n-1 original, n..n+k-1 resource nodes, n+k super source, n+k+1 super sink
    total_nodes = n + k + 2
    S = n + k
    T = n + k + 1

    graph = [[] for _ in range(total_nodes)]
    edge_list = []

    def add_edge(u, v, cap):
        graph[u].append(len(edge_list))
        edge_list.append([v, cap, 0])
        graph[v].append(len(edge_list))
        edge_list.append([u, 0, 0])

    # Resource edges: S -> resource node -> source compartment
    for i, (s, t, d) in enumerate(resources):
        add_edge(S, n + i, d)
        add_edge(n + i, s, d)

    # Original edges with capacity
    for j, (u, v, cap) in enumerate(edges):
        add_edge(u, v, cap)

    # Target edges: target compartment -> T
    for i, (s, t, d) in enumerate(resources):
        add_edge(t, T, d)

    # Dinic's max flow
    def bfs():
        level = [-1] * total_nodes
        level[S] = 0
        queue = [S]
        head = 0
        while head < len(queue):
            u = queue[head]; head += 1
            for eid in graph[u]:
                v, cap, flow = edge_list[eid]
                if cap - flow > 0 and level[v] == -1:
                    level[v] = level[u] + 1
                    queue.append(v)
        return level

    def dfs(u, pushed, level, it):
        if u == T:
            return pushed
        while it[u] < len(graph[u]):
            eid = graph[u][it[u]]
            v, cap, flow = edge_list[eid]
            if cap - flow > 0 and level[v] == level[u] + 1:
                d = dfs(v, min(pushed, cap - flow), level, it)
                if d > 0:
                    edge_list[eid][2] += d
                    edge_list[eid ^ 1][2] -= d
                    return d
            it[u] += 1
        return 0

    total_flow = 0
    while True:
        level = bfs()
        if level[T] == -1:
            break
        it = [0] * total_nodes
        while True:
            f = dfs(S, float('inf'), level, it)
            if f == 0:
                break
            total_flow += f

    total_demand = sum(d for _, _, d in resources)
    if total_flow < total_demand:
        print("NO")
        return

    # Extract per-resource flows on original edges
    # Original edges start at index 2*k (after 2*k resource edges) and come in pairs
    # Each original edge j corresponds to edge_list[2*k + 2*j]
    result = [[0] * m for _ in range(k)]

    for j in range(m):
        eid = 2 * k + 2 * j
        flow = edge_list[eid][2]
        if flow == 0:
            continue
        u = edges[j][0]
        v = edges[j][1]
        # Find resource flows: for each resource i, flow from n+i to u is on edge 2 + 2*i
        # But we need to decompose the flow on edge (u,v) into resource types
        # Use the residual graph to find paths

    # Flow decomposition for each resource
    # For resource i, we need to find paths from s_i to t_i carrying d_i total
    # We use the residual graph (forward edges with flow, backward edges with negative flow)

    # Build adjacency for flow decomposition
    flow_adj = [[] for _ in range(n)]
    for j in range(m):
        eid = 2 * k + 2 * j
        u, v, cap = edges[j]
        f = edge_list[eid][2]
        if f > 0:
            flow_adj[u].append((v, j, f))

    for i, (s, t, d) in enumerate(resources):
        remaining = d
        while remaining > 0:
            # BFS to find path from s to t in flow graph
            parent = [-1] * n
            parent_edge = [-1] * n
            parent_flow = [0] * n
            queue = [s]
            head = 0
            parent[s] = s
            parent_flow[s] = remaining
            while head < len(queue):
                u = queue[head]; head += 1
                if u == t:
                    break
                for idx, (v, j, f) in enumerate(flow_adj[u]):
                    if f > 0 and parent[v] == -1:
                        parent[v] = u
                        parent_edge[v] = j
                        parent_flow[v] = min(parent_flow[u], f)
                        queue.append(v)
                        if v == t:
                            break

            if parent[t] == -1:
                break

            path_flow = parent_flow[t]
            path_flow = min(path_flow, remaining)
            u = t
            while u != s:
                j = parent_edge[u]
                # Find and update flow_adj
                for idx, (v, ej, f) in enumerate(flow_adj[parent[u]]):
                    if v == u and ej == j:
                        flow_adj[parent[u]][idx] = (v, ej, f - path_flow)
                        break
                result[i][j] += path_flow
                u = parent[u]
            remaining -= path_flow

    print("YES")
    for i in range(k):
        print(' '.join(map(str, result[i])))

solve()