import sys

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    critical = list(map(int, input().split()))
    critical = [x-1 for x in critical]  # 0-based

    INF = 10**18
    dist = [[INF]*n for _ in range(n)]
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

    k = t
    full_mask = (1 << k) - 1

    # dp[mask][i] = min cost to connect critical nodes in mask, ending at node i
    dp = [[INF]*n for _ in range(1 << k)]

    for idx, c in enumerate(critical):
        dp[1 << idx][c] = 0

    # First, extend within same mask
    for mask in range(1 << k):
        # Relax edges for this mask
        for _ in range(n):
            changed = False
            for i in range(n):
                if dp[mask][i] == INF:
                    continue
                di = dp[mask][i]
                for j in range(n):
                    nd = di + dist[i][j]
                    if nd < dp[mask][j]:
                        dp[mask][j] = nd
                        changed = True
            if not changed:
                break

    # Combine masks
    for mask in range(1 << k):
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if sub < other:  # avoid duplicate work
                for i in range(n):
                    if dp[sub][i] < INF and dp[other][i] < INF:
                        val = dp[sub][i] + dp[other][i]
                        if val < dp[mask][i]:
                            dp[mask][i] = val
            sub = (sub - 1) & mask

        # After merging, relax again
        for _ in range(n):
            changed = False
            for i in range(n):
                if dp[mask][i] == INF:
                    continue
                di = dp[mask][i]
                for j in range(n):
                    nd = di + dist[i][j]
                    if nd < dp[mask][j]:
                        dp[mask][j] = nd
                        changed = True
            if not changed:
                break

    ans = min(dp[full_mask])
    print(ans)

if __name__ == "__main__":
    solve()