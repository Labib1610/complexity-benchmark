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
    
    if t <= 1:
        print(0)
        return
    
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        edges.append((u, v, w))
    
    # Build adjacency list
    adj = [[] for _ in range(n + 1)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # Dijkstra from each critical node
    INF = float('inf')
    dist = [[INF] * (n + 1) for _ in range(t)]
    for i, src in enumerate(critical):
        dist[i][src] = 0
        import heapq
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
    
    # For each non-critical node, cost to connect all critical nodes through it
    best = INF
    for v in range(1, n + 1):
        total = 0
        for i in range(t):
            total += dist[i][v]
        if total < best:
            best = total
    
    # Also consider Steiner tree on critical nodes using edges directly
    # Since t <= 10, we can do DP over subsets
    # dp[mask][v] = min cost to connect critical nodes in mask, with v in the tree
    # But we need to be careful: the tree can include non-critical nodes
    
    # Actually, the above approach (star through one node) might not be optimal
    # Let's do proper Steiner tree DP
    
    # Map critical nodes to bit positions
    crit_idx = {}
    for i, c in enumerate(critical):
        crit_idx[c] = i
    
    # dp[mask][v]: min cost to connect critical nodes in mask, tree includes v
    # Initialize: for each critical node, dp[1<<i][node] = dist from that critical to node
    # But actually we want: the tree connects the critical nodes in mask
    
    # Standard Steiner tree DP on graph:
    # dp[mask][v] = min over submask of (dp[submask][v] + dp[mask^submask][v])
    # Then relax: dp[mask][v] = min(dp[mask][v], dp[mask][u] + w(u,v))
    
    full_mask = (1 << t) - 1
    dp = [[INF] * (n + 1) for _ in range(1 << t)]
    
    for i in range(t):
        mask = 1 << i
        src = critical[i]
        # Initialize with shortest paths from src to all nodes
        for v in range(1, n + 1):
            dp[mask][v] = dist[i][v]
    
    # For masks with multiple bits
    for mask in range(1, 1 << t):
        if mask & (mask - 1) == 0:
            # Single bit, already initialized
            pass
        else:
            # Combine submasks
            submask = (mask - 1) & mask
            while submask > 0:
                other = mask ^ submask
                for v in range(1, n + 1):
                    val = dp[submask][v] + dp[other][v]
                    if val < dp[mask][v]:
                        dp[mask][v] = val
                submask = (submask - 1) & mask
        
        # Relax using edges (Dijkstra-like)
        # dp[mask][v] = min over u of (dp[mask][u] + dist(u, v))
        # But we can do this more efficiently with Dijkstra
        import heapq
        pq = []
        for v in range(1, n + 1):
            if dp[mask][v] < INF:
                pq.append((dp[mask][v], v))
        heapq.heapify(pq)
        while pq:
            d, u = heapq.heappop(pq)
            if d > dp[mask][u]:
                continue
            for v, w in adj[u]:
                nd = d + w
                if nd < dp[mask][v]:
                    dp[mask][v] = nd
                    heapq.heappush(pq, (nd, v))
    
    # Answer is min over v of dp[full_mask][v]
    ans = min(dp[full_mask][v] for v in range(1, n + 1))
    print(ans)

solve()