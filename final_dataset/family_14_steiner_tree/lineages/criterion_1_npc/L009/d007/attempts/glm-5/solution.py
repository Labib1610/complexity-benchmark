import sys

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    targets = []
    for _ in range(t):
        targets.append(int(input_data[idx]) - 1); idx += 1
    
    INF = float('inf')
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    
    edges = []
    for _ in range(m):
        u = int(input_data[idx]) - 1; idx += 1
        v = int(input_data[idx]) - 1; idx += 1
        w = int(input_data[idx]); idx += 1
        edges.append((u, v, w))
        if w < dist[u][v]:
            dist[u][v] = w
            dist[v][u] = w
    
    # Floyd-Warshall
    for k in range(n):
        dk = dist[k]
        for i in range(n):
            dik = dist[i][k]
            if dik == INF:
                continue
            di = dist[i]
            for j in range(n):
                nd = dik + dk[j]
                if nd < di[j]:
                    di[j] = nd
    
    if t <= 1:
        print(0)
        return
    
    # Dreyfus-Wagner Steiner tree DP
    # dp[mask][v] = min cost tree connecting terminals in mask, with v as an endpoint
    full = (1 << t) - 1
    dp = [[INF] * n for _ in range(1 << t)]
    
    for i in range(t):
        dp[1 << i][targets[i]] = 0
    
    for mask in range(1, 1 << t):
        if mask & (mask - 1) == 0:
            continue  # single bit, already initialized
        
        # For each vertex v, try splitting mask into submask and (mask ^ submask)
        for v in range(n):
            best = INF
            sub = (mask - 1) & mask
            while sub > 0:
                val = dp[sub][v] + dp[mask ^ sub][v]
                if val < best:
                    best = val
                sub = (sub - 1) & mask
            dp[mask][v] = best
        
        # Relax: dp[mask][v] = min over u of dp[mask][u] + dist[u][v]
        # Multi-source Dijkstra
        import heapq
        pq = []
        for v in range(n):
            if dp[mask][v] < INF:
                heapq.heappush(pq, (dp[mask][v], v))
        
        while pq:
            d, v = heapq.heappop(pq)
            if d > dp[mask][v]:
                continue
            for u in range(n):
                nd = d + dist[v][u]
                if nd < dp[mask][u]:
                    dp[mask][u] = nd
                    heapq.heappush(pq, (nd, u))
    
    ans = min(dp[full][v] for v in range(n))
    print(ans)

solve()