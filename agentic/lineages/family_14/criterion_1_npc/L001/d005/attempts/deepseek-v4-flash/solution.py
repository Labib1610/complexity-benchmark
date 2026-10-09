import sys
import heapq

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    targets = list(map(int, input().split()))
    targets = [x-1 for x in targets]
    
    # Build graph
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    if t == 1:
        print(0)
        return
    
    # All-pairs shortest paths using Dijkstra from each node
    INF = 10**18
    dist = [[INF]*n for _ in range(n)]
    for s in range(n):
        dist[s][s] = 0
        pq = [(0, s)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[s][u]:
                continue
            for v, w in graph[u]:
                nd = d + w
                if nd < dist[s][v]:
                    dist[s][v] = nd
                    heapq.heappush(pq, (nd, v))
    
    # DP over subsets of targets
    # dp[mask][v] = min cost to connect targets in mask, ending at node v
    dp = [[INF]*n for _ in range(1<<t)]
    for i in range(t):
        dp[1<<i][targets[i]] = 0
    
    for mask in range(1<<t):
        # Combine subsets
        sub = (mask-1) & mask
        while sub:
            other = mask ^ sub
            if sub < other:  # avoid duplicate work
                for v in range(n):
                    dp[mask][v] = min(dp[mask][v], dp[sub][v] + dp[other][v])
            sub = (sub-1) & mask
        
        # Relax via shortest paths
        for v in range(n):
            if dp[mask][v] < INF:
                for to in range(n):
                    if dist[v][to] < INF:
                        nd = dp[mask][v] + dist[v][to]
                        if nd < dp[mask][to]:
                            dp[mask][to] = nd
    
    full_mask = (1<<t) - 1
    ans = min(dp[full_mask])
    print(ans)

if __name__ == "__main__":
    solve()