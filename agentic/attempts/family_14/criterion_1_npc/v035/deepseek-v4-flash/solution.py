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
    cores = [int(next(it)) - 1 for _ in range(t)]
    
    INF = 10**18
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # Dijkstra from each core site
    core_dist = []
    for core in cores:
        d = [INF] * n
        d[core] = 0
        pq = [(0, core)]
        while pq:
            du, u = heapq.heappop(pq)
            if du != d[u]:
                continue
            for v, w in adj[u]:
                nd = du + w
                if nd < d[v]:
                    d[v] = nd
                    heapq.heappush(pq, (nd, v))
        core_dist.append(d)
    
    # DP over subsets of core sites
    # dp[mask][i] = min cost to connect core sites in mask, ending at core i
    dp = [[INF] * t for _ in range(1 << t)]
    for i in range(t):
        dp[1 << i][i] = 0
    
    for mask in range(1 << t):
        for i in range(t):
            if dp[mask][i] == INF:
                continue
            # extend to another core
            for j in range(t):
                if not (mask & (1 << j)):
                    nmask = mask | (1 << j)
                    cost = dp[mask][i] + core_dist[i][cores[j]]
                    if cost < dp[nmask][j]:
                        dp[nmask][j] = cost
            # also consider merging two subsets
            sub = (mask - 1) & mask
            while sub:
                other = mask ^ sub
                if sub < other:  # avoid double work
                    for i in range(t):
                        if dp[sub][i] == INF:
                            continue
                        for j in range(t):
                            if dp[other][j] == INF:
                                continue
                            cost = dp[sub][i] + dp[other][j]
                            if cost < dp[mask][i]:
                                dp[mask][i] = cost
                            if cost < dp[mask][j]:
                                dp[mask][j] = cost
                sub = (sub - 1) & mask
    
    ans = min(dp[(1 << t) - 1][i] for i in range(t))
    print(ans)

if __name__ == "__main__":
    solve()