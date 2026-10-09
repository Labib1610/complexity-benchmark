import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))

    terminals = [int(next(it)) - 1 for _ in range(t)]

    INF = 10 ** 18
    # distance matrix
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0

    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        if w < dist[u][v]:
            dist[u][v] = dist[v][u] = w

    # Floyd‑Warshall
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

    full = 1 << t
    dp = [[INF] * n for _ in range(full)]

    for idx, node in enumerate(terminals):
        dp[1 << idx][node] = 0

    # DP over masks
    for mask in range(1, full):
        # combine two proper sub‑masks
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            # both sub and other are non‑empty
            dps = dp[sub]
            dpo = dp[other]
            dpm = dp[mask]
            for v in range(n):
                val = dps[v] + dpo[v]
                if val < dpm[v]:
                    dpm[v] = val
            sub = (sub - 1) & mask

        # relaxation with all‑pairs shortest paths
        dpm = dp[mask]
        # new values after relaxation
        new = [INF] * n
        for v in range(n):
            best = dpm[v]          # staying at v
            for u in range(n):
                nd = dpm[u] + dist[u][v]
                if nd < best:
                    best = nd
            new[v] = best
        dp[mask] = new

    answer = min(dp[full - 1])
    print(answer)


if __name__ == "__main__":
    solve()