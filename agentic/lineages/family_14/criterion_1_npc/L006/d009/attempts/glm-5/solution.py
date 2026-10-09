import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    t = int(data[idx]); idx += 1
    
    critical = []
    for _ in range(t):
        critical.append(int(data[idx]) - 1)
        idx += 1
    
    INF = float('inf')
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    
    edges = []
    for _ in range(m):
        u = int(data[idx]) - 1; idx += 1
        v = int(data[idx]) - 1; idx += 1
        w = int(data[idx]); idx += 1
        edges.append((u, v, w))
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
    
    if t <= 1:
        print(0)
        return
    
    size = 1 << t
    dp = [INF] * size
    dp[0] = 0
    
    for mask in range(size):
        if dp[mask] == INF:
            continue
        for i in range(t):
            if not (mask & (1 << i)):
                for j in range(i + 1, t):
                    if not (mask & (1 << j)):
                        d = dist[critical[i]][critical[j]]
                        if d != INF:
                            new_mask = mask | (1 << i) | (1 << j)
                            nd = dp[mask] + d
                            if nd < dp[new_mask]:
                                dp[new_mask] = nd
    
    print(dp[size - 1])

solve()