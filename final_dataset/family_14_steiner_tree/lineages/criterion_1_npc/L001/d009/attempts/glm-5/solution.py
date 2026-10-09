import sys
import heapq

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    
    targets = []
    for _ in range(t):
        targets.append(int(next(it)))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    if t <= 1:
        print(0)
        return
    
    # Compute all-pairs shortest paths between targets using Dijkstra
    INF = float('inf')
    dist = [[INF] * (n + 1) for _ in range(n + 1)]
    
    for start in targets:
        dist[start][start] = 0
        pq = [(0, start)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[start][u]:
                continue
            for v, w in adj[u]:
                nd = d + w
                if nd < dist[start][v]:
                    dist[start][v] = nd
                    heapq.heappush(pq, (nd, v))
    
    # Steiner Tree DP
    # Map targets to indices 0..t-1
    target_idx = {targets[i]: i for i in range(t)}
    
    # dp[mask][v] = min cost to connect targets in mask, ending at vertex v
    dp = [[INF] * (n + 1) for _ in range(1 << t)]
    
    # Initialize single targets
    for i, tc in enumerate(targets):
        dp[1 << i][tc] = 0
    
    # Fill DP
    for mask in range(1, 1 << t):
        # Skip single target masks (already initialized)
        if mask & (mask - 1) == 0:
            continue
        
        # Combine smaller masks
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if sub < other:  # Avoid duplicate work
                break
            for v in range(1, n + 1):
                if dp[sub][v] + dp[other][v] < dp[mask][v]:
                    dp[mask][v] = dp[sub][v] + dp[other][v]
            sub = (sub - 1) & mask
        
        # Dijkstra to propagate
        pq = []
        for v in range(1, n + 1):
            if dp[mask][v] < INF:
                heapq.heappush(pq, (dp[mask][v], v))
        
        while pq:
            d, u = heapq.heappop(pq)
            if d > dp[mask][u]:
                continue
            for v, w in adj[u]:
                nd = d + w
                if nd < dp[mask][v]:
                    dp[mask][v] = nd
                    heapq.heappush(pq, (nd, v))
    
    full_mask = (1 << t) - 1
    result = min(dp[full_mask][v] for v in range(1, n + 1))
    print(result)

solve()