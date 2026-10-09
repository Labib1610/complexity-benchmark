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
    
    core = [int(next(it)) for _ in range(t)]
    core_set = set(core)
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # If t <= 1, no translation needed
    if t <= 1:
        print(0)
        return
    
    # Compute pairwise shortest distances between core languages
    # dist_core[i][j] = shortest distance from core[i] to core[j]
    INF = 10**18
    dist_core = [[INF] * t for _ in range(t)]
    
    for i, start in enumerate(core):
        dist = [INF] * (n + 1)
        dist[start] = 0
        pq = [(0, start)]
        while pq:
            d, u = heapq.heappop(pq)
            if d != dist[u]:
                continue
            for v, w in adj[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))
        
        for j, end in enumerate(core):
            dist_core[i][j] = dist[end]
    
    # Steiner tree DP on core nodes
    # dp[mask][v] = min cost to connect core nodes in mask, with tree ending at node v
    # We use 1D array for each mask, indexed by node
    dp = [[INF] * (n + 1) for _ in range(1 << t)]
    
    # Initialize: single core nodes
    for i, c in enumerate(core):
        dp[1 << i][c] = 0
    
    # Iterate over all masks
    for mask in range(1, 1 << t):
        # Skip single-node masks already initialized
        if mask & (mask - 1) == 0:
            continue
        
        # Combine submasks
        submask = (mask - 1) & mask
        while submask:
            other = mask ^ submask
            for v in range(1, n + 1):
                if dp[submask][v] < INF and dp[other][v] < INF:
                    dp[mask][v] = min(dp[mask][v], dp[submask][v] + dp[other][v])
            submask = (submask - 1) & mask
        
        # Dijkstra to propagate: dp[mask][u] + dist(u,v) -> dp[mask][v]
        pq = []
        for v in range(1, n + 1):
            if dp[mask][v] < INF:
                heapq.heappush(pq, (dp[mask][v], v))
        
        while pq:
            d, u = heapq.heappop(pq)
            if d != dp[mask][u]:
                continue
            for v, w in adj[u]:
                nd = d + w
                if nd < dp[mask][v]:
                    dp[mask][v] = nd
                    heapq.heappush(pq, (nd, v))
    
    full_mask = (1 << t) - 1
    result = min(dp[full_mask])
    print(result)

if __name__ == "__main__":
    solve()