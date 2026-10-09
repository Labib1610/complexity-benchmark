import sys
import heapq

input = sys.stdin.readline

def solve():
    n, m, t = map(int, input().split())
    primary = list(map(int, input().split()))
    primary_set = set(primary)
    
    # Build graph
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    if t == 1:
        print(0)
        return
    
    # Map primary languages to bit positions
    idx = {lang: i for i, lang in enumerate(primary)}
    
    # dp[mask][v] = min cost to connect primary nodes in mask, ending at node v
    INF = 10**18
    dp = [[INF]*(n+1) for _ in range(1<<t)]
    
    # Initialize: for each primary node, cost 0 to reach itself
    for i, lang in enumerate(primary):
        dp[1<<i][lang] = 0
    
    # Dijkstra for each mask
    for mask in range(1<<t):
        # First, combine subsets
        sub = (mask-1) & mask
        while sub:
            other = mask ^ sub
            if sub < other:  # avoid double work
                for v in range(1, n+1):
                    dp[mask][v] = min(dp[mask][v], dp[sub][v] + dp[other][v])
            sub = (sub-1) & mask
        
        # Then run Dijkstra from current dp[mask]
        pq = []
        for v in range(1, n+1):
            if dp[mask][v] < INF:
                heapq.heappush(pq, (dp[mask][v], v))
        
        while pq:
            d, u = heapq.heappop(pq)
            if d != dp[mask][u]:
                continue
            for v, w in graph[u]:
                nd = d + w
                if nd < dp[mask][v]:
                    dp[mask][v] = nd
                    heapq.heappush(pq, (nd, v))
    
    full_mask = (1<<t) - 1
    ans = min(dp[full_mask][v] for v in range(1, n+1))
    print(ans)

if __name__ == "__main__":
    solve()