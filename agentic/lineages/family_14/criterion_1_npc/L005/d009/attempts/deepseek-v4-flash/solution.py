import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    core = [int(next(it)) - 1 for _ in range(t)]

    INF = 10**18
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0

    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        if w < dist[u][v]:
            dist[u][v] = w
            dist[v][u] = w

    # Floyd-Warshall
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

    if t == 1:
        print(0)
        return

    full_mask = (1 << t) - 1
    # dp[mask][v] = min cost to connect terminals in mask, with v in the tree
    dp = [[INF] * n for _ in range(1 << t)]

    for i, node in enumerate(core):
        dp[1 << i][node] = 0

    # DP over subsets
    for mask in range(1, 1 << t):
        # Merge two submasks
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if sub < other:  # avoid double work
                for v in range(n):
                    if dp[sub][v] < INF and dp[other][v] < INF:
                        val = dp[sub][v] + dp[other][v]
                        if val < dp[mask][v]:
                            dp[mask][v] = val
            sub = (sub - 1) & mask

        # Relax edges (shortest path extension)
        # Use a simple Dijkstra-like relaxation since n is small
        # We can just run Floyd-like relaxation for this mask
        for _ in range(n):
            updated = False
            for u in range(n):
                if dp[mask][u] == INF:
                    continue
                du = dp[mask][u]
                for v in range(n):
                    nd = du + dist[u][v]
                    if nd < dp[mask][v]:
                        dp[mask][v] = nd
                        updated = True
            if not updated:
                break

    ans = min(dp[full_mask])
    print(ans)

if __name__ == "__main__":
    solve()