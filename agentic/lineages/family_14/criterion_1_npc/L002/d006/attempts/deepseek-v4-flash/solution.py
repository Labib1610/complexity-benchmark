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
    
    essential = [int(next(it)) - 1 for _ in range(t)]
    essential_set = set(essential)
    
    # We'll build a graph with n nodes, edges are candidate covectors
    # We need to find minimum cost to connect all essential nodes
    # This is a Steiner tree problem, but since t <= 10, we can use DP over subsets.
    
    INF = 10**18
    # Floyd-Warshall for all-pairs shortest paths
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
    
    # If t == 1, answer is 0
    if t == 1:
        print(0)
        return
    
    # DP over subsets of essential nodes
    # dp[mask][i] = min cost to connect nodes in mask, ending at essential node i
    k = t
    dp = [[INF] * k for _ in range(1 << k)]
    
    for i in range(k):
        dp[1 << i][i] = 0
    
    for mask in range(1 << k):
        for i in range(k):
            if dp[mask][i] == INF:
                continue
            # Try to extend to another essential node
            for j in range(k):
                if not (mask & (1 << j)):
                    new_mask = mask | (1 << j)
                    cost = dist[essential[i]][essential[j]]
                    if cost < INF:
                        if dp[mask][i] + cost < dp[new_mask][j]:
                            dp[new_mask][j] = dp[mask][i] + cost
            # Also try to combine two subsets
            sub = (mask - 1) & mask
            while sub:
                other = mask ^ sub
                if sub < other:  # avoid double counting
                    for i in range(k):
                        if dp[sub][i] == INF:
                            continue
                        for j in range(k):
                            if dp[other][j] == INF:
                                continue
                            if dp[sub][i] + dp[other][j] < dp[mask][i]:
                                dp[mask][i] = dp[sub][i] + dp[other][j]
                sub = (sub - 1) & mask
    
    full_mask = (1 << k) - 1
    ans = min(dp[full_mask])
    print(ans)

if __name__ == "__main__":
    solve()