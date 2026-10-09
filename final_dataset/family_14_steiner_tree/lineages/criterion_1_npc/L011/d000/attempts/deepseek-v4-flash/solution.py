import sys

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    primaries = list(map(int, input().split()))
    primaries = [p - 1 for p in primaries]  # 0-index

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
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    # DP over subsets
    full_mask = 1 << t
    dp = [[INF] * n for _ in range(full_mask)]

    # Initialize: single primary nodes
    for i, p in enumerate(primaries):
        dp[1 << i][p] = 0

    # For each subset
    for mask in range(1, full_mask):
        # Combine two smaller subsets
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

        # Relax via shortest paths
        # Run Dijkstra-like relaxation using dist matrix
        # Since n ≤ 100, we can do simple relaxation
        for _ in range(n):
            updated = False
            for u in range(n):
                if dp[mask][u] == INF:
                    continue
                for v in range(n):
                    if dist[u][v] < INF and dp[mask][u] + dist[u][v] < dp[mask][v]:
                        dp[mask][v] = dp[mask][u] + dist[u][v]
                        updated = True
            if not updated:
                break

    ans = min(dp[full_mask - 1][v] for v in range(n))
    print(ans)

if __name__ == "__main__":
    solve()