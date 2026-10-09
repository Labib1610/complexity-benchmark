import heapq
import sys

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    terminals = []
    for _ in range(t):
        terminals.append(int(input_data[idx]) - 1)
        idx += 1
    
    INF = float('inf')
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    
    for _ in range(m):
        u = int(input_data[idx]) - 1; idx += 1
        v = int(input_data[idx]) - 1; idx += 1
        w = int(input_data[idx]); idx += 1
        if w < dist[u][v]:
            dist[u][v] = w
            dist[v][u] = w
    
    for k in range(n):
        for i in range(n):
            if dist[i][k] < INF:
                for j in range(n):
                    if dist[k][j] < INF:
                        nd = dist[i][k] + dist[k][j]
                        if nd < dist[i][j]:
                            dist[i][j] = nd
    
    if t <= 1:
        print(0)
        return
    
    T = 1 << t
    dp = [[INF] * n for _ in range(T)]
    
    for i in range(t):
        dp[1 << i][terminals[i]] = 0
    
    for mask in range(1, T):
        sub = (mask - 1) & mask
        while sub > 0:
            comp = mask ^ sub
            for v in range(n):
                if dp[sub][v] < INF and dp[comp][v] < INF:
                    val = dp[sub][v] + dp[comp][v]
                    if val < dp[mask][v]:
                        dp[mask][v] = val
            sub = (sub - 1) & mask
        
        # Dijkstra relaxation
        pq = []
        for v in range(n):
            if dp[mask][v] < INF:
                heapq.heappush(pq, (dp[mask][v], v))
        
        while pq:
            d, v = heapq.heappop(pq)
            if d > dp[mask][v]:
                continue
            for u in range(n):
                if dist[v][u] < INF:
                    nd = d + dist[v][u]
                    if nd < dp[mask][u]:
                        dp[mask][u] = nd
                        heapq.heappush(pq, (nd, u))
    
    full = T - 1
    ans = min(dp[full][v] for v in range(n))
    print(ans)

solve()