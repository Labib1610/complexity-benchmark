import sys
import heapq

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    required = list(map(int, input().split()))
    required = [x - 1 for x in required]  # 0-based

    INF = 10**18
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0

    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append((v, w))
        graph[v].append((u, w))

    # Dijkstra from each node to get all-pairs shortest paths
    for src in range(n):
        d = [INF] * n
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
        dist[src] = d

    # DP over subsets of required sites
    # dp[mask][v] = min cost to connect required sites in mask, ending at v
    full_mask = 1 << t
    dp = [[INF] * n for _ in range(full_mask)]

    for i in range(t):
        dp[1 << i][required[i]] = 0

    for mask in range(1, full_mask):
        # Combine two submasks
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if sub < other:  # avoid duplicate work
                for v in range(n):
                    dp[mask][v] = min(dp[mask][v], dp[sub][v] + dp[other][v])
            sub = (sub - 1) & mask

        # Relax via shortest paths
        for v in range(n):
            if dp[mask][v] < INF:
                for u in range(n):
                    if dist[v][u] < INF:
                        nd = dp[mask][v] + dist[v][u]
                        if nd < dp[mask][u]:
                            dp[mask][u] = nd

    ans = min(dp[full_mask - 1][v] for v in range(n))
    print(ans)

if __name__ == "__main__":
    solve()