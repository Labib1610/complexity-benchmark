import sys

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    terminals = list(map(int, input().split()))
    terminals = [x-1 for x in terminals]  # 0-based

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
    dp = [[INF]*n for _ in range(1 << t)]

    for i, term in enumerate(terminals):
        dp[1 << i][term] = 0

    for mask in range(1 << t):
        # Merge subsets
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if sub < other:  # avoid duplicate work
                for v in range(n):
                    dp[mask][v] = min(dp[mask][v], dp[sub][v] + dp[other][v])
            sub = (sub - 1) & mask

        # Relax via shortest paths
        for u in range(n):
            if dp[mask][u] < INF:
                du = dp[mask][u]
                for v in range(n):
                    nd = du + dist[u][v]
                    if nd < dp[mask][v]:
                        dp[mask][v] = nd

    ans = min(dp[full_mask])
    print(ans)

if __name__ == "__main__":
    solve()