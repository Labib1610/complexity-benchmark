import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    t = int(data[idx]); idx += 1
    
    critical = [int(data[idx+i]) - 1 for i in range(t)]
    idx += t
    
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
    
    if t <= 1:
        print(0)
        return
    
    # DP over subsets of critical nodes
    size = 1 << t
    dp = [INF] * size
    for i in range(t):
        dp[1 << i] = 0
    
    for mask in range(1, size):
        if dp[mask] == INF:
            continue
        # Try splitting mask into two non-empty disjoint subsets
        sub = (mask - 1) & mask
        while sub > 0:
            other = mask ^ sub
            if sub < other:
                val = dp[sub] + dp[other]
                if val < dp[mask]:
                    dp[mask] = val
            sub = (sub - 1) & mask
        
        # Try extending: pick a critical node in mask and one outside, connect via shortest path
        for i in range(t):
            if not (mask & (1 << i)):
                continue
            for j in range(t):
                if mask & (1 << j):
                    continue
                new_mask = mask | (1 << j)
                val = dp[mask] + dist[critical[i]][critical[j]]
                if val < dp[new_mask]:
                    dp[new_mask] = val
    
    print(dp[size - 1])

solve()