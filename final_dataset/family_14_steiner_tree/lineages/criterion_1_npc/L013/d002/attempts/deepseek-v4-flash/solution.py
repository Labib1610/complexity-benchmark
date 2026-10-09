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
    
    # Build graph
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        graph[u].append((v, w))
        graph[v].append((u, w))
    
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
    # dp[mask][v] = min cost to connect terminals in mask, ending at v
    full_mask = 1 << t
    dp = [[INF] * n for _ in range(full_mask)]
    
    for i in range(t):
        dp[1 << i][terminals[i]] = 0
    
    for mask in range(1, full_mask):
        # Combine subsets
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if sub < other:  # avoid double work
                for v in range(n):
                    if dp[sub][v] < INF and dp[other][v] < INF:
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
    
    ans = min(dp[full_mask - 1][v] for v in range(n))
    print(ans)

if __name__ == "__main__":
    solve()