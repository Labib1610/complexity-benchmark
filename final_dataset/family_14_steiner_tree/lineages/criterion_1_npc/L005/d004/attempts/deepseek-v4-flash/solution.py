import sys

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    keys = list(map(int, input().split()))
    keys = [k-1 for k in keys]  # 0-index

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

    # Floyd-Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    full_mask = (1 << t) - 1
    dp = [[INF]*n for _ in range(1 << t)]

    for i, key in enumerate(keys):
        dp[1 << i][key] = 0

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