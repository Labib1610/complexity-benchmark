import sys

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    terminals = list(map(int, input().split()))
    terminals = [x-1 for x in terminals]
    
    INF = 10**18
    dist = [[INF]*n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        if w < dist[u][v]:
            dist[u][v] = w
            dist[v][u] = w
    
    # Floyd-Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    if t == 1:
        print(0)
        return
    
    full_mask = (1 << t) - 1
    dp = [[INF]*n for _ in range(1 << t)]
    
    # Initialize: each terminal alone
    for i, term in enumerate(terminals):
        dp[1 << i][term] = 0
    
    # DP over masks
    for mask in range(1 << t):
        # Combine submasks
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if sub < other:  # avoid double work
                for v in range(n):
                    if dp[sub][v] < INF and dp[other][v] < INF:
                        dp[mask][v] = min(dp[mask][v], dp[sub][v] + dp[other][v])
            sub = (sub - 1) & mask
        
        # Relax via shortest paths
        for v in range(n):
            if dp[mask][v] < INF:
                for u in range(n):
                    if dist[v][u] < INF:
                        if dp[mask][v] + dist[v][u] < dp[mask][u]:
                            dp[mask][u] = dp[mask][v] + dist[v][u]
    
    ans = min(dp[full_mask][v] for v in range(n))
    print(ans)

if __name__ == "__main__":
    solve()