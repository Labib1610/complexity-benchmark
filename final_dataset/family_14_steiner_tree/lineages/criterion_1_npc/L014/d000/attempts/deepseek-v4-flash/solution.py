import sys

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    critical = list(map(int, input().split()))
    INF = 10**18

    dist = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dist[i][i] = 0

    for _ in range(m):
        u, v, w = map(int, input().split())
        if w < dist[u][v]:
            dist[u][v] = w
            dist[v][u] = w

    # Floyd-Warshall
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            if dist[i][k] == INF:
                continue
            for j in range(1, n + 1):
                if dist[k][j] == INF:
                    continue
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    # Map critical nodes to indices
    crit_idx = {node: i for i, node in enumerate(critical)}
    full_mask = (1 << t) - 1

    dp = [[INF] * (n + 1) for _ in range(1 << t)]
    for i, node in enumerate(critical):
        dp[1 << i][node] = 0

    for mask in range(1 << t):
        # Combine subsets
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if other < sub:  # avoid duplicate work
                sub = (sub - 1) & mask
                continue
            for v in range(1, n + 1):
                if dp[sub][v] + dp[other][v] < dp[mask][v]:
                    dp[mask][v] = dp[sub][v] + dp[other][v]
            sub = (sub - 1) & mask

        # Relax via shortest paths
        for u in range(1, n + 1):
            if dp[mask][u] == INF:
                continue
            for v in range(1, n + 1):
                if dist[u][v] == INF:
                    continue
                if dp[mask][u] + dist[u][v] < dp[mask][v]:
                    dp[mask][v] = dp[mask][u] + dist[u][v]

    ans = min(dp[full_mask][1:])
    print(ans)

if __name__ == "__main__":
    solve()