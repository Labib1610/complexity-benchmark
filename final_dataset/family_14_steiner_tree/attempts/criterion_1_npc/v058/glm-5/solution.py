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
    
    terminals = [int(next(it)) - 1 for _ in range(t)]
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    if t <= 1:
        print(0)
        return
    
    # Dijkstra from each terminal
    dist = [[float('inf')] * n for _ in range(t)]
    for i in range(t):
        start = terminals[i]
        dist[i][start] = 0
        pq = [(0, start)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[i][u]:
                continue
            for v, w in adj[u]:
                nd = d + w
                if nd < dist[i][v]:
                    dist[i][v] = nd
                    heapq.heush(pq, (nd, v))
    
    # Steiner Tree DP on terminal set
    # dp[mask][v] = min cost to connect terminals in mask, with Steiner point at v
    K = t
    dp = [[float('inf')] * n for _ in range(1 << K)]
    for i in range(K):
        dp[1 << i][terminals[i]] = 0
    
    for mask in range(1, 1 << K):
        # Merge smaller subsets
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            for v in range(n):
                dp[mask][v] = min(dp[mask][v], dp[sub][v] + dp[other][v])
            sub = (sub - 1) & mask
        
        # Dijkstra-like relaxation for this mask
        pq = []
        for v in range(n):
            if dp[mask][v] < float('inf'):
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
    
    full_mask = (1 << K) - 1
    result = min(dp[full_mask])
    print(result)

solve()