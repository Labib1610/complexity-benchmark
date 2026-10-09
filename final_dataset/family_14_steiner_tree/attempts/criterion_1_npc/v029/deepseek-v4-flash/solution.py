import sys
import heapq

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    core = list(map(int, input().split()))
    core_set = set(core)
    
    # Build adjacency list
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # Map core nodes to indices 0..t-1
    core_index = {node: i for i, node in enumerate(core)}
    
    # If only one core, cost is 0
    if t == 1:
        print(0)
        return
    
    # Step 1: Compute shortest paths between all pairs of core nodes
    # Use Dijkstra from each core node
    INF = 10**18
    dist = [[INF]*n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
        pq = [(0, i)]
        while pq:
            d, u = heapq.heappop(pq)
            if d != dist[i][u]:
                continue
            for v, w in graph[u]:
                nd = d + w
                if nd < dist[i][v]:
                    dist[i][v] = nd
                    heapq.heappush(pq, (nd, v))
    
    # Step 2: Steiner tree DP
    # dp[mask][v] = min cost to connect core nodes in mask, ending at node v
    full_mask = (1 << t) - 1
    dp = [[INF]*n for _ in range(1 << t)]
    
    # Initialize: each core node alone
    for i, node in enumerate(core):
        dp[1 << i][node] = 0
    
    # For each mask
    for mask in range(1 << t):
        # Combine two submasks
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if other < sub:  # avoid duplicate work
                sub = (sub - 1) & mask
                continue
            for v in range(n):
                dp[mask][v] = min(dp[mask][v], dp[sub][v] + dp[other][v])
            sub = (sub - 1) & mask
        
        # Relax via shortest paths
        # Use Dijkstra-like relaxation
        pq = [(dp[mask][v], v) for v in range(n) if dp[mask][v] < INF]
        heapq.heapify(pq)
        while pq:
            d, u = heapq.heappop(pq)
            if d != dp[mask][u]:
                continue
            for v, w in graph[u]:
                nd = d + w
                if nd < dp[mask][v]:
                    dp[mask][v] = nd
                    heapq.heappush(pq, (nd, v))
    
    # Answer: min over all nodes for full mask
    ans = min(dp[full_mask][v] for v in range(n))
    print(ans)

if __name__ == "__main__":
    solve()