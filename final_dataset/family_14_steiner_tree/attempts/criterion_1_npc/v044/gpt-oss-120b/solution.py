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
    full = 1 << t
    dp = [[INF] * n for _ in range(full)]
    # init singletons
    for i, node in enumerate(cores):
        mask = 1 << i
        drow = dist[node]
        dp_mask = dp[mask]
        for v in range(n):
            dp_mask[v] = drow[v]
    # DP over subsets
    for mask in range(1, full):
        # skip singletons (already optimal)
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if other:
                dp_sub = dp[sub]
                dp_other = dp[other]
                dp_mask = dp[mask]
                for v in range(n):
                    val = dp_sub[v] + dp_other[v]
                    if val < dp_mask[v]:
                        dp_mask[v] = val
            sub = (sub - 1) & mask
        # closure with shortest paths
        dp_mask = dp[mask]
        # we can apply Floyd-like relaxation: dp_mask[v] = min_u dp_mask[u] + dist[u][v]
        # O(n^2)
        for u in range(n):
            du = dp_mask[u]
            if du == INF:
                continue
            drow = dist[u]
            for v in range(n):
                nd = du + drow[v]
                if nd < dp_mask[v]:
                    dp_mask[v] = nd
    ans = min(dp[full - 1])
    print(ans)

if __name__ == "__main__":
    solve()