import sys
import heapq

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    terminals = list(map(int, input().split()))
    terminals = [x-1 for x in terminals]

    INF = 10**15
    dist = [[INF]*n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0

    edges = []
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
            if dist[i][k] == INF: continue
            for j in range(n):
                if dist[k][j] == INF: continue
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    # Steiner DP
    full_mask = 1 << t
    dp = [[INF]*n for _ in range(full_mask)]

    for i, term in enumerate(terminals):
        dp[1 << i][term] = 0

    for mask in range(full_mask):
        # Combine submasks
        sub = (mask-1) & mask
        while sub:
            other = mask ^ sub
            if sub < other: # avoid double processing
                for v in range(n):
                    if dp[sub][v] + dp[other][v] < dp[mask][v]:
                        dp[mask][v] = dp[sub][v] + dp[other][v]
            sub = (sub-1) & mask

        # Relaxation using Dijkstra for this mask
        pq = []
        for v in range(n):
            if dp[mask][v] < INF:
                heapq.heappush(pq, (dp[mask][v], v))
        while pq:
            d, u = heapq.heappop(pq)
            if d != dp[mask][u]:
                continue
            for v in range(n):
                if dist[u][v] == INF:
                    continue
                nd = d + dist[u][v]
                if nd < dp[mask][v]:
                    dp[mask][v] = nd
                    heapq.heappush(pq, (nd, v))

    ans = min(dp[full_mask-1][v] for v in range(n))
    print(ans)

if __name__ == "__main__":
    solve()