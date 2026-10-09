import sys
import heapq

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    core = list(map(int, input().split()))
    core_index = {v: i for i, v in enumerate(core)}
    
    # Build graph
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    if t == 1:
        print(0)
        return
    
    # Compute shortest distances between all core nodes
    INF = 10**18
    dist = [[INF]*t for _ in range(t)]
    
    for i, start in enumerate(core):
        # Dijkstra from start
        d = [INF]*(n+1)
        d[start] = 0
        pq = [(0, start)]
        while pq:
            du, u = heapq.heappop(pq)
            if du != d[u]:
                continue
            for v, w in graph[u]:
                nd = du + w
                if nd < d[v]:
                    d[v] = nd
                    heapq.heappush(pq, (nd, v))
        for j, node in enumerate(core):
            dist[i][j] = d[node]
    
    # DP over subsets
    full_mask = 1 << t
    dp = [[INF]*t for _ in range(full_mask)]
    
    for i in range(t):
        dp[1<<i][i] = 0
    
    for mask in range(1, full_mask):
        # Try merging two submasks
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if sub < other:  # avoid duplicate work
                for i in range(t):
                    if dp[sub][i] == INF:
                        continue
                    for j in range(t):
                        if dp[other][j] == INF:
                            continue
                        cost = dp[sub][i] + dp[other][j] + dist[i][j]
                        if cost < dp[mask][i]:
                            dp[mask][i] = cost
                        if cost < dp[mask][j]:
                            dp[mask][j] = cost
            sub = (sub - 1) & mask
        
        # Try extending from a node to another via shortest path
        for i in range(t):
            if dp[mask][i] == INF:
                continue
            for j in range(t):
                if mask & (1 << j):
                    continue
                nmask = mask | (1 << j)
                cost = dp[mask][i] + dist[i][j]
                if cost < dp[nmask][j]:
                    dp[nmask][j] = cost
    
    ans = min(dp[full_mask-1])
    print(ans)

if __name__ == "__main__":
    solve()