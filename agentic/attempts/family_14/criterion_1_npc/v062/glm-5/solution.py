import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    focal = [int(next(it)) for _ in range(t)]
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        edges.append((u, v, w))
    
    if t <= 1:
        print(0)
        return
    
    # Dijkstra between all pairs of focal nodes
    INF = float('inf')
    dist = [[INF] * (n + 1) for _ in range(n + 1)]
    adj = [[] for _ in range(n + 1)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    import heapq
    for s in focal:
        dist[s][s] = 0
        pq = [(0, s)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[s][u]:
                continue
            for v, w in adj[u]:
                nd = d + w
                if nd < dist[s][v]:
                    dist[s][v] = nd
                    heapq.heappush(pq, (nd, v))
    
    # Build complete graph on focal nodes
    K = t
    focal_edges = []
    for i in range(K):
        for j in range(i + 1, K):
            focal_edges.append((i, j, dist[focal[i]][focal[j]]))
    
    # DP over subsets (Steiner tree on terminals)
    dp = [[INF] * K for _ in range(1 << K)]
    for i in range(K):
        dp[1 << i][i] = 0
    
    for mask in range(1, 1 << K):
        for i in range(K):
            if not (mask & (1 << i)):
                continue
            sub = (mask - 1) & mask
            while sub > 0:
                comp = mask ^ sub
                if sub & (1 << i) and comp:
                    for j in range(K):
                        if comp & (1 << j):
                            val = dp[sub][i] + dp[comp][j] + focal_edges[min(i, j)][2] if i != j else dp[sub][i] + dp[comp][j]
                            if i == j:
                                val = dp[sub][i] + dp[comp][j]
                            if val < dp[mask][i]:
                                dp[mask][i] = val
                sub = (sub - 1) & mask
        # Relax using focal edges
        for i in range(K):
            if not (mask & (1 << i)):
                continue
            for j in range(K):
                if mask & (1 << j):
                    continue
                val = dp[mask][i] + focal_edges[min(i, j)][2]
                if val < dp[mask | (1 << j)][j]:
                    dp[mask | (1 << j)][j] = val
    
    full = (1 << K) - 1
    ans = min(dp[full][i] for i in range(K))
    print(ans)

solve()