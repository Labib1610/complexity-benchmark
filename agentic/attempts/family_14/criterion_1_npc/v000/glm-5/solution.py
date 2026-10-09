import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    t = int(data[idx]); idx += 1
    
    required = []
    for _ in range(t):
        required.append(int(data[idx]) - 1)
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
    
    T = len(required)
    dp = [[INF] * T for _ in range(1 << T)]
    for i in range(T):
        dp[1 << i][i] = 0
    
    for mask in range(1 << T):
        for i in range(T):
            if not (mask & (1 << i)):
                continue
            if dp[mask][i] == INF:
                continue
            for j in range(T):
                if mask & (1 << j):
                    continue
                new_mask = mask | (1 << j)
                cost = dp[mask][i] + dist[required[i]][required[j]]
                if cost < dp[new_mask][j]:
                    dp[new_mask][j] = cost
    
    full = (1 << T) - 1
    ans = min(dp[full])
    print(ans)

solve()