import sys
import heapq

input = sys.stdin.readline

def solve():
    n, m, t = map(int, input().split())
    terminals = list(map(int, input().split()))
    terminals = [x - 1 for x in terminals]
    
    # Build graph
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # If only one terminal, cost is 0
    if t == 1:
        print(0)
        return
    
    # Dijkstra from each terminal to all nodes
    INF = 10**18
    dist = [[INF] * n for _ in range(t)]
    for i, src in enumerate(terminals):
        d = dist[i]
        d[src] = 0
        pq = [(0, src)]
        while pq:
            du, u = heapq.heappop(pq)
            if du != d[u]:
                continue
            for v, w in graph[u]:
                nd = du + w
                if nd < d[v]:
                    d[v] = nd
                    heapq.heappush(pq, (nd, v))
    
    # DP over subsets of terminals
    # dp[mask][v] = min cost to connect terminals in mask, ending at node v
    full_mask = 1 << t
    dp = [[INF] * n for _ in range(full_mask)]
    
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
        
        # Run Dijkstra to propagate within this mask
        pq = []
        for v in range(n):
            if dp[mask][v] < INF:
                heapq.heappush(pq, (dp[mask][v], v))
        while pq:
            du, u = heapq.heappop(pq)
            if du != dp[mask][u]:
                continue
            for v, w in graph[u]:
                nd = du + w
                if nd < dp[mask][v]:
                    dp[mask][v] = nd
                    heapq.heappush(pq, (nd, v))
    
    # Answer is min over all nodes of dp[full_mask-1][v]
    ans = min(dp[full_mask - 1])
    print(ans)

if __name__ == "__main__":
    solve()