import sys
import math
def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); t = int(next(it))
    terminals = [int(next(it)) - 1 for _ in range(t)]
    INF = 10**18
    # adjacency matrix for Floyd
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
            dj = dist
            for j in range(n):
                nd = ik + dk[j]
                if nd < di[j]:
                    di[j] = nd
    full = (1<<t) - 1
    dp = [[INF]*n for _ in range(1<<t)]
    # init single terminals
    for i, term in enumerate(terminals):
        mask = 1<<i
        for v in range(n):
            dp[mask][v] = dist[term][v]
    # DP over subsets
    for mask in range(1, full+1):
        # skip singletons
        sub = (mask-1) & mask
        while sub:
            other = mask ^ sub
            # combine sub and other
            for v in range(n):
                val = dp[sub][v] + dp[other][v]
                if val < dp[mask][v]:
                    dp[mask][v] = val
            sub = (sub-1) & mask
        # after combine, run relaxation via any node as Steiner point
        # i.e., dp[mask][v] = min_u dp[mask][u] + dist[u][v]
        # This is a shortest path relaxation; we can apply Floyd-like update
        # Since dist is all-pairs, we can just do:
        for u in range(n):
            du = dp[mask][u]
            if du == INF: continue
            drow = dist[u]
            for v in range(n):
                nd = du + drow[v]
                if nd < dp[mask][v]:
                    dp[mask][v] = nd
    ans = min(dp[full])
    print(ans)

if __name__ == "__main__":
    solve()