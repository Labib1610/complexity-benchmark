import sys

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    targets = list(map(int, input().split()))
    targets = [x-1 for x in targets]  # 0-index

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
            if dist[i][k] == INF:
                continue
            for j in range(n):
                if dist[k][j] == INF:
                    continue
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    if t == 1:
        print(0)
        return

    full_mask = (1 << t) - 1
    dp = [[INF]*n for _ in range(1 << t)]
    for i, term in enumerate(targets):
        dp[1 << i][term] = 0

    for mask in range(1 << t):
        # merge subsets
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if other < sub:  # avoid duplicate work
                for v in range(n):
                    if dp[sub][v] + dp[other][v] < dp[mask][v]:
                        dp[mask][v] = dp[sub][v] + dp[other][v]
            sub = (sub - 1) & mask

        # relax via shortest paths
        for v in range(n):
            if dp[mask][v] == INF:
                continue
            for u in range(n):
                if dist[v][u] < INF:
                    nd = dp[mask][v] + dist[v][u]
                    if nd < dp[mask][u]:
                        dp[mask][u] = nd

    ans = min(dp[full_mask])
    print(ans)

if __name__ == "__main__":
    solve()