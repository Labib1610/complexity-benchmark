import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); t = int(next(it))
    terminals = [int(next(it)) - 1 for _ in range(t)]
    INF = 10**18
    # adjacency matrix for Floyd-Warshall
    dist = [[INF]*n for _ in range(n)]
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
            if ik == INF: continue
            for j in range(n):
                nd = ik + dk[j]
                if nd < di[j]:
                    di[j] = nd
    if t == 1:
        print(0)
        return
    full = (1 << t) - 1
    # DP[mask][v]
    DP = [[INF]*n for _ in range(full+1)]
    # init singletons
    for idx, term in enumerate(terminals):
        mask = 1 << idx
        for v in range(n):
            DP[mask][v] = dist[term][v]
    # iterate masks
    for mask in range(1, full+1):
        # skip singletons
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            # combine only when both non-zero
            if other:
                dp_sub = DP[sub]
                dp_other = DP[other]
                dp_mask = DP[mask]
                for v in range(n):
                    val = dp_sub[v] + dp_other[v]
                    if val < dp_mask[v]:
                        dp_mask[v] = val
            sub = (sub - 1) & mask
        # after combine, propagate through shortest paths
        # DP2[u] = min_v DP[mask][v] + dist[v][u]
        dp_mask = DP[mask]
        new = dp_mask[:]  # copy to update
        for v in range(n):
            dv = dp_mask[v]
            if dv == INF:
                continue
            drow = dist[v]
            for u in range(n):
                nd = dv + drow[u]
                if nd < new[u]:
                    new[u] = nd
        DP[mask] = new
    ans = min(DP[full])
    print(ans)

if __name__ == "__main__":
    solve()