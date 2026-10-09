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
    
    priority = [int(next(it)) for _ in range(t)]
    priority_set = set(priority)
    
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
    
    # Dijkstra from each priority node
    dist = [[float('inf')] * (n + 1) for _ in range(t)]
    for i in range(t):
        start = priority[i]
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
                    heapq.heappush(pq, (nd, v))
    
    # Steiner tree DP
    INF = float('inf')
    dp = [[INF] * (n + 1) for _ in range(1 << t)]
    
    for i in range(t):
        for v in range(1, n + 1):
            dp[1 << i][v] = dist[i][v]
    
    for mask in range(1, 1 << t):
        if mask & (mask - 1) == 0:
            continue
        # Combine submasks
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            for v in range(1, n + 1):
                dp[mask][v] = min(dp[mask][v], dp[sub][v] + dp[other][v])
            sub = (sub - 1) & mask
        
        # Dijkstra-like relaxation
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
    print(min(dp[full_mask][1:]))

if __name__ == "__main__":
    solve()