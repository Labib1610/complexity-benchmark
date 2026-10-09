import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    primary = [int(next(it)) - 1 for _ in range(t)]

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

    # Floyd–Warshall
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

    # DP over subsets of primary forks
    size = 1 << t
    dp = [[INF] * n for _ in range(size)]
    for i in range(t):
        dp[1 << i][primary[i]] = 0

    for mask in range(size):
        # Combine subsets
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if sub < other:  # avoid double work
                for v in range(n):
                    if dp[sub][v] == INF:
                        continue
                    for u in range(n):
                        if dp[other][u] == INF:
                            continue
                        val = dp[sub][v] + dp[other][u] + dist[v][u]
                        if val < dp[mask][v]:
                            dp[mask][v] = val
                        if val < dp[mask][u]:
                            dp[mask][u] = val
            sub = (sub - 1) & mask

        # Relax shortest paths for this mask
        for v in range(n):
            if dp[mask][v] == INF:
                continue
            for u in range(n):
                if dist[v][u] == INF:
                    continue
                nd = dp[mask][v] + dist[v][u]
                if nd < dp[mask][u]:
                    dp[mask][u] = nd

    ans = min(dp[(1 << t) - 1][v] for v in range(n))
    print(ans)

if __name__ == "__main__":
    solve()