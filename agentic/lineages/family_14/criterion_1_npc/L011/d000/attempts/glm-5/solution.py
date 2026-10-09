import sys
import heapq

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    
    primary = set()
    for _ in range(t):
        primary.add(int(next(it)))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    if t <= 1:
        print(0)
        return
    
    # Compute all-pairs shortest paths among primary nodes
    # dist_primary[u][v] = shortest distance from primary u to primary v
    primary_list = list(primary)
    primary_idx = {p: i for i, p in enumerate(primary_list)}
    num_primary = len(primary_list)
    
    # For each primary node, run Dijkstra
    dist_primary = [[float('inf')] * num_primary for _ in range(num_primary)]
    
    for idx, start in enumerate(primary_list):
        dist = [float('inf')] * (n + 1)
        dist[start] = 0
        pq = [(0, start)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, w in adj[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))
        
        for j, p in enumerate(primary_list):
            dist_primary[idx][j] = dist[p]
    
    # Prim's algorithm on the complete graph of primary nodes
    total_cost = 0
    in_mst = [False] * num_primary
    min_edge = [float('inf')] * num_primary
    min_edge[0] = 0
    
    for _ in range(num_primary):
        # Find minimum edge to add
        u = -1
        for v in range(num_primary):
            if not in_mst[v] and (u == -1 or min_edge[v] < min_edge[u]):
                u = v
        
        in_mst[u] = True
        total_cost += min_edge[u]
        
        # Update minimum edges
        for v in range(num_primary):
            if not in_mst[v] and dist_primary[u][v] < min_edge[v]:
                min_edge[v] = dist_primary[u][v]
    
    print(total_cost)

solve()