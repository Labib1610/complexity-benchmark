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
    
    delegated = [int(next(it)) for _ in range(t)]
    
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
    
    # Dijkstra from each delegated language
    dist = [[float('inf')] * (n + 1) for _ in range(t)]
    for i, src in enumerate(delegated):
        d = dist[i]
        d[src] = 0
        pq = [(0, src)]
        while pq:
            cur_d, u = heapq.heappop(pq)
            if cur_d > d[u]:
                continue
            for v, w in adj[u]:
                nd = cur_d + w
                if nd < d[v]:
                    d[v] = nd
                    heapq.heappush(pq, (nd, v))
    
    # Steiner Tree DP: dp[mask][v] = min cost to connect languages in mask, ending at v
    INF = float('inf')
    dp = [[INF] * (n + 1) for _ in range(1 << t)]
    
    for i in range(t):
        for v in range(1, n + 1):
            dp[1 << i][v] = dist[i][v]
    
    for mask in range(1, 1 << t):
        # Skip single-bit masks already initialized
        if mask & (mask - 1) == 0:
            continue
        
        # Combine smaller masks
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            for v in range(1, n + 1):
                val = dp[sub][v] + dp[other][v]
                if val < dp[mask][v]:
                    dp[mask][v] = val
            sub = (sub - 1) & mask
        
        # Propagate: dp[mask][v] = min over u of (dp[mask][u] + dist[u][v])
        # Use Dijkstra-like approach
        pq = []
        for v in range(1, n + 1):
            if dp[mask][v] < INF:
                heapq.heappush(pq, (dp[mask][v], v))
        
        while pq:
            cur_d, u = heapq.heappop(pq)
            if cur_d > dp[mask][u]:
                continue
            for v, w in adj[u]:
                nd = cur_d + w
                if nd < dp[mask][v]:
                    dp[mask][v] = nd
                    heapq.heappush(pq, (nd, v))
    
    full_mask = (1 << t) - 1
    print(min(dp[full_mask]))

if __name__ == "__main__":
    solve()