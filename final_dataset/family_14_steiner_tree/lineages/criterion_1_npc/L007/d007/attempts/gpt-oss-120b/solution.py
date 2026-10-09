import sys
def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); t = int(next(it))
    key = [int(next(it)) - 1 for _ in range(t)]
    INF = 10**18
    # adjacency matrix for Floyd-Warshall
    dist = [[INF]*n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for _ in range(m):
        u = int(next(it))-1
        v = int(next(it))-1
        w = int(next(it))
        if w < dist[u][v]:
            dist[u][v] = dist[v][u] = w
    # Floyd-Warshall
    for k in range(n):
        dk = dist[k]
        for i in range(n):
            di = dist[i]
            ik = di[k]
            if ik == INF: continue
            for j in range(n):
                nd = ik + dk[j]
                if nd < di[j]:
                    di[j] = nd
    if t <= 1:
        print(0)
        return
    full = (1<<t) - 1
    dp = [[INF]*n for _ in range(1<<t)]
    # init single terminals
    for i, node in enumerate(key):
        mask = 1<<i
        for v in range(n):
            dp[mask][v] = dist[node][v]
    # DP over subsets
    for mask in range(1, full+1):
        # skip singletons
        sub = (mask-1) & mask
        while sub:
            other = mask ^ sub
            # combine at same root v
            for v in range(n):
                val = dp[sub][v] + dp[other][v]
                if val < dp[mask][v]:
                    dp[mask][v] = val
            sub = (sub-1) & mask
        # relaxation via shortest paths
        # dp[mask][j] = min_i dp[mask][i] + dist[i][j]
        # simple O(n^2)
        improved = True
        # one pass is enough because dist is already shortest
        for i in range(n):
            di = dp[mask][i]
            if di == INF: continue
            row = dist[i]
            for j in range(n):
                nd = di + row[j]
                if nd < dp[mask][j]:
                    dp[mask][j] = nd
    ans = min(dp[full])
    print(ans)

if __name__ == "__main__":
    solve()