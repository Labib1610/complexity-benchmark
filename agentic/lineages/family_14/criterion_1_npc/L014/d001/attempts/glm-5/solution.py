import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    primaries = [int(next(it)) for _ in range(t)]
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        edges.append((u, v, w))
    
    if t <= 1:
        print(0)
        return
    
    # We need to connect all primary ledgers using any subset of edges.
    # This is equivalent to finding a minimum Steiner tree where terminals = primaries.
    # Since t <= 10, we can use the Dreyfus-Wagner DP over subsets of terminals.
    
    INF = float('inf')
    # dist[i][j] shortest path between i and j
    dist = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dist[i][i] = 0
    for u, v, w in edges:
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
    
    # dp[mask][v] = min cost of Steiner tree connecting terminals in mask, with v included in the tree
    full = (1 << t) - 1
    dp = [[INF] * (n + 1) for _ in range(1 << t)]
    for i, p in enumerate(primaries):
        dp[1 << i][p] = 0
    
    # Iterate over masks in increasing order of popcount
    for mask in range(1, 1 << t):
        # First, for each v, combine submasks
        # submask enumeration
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if sub < other:
                # process pair (sub, other) once
                dp_mask = dp[mask]
                dp_sub = dp[sub]
                dp_other = dp[other]
                for v in range(1, n + 1):
                    a = dp_sub[v]
                    if a == INF:
                        continue
                    b = dp_other[v]
                    if b == INF:
                        continue
                    s = a + b
                    if s < dp_mask[v]:
                        dp_mask[v] = s
            sub = (sub - 1) & mask
        
        # Then, relax using shortest paths: dp[mask][v] = min over u of dp[mask][u] + dist[u][v]
        # This is like a shortest path relaxation. We can do Dijkstra for each mask.
        # But since n is small (<=100), we can do a simple O(n^2) relaxation or repeated passes.
        # Let's do Dijkstra.
        import heapq
        d = dp[mask]
        heap = []
        for v in range(1, n + 1):
            if d[v] < INF:
                heapq.heappush(heap, (d[v], v))
        while heap:
            cost, u = heapq.heappop(heap)
            if cost > d[u]:
                continue
            du = d[u]
            dist_u = dist[u]
            for v in range(1, n + 1):
                w = dist_u[v]
                if w == INF:
                    continue
                nd = du + w
                if nd < d[v]:
                    d[v] = nd
                    heapq.heappush(heap, (nd, v))
    
    ans = min(dp[full][p] for p in primaries)
    print(ans)

solve()