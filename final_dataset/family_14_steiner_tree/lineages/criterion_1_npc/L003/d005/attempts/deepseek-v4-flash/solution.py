import sys
import heapq

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    targets = list(map(int, input().split()))
    targets = [x-1 for x in targets]  # 0-based

    INF = 10**18
    dist = [[INF]*n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0

    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        if w < dist[u][v]:
            dist[u][v] = w
            dist[v][u] = w

    # Floyd-Warshall for all-pairs shortest paths
    for k in range(n):
        dk = dist[k]
        for i in range(n):
            dik = dist[i][k]
            if dik == INF:
                continue
            di = dist[i]
            for j in range(n):
                nd = dik + dk[j]
                if nd < di[j]:
                    di[j] = nd

    # DP over subsets of terminals
    full_mask = (1 << t) - 1
    dp = [[INF]*n for _ in range(1 << t)]

    for i, node in enumerate(targets):
        dp[1 << i][node] = 0

    # Precompute distances from each node to each terminal subset? Not needed, we do DP directly.

    for mask in range(1 << t):
        # Merge subsets
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if sub < other:  # avoid duplicate work
                for v in range(n):
                    best = INF
                    for u in range(n):
                        val = dp[sub][u] + dist[u][v]
                        if val < best:
                            best = val
                    if best + dp[other][v] < dp[mask][v]:
                        dp[mask][v] = best + dp[other][v]
            sub = (sub - 1) & mask

        # Relax using shortest paths
        # Dijkstra-like relaxation for this mask
        pq = [(dp[mask][v], v) for v in range(n) if dp[mask][v] < INF]
        heapq.heapify(pq)
        while pq:
            d, u = heapq.heappop(pq)
            if d != dp[mask][u]:
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