import sys
from heapq import heappush, heappop

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    
    key_companies = [int(next(it)) for _ in range(t)]
    key_set = set(key_companies)
    
    # Build adjacency list
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # If t <= 1, no mergers needed
    if t <= 1:
        print(0)
        return
    
    # Compute shortest paths between all pairs of key companies
    # dist_key[i][j] = shortest path between key i and key j
    key_indices = {key: i for i, key in enumerate(key_companies)}
    num_keys = t
    
    # dist_key[i][j] stores the minimum cost to connect key i and key j
    dist_key = [[float('inf')] * num_keys for _ in range(num_keys)]
    
    for idx, start in enumerate(key_companies):
        # Dijkstra from start
        dist = [float('inf')] * (n + 1)
        dist[start] = 0
        pq = [(0, start)]
        while pq:
            d, u = heappop(pq)
            if d > dist[u]:
                continue
            for v, w in adj[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heappush(pq, (nd, v))
        
        # Record distances to other key companies
        for other_idx, other in enumerate(key_companies):
            dist_key[idx][other_idx] = dist[other]
    
    # Steiner Tree DP
    # dp[mask][v] = minimum cost to connect key companies in mask, ending at node v
    # We use a 2D array where v is indexed by key company index
    
    INF = float('inf')
    dp = [[INF] * num_keys for _ in range(1 << num_keys)]
    
    # Base case: single key company
    for i in range(num_keys):
        dp[1 << i][i] = 0
    
    # Iterate over all masks
    for mask in range(1, 1 << num_keys):
        # Skip single element masks (already initialized)
        if mask & (mask - 1) == 0:
            continue
        
        # For each ending key company v
        for v in range(num_keys):
            if not (mask & (1 << v)):
                continue
            
            # Try all submasks
            submask = (mask - 1) & mask
            while submask:
                other = mask ^ submask
                if submask & (1 << v):
                    # v is in submask, need to connect other to v
                    for u in range(num_keys):
                        if other & (1 << u):
                            cost = dp[submask][v] + dp[other][u] + dist_key[u][v]
                            if cost < dp[mask][v]:
                                dp[mask][v] = cost
                submask = (submask - 1) & mask
        
        # Dijkstra-like optimization: propagate through edges
        # This handles the case where we extend the tree by adding an edge
        pq = []
        for v in range(num_keys):
            if mask & (1 << v):
                heappush(pq, (dp[mask][v], v))
        
        while pq:
            d, u = heappop(pq)
            if d > dp[mask][u]:
                continue
            for v in range(num_keys):
                nd = d + dist_key[u][v]
                if nd < dp[mask][v]:
                    dp[mask][v] = nd
                    heappush(pq, (nd, v))
    
    full_mask = (1 << num_keys) - 1
    result = min(dp[full_mask])
    print(result)

solve()