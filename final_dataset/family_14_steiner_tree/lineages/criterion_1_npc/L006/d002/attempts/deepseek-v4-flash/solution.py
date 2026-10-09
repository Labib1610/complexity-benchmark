import sys
import heapq

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    primary = list(map(int, input().split()))
    primary = [p-1 for p in primary]
    
    INF = 10**18
    dist = [[INF]*n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # Dijkstra from each node to get all-pairs shortest paths
    for s in range(n):
        d = [INF]*n
        d[s] = 0
        pq = [(0, s)]
        while pq:
            du, u = heapq.heappop(pq)
            if du != d[u]:
                continue
            for v, w in adj[u]:
                nd = du + w
                if nd < d[v]:
                    d[v] = nd
                    heapq.heappush(pq, (nd, v))
        dist[s] = d
    
    # DP over subsets of primary nodes
    # dp[mask][i] = min cost to connect primary nodes in mask, ending at node i
    size = 1 << t
    dp = [[INF]*n for _ in range(size)]
    
    for i in range(t):
        dp[1 << i][primary[i]] = 0
    
    for mask in range(size):
        # Combine two subsets
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if sub < other:  # avoid duplicate work
                for i in range(n):
                    if dp[sub][i] < INF and dp[other][i] < INF:
                        dp[mask][i] = min(dp[mask][i], dp[sub][i] + dp[other][i])
            sub = (sub - 1) & mask
        
        # Relax via shortest paths
        for i in range(n):
            if dp[mask][i] < INF:
                for j in range(n):
                    if dist[i][j] < INF:
                        nd = dp[mask][i] + dist[i][j]
                        if nd < dp[mask][j]:
                            dp[mask][j] = nd
    
    full_mask = size - 1
    ans = min(dp[full_mask][i] for i in range(n))
    print(ans)

if __name__ == "__main__":
    solve()