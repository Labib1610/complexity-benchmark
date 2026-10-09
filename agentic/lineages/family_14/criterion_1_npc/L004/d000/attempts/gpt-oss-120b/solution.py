import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    cores = [int(next(it)) - 1 for _ in range(t)]
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
    # Floyd‑Warshall to get shortest paths using any relays
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
    # init single core subsets
    for idx, v in enumerate(cores):
        dp[1 << idx][v] = 0
    # DP over subsets
    for mask in range(1, full_mask + 1):
        # combine two non‑empty proper submasks
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            # only need each partition once
            if sub < other:
                for v in range(n):
                    val = dp[sub][v] + dp[other][v]
                    if val < dp[mask][v]:
                        dp[mask][v] = val
            sub = (sub - 1) & mask
        # propagate through shortest paths: end at any node u can move to v paying dist[u][v]
        # This is a relaxation similar to Dijkstra but with all‑pairs distances we can just
        # take min over u.
        best = dp[mask]
        # compute new best using distances
        new_best = best[:]  # copy
        for v in range(n):
            bv = best[v]
            if bv == INF:
                continue
            dv = dist[v]
            for u in range(n):
                nd = bv + dv[u]
                if nd < new_best[u]:
                    new_best[u] = nd
        dp[mask] = new_best
    answer = min(dp[full_mask])
    print(answer)

if __name__ == "__main__":
    solve()