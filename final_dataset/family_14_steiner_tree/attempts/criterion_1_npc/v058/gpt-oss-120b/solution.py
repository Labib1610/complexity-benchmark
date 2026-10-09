import sys
import math

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

    # initialise singletons
    for idx, term in enumerate(terminals):
        mask = 1 << idx
        drow = dist[term]
        dp[mask] = drow[:]   # copy list

    # iterate over masks
    for mask in range(1, full):
        # skip singletons (already optimal)
        if mask & (mask - 1) == 0:
            continue

        # merge submasks
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            # combine only once per unordered pair
            if sub < other:
                dp_sub = dp[sub]
                dp_other = dp[other]
                for v in range(n):
                    val = dp_sub[v] + dp_other[v]
                    if val < dp[mask][v]:
                        dp[mask][v] = val
            sub = (sub - 1) & mask

        # propagation through shortest paths
        # new_dp[u] = min_v dp[mask][v] + dist[v][u]
        new_row = [INF] * n
        cur = dp[mask]
        for v in range(n):
            cv = cur[v]
            if cv == INF:
                continue
            dv = dist[v]
            for u in range(n):
                nd = cv + dv[u]
                if nd < new_row[u]:
                    new_row[u] = nd
        dp[mask] = new_row

    ans = min(dp[full - 1])
    print(ans)

if __name__ == "__main__":
    solve()