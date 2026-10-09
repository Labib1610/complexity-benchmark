import sys
from collections import deque

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    products = []
    for _ in range(k):
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        d = int(next(it))
        products.append((s, t, d))
    
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        cap = int(next(it))
        edges.append((u, v, cap))
    
    # Build multi-commodity flow network
    # Node indexing: 
    # For each hub v and product p: node = v * k + p (k nodes per hub)
    # Source: n*k
    # Sink: n*k + 1
    # Total nodes: n*k + 2
    
    base = n * k
    S = base
    T = base + 1
    N = base + 2
    
    graph = [[] for _ in range(N)]
    edge_list = []
    
    def add_edge(u, v, cap, rev_idx):
        graph[u].append(len(edge_list))
        edge_list.append([v, cap, rev_idx])
    
    # Add edges for each product
    for p, (s, t, d) in enumerate(products):
        # Source to origin
        add_edge(S, s * k + p, d, len(graph[s * k + p]))
        add_edge(s * k + p, S, 0, len(graph[S]) - 1)
        
        # Destination to sink
        add_edge(t * k + p, T, d, len(graph[T]))
        add_edge(T, t * k + p, 0, len(graph[t * k + p]) - 1)
        
        # Internal edges within product (hub to hub via lanes)
        for j, (u, v, _) in enumerate(edges):
            u_node = u * k + p
            v_node = v * k + p
            add_edge(u_node, v_node, d, len(graph[v_node]))
            add_edge(v_node, u_node, 0, len(graph[u_node]) - 1)
    
    # Add shared capacity edges (product p to product p+1 on same lane)
    for j, (u, v, cap) in enumerate(edges):
        for p in range(k - 1):
            u_node_from = u * k + p
            u_node_to = u * k + p + 1
            v_node_from = v * k + p
            v_node_to = v * k + p + 1
            
            # Forward lane: capacity constraint
            add_edge(u_node_from, u_node_to, cap, len(graph[u_node_to]))
            add_edge(u_node_to, u_node_from, 0, len(graph[u_node_from]) - 1)
            
            # Backward lane: capacity constraint
            add_edge(v_node_to, v_node_from, cap, len(graph[v_node_from]))
            add_edge(v_node_from, v_node_to, 0, len(graph[v_node_to]) - 1)
    
    # Dinic's max flow
    def bfs():
        level = [-1] * N
        level[S] = 0
        q = deque([S])
        while q:
            u = q.popleft()
            for ei in graph[u]:
                v, cap, _ = edge_list[ei]
                if cap > 0 and level[v] == -1:
                    level[v] = level[u] + 1
                    q.append(v)
        return level
    
    def dfs(u, flow, level, ptr):
        if u == T:
            return flow
        for i in range(ptr[u], len(graph[u])):
            ei = graph[u][i]
            v, cap, rev_idx = edge_list[ei]
            if cap > 0 and level[v] == level[u] + 1:
                pushed = dfs(v, min(flow, cap), level, ptr)
                if pushed > 0:
                    edge_list[ei][1] -= pushed
                    edge_list[rev_idx][1] += pushed
                    return pushed
            ptr[u] += 1
        return 0
    
    total_demand = sum(d for _, _, d in products)
    total_flow = 0
    
    while True:
        level = bfs()
        if level[T] == -1:
            break
        ptr = [0] * N
        while True:
            pushed = dfs(S, float('inf'), level, ptr)
            if pushed == 0:
                break
            total_flow += pushed
    
    if total_flow != total_demand:
        print("NO")
        return
    
    print("YES")
    
    # Extract flows for each product on each lane
    # Find the edge index for product p on lane j
    for p in range(k):
        result = []
        for j, (u, v, _) in enumerate(edges):
            u_node = u * k + p
            v_node = v * k + p
            # Find the edge from u_node to v_node
            flow_on_lane = 0
            for ei in graph[u_node]:
                if edge_list[ei][0] == v_node:
                    # Original capacity was d, current remaining is edge_list[ei][1]
                    # Flow sent = original_cap - remaining
                    # But we need to find original capacity
                    # For product edges, original cap = d (product demand)
                    # Actually, we need to track original capacity
                    # Let's use the reverse edge's capacity to get flow
                    rev_idx = edge_list[ei][2]
                    flow_on_lane = edge_list[rev_idx][1]
                    break
            result.append(str(flow_on_lane))
        print(' '.join(result))

solve()