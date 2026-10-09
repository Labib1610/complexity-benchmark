import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    priority = [int(next(it)) for _ in range(t)]
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        edges.append((u, v, w))
    
    if t <= 1:
        print(0)
        return
    
    # Build adjacency list
    adj = [[] for _ in range(n + 1)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # Dijkstra from each priority node
    import heapq
    dist = [[float('inf')] * (n + 1) for _ in range(t)]
    for i, src in enumerate(priority):
        dist[i][src] = 0
        pq = [(0, src)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[i][u]:
                continue
            for v, w in adj[u]:
                nd = d + w
                if nd < dist[i][v]:
                    dist[i][v] = nd
                    heapq.heappush(pq, (nd, v))
    
    # DP over subsets
    INF = float('inf')
    size = 1 << t
    dp = [[INF] * (n + 1) for _ in range(size)]
    for i in range(t):
        dp[1 << i][priority[i]] = 0
    
    for mask in range(1, size):
        # Combine submasks
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if sub < other:
                for v in range(1, n + 1):
                    if dp[sub][v] != INF and dp[other][v] != INF:
                        val = dp[sub][v] + dp[other][v]
                        if val < dp[mask][v]:
                            dp[mask][v] = val
            sub = (sub - 1) & mask
        # Relax using shortest paths between priority nodes
        for i in range(t):
            if not (mask & (1 << i)):
                continue
            prev = mask ^ (1 << i)
            if prev == 0:
                continue
            for v in range(1, n + 1):
                if dp[prev][v] != INF:
                    val = dp[prev][v] + dist[i][v]
                    if val < dp[mask][v]:
                        dp[mask][v] = val
    
    ans = min(dp[size - 1][v] for v in range(1, n + 1))
    print(ans)

solve()