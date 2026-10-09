import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    t = int(data[idx]); idx += 1
    primary = [int(data[idx+i]) for i in range(t)]
    idx += t
    edges = []
    for _ in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        w = int(data[idx]); idx += 1
        edges.append((u, v, w))
    
    if t <= 1:
        print(0)
        return
    
    INF = float('inf')
    dist = [[INF] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        dist[i][i] = 0
    for u, v, w in edges:
        if w < dist[u][v]:
            dist[u][v] = w
            dist[v][u] = w
    for k in range(1, n+1):
        dk = dist[k]
        for i in range(1, n+1):
            dik = dist[i][k]
            if dik == INF:
                continue
            di = dist[i]
            for j in range(1, n+1):
                nd = dik + dk[j]
                if nd < di[j]:
                    di[j] = nd
    
    # Steiner tree DP on primary terminals
    K = t
    size = 1 << K
    dp = [[INF] * (n+1) for _ in range(size)]
    for i in range(K):
        node = primary[i]
        dp[1 << i][node] = 0
    
    for mask in range(1, size):
        best = INF
        for v in range(1, n+1):
            cur = dp[mask][v]
            if cur == INF:
                continue
            sub = (mask - 1) & mask
            while sub > 0:
                alt = cur + dp[sub][v]
                if alt < dp[mask][v]:
                    dp[mask][v] = alt
                sub = (sub - 1) & mask
            if dp[mask][v] < best:
                best = dp[mask][v]
        for u in range(1, n+1):
            if best < INF:
                for v in range(1, n+1):
                    nd = best + dist[u][v]
                    if nd < dp[mask][v]:
                        dp[mask][v] = nd
    
    full = size - 1
    ans = min(dp[full][v] for v in range(1, n+1))
    print(ans)

solve()