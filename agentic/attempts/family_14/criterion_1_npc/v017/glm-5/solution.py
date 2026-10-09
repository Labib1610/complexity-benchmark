import sys

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    terminals = []
    for i in range(t):
        terminals.append(int(input_data[idx]) - 1); idx += 1
    
    INF = float('inf')
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    
    for i in range(m):
        u = int(input_data[idx]) - 1; idx += 1
        v = int(input_data[idx]) - 1; idx += 1
        w = int(input_data[idx]); idx += 1
        if w < dist[u][v]:
            dist[u][v] = w
            dist[v][u] = w
    
    # Floyd-Warshall
    for k in range(n):
        for i in range(n):
            if dist[i][k] < INF:
                for j in range(n):
                    if dist[k][j] < INF:
                        nd = dist[i][k] + dist[k][j]
                        if nd < dist[i][j]:
                            dist[i][j] = nd
    
    # Dreyfus-Wagner Steiner Tree DP
    # dp[mask][v] = min cost tree connecting terminals in mask, rooted at v
    full = (1 << t) - 1
    dp = [[INF] * n for _ in range(1 << t)]
    
    # Base case: single terminals
    for i in range(t):
        mask = 1 << i
        for v in range(n):
            dp[mask][v] = dist[terminals[i]][v]
    
    # Fill DP for all masks
    for mask in range(1, 1 << t):
        if mask & (mask - 1) == 0:
            continue  # single bit, already initialized
        
        # For each vertex v, try all partitions
        for v in range(n):
            best = dp[mask][v]
            # Iterate over proper non-empty subsets
            sub = (mask - 1) & mask
            while sub > 0:
                comp = mask ^ sub
                if sub < comp:
                    val = dp[sub][v] + dp[comp][v]
                    if val < best:
                        best = val
                sub = (sub - 1) & mask
            dp[mask][v] = best
        
        # Extend: relax using shortest paths
        # dp[mask][v] = min(dp[mask][v], dp[mask][u] + dist[u][v])
        # This is like running Dijkstra from all nodes simultaneously
        # But since we have all-pairs shortest paths, we can do:
        for v in range(n):
            for u in range(n):
                if dp[mask][u] < INF and dist[u][v] < INF:
                    val = dp[mask][u] + dist[u][v]
                    if val < dp[mask][v]:
                        dp[mask][v] = val
    
    print(dp[full][0] if t == 1 else min(dp[full]))

solve()