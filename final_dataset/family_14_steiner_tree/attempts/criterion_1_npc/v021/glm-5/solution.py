import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    keys = [int(next(it)) for _ in range(t)]
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        edges.append((u, v, w))
    
    if t <= 1:
        print(0)
        return
    
    INF = float('inf')
    dist = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dist[i][i] = 0
    for u, v, w in edges:
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
    
    K = len(keys)
    dp = [[INF] * K for _ in range(1 << K)]
    for i in range(K):
        dp[1 << i][i] = 0
    
    for mask in range(1 << K):
        for i in range(K):
            if not (mask & (1 << i)):
                continue
            if dp[mask][i] == INF:
                continue
            for j in range(K):
                if mask & (1 << j):
                    continue
                cost = dist[keys[i]][keys[j]]
                if cost == INF:
                    continue
                nm = mask | (1 << j)
                if dp[mask][i] + cost < dp[nm][j]:
                    dp[nm][j] = dp[mask][i] + cost
    
    full = (1 << K) - 1
    ans = min(dp[full][i] for i in range(K))
    print(ans)

solve()