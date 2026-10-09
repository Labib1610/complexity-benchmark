import sys

INF = 10 ** 18

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))

    terminals = [int(next(it)) - 1 for _ in range(t)]

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

    full_mask = (1 << t) - 1
    dp = [[INF] * n for _ in range(1 << t)]

    # base masks – single terminal
    for i, node in enumerate(terminals):
        mask = 1 << i
        row = dp[mask]
        drow = dist[node]
        for v in range(n):
            row[v] = drow[v]

    # iterate over all masks
    for mask in range(1, full_mask + 1):
        # skip singletons (already optimal)
        if mask & (mask - 1):
            # combine two proper sub‑masks
            sub = (mask - 1) & mask
            while sub:
                other = mask ^ sub
                if other:
                    dp_sub = dp[sub]
                    dp_oth = dp[other]
                    dp_cur = dp[mask]
                    for v in range(n):
                        cand = dp_sub[v] + dp_oth[v]
                        if cand < dp_cur[v]:
                            dp_cur[v] = cand
                sub = (sub - 1) & mask

            # relaxation with all‑pairs shortest paths
            cur = dp[mask]
            new = [INF] * n
            for v in range(n):
                best = INF
                # min_u cur[u] + dist[u][v]
                for u in range(n):
                    val = cur[u] + dist[u][v]
                    if val < best:
                        best = val
                new[v] = best
            dp[mask] = new

    ans = min(dp[full_mask])
    print(ans)


if __name__ == "__main__":
    solve()