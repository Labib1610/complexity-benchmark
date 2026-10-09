import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    terminals = [int(next(it)) - 1 for _ in range(t)]
    
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
            dik = dist[i][k]
            if dik == INF:
                continue
            di = dist[i]
            for j in range(n):
                nd = dik + dk[j]
                if nd < di[j]:
                    di[j] = nd
    
    k = t
    full_mask = (1 << k) - 1
    dp = [[INF] * n for _ in range(1 << k)]
    
    for i, term in enumerate(terminals):
        dp[1 << i][term] = 0
    
    for mask in range(1, 1 << k):
        # Combine submasks
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if sub < other:  # avoid duplicate work
                for v in range(n):
                    best = INF
                    for u in range(n):
                        val = dp[sub][u] + dp[other][u] + dist[u][v]
                        if val < best:
                            best = val
                    if best < dp[mask][v]:
                        dp[mask][v] = best
            sub = (sub - 1) & mask
        
        # Relax via shortest paths
        for v in range(n):
            dv = dp[mask][v]
            if dv == INF:
                continue
            for u in range(n):
                nd = dv + dist[v][u]
                if nd < dp[mask][u]:
                    dp[mask][u] = nd
    
    ans = min(dp[full_mask])
    print(ans)

if __name__ == "__main__":
    solve()