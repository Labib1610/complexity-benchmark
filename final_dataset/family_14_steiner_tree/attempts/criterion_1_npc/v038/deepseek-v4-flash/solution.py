import sys

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    cores = list(map(int, input().split()))
    core_index = {node: i for i, node in enumerate(cores)}

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

    full_mask = (1 << t) - 1
    dp = [[INF] * n for _ in range(1 << t)]

    for i, node in enumerate(cores):
        dp[1 << i][node] = 0

    for mask in range(1 << t):
        # Combine subsets
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
        for v in range(n):
            if dp[mask][v] == INF:
                continue
            for u in range(n):
                nd = dp[mask][v] + dist[v][u]
                if nd < dp[mask][u]:
                    dp[mask][u] = nd

    ans = min(dp[full_mask])
    print(ans)

if __name__ == "__main__":
    solve()