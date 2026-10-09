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
    
    # DP over subsets of terminals
    full_mask = 1 << t
    dp = [[INF] * n for _ in range(full_mask)]
    
    for i in range(t):
        dp[1 << i][terminals[i]] = 0
    
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
                        nd = dp[mask][v] + dist[v][u]
                        if nd < dp[mask][u]:
                            dp[mask][u] = nd
    
    ans = min(dp[full_mask - 1][v] for v in range(n))
    print(ans)

if __name__ == "__main__":
    solve()