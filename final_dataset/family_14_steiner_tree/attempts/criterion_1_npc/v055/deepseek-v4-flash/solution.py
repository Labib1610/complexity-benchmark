import sys
import heapq

input = sys.stdin.readline

def solve():
    n, m, t = map(int, input().split())
    terminals = list(map(int, input().split()))
    terminals = [x - 1 for x in terminals]
    
    INF = 10**18
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append((v, w))
        adj[v].append((u, w))
        if w < dist[u][v]:
            dist[u][v] = w
            dist[v][u] = w
    
    # Floyd-Warshall for all-pairs shortest paths
    for k in range(n):
        for i in range(n):
            if dist[i][k] == INF:
                continue
            for j in range(n):
                if dist[k][j] == INF:
                    continue
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    # DP over subsets of terminals
    # dp[mask][v] = min cost to connect terminals in mask, ending at v
    full_mask = 1 << t
    dp = [[INF] * n for _ in range(full_mask)]
    
    for i in range(t):
        dp[1 << i][terminals[i]] = 0
    
    for mask in range(full_mask):
        # Combine two submasks
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if sub < other:  # avoid double work
                for v in range(n):
                    if dp[sub][v] + dp[other][v] < dp[mask][v]:
                        dp[mask][v] = dp[sub][v] + dp[other][v]
            sub = (sub - 1) & mask
        
        # Relax via shortest paths
        for v in range(n):
            if dp[mask][v] < INF:
                for u in range(n):
                    if dist[v][u] < INF:
                        if dp[mask][u] > dp[mask][v] + dist[v][u]:
                            dp[mask][u] = dp[mask][v] + dist[v][u]
    
    ans = min(dp[full_mask - 1][v] for v in range(n))
    print(ans)

if __name__ == "__main__":
    solve()