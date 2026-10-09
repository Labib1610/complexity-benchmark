import sys
import heapq

input = sys.stdin.readline

def solve():
    n, m, t = map(int, input().split())
    focal = list(map(int, input().split()))
    focal_set = set(focal)
    
    # Build adjacency list
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    if t == 1:
        print(0)
        return
    
    # Map focal dialects to bit positions
    idx = {node: i for i, node in enumerate(focal)}
    
    INF = 10**18
    # dp[mask][v] = min cost to connect the focal nodes in mask, ending at v
    dp = [[INF]*(n+1) for _ in range(1<<t)]
    
    # Initialize: for each focal node, cost 0 to connect just itself
    for i, node in enumerate(focal):
        dp[1<<i][node] = 0
    
    # Dijkstra for each mask
    for mask in range(1<<t):
        # Combine submasks
        sub = (mask-1) & mask
        while sub:
            other = mask ^ sub
            if sub < other:  # avoid double work
                for v in range(1, n+1):
                    if dp[sub][v] + dp[other][v] < dp[mask][v]:
                        dp[mask][v] = dp[sub][v] + dp[other][v]
            sub = (sub-1) & mask
        
        # Dijkstra to propagate costs
        pq = []
        for v in range(1, n+1):
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
    
    full_mask = (1<<t) - 1
    ans = min(dp[full_mask][v] for v in range(1, n+1))
    print(ans)

if __name__ == "__main__":
    solve()