import sys
import heapq

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    terminals = [int(next(it)) - 1 for _ in range(t)]
    
    # adjacency list
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # If only one terminal, cost is 0
    if t == 1:
        print(0)
        return
    
    # Precompute all-pairs shortest paths (Dijkstra from each terminal)
    INF = 10**18
    dist = [[INF]*n for _ in range(t)]
    for idx, s in enumerate(terminals):
        d = [INF]*n
        d[s] = 0
        pq = [(0, s)]
        while pq:
            du, u = heapq.heappop(pq)
            if du != d[u]:
                continue
            for v, w in adj[u]:
                nd = du + w
                if nd < d[v]:
                    d[v] = nd
                    heapq.heappush(pq, (nd, v))
        dist[idx] = d
    
    # DP over subsets
    # dp[mask][v] = min cost to connect terminals in mask, with v as root
    full_mask = 1 << t
    dp = [[INF]*n for _ in range(full_mask)]
    
    # Initialize: single terminal
    for i in range(t):
        for v in range(n):
            dp[1 << i][v] = dist[i][v]
    
    # Combine subsets
    for mask in range(1, full_mask):
        # Split mask into two non-empty subsets
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if sub < other:  # avoid duplicate work
                for v in range(n):
                    dp[mask][v] = min(dp[mask][v], dp[sub][v] + dp[other][v])
            sub = (sub - 1) & mask
        
        # Relax via Dijkstra for this mask
        # We can run Dijkstra from all nodes with current dp[mask][v]
        pq = [(dp[mask][v], v) for v in range(n) if dp[mask][v] < INF]
        heapq.heapify(pq)
        while pq:
            du, u = heapq.heappop(pq)
            if du != dp[mask][u]:
                continue
            for v, w in adj[u]:
                nd = du + w
                if nd < dp[mask][v]:
                    dp[mask][v] = nd
                    heapq.heappush(pq, (nd, v))
    
    ans = min(dp[full_mask - 1][v] for v in range(n))
    print(ans)

if __name__ == "__main__":
    solve()