import sys
import heapq

input = sys.stdin.readline
INF = 10**18

def solve():
    n, m, t = map(int, input().split())
    core = list(map(int, input().split()))
    core_idx = {v: i for i, v in enumerate(core)}
    
    # Build graph
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # If only one core, cost is 0
    if t == 1:
        print(0)
        return
    
    # Step 1: Compute shortest paths between all pairs of nodes
    # Use Dijkstra from each node (n <= 100, so O(n * m log n) is fine)
    dist = [[INF] * n for _ in range(n)]
    for s in range(n):
        dist[s][s] = 0
        pq = [(0, s)]
        while pq:
            d, u = heapq.heappop(pq)
            if d != dist[s][u]:
                continue
            for v, w in graph[u]:
                nd = d + w
                if nd < dist[s][v]:
                    dist[s][v] = nd
                    heapq.heappush(pq, (nd, v))
    
    # Step 2: DP over subsets of core nodes
    # dp[mask][v] = min cost to connect core nodes in mask, ending at node v
    full_mask = (1 << t) - 1
    dp = [[INF] * n for _ in range(1 << t)]
    
    # Initialize: for each core node, cost 0 to be at that node
    for i, node in enumerate(core):
        dp[1 << i][node] = 0
    
    # Iterate over masks
    for mask in range(1 << t):
        # Combine two submasks
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if sub < other:  # avoid duplicate work
                for v in range(n):
                    dp[mask][v] = min(dp[mask][v], dp[sub][v] + dp[other][v])
            sub = (sub - 1) & mask
        
        # Relax via shortest paths
        # Run Dijkstra-like relaxation using dist matrix
        for v in range(n):
            if dp[mask][v] < INF:
                for u in range(n):
                    if dist[v][u] < INF:
                        nd = dp[mask][v] + dist[v][u]
                        if nd < dp[mask][u]:
                            dp[mask][u] = nd
    
    # Answer is min over all nodes of dp[full_mask][node]
    ans = min(dp[full_mask])
    print(ans)

if __name__ == "__main__":
    solve()