import sys

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    targets = list(map(int, input().split()))
    targets = [x-1 for x in targets]
    
    INF = 10**18
    dist = [[INF]*n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        edges.append((u, v, w))
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
    full_mask = 1 << t
    dp = [[INF]*n for _ in range(full_mask)]
    
    for i in range(t):
        dp[1 << i][targets[i]] = 0
    
    for mask in range(full_mask):
        # combine subsets
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if sub < other:  # avoid double work
                for v in range(n):
                    if dp[sub][v] < INF and dp[other][v] < INF:
                        dp[mask][v] = min(dp[mask][v], dp[sub][v] + dp[other][v])
            sub = (sub - 1) & mask
        
        # relax via shortest paths
        for v in range(n):
            if dp[mask][v] < INF:
                for u in range(n):
                    if dist[v][u] < INF:
                        if dp[mask][v] + dist[v][u] < dp[mask][u]:
                            dp[mask][u] = dp[mask][v] + dist[v][u]
    
    ans = min(dp[full_mask-1][v] for v in range(n))
    print(ans)

if __name__ == "__main__":
    solve()