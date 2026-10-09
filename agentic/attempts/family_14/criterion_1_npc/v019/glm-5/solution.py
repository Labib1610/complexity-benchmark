import sys
import heapq

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    
    focal = [int(next(it)) for _ in range(t)]
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # Dijkstra from each focal crystal
    dist = [[float('inf')] * (n + 1) for _ in range(t)]
    for i in range(t):
        s = focal[i]
        dist[i][s] = 0
        pq = [(0, s)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[i][u]:
                continue
            for v, w in adj[u]:
                nd = d + w
                if nd < dist[i][v]:
                    dist[i][v] = nd
                    heapq.heappush(pq, (nd, v))
    
    # Steiner tree DP
    # dp[mask][v] = min cost to connect focal crystals in mask, ending at v
    INF = float('inf')
    dp = [[INF] * (n + 1) for _ in range(1 << t)]
    
    for i in range(t):
        for v in range(1, n + 1):
            dp[1 << i][v] = dist[i][v]
    
    for mask in range(1, 1 << t):
        # Skip single-bit masks (already initialized)
        if mask & (mask - 1) == 0:
            continue
        
        # Combine submasks
        sub = (mask - 1) & mask
        while sub > 0:
            other = mask ^ sub
            for v in range(1, n + 1):
                val = dp[sub][v] + dp[other][v]
                if val < dp[mask][v]:
                    dp[mask][v] = val
            sub = (sub - 1) & mask
        
        # Dijkstra to propagate
        pq = []
        for v in range(1, n + 1):
            if dp[mask][v] < INF:
                heapq.heappush(pq, (dp[mask][v], v))
        
        while pq:
            d, u = heapq.heappop(pq)
            if d > dp[mask][u]:
                continue
            for v, w in adj[u]:
                nd = d + w
                if nd < dp[mask][v]:
                    dp[mask][v] = nd
                    heapq.heappush(pq, (nd, v))
    
    full_mask = (1 << t) - 1
    result = min(dp[full_mask])
    print(int(result))

solve()