import sys
import heapq

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    
    primaries = [int(next(it)) - 1 for _ in range(t)]
    
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
    
    # Floyd-Warshall for all-pairs shortest paths
    for k in range(n):
        for i in range(n):
            if dist[i][k] == INF:
                continue
            for j in range(n):
                if dist[k][j] == INF:
                    continue
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    # DP over subsets of primary nodes
    full_mask = 1 << t
    dp = [[INF] * n for _ in range(full_mask)]
    
    # Initialize: single primary node
    for i, p in enumerate(primaries):
        dp[1 << i][p] = 0
    
    # For each mask, try to combine two submasks
    for mask in range(1, full_mask):
        # Combine submasks
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if sub < other:  # avoid double work
                for v in range(n):
                    if dp[sub][v] + dp[other][v] < dp[mask][v]:
                        dp[mask][v] = dp[sub][v] + dp[other][v]
            sub = (sub - 1) & mask
        
        # Relax via shortest paths
        # Dijkstra-like relaxation using distances
        for v in range(n):
            if dp[mask][v] == INF:
                continue
            for u in range(n):
                if dist[v][u] < INF:
                    nd = dp[mask][v] + dist[v][u]
                    if nd < dp[mask][u]:
                        dp[mask][u] = nd
    
    ans = min(dp[full_mask - 1][v] for v in range(n))
    print(ans)

if __name__ == "__main__":
    solve()