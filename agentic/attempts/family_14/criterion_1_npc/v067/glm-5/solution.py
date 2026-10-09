import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    terminals = [int(next(it)) for _ in range(t)]
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        edges.append((u, v, w))
    
    if t <= 1:
        print(0)
        return
    
    INF = 10**18
    # dist[i][j] shortest path between i and j (1-indexed)
    dist = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dist[i][i] = 0
    for u, v, w in edges:
        if w < dist[u][v]:
            dist[u][v] = w
            dist[v][u] = w
    for k in range(1, n + 1):
        dk = dist[k]
        for i in range(1, n + 1):
            dik = dist[i][k]
            if dik == INF:
                continue
            di = dist[i]
            for j in range(1, n + 1):
                nd = dik + dk[j]
                if nd < di[j]:
                    di[j] = nd
    
    # Steiner tree DP over terminals
    K = t
    # map terminal index 0..K-1 to node id
    term = terminals
    # dp[mask][v] = min cost of tree connecting terminals in mask, rooted at v
    size = 1 << K
    dp = [[INF] * (n + 1) for _ in range(size)]
    for i in range(K):
        dp[1 << i][term[i]] = 0
    
    for mask in range(1, size):
        # subset merge
        sub = (mask - 1) & mask
        while sub > 0:
            comp = mask ^ sub
            if comp < sub:
                # process pair (sub, comp)
                for v in range(1, n + 1):
                    if dp[sub][v] < INF and dp[comp][v] < INF:
                        val = dp[sub][v] + dp[comp][v]
                        if val < dp[mask][v]:
                            dp[mask][v] = val
            sub = (sub - 1) & mask
        # relaxation via shortest paths
        # find min over u of dp[mask][u] + dist[u][v]
        best = INF
        for u in range(1, n + 1):
            if dp[mask][u] < INF:
                du = dist[u]
                for v in range(1, n + 1):
                    nd = dp[mask][u] + du[v]
                    if nd < dp[mask][v]:
                        dp[mask][v] = nd
    
    full = size - 1
    ans = min(dp[full][v] for v in range(1, n + 1))
    print(ans)

solve()