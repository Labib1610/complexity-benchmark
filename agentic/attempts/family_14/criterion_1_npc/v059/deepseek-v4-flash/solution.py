import sys

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    terminals = list(map(int, input().split()))
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

    # Map terminals to indices
    term_idx = [x - 1 for x in terminals]
    full_mask = (1 << t) - 1

    # dp[mask][v]
    dp = [[INF] * n for _ in range(1 << t)]
    for i in range(t):
        dp[1 << i][term_idx[i]] = 0

    for mask in range(1 << t):
        # Combine subsets
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if sub < other:  # avoid double work
                for v in range(n):
                    if dp[sub][v] + dp[other][v] < dp[mask][v]:
                        dp[mask][v] = dp[sub][v] + dp[other][v]
            sub = (sub - 1) & mask

        # Relax via shortest paths
        for v in range(n):
            dv = dp[mask][v]
            if dv == INF:
                continue
            for u in range(n):
                nd = dv + dist[v][u]
                if nd < dp[mask][u]:
                    dp[mask][u] = nd

    ans = min(dp[full_mask])
    print(ans)

if __name__ == "__main__":
    solve()