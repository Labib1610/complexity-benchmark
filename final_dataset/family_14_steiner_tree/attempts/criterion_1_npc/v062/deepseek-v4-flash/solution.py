import sys
import heapq

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    terminals = list(map(int, input().split()))
    terminals = [x-1 for x in terminals]
    
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
    
    INF = 10**18
    # dist[i][v] = shortest distance from terminal i to v
    dist = [[INF]*n for _ in range(t)]
    for i, term in enumerate(terminals):
        d = dist[i]
        d[term] = 0
        pq = [(0, term)]
        while pq:
            du, u = heapq.heappop(pq)
            if du != d[u]:
                continue
            for v, w in graph[u]:
                nd = du + w
                if nd < d[v]:
                    d[v] = nd
                    heapq.heappush(pq, (nd, v))
    
    full_mask = (1 << t) - 1
    dp = [[INF]*n for _ in range(1 << t)]
    
    for i in range(t):
        dp[1 << i][terminals[i]] = 0
    
    # For each mask, relax using shortest paths
    for mask in range(1 << t):
        # Combine submasks
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if sub < other:  # avoid double work
                for v in range(n):
                    if dp[sub][v] + dp[other][v] < dp[mask][v]:
                        dp[mask][v] = dp[sub][v] + dp[other][v]
            sub = (sub - 1) & mask
        
        # Dijkstra relaxation for this mask
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
    
    ans = min(dp[full_mask])
    print(ans)

if __name__ == "__main__":
    solve()