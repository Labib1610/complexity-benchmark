import sys
import heapq

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))

    terminals = [int(next(it)) - 1 for _ in range(t)]

    INF = 10**18

    # adjacency with min edge weight
    adj = [dict() for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        if v not in adj[u] or adj[u][v] > w:
            adj[u][v] = w
        if u not in adj[v] or adj[v][u] > w:
            adj[v][u] = w

    # all-pairs shortest paths
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for u in range(n):
        for v, w in adj[u].items():
            dist[u][v] = w

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

    full = (1 << t) - 1

    # dp[mask][v] = minimum cost to connect terminals in mask with v as a Steiner root
    dp = [[INF] * n for _ in range(1 << t)]

    for i, node in enumerate(terminals):
        dp[1 << i][node] = 0

    for mask in range(1, full + 1):
        # split the mask
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if sub < other:
                dp_mask = dp[mask]
                dp_sub = dp[sub]
                dp_oth = dp[other]
                for v in range(n):
                    val = dp_sub[v] + dp_oth[v]
                    if val < dp_mask[v]:
                        dp_mask[v] = val
            sub = (sub - 1) & mask

        # shortest-path closure: move along any graph edges
        dp_mask = dp[mask]
        for v in range(n):
            best = dp_mask[v]
            for u in range(n):
                cand = dp_mask[u] + dist[u][v]
                if cand < best:
                    best = cand
            dp_mask[v] = best

    ans = min(dp[full][node] for node in terminals)
    print(ans)

if __name__ == "__main__":
    solve()