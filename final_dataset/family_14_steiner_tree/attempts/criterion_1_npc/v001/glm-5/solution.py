import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    mandatory = [int(next(it)) - 1 for _ in range(t)]
    
    INF = 10**18
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        if w < dist[u][v]:
            dist[u][v] = w
            dist[v][u] = w
    
    # Floyd-Warshall
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
    
    # DP over subsets of mandatory facilities
    size = 1 << t
    dp = [INF] * size
    for i in range(t):
        dp[1 << i] = 0
    
    for mask in range(1, size):
        # iterate over submasks to split mask into two parts
        sub = (mask - 1) & mask
        while sub > 0:
            other = mask ^ sub
            if sub < other:  # avoid duplicate work
                val = dp[sub] + dp[other]
                if val < dp[mask]:
                    dp[mask] = val
            sub = (sub - 1) & mask
        
        # try to connect all mandatory facilities in mask via a Steiner-like center
        # pick the lowest-index mandatory facility in mask as base
        low = mask & (-mask)
        base = low.bit_length() - 1
        best = INF
        dbase = dist[mandatory[base]]
        for v in range(n):
            s = 0
            for i in range(t):
                if mask & (1 << i):
                    s += dist[mandatory[i]][v]
            if s < best:
                best = s
        if best < dp[mask]:
            dp[mask] = best
    
    print(dp[size - 1])

solve()