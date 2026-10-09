import sys
import heapq

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    required = list(map(int, input().split()))
    required = [x-1 for x in required]  # 0-index

    INF = 10**18
    dist = [[INF]*n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0

    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append((v, w))
        adj[v].append((u, w))

    # Dijkstra from each node
    for s in range(n):
        d = [INF]*n
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

    # Map required sites to bit positions
    req_index = {node: i for i, node in enumerate(required)}
    full_mask = (1 << t) - 1

    dp = [[INF]*n for _ in range(1 << t)]
    for i, node in enumerate(required):
        dp[1 << i][node] = 0

    # DP over masks
    for mask in range(1 << t):
        # Try merging two submasks
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if sub < other:  # avoid duplicate work
                for u in range(n):
                    if dp[sub][u] < INF:
                        for v in range(n):
                            if dp[other][v] < INF:
                                dp[mask][u] = min(dp[mask][u], dp[sub][u] + dp[other][v] + dist[u][v])
            sub = (sub - 1) & mask

        # Relax via shortest paths
        for u in range(n):
            if dp[mask][u] < INF:
                for v in range(n):
                    if dist[u][v] < INF:
                        dp[mask][v] = min(dp[mask][v], dp[mask][u] + dist[u][v])

    ans = min(dp[full_mask])
    print(ans)

if __name__ == "__main__":
    solve()