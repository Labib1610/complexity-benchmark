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
    for i, v in enumerate(terminals):
        dp[1 << i][v] = 0

    # iterate masks
    for mask in range(1, full):
        # merging submasks
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            # only need each unordered pair once; enforce sub < other to cut work
            if sub < other:
                dp_sub = dp[sub]
                dp_other = dp[other]
                dp_mask = dp[mask]
                for v in range(n):
                    val = dp_sub[v] + dp_other[v]
                    if val < dp_mask[v]:
                        dp_mask[v] = val
            sub = (sub - 1) & mask

        # shortest‑path relaxation: dp[mask][w] = min_v dp[mask][v] + dist[v][w]
        dp_mask = dp[mask]
        # we can compute new array then assign
        new = dp_mask[:]  # copy current values
        for v in range(n):
            dv = dp_mask[v]
            if dv == INF:
                continue
            drow = dist[v]
            for w in range(n):
                nd = dv + drow[w]
                if nd < new[w]:
                    new[w] = nd
        dp[mask] = new

    ans = min(dp[full - 1])
    print(ans)

if __name__ == "__main__":
    solve()