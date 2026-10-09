import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    mandatory = [int(next(it)) - 1 for _ in range(t)]

    INF = 10**18
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0

    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
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

    # DP over subsets of mandatory nodes
    full_mask = (1 << t) - 1
    dp = [[INF] * n for _ in range(1 << t)]

    for i in range(t):
        dp[1 << i][mandatory[i]] = 0

    for mask in range(1 << t):
        # Combine submasks
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if sub < other:  # avoid double work
                for i in range(n):
                    if dp[sub][i] == INF:
                        continue
                    for j in range(n):
                        if dp[other][j] == INF:
                            continue
                        nd = dp[sub][i] + dp[other][j] + dist[i][j]
                        if nd < dp[mask][i]:
                            dp[mask][i] = nd
                        if nd < dp[mask][j]:
                            dp[mask][j] = nd
            sub = (sub - 1) & mask

        # Relax via shortest paths
        for i in range(n):
            if dp[mask][i] == INF:
                continue
            for j in range(n):
                nd = dp[mask][i] + dist[i][j]
                if nd < dp[mask][j]:
                    dp[mask][j] = nd

    ans = min(dp[full_mask])
    print(ans)

if __name__ == "__main__":
    solve()