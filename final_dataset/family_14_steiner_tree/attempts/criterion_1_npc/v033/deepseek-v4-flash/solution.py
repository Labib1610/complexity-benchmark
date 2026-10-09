import sys

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    cores = list(map(int, input().split()))
    core_set = set(cores)

    INF = 10**18
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0

    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
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

    # Map core nodes to indices 0..t-1
    core_idx = {node: i for i, node in enumerate(cores)}

    full_mask = (1 << t) - 1
    # dp[mask][v] = min cost to connect core set 'mask' and end at node v
    dp = [[INF] * n for _ in range(1 << t)]

    # Initialize: single core endpoints
    for i, node in enumerate(cores):
        dp[1 << i][node] = 0

    # DP over masks
    for mask in range(1 << t):
        # Combine subsets
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if sub < other:  # avoid double work
                for v in range(n):
                    best = INF
                    for u in range(n):
                        val = dp[sub][u] + dist[u][v] + dp[other][v]
                        if val < best:
                            best = val
                    if best < dp[mask][v]:
                        dp[mask][v] = best
            sub = (sub - 1) & mask

        # Relax within the same mask using shortest paths
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