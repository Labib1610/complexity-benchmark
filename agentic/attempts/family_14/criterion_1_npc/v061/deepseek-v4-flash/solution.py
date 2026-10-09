import sys
import heapq

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    keys = list(map(int, input().split()))
    keys = [k - 1 for k in keys]  # 0-index

    INF = 10**18
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0

    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        if w < dist[u][v]:
            dist[u][v] = w
            dist[v][u] = w

    # Floyd-Warshall
    for k in range(n):
        for i in range(n):
            if dist[i][k] == INF:
                continue
            for j in range(n):
                if dist[k][j] == INF:
                    continue
                nd = dist[i][k] + dist[k][j]
                if nd < dist[i][j]:
                    dist[i][j] = nd

    # DP over subsets
    full_mask = (1 << t) - 1
    dp = [[INF] * n for _ in range(1 << t)]

    for i in range(t):
        dp[1 << i][keys[i]] = 0

    for mask in range(1 << t):
        # Combine two submasks
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if other < sub:  # avoid duplicate work
                sub = (sub - 1) & mask
                continue
            for v in range(n):
                if dp[sub][v] + dp[other][v] < dp[mask][v]:
                    dp[mask][v] = dp[sub][v] + dp[other][v]
            sub = (sub - 1) & mask

        # Run Dijkstra-like relaxation from current mask
        # Use a priority queue
        pq = []
        for v in range(n):
            if dp[mask][v] < INF:
                heapq.heappush(pq, (dp[mask][v], v))
        while pq:
            d, u = heapq.heappop(pq)
            if d > dp[mask][u]:
                continue
            for v in range(n):
                nd = d + dist[u][v]
                if nd < dp[mask][v]:
                    dp[mask][v] = nd
                    heapq.heappush(pq, (nd, v))

    ans = min(dp[full_mask])
    print(ans)

if __name__ == "__main__":
    solve()