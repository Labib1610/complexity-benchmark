import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    t = int(data[idx]); idx += 1
    deposits = []
    for _ in range(t):
        deposits.append(int(data[idx]) - 1)
        idx += 1
    INF = float('inf')
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for _ in range(m):
        u = int(data[idx]) - 1; idx += 1
        v = int(data[idx]) - 1; idx += 1
        w = int(data[idx]); idx += 1
        if w < dist[u][v]:
            dist[u][v] = w
            dist[v][u] = w
    for k in range(n):
        dk = dist[k]
        for i in range(n):
            di = dist[i]
            dik = di[k]
            if dik == INF:
                continue
            for j in range(n):
                nd = dik + dk[j]
                if nd < di[j]:
                    di[j] = nd
    if t == 1:
        print(0)
        return
    full = (1 << t) - 1
    dp = [INF] * (1 << t)
    for i in range(t):
        dp[1 << i] = 0
    for mask in range(1, 1 << t):
        if dp[mask] == INF:
            continue
        for i in range(t):
            if mask & (1 << i):
                continue
            for j in range(t):
                if mask & (1 << j):
                    nd = dp[mask] + dist[deposits[j]][deposits[i]]
                    nm = mask | (1 << i)
                    if nd < dp[nm]:
                        dp[nm] = nd
    print(dp[full])

solve()