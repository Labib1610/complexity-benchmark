import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    required = [int(next(it)) for _ in range(t)]
    
    INF = float('inf')
    dist = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dist[i][i] = 0
    
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        if w < dist[u][v]:
            dist[u][v] = w
            dist[v][u] = w
    
    # Floyd-Warshall
    for k in range(1, n + 1):
        dk = dist[k]
        for i in range(1, n + 1):
            di = dist[i]
            dik = di[k]
            if dik == INF:
                continue
            for j in range(1, n + 1):
                nd = dik + dk[j]
                if nd < di[j]:
                    di[j] = nd
    
    if t <= 1:
        print(0)
        return
    
    # Dreyfus-Wagner: Steiner tree on required terminals
    # dp[mask][v] = min cost of subtree connecting terminals in mask, rooted at v
    K = t
    # Map terminal index to actual node
    terminals = required
    
    # dp[mask][v]
    dp = [[INF] * (n + 1) for _ in range(1 << K)]
    
    for i in range(K):
        mask = 1 << i
        v = terminals[i]
        for j in range(1, n + 1):
            dp[mask][j] = dist[v][j]
    
    for mask in range(1, 1 << K):
        if mask & (mask - 1) == 0:
            continue  # single bit, already initialized
        
        # Combine submasks
        sub = (mask - 1) & mask
        while sub > 0:
            comp = mask ^ sub
            if sub < comp:
                a, b = sub, comp
            else:
                a, b = comp, sub
            
            for v in range(1, n + 1):
                val = dp[a][v] + dp[b][v]
                if val < dp[mask][v]:
                    dp[mask][v] = val
            
            sub = (sub - 1) & mask
        
        # Optimize: for each v, dp[mask][v] = min over u of (dp[mask][u] + dist[u][v])
        # This is like running a shortest path / relaxation
        # We can do: for each u, for each v, relax
        # But that's O(n^2) per mask, which is fine for n=100, masks up to 1024
        for u in range(1, n + 1):
            du = dp[mask][u]
            if du == INF:
                continue
            du_row = dist[u]
            for v in range(1, n + 1):
                nd = du + du_row[v]
                if nd < dp[mask][v]:
                    dp[mask][v] = nd
    
    full = (1 << K) - 1
    ans = min(dp[full][v] for v in range(1, n + 1))
    print(ans)

solve()