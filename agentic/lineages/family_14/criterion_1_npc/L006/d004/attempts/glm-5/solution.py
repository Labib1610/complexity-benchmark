import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    targets = [int(next(it)) for _ in range(t)]
    target_set = set(targets)
    
    # Build graph
    adj = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    # If t <= 1, no pairwise differences needed
    if t <= 1:
        print(0)
        return
    
    # Dijkstra from each target
    INF = float('inf')
    dist = [[INF] * (n + 1) for _ in range(t)]
    import heapq
    for i, s in enumerate(targets):
        dist[i][s] = 0
        pq = [(0, s)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[i][u]:
                continue
            for v, w in adj[u]:
                nd = d + w
                if nd < dist[i][v]:
                    dist[i][v] = nd
                    heapq.heappush(pq, (nd, v))
    
    # For each edge, compute cost to connect targets across it
    # An edge (u,v,w) can connect target i and target j if dist[i][u] + w + dist[j][v] is finite
    # or dist[i][v] + w + dist[j][u] is finite
    # The cost of this connection is dist[i][u] + w + dist[j][v] (or the other way)
    
    # Build complete graph on t targets
    # For each pair (i,j), find minimum over all edges of min(dist[i][u]+w+dist[j][v], dist[i][v]+w+dist[j][u])
    
    # Also consider direct paths that don't use any edge as "bridge" - but those are captured
    # because if target i and j are in same component, there's a path, and the shortest path
    # uses some edge as the "highest" edge in some sense... Actually let's think differently.
    
    # The key insight: we need to select a set of edges forming a Steiner tree connecting all targets.
    # The minimum Steiner tree in a graph where we can use any edges.
    # 
    # For small t (<= 10), we can use the Dreyfus-Wagner DP.
    # State: dp[S][v] = minimum cost of a tree connecting the subset S of targets, rooted at vertex v
    # 
    # But n can be 100, t can be 10, so 2^10 * 100 = 102400 states, and transitions are O(2^|S| * n) per state
    # which might be too much... Let's think about the complexity.
    # 
    # Dreyfus-Wagner:
    # dp[S][v] = min over partitions S = S1 U S2 of dp[S1][v] + dp[S2][v]
    # dp[S][v] = min over u of dp[S][u] + dist(u, v)  -- this is handled by shortest path
    # 
    # The standard approach:
    # 1. For each target, compute shortest paths to all vertices.
    # 2. dp[S][v] for |S| = 1: dp[{i}][v] = dist[i][v]
    # 3. For |S| >= 2: dp[S][v] = min over non-empty proper subsets S1 of S: dp[S1][v] + dp[S\S1][v]
    # 4. Then "relax" dp[S][v] by considering dp[S][u] + dist(u,v) for all u -- this is like
    #    running a shortest path / Dijkstra to propagate.
    # 
    # Actually the standard Dreyfus-Wagner does:
    # - For each subset S and vertex v, compute dp[S][v]
    # - For |S|=1: dp[{i}][v] = shortest distance from target i to v
    # - For |S|>=2: first compute dp[S][v] = min over partitions, then run Dijkstra to relax
    # 
    # Let me implement this properly.
    
    # Map target index to 0..t-1
    # dp[S][v] where S is a bitmask
    
    # Initialize
    dp = [[INF] * (n + 1) for _ in range(1 << t)]
    
    # Base case: single targets
    for i in range(t):
        for v in range(1, n + 1):
            dp[1 << i][v] = dist[i][v]
    
    # For each subset S
    for S in range(1, 1 << t):
        if bin(S).count('1') < 2:
            continue
        
        # Compute dp[S][v] = min over partitions S1 | S2 = S, S1 & S2 = 0, S1 != 0, S1 != S
        # of dp[S1][v] + dp[S2][v]
        # To avoid redundant computation, iterate S1 as submasks of S with S1 < S (to avoid double counting)
        sub = (S - 1) & S
        while sub > 0:
            if sub < (S ^ sub):  # only consider one ordering to avoid double work
                for v in range(1, n + 1):
                    if dp[sub][v] < INF and dp[S ^ sub][v] < INF:
                        val = dp[sub][v] + dp[S ^ sub][v]
                        if val < dp[S][v]:
                            dp[S][v] = val
            sub = (sub - 1) & S
        
        # Now run Dijkstra to relax dp[S][v] using dp[S][u] + dist(u, v)
        # This is equivalent to: dp[S][v] = min(dp[S][v], min_u dp[S][u] + shortest_dist(u, v))
        # But shortest_dist(u, v) is the shortest path in the original graph
        # 
        # Actually, we need to be careful. The Dreyfus-Wagner algorithm works as follows:
        # After computing the partition-based dp[S][v], we need to "propagate" using the graph edges.
        # This is done by treating dp[S][v] as initial distances and running Dijkstra on the original graph.
        
        pq = []
        for v in range(1, n + 1):
            if dp[S][v] < INF:
                heapq.heappush(pq, (dp[S][v], v))
        
        while pq:
            d, u = heapq.heappop(pq)
            if d > dp[S][u]:
                continue
            for v, w in adj[u]:
                nd = d + w
                if nd < dp[S][v]:
                    dp[S][v] = nd
                    heapq.heappush(pq, (nd, v))
    
    # Answer is min over v of dp[(1<<t)-1][v]
    full = (1 << t) - 1
    ans = min(dp[full][v] for v in range(1, n + 1))
    print(ans)

solve()