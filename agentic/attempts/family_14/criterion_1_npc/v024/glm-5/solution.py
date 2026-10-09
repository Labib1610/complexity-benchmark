import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    cameras = [int(next(it)) for _ in range(t)]
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        edges.append((u, v, w))
    
    if t <= 1:
        print(0)
        return
    
    INF = 10**18
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
    
    k = t
    dp = [[INF] * k for _ in range(1 << k)]
    for i in range(k):
        dp[1 << i][i] = 0
    
    for mask in range(1 << k):
        for last in range(k):
            if not (mask & (1 << last)):
                continue
            cur = dp[mask][last]
            if cur == INF:
                continue
            for nxt in range(k):
                if mask & (1 << nxt):
                    continue
                d = dist[cameras[last]][cameras[nxt]]
                if d == INF:
                    continue
                nm = mask | (1 << nxt)
                if cur + d < dp[nm][nxt]:
                    dp[nm][nxt] = cur + d
    
    full = (1 << k) - 1
    ans = min(dp[full])
    print(ans)

solve()