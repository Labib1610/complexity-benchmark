import sys
from collections import defaultdict, deque

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    k = int(input_data[idx]); idx += 1
    
    orders = []
    for i in range(k):
        s = int(input_data[idx]); idx += 1
        t = int(input_data[idx]); idx += 1
        d = int(input_data[idx]); idx += 1
        orders.append((s, t, d))
    
    tubes = []
    for j in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        cap = int(input_data[idx]); idx += 1
        tubes.append((u, v, cap))
    
    # Node numbering: 0..n-1 are vats, n is super-source, n+1 is super-sink
    super_src = n
    super_snk = n + 1
    
    # Build adjacency list for Dinic's
    # Edge: (to, cap, edge_id)
    # We store edges in a list: edges[edge_id] = [to, cap, rev_id]
    
    graph = defaultdict(list)
    edges = []
    
    def add_edge(u, v, cap):
        graph[u].append(len(edges))
        edges.append([v, cap])
        graph[v].append(len(edges))
        edges.append([u, 0])
    
    # Add super-source to order origins
    for i, (s, t, d) in enumerate(orders):
        add_edge(super_src, s, d)
    
    # Add tubes (shared capacity)
    for u, v, cap in tubes:
        add_edge(u, v, cap)
    
    # Add order destinations to super-sink
    for i, (s, t, d) in enumerate(orders):
        add_edge(t, super_snk, d)
    
    total_demand = sum(d for _, _, d in orders)
    
    # Dinic's algorithm
    def bfs_level():
        level = defaultdict(lambda: -1)
        level[super_src] = 0
        q = deque([super_src])
        while q:
            u = q.popleft()
            for eid in graph[u]:
                v, cap = edges[eid]
                if cap > 0 and level[v] < 0:
                    level[v] = level[u] + 1
                    q.append(v)
        return level if level[super_snk] >= 0 else None
    
    def dfs_flow(u, pushed, level, it):
        if u == super_snk:
            return pushed
        while it[u] < len(graph[u]):
            eid = graph[u][it[u]]
            v, cap = edges[eid]
            if cap > 0 and level[v] == level[u] + 1:
                d = dfs_flow(v, min(pushed, cap), level, it)
                if d > 0:
                    edges[eid][1] -= d
                    edges[eid ^ 1][1] += d
                    return d
            it[u] += 1
        return 0
    
    max_flow = 0
    while True:
        level = bfs_level()
        if level is None:
            break
        it = defaultdict(int)
        while True:
            f = dfs_flow(super_src, float('inf'), level, it)
            if f == 0:
                break
            max_flow += f
    
    if max_flow < total_demand:
        print("NO")
        return
    
    # Now extract per-order flows
    # For each order, find paths from s to t in residual graph and push flow
    # We need to track which edges correspond to which tubes
    
    # Build mapping from (u,v) to list of edge ids (for tubes)
    # Actually, let's track the edge ids for tubes specifically
    
    # The edges were added in order:
    # - k pairs for super_src -> origins (edge ids 0..2k-1)
    # - m pairs for tubes (edge ids 2k..2k+2m-1)
    # - k pairs for destinations -> super_snk (edge ids 2k+2m..2k+2m+2k-1)
    
    tube_edge_start = 2 * k
    result = [[0] * m for _ in range(k)]
    
    # For each order, extract flow
    for order_idx, (s, t, d) in enumerate(orders):
        remaining = d
        while remaining > 0:
            # BFS/DFS to find path from s to t in residual graph
            # We need to avoid super_src and super_snk edges
            parent = {}
            visited = set()
            visited.add(s)
            q = deque([s])
            found = False
            while q and not found:
                u = q.popleft()
                for eid in graph[u]:
                    v, cap = edges[eid]
                    if cap > 0 and v not in visited:
                        # Skip super source/sink edges
                        if v == super_src or v == super_snk:
                            continue
                        if u == super_src or u == super_snk:
                            continue
                        visited.add(v)
                        parent[v] = (u, eid)
                        if v == t:
                            found = True
                            break
                        q.append(v)
            
            if not found:
                # This shouldn't happen if max_flow == total_demand
                print("NO")
                return
            
            # Find bottleneck
            path_edges = []
            curr = t
            bottleneck = remaining
            while curr != s:
                u, eid = parent[curr]
                path_edges.append(eid)
                bottleneck = min(bottleneck, edges[eid][1])
                curr = u
            
            # Push flow
            for eid in path_edges:
                edges[eid][1] -= bottleneck
                edges[eid ^ 1][1] += bottleneck
                # Check if this edge is a tube edge
                if eid >= tube_edge_start and eid < tube_edge_start + 2 * m:
                    tube_idx = (eid - tube_edge_start) // 2
                    result[order_idx][tube_idx] += bottleneck
            
            remaining -= bottleneck
    
    print("YES")
    for row in result:
        print(' '.join(map(str, row)))

solve()