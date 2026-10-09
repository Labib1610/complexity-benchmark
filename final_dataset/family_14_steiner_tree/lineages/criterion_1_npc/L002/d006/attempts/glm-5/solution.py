import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    t = int(data[idx]); idx += 1
    
    essential = [int(data[idx + i]) for i in range(t)]
    idx += t
    
    if t <= 1:
        print(0)
        return
    
    edges = []
    for _ in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        w = int(data[idx]); idx += 1
        edges.append((u, v, w))
    
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
    
    K = t
    dp = [[INF] * (n + 1) for _ in range(1 << K)]
    
    for j in range(1, n + 1):
        dp[1 << 0][j] = dist[essential[0]][j]
    
    for mask in range(1, 1 << K):
        dpm = dp[mask]
        bits = [i for i in range(K) if (mask >> i) & 1]
        if len(bits) <= 1:
            continue
        half = (len(bits) + 1) // 2
        for s in range(1, (1 << len(bits)) - 1):
            if bin(s).count('1') != half:
                continue
            sub1 = 0
            for i in range(len(bits)):
                if (s >> i) & 1:
                    sub1 |= (1 << bits[i])
            sub2 = mask ^ sub1
            dp1 = dp[sub1]
            dp2 = dp[sub2]
            for j in range(1, n + 1):
                val = dp1[j]
                if val == INF:
                    continue
                for k in range(1, n + 1):
                    nd = val + dp2[k] + dist[j][k]
                    if nd < dpm[k]:
                        dpm[k] = nd
    
    ans = INF
    full = (1 << K) - 1
    for j in range(1, n + 1):
        if dp[full][j] < ans:
            ans = dp[full][j]
    
    print(ans)

solve()