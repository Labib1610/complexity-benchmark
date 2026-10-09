import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    targets = [int(next(it)) for _ in range(t)]
    
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
            di = dist[i]
            dik = di[k]
            if dik == INF:
                continue
            for j in range(1, n + 1):
                nd = dik + dk[j]
                if nd < di[j]:
                    di[j] = nd
    
    if t == 1:
        print(0)
        return
    
    K = t
    cost = [[INF] * K for _ in range(K)]
    for i in range(K):
        for j in range(K):
            cost[i][j] = dist[targets[i]][targets[j]]
        cost[i][i] = 0
    
    full_mask = (1 << K) - 1
    dp = [[INF] * K for _ in range(1 << K)]
    for i in range(K):
        dp[1 << i][i] = 0
    
    for mask in range(1, 1 << K):
        for last in range(K):
            if not (mask & (1 << last)):
                continue
            cur = dp[mask][last]
            if cur == INF:
                continue
            for nxt in range(K):
                if mask & (1 << nxt):
                    continue
                new_mask = mask | (1 << nxt)
                new_cost = cur + cost[last][nxt]
                if new_cost < dp[new_mask][nxt]:
                    dp[new_mask][nxt] = new_cost
    
    ans = min(dp[full_mask][i] for i in range(K))
    print(ans)

solve()