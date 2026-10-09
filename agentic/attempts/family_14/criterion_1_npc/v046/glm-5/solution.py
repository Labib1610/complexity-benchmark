import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    regulated = [int(next(it)) for _ in range(t)]
    
    INF = 10**18
    dist = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dist[i][i] = 0
    
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        if w < dist[u][v]:
            dist[u][v] = w
            dist[v][u] = w
    
    for k in range(1, n + 1):
        dk = dist[k]
        for i in range(1, n + 1):
            di = dist[i]
            dik = di[k]
            if dik == INF:
                continue
            for j in range(1, n + 1):
                nd = dik + dk[j]
                if nd < di[j]:
                    di[j] = nd
    
    if t <= 1:
        print(0)
        return
    
    full = (1 << t) - 1
    dp = [INF] * (1 << t)
    for i in range(t):
        dp[1 << i] = 0
    
    for mask in range(1 << t):
        if dp[mask] == INF:
            continue
        for i in range(t):
            if not (mask & (1 << i)):
                continue
            for j in range(t):
                if mask & (1 << j):
                    continue
                new_mask = mask | (1 << j)
                cost = dp[mask] + dist[regulated[i]][regulated[j]]
                if cost < dp[new_mask]:
                    dp[new_mask] = cost
    
    print(dp[full])

solve()