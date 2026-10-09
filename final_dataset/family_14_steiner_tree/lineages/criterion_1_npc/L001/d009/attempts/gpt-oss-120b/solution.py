import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    targets = [int(next(it)) - 1 for _ in range(t)]

    INF = 10**18
    # Floyd-Warshall distances
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        if w < dist[u][v]:
            dist[u][v] = dist[v][u] = w

    # Floyd
    for k in range(n):
        dk = dist[k]
        for i in range(n):
            di = dist[i]
            ik = di[k]
            if ik == INF:
                continue
            for j in range(n):
                nd = ik + dk[j]
                if nd < di[j]:
                    di[j] = nd

    full = 1 << t
    dp = [[INF] * n for _ in range(full)]

    # base masks
    for i, c in enumerate(targets):
        mask = 1 << i
        for v in range(n):
            dp[mask][v] = dist[c][v]

    # DP over subsets
    for mask in range(1, full):
        # skip singletons
        if mask & (mask - 1):
            # combine submasks
            sub = (mask - 1) & mask
            while sub:
                other = mask ^ sub
                if other:
                    for v in range(n):
                        val = dp[sub][v] + dp[other][v]
                        if val < dp[mask][v]:
                            dp[mask][v] = val
                sub = (sub - 1) & mask
        # relaxation via moving root using shortest paths
        # dp[mask][v] = min_u dp[mask][u] + dist[u][v]
        # we can do a simple O(n^2) update
        for u in range(n):
            du = dp[mask][u]
            if du == INF:
                continue
            for v in range(n):
                nd = du + dist[u][v]
                if nd < dp[mask][v]:
                    dp[mask][v] = nd

    ans = min(dp[full - 1])
    print(ans)

if __name__ == "__main__":
    solve()