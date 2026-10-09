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

    INF = 10**15
    # all‑pairs distances
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

    # base masks: single terminal
    for i, term in enumerate(terminals):
        mask = 1 << i
        dterm = dist[term]
        row = dp[mask]
        for v in range(n):
            row[v] = dterm[v]

    # DP over subsets
    for mask in range(1, full):
        # skip singletons (already optimal)
        if mask & (mask - 1):
            # combine two non‑empty proper submasks
            sub = (mask - 1) & mask
            while sub:
                other = mask ^ sub
                # to avoid duplicate work we can enforce sub < other
                if sub < other:
                    dp_sub = dp[sub]
                    dp_other = dp[other]
                    row = dp[mask]
                    for v in range(n):
                        val = dp_sub[v] + dp_other[v]
                        if val < row[v]:
                            row[v] = val
                sub = (sub - 1) & mask

        # relaxation via all‑pairs distances
        newrow = [INF] * n
        cur = dp[mask]
        for u in range(n):
            du = cur[u]
            if du == INF:
                continue
            du_row = dist[u]
            for v in range(n):
                nd = du + du_row[v]
                if nd < newrow[v]:
                    newrow[v] = nd
        dp[mask] = newrow

    ans = min(dp[full - 1])
    print(ans)


if __name__ == "__main__":
    solve()