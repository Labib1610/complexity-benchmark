import sys
import heapq

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    S = []
    for _ in range(t):
        S.append(int(input_data[idx]) - 1); idx += 1
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(input_data[idx]) - 1; idx += 1
        v = int(input_data[idx]) - 1; idx += 1
        w = int(input_data[idx]); idx += 1
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    if t <= 1:
        print(0)
        return
    
    INF = float('inf')
    size = 1 << t
    dp = [[INF] * n for _ in range(size)]
    
    for i in range(t):
        dp[1 << i][S[i]] = 0
    
    for mask in range(1, size):
        for v in range(n):
            sub = (mask - 1) & mask
            while sub > 0:
                other = mask ^ sub
                if dp[sub][v] + dp[other][v] < dp[mask][v]:
                    dp[mask][v] = dp[sub][v] + dp[other][v]
                sub = (sub - 1) & mask
        
        # Dijkstra relaxation
        dist = [INF] * n
        for v in range(n):
            if dp[mask][v] < dist[v]:
                dist[v] = dp[mask][v]
        
        pq = []
        for v in range(n):
            if dist[v] < INF:
                heapq.heappush(pq, (dist[v], v))
        
        while pq:
            d, v = heapq.heappop(pq)
            if d > dist[v]:
                continue
            for u, w in adj[v]:
                nd = d + w
                if nd < dist[u]:
                    dist[u] = nd
                    heapq.heappush(pq, (nd, u))
        
        for v in range(n):
            dp[mask][v] = dist[v]
    
    print(dp[size - 1][S[0]])

solve()