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
        for i in range(n):
            if dist[i][k] == INF:
                continue
            for j in range(n):
                if dist[k][j] == INF:
                    continue
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    # DP over subsets
    full_mask = (1 << t) - 1
    dp = [[INF] * n for _ in range(1 << t)]
    
    for i, term in enumerate(terminals):
        dp[1 << i][term] = 0
    
    for mask in range(1 << t):
        # Combine subsets
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if sub < other:  # avoid double work
                for v in range(n):
                    if dp[sub][v] == INF or dp[other][v] == INF:
                        continue
                    val = dp[sub][v] + dp[other][v]
                    if val < dp[mask][v]:
                        dp[mask][v] = val
            sub = (sub - 1) & mask
        
        # Relax via shortest paths
        for v in range(n):
            if dp[mask][v] == INF:
                continue
            for u in range(n):
                if dist[v][u] == INF:
                    continue
                if dp[mask][v] + dist[v][u] < dp[mask][u]:
                    dp[mask][u] = dp[mask][v] + dist[v][u]
    
    ans = min(dp[full_mask])
    print(ans)

if __name__ == "__main__":
    solve()