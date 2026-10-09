import sys

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    targets = list(map(int, input().split()))
    targets = [x - 1 for x in targets]
    
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((u - 1, v - 1, w))
    
    if t == 1:
        print(0)
        return
    
    INF = float('inf')
    ans = INF
    
    # Try all 2^t subsets of targets that must be in the same component
    for mask in range(1, 1 << t):
        # We want all targets in this subset to be in the same component.
        # Targets not in the subset can be in any component (including the same one).
        # We need to find the minimum cost to connect all targets in the subset.
        # This is a Steiner tree problem on the targets in the subset.
        
        # Get the targets in this subset
        subset_targets = [targets[i] for i in range(t) if (mask >> i) & 1]
        k = len(subset_targets)
        
        if k == 1:
            # Only one target needs to be connected, cost is 0
            ans = min(ans, 0)
            continue
        
        # Steiner tree DP
        # dp[S] = minimum cost to connect the set S of terminals
        # where S is a subset of the k terminals
        
        # Initialize: dp[{i}] = 0 for each single terminal
        dp = [INF] * (1 << k)
        for i in range(k):
            dp[1 << i] = 0
        
        # For each subset, compute the minimum cost to connect those terminals
        # We use a modified Dijkstra-like approach for each subset
        
        # First, compute all-pairs shortest paths between terminals
        # using only edges (this is the metric closure)
        
        # Actually, let's do the standard Steiner tree DP with Dijkstra
        # For each mask, we maintain the minimum cost to connect those terminals
        # We process masks in increasing order of size
        
        # For the Steiner tree, we need:
        # 1. dp[S] = min over partitions S = A | B of dp[A] + dp[B]
        # 2. dp[S] = min over all vertices v of (cost to connect all terminals in S to v)
        #    This is done by running Dijkstra from the terminals in S
        
        # Let's implement this properly
        
        # dist[mask][v] = minimum cost to connect all terminals in mask, rooted at v
        # We use Dijkstra to propagate
        
        # Initialize
        dist = [[INF] * n for _ in range(1 << k)]
        for i in range(k):
            dist[1 << i][subset_targets[i]] = 0
        
        # Process masks in increasing order
        for mask in range(1, 1 << k):
            # First, compute dp[mask] from submasks
            sub = (mask - 1) & mask
            while sub > 0:
                complement = mask ^ sub
                if sub < complement:
                    break
                # dp[mask] = min(dp[mask], dp[sub] + dp[complement])
                # But we need to combine the distances
                for v in range(n):
                    if dist[sub][v] + dist[complement][v] < dist[mask][v]:
                        dist[mask][v] = dist[sub][v] + dist[complement][v]
                sub = (sub - 1) & mask
            
            # Now run Dijkstra to propagate dist[mask] along edges
            # This computes the minimum cost to connect all terminals in mask,
            # where the "tree" is rooted at some vertex v
            import heapq
            pq = []
            for v in range(n):
                if dist[mask][v] < INF:
                    heapq.heappush(pq, (dist[mask][v], v))
            
            while pq:
                d, u = heapq.heappop(pq)
                if d > dist[mask][u]:
                    continue
                for uu, vv, w in edges:
                    if uu == u:
                        v2 = vv
                    elif vv == u:
                        v2 = uu
                    else:
                        continue
                    if dist[mask][v2] > d + w:
                        dist[mask][v2] = d + w
                        heapq.heappush(pq, (dist[mask][v2], v2))
        
        # The answer for this subset is the minimum cost to connect all terminals
        full_mask = (1 << k) - 1
        cost = min(dist[full_mask])
        ans = min(ans, cost)
    
    print(ans)

solve()