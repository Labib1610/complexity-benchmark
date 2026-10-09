import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    delegated = [int(next(it)) for _ in range(t)]
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
            dik = dist[i][k]
            if dik == INF:
                continue
            di = dist[i]
            for j in range(1, n + 1):
                nd = dik + dk[j]
                if nd < di[j]:
                    di[j] = nd
    
    D = len(delegated)
    dp = [[INF] * D for _ in range(1 << D)]
    for i in range(D):
        dp[1 << i][i] = 0
    
    for mask in range(1 << D):
        for last in range(D):
            if not (mask & (1 << last)):
                continue
            cur = dp[mask][last]
            if cur == INF:
                continue
            for nxt in range(D):
                if mask & (1 << nxt):
                    continue
                cost = dist[delegated[last]][delegated[nxt]]
                if cost == INF:
                    continue
                nmask = mask | (1 << nxt)
                if cur + cost < dp[nmask][nxt]:
                    dp[nmask][nxt] = cur + cost
    
    full = (1 << D) - 1
    ans = min(dp[full][i] for i in range(D))
    print(ans)

solve()