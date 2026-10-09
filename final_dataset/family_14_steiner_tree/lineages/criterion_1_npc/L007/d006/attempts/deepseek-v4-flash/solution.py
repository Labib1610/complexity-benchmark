import sys
import heapq

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    targets = list(map(int, input().split()))
    targets = [x - 1 for x in targets]  # 0-based

    INF = 10**18
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0

    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append((v, w))
        adj[v].append((u, w))

    # Dijkstra from each node to get all-pairs shortest paths
    for s in range(n):
        d = [INF] * n
        d[s] = 0
        pq = [(0, s)]
        while pq:
            du, u = heapq.heappop(pq)
            if du != d[u]:
                continue
            for v, w in adj[u]:
                nd = du + w
                if nd < d[v]:
                    d[v] = nd
                    heapq.heappush(pq, (nd, v))
        dist[s] = d

    # DP over subsets
    full_mask = (1 << t) - 1
    dp = [[INF] * n for _ in range(1 << t)]

    for i in range(t):
        dp[1 << i][targets[i]] = 0

    for mask in range(1 << t):
        # Merge subsets
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if other < sub:  # avoid duplicate work
                for v in range(n):
                    dp[mask][v] = min(dp[mask][v], dp[sub][v] + dp[other][v])
            sub = (sub - 1) & mask

        # Relax via shortest paths
        for u in range(n):
            if dp[mask][u] < INF:
                for v in range(n):
                    if dist[u][v] < INF:
                        nd = dp[mask][u] + dist[u][v]
                        if nd < dp[mask][v]:
                            dp[mask][v] = nd

    ans = min(dp[full_mask])
    print(ans)

if __name__ == "__main__":
    solve()