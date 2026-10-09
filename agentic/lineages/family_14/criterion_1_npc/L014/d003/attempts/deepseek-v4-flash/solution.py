import sys
import heapq

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    critical = list(map(int, input().split()))
    critical_set = set(critical)
    
    # Build adjacency list
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    if t == 1:
        print(0)
        return
    
    # Map critical nodes to bit positions
    idx = {node: i for i, node in enumerate(critical)}
    full_mask = (1 << t) - 1
    
    INF = 10**18
    dp = [[INF] * n for _ in range(1 << t)]
    
    # Initialize: single critical node masks
    for i, node in enumerate(critical):
        dp[1 << i][node] = 0
    
    # Steiner tree DP
    for mask in range(1 << t):
        # Combine submasks
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if other < sub:  # avoid duplicate work
                for v in range(n):
                    if dp[sub][v] + dp[other][v] < dp[mask][v]:
                        dp[mask][v] = dp[sub][v] + dp[other][v]
            sub = (sub - 1) & mask
        
        # Dijkstra to propagate shortest paths for this mask
        pq = [(dp[mask][v], v) for v in range(n) if dp[mask][v] < INF]
        heapq.heapify(pq)
        while pq:
            d, u = heapq.heappop(pq)
            if d != dp[mask][u]:
                continue
            for v, w in adj[u]:
                nd = d + w
                if nd < dp[mask][v]:
                    dp[mask][v] = nd
                    heapq.heappush(pq, (nd, v))
    
    ans = min(dp[full_mask][v] for v in range(n))
    print(ans)

if __name__ == "__main__":
    solve()