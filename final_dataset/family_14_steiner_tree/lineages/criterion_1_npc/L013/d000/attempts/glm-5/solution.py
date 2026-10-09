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
    # DP over subsets of critical nodes
    size = 1 << t
    dp = [[INF] * n for _ in range(size)]
    for i in range(t):
        node = critical[i]
        for v in range(n):
            dp[1 << i][v] = dist[node][v]
    for mask in range(1, size):
        if (mask & (mask - 1)) == 0:
            continue
        for v in range(n):
            best = INF
            sub = (mask - 1) & mask
            while sub > 0:
                comp = mask ^ sub
                val = dp[sub][v] + dp[comp][v]
                if val < best:
                    best = val
                sub = (sub - 1) & mask
            dp[mask][v] = best
    full = size - 1
    ans = min(dp[full][v] for v in range(n))
    print(ans)

solve()