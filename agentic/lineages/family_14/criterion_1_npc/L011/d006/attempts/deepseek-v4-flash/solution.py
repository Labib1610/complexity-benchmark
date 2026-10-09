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
    
    # Floyd-Warshall to get all-pairs shortest paths
    for k in range(n):
        for i in range(n):
            if dist[i][k] == INF:
                continue
            for j in range(n):
                if dist[k][j] == INF:
                    continue
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    # DP over subsets of terminals
    # dp[mask][v] = min cost to connect terminals in mask with v as root
    dp = [[INF] * n for _ in range(1 << t)]
    for i in range(t):
        dp[1 << i][terminals[i]] = 0
    
    for mask in range(1 << t):
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
        # Use Dijkstra-like relaxation
        visited = [False] * n
        heap = []
        for v in range(n):
            if dp[mask][v] < INF:
                heapq.heappush(heap, (dp[mask][v], v))
        while heap:
            d, u = heapq.heappop(heap)
            if visited[u]:
                continue
            visited[u] = True
            for v in range(n):
                if dist[u][v] < INF and d + dist[u][v] < dp[mask][v]:
                    dp[mask][v] = d + dist[u][v]
                    heapq.heappush(heap, (dp[mask][v], v))
    
    full_mask = (1 << t) - 1
    ans = min(dp[full_mask][v] for v in range(n))
    print(ans)

if __name__ == "__main__":
    solve()