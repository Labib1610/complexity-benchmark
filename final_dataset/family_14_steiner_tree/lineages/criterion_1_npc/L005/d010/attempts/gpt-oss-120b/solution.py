import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    crit = [int(next(it)) - 1 for _ in range(t)]
    INF = 10**15
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        if w < dist[u][v]:
            dist[u][v] = dist[v][u] = w
    # Floyd-Warshall
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

    if t <= 1:
        print(0)
        return

    T = t
    full = (1 << T) - 1
    dp = [[INF] * n for _ in range(1 << T)]

    # base masks
    for idx, node in enumerate(crit):
        mask = 1 << idx
        for v in range(n):
            dp[mask][v] = dist[node][v]

    # DP over subsets
    for mask in range(1, full + 1):
        # combine submasks
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
        # propagate through graph using all-pairs distances
        # dp[mask][u] = min_v dp[mask][v] + dist[v][u]
        # O(n^2)
        new = dp[mask][:]
        for u in range(n):
            best = new[u]
            for v in range(n):
                cand = dp[mask][v] + dist[v][u]
                if cand < best:
                    best = cand
            new[u] = best
        dp[mask] = new

    answer = min(dp[full])
    print(answer)

if __name__ == "__main__":
    solve()