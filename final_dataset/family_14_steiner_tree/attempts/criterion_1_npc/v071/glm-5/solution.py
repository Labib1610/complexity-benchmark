import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    core = [int(next(it)) for _ in range(t)]
    INF = float('inf')
    dist = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
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
            dik = dist[i][k]
            if dik == INF:
                continue
            di = dist[i]
            for j in range(1, n + 1):
                nd = dik + dk[j]
                if nd < di[j]:
                    di[j] = nd
    if t <= 1:
        print(0)
        return
    dp = [[INF] * t for _ in range(1 << t)]
    for i in range(t):
        dp[1 << i][i] = 0
    for mask in range(1 << t):
        for i in range(t):
            if not (mask & (1 << i)):
                continue
            cur = dp[mask][i]
            if cur == INF:
                continue
            for j in range(t):
                if mask & (1 << j):
                    continue
                nd = cur + dist[core[i]][core[j]]
                nm = mask | (1 << j)
                if nd < dp[nm][j]:
                    dp[nm][j] = nd
    full = (1 << t) - 1
    print(min(dp[full]))

solve()