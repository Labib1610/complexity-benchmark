import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    required = [int(next(it)) - 1 for _ in range(t)]
    
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
        for i in range(n):
            if dist[i][k] == INF:
                continue
            for j in range(n):
                if dist[k][j] == INF:
                    continue
                nd = dist[i][k] + dist[k][j]
                if nd < dist[i][j]:
                    dist[i][j] = nd
    
    full_mask = (1 << t) - 1
    dp = [[INF] * n for _ in range(1 << t)]
    
    # Initialize: each required site alone
    for i, node in enumerate(required):
        dp[1 << i][node] = 0
    
    # DP over masks
    for mask in range(1 << t):
        # Combine submasks
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if sub < other:  # avoid double work
                for v in range(n):
                    if dp[sub][v] == INF:
                        continue
                    for u in range(n):
                        if dp[other][u] == INF:
                            continue
                        nd = dp[sub][v] + dp[other][u] + dist[v][u]
                        if nd < dp[mask][v]:
                            dp[mask][v] = nd
                        if nd < dp[mask][u]:
                            dp[mask][u] = nd
            sub = (sub - 1) & mask
        
        # Relax via shortest paths
        for v in range(n):
            if dp[mask][v] == INF:
                continue
            for u in range(n):
                nd = dp[mask][v] + dist[v][u]
                if nd < dp[mask][u]:
                    dp[mask][u] = nd
    
    ans = min(dp[full_mask])
    print(ans)

if __name__ == "__main__":
    solve()