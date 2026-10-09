import sys

INF = 10 ** 15

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))

    terminals = [int(next(it)) - 1 for _ in range(t)]

    # ---------- all‑pairs shortest paths ----------
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
            row_i = dist[i]
            nd = dik
            for j in range(n):
                val = nd + dk[j]
                if val < row_i[j]:
                    row_i[j] = val

    # ---------- DP ----------
    size = 1 << t
    dp = [[INF] * n for _ in range(size)]

    # single terminal masks
    for i, term in enumerate(terminals):
        dp[1 << i][term] = 0

    # process all masks
    for mask in range(1, size):
        # combine two proper sub‑masks
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            # both sub and other are non‑empty and smaller than mask
            dp_sub = dp[sub]
            dp_other = dp[other]
            dp_mask = dp[mask]
            for v in range(n):
                cand = dp_sub[v] + dp_other[v]
                if cand < dp_mask[v]:
                    dp_mask[v] = cand
            sub = (sub - 1) & mask

        # propagate through the graph (use pre‑computed shortest paths)
        cur = dp[mask]
        new = [INF] * n
        for u in range(n):
            du = cur[u]
            if du == INF:
                continue
            row = dist[u]
            nd = du
            for v in range(n):
                val = nd + row[v]
                if val < new[v]:
                    new[v] = val
        dp[mask] = new

    full = size - 1
    answer = min(dp[full])
    print(answer)


if __name__ == "__main__":
    solve()