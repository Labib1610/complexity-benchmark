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
    essential = [int(next(it)) - 1 for _ in range(t)]
    
    # Build adjacency list
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # If only one essential, cost is 0
    if t == 1:
        print(0)
        return
    
    # Map essential vertices to bit positions
    term_index = {}
    for idx, v in enumerate(essential):
        term_index[v] = idx
    
    INF = 10**18
    # dp[mask][v] = min cost to connect terminals in mask, ending at vertex v
    dp = [[INF] * n for _ in range(1 << t)]
    
    # Initialize: for each terminal, mask with only that terminal, cost 0 at that vertex
    for i, v in enumerate(essential):
        dp[1 << i][v] = 0
    
    # Dijkstra for each mask
    for mask in range(1 << t):
        # First, combine submasks
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if sub < other:  # avoid double work
                for v in range(n):
                    if dp[sub][v] + dp[other][v] < dp[mask][v]:
                        dp[mask][v] = dp[sub][v] + dp[other][v]
            sub = (sub - 1) & mask
        
        # Then run Dijkstra from all nodes with finite dp[mask][v]
        pq = []
        for v in range(n):
            if dp[mask][v] < INF:
                heapq.heappush(pq, (dp[mask][v], v))
        
        while pq:
            d, u = heapq.heappop(pq)
            if d != dp[mask][u]:
                continue
            for v, w in adj[u]:
                nd = d + w
                if nd < dp[mask][v]:
                    dp[mask][v] = nd
                    heapq.heappush(pq, (nd, v))
    
    full_mask = (1 << t) - 1
    ans = min(dp[full_mask][v] for v in range(n))
    print(ans)

if __name__ == "__main__":
    solve()