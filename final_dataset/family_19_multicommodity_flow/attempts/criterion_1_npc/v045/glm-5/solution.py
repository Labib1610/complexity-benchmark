import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    try:
        n = int(next(it))
        m = int(next(it))
        k = int(next(it))
    except StopIteration:
        return

    consignments = []
    for _ in range(k):
        s = int(next(it))
        t = int(next(it))
        d = int(next(it))
        consignments.append((s, t, d))

    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        c = int(next(it))
        edges.append((u, v, c))

    # Build flow network
    # Nodes: 0..n-1 (original), n..n+m-1 (edge nodes), n+m (super source), n+m+1 (super sink)
    N = n + m + 2
    s_super = n + m
    t_super = n + m + 1
    
    graph = [[] for _ in range(N)]
    
    def add_edge(u, v, cap, rev_cap=0):
        graph[u].append([v, cap, len(graph[v])])
        graph[v].append([u, rev_cap, len(graph[u]) - 1])

    # Edges from edge nodes to original nodes (infinite capacity)
    for i, (u, v, c) in enumerate(edges):
        edge_node = n + i
        add_edge(edge_node, v - 1, float('inf'))
        add_edge(u - 1, edge_node, float('inf'))

    # Edges from super source to consignment starts
    for i, (s, t, d) in enumerate(consignments):
        add_edge(s_super, s - 1, d)

    # Edges from consignment ends to super sink
    for i, (s, t, d) in enumerate(consignments):
        add_edge(t - 1, t_super, d)

    # Edges from super source to edge nodes (corridor capacities)
    for i, (u, v, c) in enumerate(edges):
        add_edge(s_super, n + i, c)

    # Dinic's algorithm
    level = [0] * N
    ptr = [0] * N
    
    def bfs():
        for i in range(N):
            level[i] = -1
        level[t_super] = N  # Start from sink
        queue = [t_super]
        head = 0
        while head < len(queue):
            u = queue[head]
            head += 1
            for v, cap, rev_idx in graph[u]:
                # Check reverse edge capacity (flow available in original direction)
                if cap > 0 and level[v] == -1:
                    level[v] = level[u] - 1
                    queue.append(v)
        return level[s_super] != -1

    def dfs(u, flow):
        if u == t_super:
            return flow
        for i in range(ptr[u], len(graph[u])):
            ptr[u] = i
            v, cap, rev_idx = graph[u][i]
            if cap > 0 and level[v] == level[u] + 1:
                pushed = dfs(v, min(flow, cap))
                if pushed > 0:
                    graph[u][i][1] -= pushed
                    graph[v][rev_idx][1] += pushed
                    return pushed
        return 0

    total_flow = 0
    while bfs():
        ptr = [0] * N
        while True:
            pushed = dfs(s_super, float('inf'))
            if pushed == 0:
                break
            total_flow += pushed

    # Check if all demands are satisfied
    total_demand = sum(d for s, t, d in consignments)
    if total_flow < total_demand:
        print("NO")
        return

    print("YES")
    
    # Extract flow for each consignment on each corridor
    # We need to find how much of each consignment's flow goes through each edge
    # This requires running k individual max flows
    
    result = [[0] * m for _ in range(k)]
    
    for idx, (s, t, d) in enumerate(consignments):
        # Build residual graph for this consignment
        # Nodes: 0..n-1 (original), n..n+m-1 (edge nodes)
        N_local = n + m
        g = [[] for _ in range(N_local)]
        
        def add_edge_local(u, v, cap):
            g[u].append([v, cap, len(g[v])])
            g[v].append([u, 0, len(g[u]) - 1])
        
        # Add edges from edge nodes to original nodes
        for i, (u, v, c) in enumerate(edges):
            edge_node = n + i
            add_edge_local(edge_node, v - 1, float('inf'))
            add_edge_local(u - 1, edge_node, float('inf'))
        
        # Add capacity constraints on corridors
        for i in range(m):
            # Remaining capacity for this consignment
            remaining = edges[i][2]
            for j in range(idx):
                remaining -= result[j][i]
            if remaining > 0:
                add_edge_local(n + i, edges[i][1] - 1, remaining)
        
        # Dinic for this consignment
        level_local = [0] * N_local
        ptr_local = [0] * N_local
        source = s - 1
        sink = t - 1
        
        def bfs_local():
            for i in range(N_local):
                level_local[i] = -1
            level_local[source] = 0
            queue = [source]
            head = 0
            while head < len(queue):
                u = queue[head]
                head += 1
                for v, cap, rev_idx in g[u]:
                    if cap > 0 and level_local[v] == -1:
                        level_local[v] = level_local[u] + 1
                        queue.append(v)
            return level_local[sink] != -1
        
        def dfs_local(u, flow):
            if u == sink:
                return flow
            for i in range(ptr_local[u], len(g[u])):
                ptr_local[u] = i
                v, cap, rev_idx = g[u][i]
                if cap > 0 and level_local[v] == level_local[u] + 1:
                    pushed = dfs_local(v, min(flow, cap))
                    if pushed > 0:
                        g[u][i][1] -= pushed
                        g[v][rev_idx][1] += pushed
                        return pushed
            return 0
        
        flow_sent = 0
        while bfs_local():
            ptr_local = [0] * N_local
            while True:
                pushed = dfs_local(source, float('inf'))
                if pushed == 0:
                    break
                flow_sent += pushed
        
        # Extract flow on each corridor
        for i in range(m):
            edge_node = n + i
            v = edges[i][1] - 1
            # Find the edge from edge_node to v and check reverse edge
            for j, (to, cap, rev_idx) in enumerate(g[edge_node]):
                if to == v:
                    # The reverse edge (v -> edge_node) has the flow
                    flow_on_edge = g[v][rev_idx][1]
                    result[idx][i] = flow_on_edge
                    break
    
    for row in result:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    solve()