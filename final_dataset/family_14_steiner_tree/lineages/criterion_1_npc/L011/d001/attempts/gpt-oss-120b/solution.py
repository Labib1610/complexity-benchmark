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

    INF = 10**18
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

    # base masks
    for idx, term in enumerate(terminals):
        mask = 1 << idx
        drow = dist[term]
        dp_mask = dp[mask]
        for v in range(n):
            dp_mask[v] = drow[v]

    # DP over subsets
    for mask in range(1, full):
        # skip singletons (already initialized)
        if mask & (mask - 1):
            dp_mask = dp[mask]
            sub = (mask - 1) & mask
            while sub:
                other = mask ^ sub
                # to avoid duplicate work we can enforce sub < other, but not necessary
                dp_sub = dp[sub]
                dp_other = dp[other]
                for v in range(n):
                    cand = dp_sub[v] + dp_other[v]
                    if cand < dp_mask[v]:
                        dp_mask[v] = cand
                sub = (sub - 1) & mask

        # relaxation using all‑pairs shortest paths
        dp_mask = dp[mask]
        # compute min_u (dp[mask][u] + dist[u][v]) for each v
        # naive O(n^2) is fine (n ≤ 100)
        new = [INF] * n
        for u in range(n):
            du = dp_mask[u]
            if du == INF:
                continue
            drow = dist[u]
            for v in range(n):
                cand = du + drow[v]
                if cand < new[v]:
                    new[v] = cand
        dp[mask] = new

    ans = min(dp[full - 1])
    print(ans)

if __name__ == "__main__":
    solve()