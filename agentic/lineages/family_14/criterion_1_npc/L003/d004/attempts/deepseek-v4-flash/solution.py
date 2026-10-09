import sys
import heapq

input = sys.stdin.readline

def solve():
    n, m, t = map(int, input().split())
    focal = list(map(int, input().split()))
    focal_set = set(focal)
    
    # Map focal variables to indices 0..t-1
    focal_index = {v: i for i, v in enumerate(focal)}
    
    # Build graph
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    if t == 1:
        print(0)
        return
    
    # Step 1: Compute shortest paths from each focal variable to all nodes
    INF = 10**18
    dist = [[INF] * (n + 1) for _ in range(t)]
    for i, fv in enumerate(focal):
        d = dist[i]
        d[fv] = 0
        pq = [(0, fv)]
        while pq:
            du, u = heapq.heappop(pq)
            if du != d[u]:
                continue
            for v, w in graph[u]:
                nd = du + w
                if nd < d[v]:
                    d[v] = nd
                    heapq.heappush(pq, (nd, v))
    
    # Step 2: DP over subsets of focal variables
    # dp[mask][v] = min cost to connect focal set 'mask' with v as root/terminal
    dp = [[INF] * (n + 1) for _ in range(1 << t)]
    
    # Initialize: single focal variable
    for i in range(t):
        mask = 1 << i
        for v in range(1, n + 1):
            dp[mask][v] = dist[i][v]
    
    # Combine subsets
    for mask in range(1, 1 << t):
        # Try splitting mask into two non-empty subsets
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if sub < other:  # avoid duplicate work
                for v in range(1, n + 1):
                    dp[mask][v] = min(dp[mask][v], dp[sub][v] + dp[other][v])
            sub = (sub - 1) & mask
        
        # Run Dijkstra-like relaxation for this mask
        pq = [(dp[mask][v], v) for v in range(1, n + 1) if dp[mask][v] < INF]
        heapq.heapify(pq)
        while pq:
            du, u = heapq.heappop(pq)
            if du != dp[mask][u]:
                continue
            for v, w in graph[u]:
                nd = du + w
                if nd < dp[mask][v]:
                    dp[mask][v] = nd
                    heapq.heappush(pq, (nd, v))
    
    full_mask = (1 << t) - 1
    ans = min(dp[full_mask][v] for v in range(1, n + 1))
    print(ans)

if __name__ == "__main__":
    solve()