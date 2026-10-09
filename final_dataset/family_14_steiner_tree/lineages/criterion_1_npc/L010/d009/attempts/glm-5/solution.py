import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    critical = [int(next(it)) for _ in range(t)]
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        edges.append((u, v, w))
    
    if t <= 1:
        print(0)
        return
    
    # We need to connect all critical chambers into one component.
    # This is a Steiner tree problem on a small graph (n <= 100, t <= 10).
    # We'll use the Dreyfus-Wagner DP.
    
    INF = float('inf')
    
    # Build adjacency list with minimum edge weights
    adj = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        adj[i][i] = 0
    for u, v, w in edges:
        if w < adj[u][v]:
            adj[u][v] = w
            adj[v][u] = w
    
    # Floyd-Warshall to get all-pairs shortest paths
    dist = [row[:] for row in adj]
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            if dist[i][k] == INF:
                continue
            dik = dist[i][k]
            for j in range(1, n + 1):
                if dist[k][j] == INF:
                    continue
                nd = dik + dist[k][j]
                if nd < dist[i][j]:
                    dist[i][j] = nd
    
    # Map critical chambers to indices 0..t-1
    crit = critical
    tc = len(crit)
    
    # dp[mask][v] = min cost to connect subset (mask) of criticals, with tree rooted at v
    # We'll use a dictionary or 2D array
    full = (1 << tc) - 1
    dp = [[INF] * (n + 1) for _ in range(1 << tc)]
    
    # Base cases: single critical nodes
    for i in range(tc):
        mask = 1 << i
        v = crit[i]
        dp[mask][v] = 0
    
    # Dreyfus-Wagner
    for mask in range(1, 1 << tc):
        # For each v, compute dp[mask][v] by combining submasks
        # First, combine two submasks
        sub = (mask - 1) & mask
        while sub > 0:
            other = mask ^ sub
            if sub < other:
                # process pair (sub, other)
                for v in range(1, n + 1):
                    if dp[sub][v] == INF or dp[other][v] == INF:
                        continue
                    val = dp[sub][v] + dp[other][v]
                    if val < dp[mask][v]:
                        dp[mask][v] = val
            sub = (sub - 1) & mask
        
        # Then, relax dp[mask][v] over all v using shortest paths
        # dp[mask][u] = min over v of dp[mask][v] + dist[u][v]
        # We compute this by taking current dp[mask][v] values and relaxing
        best = [INF] * (n + 1)
        for v in range(1, n + 1):
            if dp[mask][v] < INF:
                best[v] = dp[mask][v]
        # Now relax using shortest paths: for each u, best[u] = min_v (dp[mask][v] + dist[v][u])
        # Since dist is all-pairs shortest, we can just do:
        for u in range(1, n + 1):
            mn = INF
            for v in range(1, n + 1):
                if dp[mask][v] == INF or dist[v][u] == INF:
                    continue
                val = dp[mask][v] + dist[v][u]
                if val < mn:
                    mn = val
            if mn < dp[mask][u]:
                dp[mask][u] = mn
    
    ans = min(dp[full][v] for v in range(1, n + 1))
    print(ans)

solve()