import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    primaries = [int(next(it)) for _ in range(t)]
    
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
    
    # DP over subsets of primary crystals
    size = 1 << t
    dp = [INF] * size
    for i in range(t):
        dp[1 << i] = 0
    
    for mask in range(1, size):
        if dp[mask] == INF:
            continue
        # Try to add a single primary crystal j not in mask
        for j in range(t):
            if mask & (1 << j):
                continue
            new_mask = mask | (1 << j)
            # Find best Steiner point s connecting mask to j
            best = INF
            for s in range(1, n + 1):
                d1 = dp[mask]
                # distance from s to any primary in mask
                d2 = INF
                for i in range(t):
                    if mask & (1 << i):
                        d2 = min(d2, dist[s][primaries[i]])
                d3 = dist[s][primaries[j]]
                val = d1 + d2 + d3
                if val < best:
                    best = val
            if best < dp[new_mask]:
                dp[new_mask] = best
    
    print(dp[size - 1])

solve()