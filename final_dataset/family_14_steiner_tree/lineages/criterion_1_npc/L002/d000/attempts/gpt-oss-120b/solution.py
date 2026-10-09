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
    INF = 10**15
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

    full_mask = (1 << t) - 1
    # dp[mask][v]
    dp = [[INF] * n for _ in range(1 << t)]
    # init single terminals
    for idx, term in enumerate(terminals):
        mask = 1 << idx
        for v in range(n):
            dp[mask][v] = dist[term][v]

    # iterate over masks
    for mask in range(1, 1 << t):
        # skip singletons (already init)
        if mask & (mask - 1):
            # combine submasks
            sub = (mask - 1) & mask
            while sub:
                other = mask ^ sub
                # to avoid duplicate work, ensure sub < other (optional)
                for v in range(n):
                    val = dp[sub][v] + dp[other][v]
                    if val < dp[mask][v]:
                        dp[mask][v] = val
                sub = (sub - 1) & mask
        # after combination, improve via moving root using distances
        # classic Steiner DP relaxation: dp[mask][v] = min_u dp[mask][u] + dist[u][v]
        # we can run a simple Dijkstra-like relaxation using Floyd distances:
        # Since we have all-pairs shortest paths, we can just take min over u.
        for v in range(n):
            best = dp[mask][v]
            for u in range(n):
                cand = dp[mask][u] + dist[u][v]
                if cand < best:
                    best = cand
            dp[mask][v] = best

    answer = min(dp[full_mask])
    print(answer)

if __name__ == "__main__":
    solve()