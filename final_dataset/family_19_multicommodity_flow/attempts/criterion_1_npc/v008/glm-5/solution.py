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
    
    products = []
    for _ in range(k):
        s = int(next(it))
        t = int(next(it))
        d = int(next(it))
        products.append((s, t, d))
    
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        cap = int(next(it))
        edges.append((u, v, cap))
    
    # Build flow network
    # Nodes: 0..n-1 are original hubs
    # Node n is super source, node n+1 is super sink
    N = n + 2
    source = n
    sink = n + 1
    
    # Edge structure: to, capacity, flow, rev_index
    graph = [[] for _ in range(N)]
    edge_info = []  # (from, to, capacity, index_in_graph[from])
    
    # Add product edges from super source to origins
    for i, (s, t, d) in enumerate(products):
        u = source
        v = s - 1  # 0-indexed
        cap = d
        graph[u].append([v, cap, 0, len(graph[v])])
        graph[v].append([u, 0, 0, len(graph[u]) - 1])
        edge_info.append((u, v, cap, len(graph[u]) - 1))
    
    # Add product edges from destinations to super sink
    for i, (s, t, d) in enumerate(products):
        u = t - 1  # 0-indexed
        v = sink
        cap = d
        graph[u].append([v, cap, 0, len(graph[v])])
        graph[v].append([u, 0, 0, len(graph[u]) - 1])
    
    # Add shared lane edges
    lane_edge_indices = []
    for u, v, cap in edges:
        u0 = u - 1
        v0 = v - 1
        graph[u0].append([v0, cap, 0, len(graph[v0])])
        graph[v0].append([u0, 0, 0, len(graph[u0]) - 1])
        lane_edge_indices.append((u0, len(graph[u0]) - 1))
    
    total_demand = sum(d for _, _, d in products)
    
    # Dinic's algorithm
    def bfs():
        level = [-1] * N
        level[source] = 0
        q = deque([source])
        while q:
            u = q.popleft()
            for e in graph[u]:
                if e[1] - e[2] > 0 and level[e[0]] < 0:
                    level[e[0]] = level[u] + 1
                    q.append(e[0])
        return level
    
    def dfs(u, flow, level, ptr):
        if u == sink:
            return flow
        for i in range(ptr[u], len(graph[u])):
            e = graph[u][i]
            v, cap, f, rev = e
            if cap - f > 0 and level[v] == level[u] + 1:
                pushed = dfs(v, min(flow, cap - f), level, ptr)
                if pushed > 0:
                    e[2] += pushed
                    graph[v][rev][2] -= pushed
                    return pushed
            ptr[u] += 1
        return 0
    
    flow = 0
    while True:
        level = bfs()
        if level[sink] < 0:
            break
        ptr = [0] * N
        while True:
            pushed = dfs(source, float('inf'), level, ptr)
            if pushed == 0:
                break
            flow += pushed
    
    if flow != total_demand:
        print("NO")
        return
    
    print("YES")
    
    # Decompose flow for each product
    # We need to find how much of each product goes through each lane
    # Use flow decomposition with product-specific tracking
    
    # Build residual graph for decomposition
    # For each edge, track which products can use it
    
    # Product flows: for each product, track flow on each lane
    product_flows = [[0] * m for _ in range(k)]
    
    # For each product, decompose its flow
    for prod_idx in range(k):
        s, t, d = products[prod_idx]
        s0 = s - 1
        t0 = t - 1
        
        # Find paths from s0 to t0 in the residual graph
        # that were used by this product
        remaining = d
        
        # Use DFS to find augmenting paths for this product
        # We need to track which edges belong to which product
        
        # Build a subgraph for this product
        # An edge (u,v) can be used by product i if:
        # - It's a lane edge with positive flow
        # - Or it's the source edge for this product
        # - Or it's the sink edge for this product
        
        while remaining > 0:
            # BFS to find a path
            parent = [-1] * N
            parent_edge = [-1] * N
            q = deque([s0])
            parent[s0] = s0
            
            while q and parent[t0] == -1:
                u = q.popleft()
                for ei, e in enumerate(graph[u]):
                    v, cap, f, rev = e
                    if f > 0 and parent[v] == -1:
                        parent[v] = u
                        parent_edge[v] = ei
                        q.append(v)
            
            if parent[t0] == -1:
                break
            
            # Find bottleneck
            path = []
            v = t0
            while v != s0:
                u = parent[v]
                ei = parent_edge[v]
                path.append((u, ei))
                v = u
            path.reverse()
            
            # Find minimum flow on path
            bottleneck = remaining
            v = t0
            while v != s0:
                u = parent[v]
                ei = parent_edge[v]
                e = graph[u][ei]
                bottleneck = min(bottleneck, e[2])
                v = u
            
            # Update flows and track lane usage
            v = t0
            while v != s0:
                u = parent[v]
                ei = parent_edge[v]
                e = graph[u][ei]
                e[2] -= bottleneck
                rev = e[3]
                graph[v][rev][2] += bottleneck
                
                # Check if this is a lane edge
                for lane_idx, (lu, lei) in enumerate(lane_edge_indices):
                    if lu == u and lei == ei:
                        product_flows[prod_idx][lane_idx] += bottleneck
                        break
                
                v = u
            
            remaining -= bottleneck
    
    for pf in product_flows:
        print(' '.join(map(str, pf)))

if __name__ == "__main__":
    solve()