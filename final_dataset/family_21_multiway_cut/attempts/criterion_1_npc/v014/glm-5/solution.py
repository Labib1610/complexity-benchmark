import sys

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    k = int(data[idx]); idx += 1
    B = int(data[idx]); idx += 1

    zones = [int(data[idx + i]) for i in range(k)]
    idx += k

    edges = []
    for _ in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        w = int(data[idx]); idx += 1
        edges.append((u, v, w))

    if k <= 1:
        print("YES")
        print(0)
        return

    INF = float('inf')
    dist = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dist[i][i] = 0
    for u, v, w in edges:
        if w < dist[u][v]:
            dist[u][v] = w
            dist[v][u] = w

    for t in range(1, n + 1):
        for i in range(1, n + 1):
            if dist[i][t] == INF:
                continue
            for j in range(1, n + 1):
                nd = dist[i][t] + dist[t][j]
                if nd < dist[i][j]:
                    dist[i][j] = nd

    K = k
    dp = [[INF] * K for _ in range(1 << K)]
    parent = [[-1] * K for _ in range(1 << K)]

    for i in range(K):
        dp[1 << i][i] = 0

    for mask in range(1 << K):
        for i in range(K):
            if not (mask & (1 << i)):
                continue
            if dp[mask][i] == INF:
                continue
            for j in range(K):
                if mask & (1 << j):
                    continue
                nmask = mask | (1 << j)
                nd = dp[mask][i] + dist[zones[i]][zones[j]]
                if nd < dp[nmask][j]:
                    dp[nmask][j] = nd
                    parent[nmask][j] = i

    full = (1 << K) - 1
    best = INF
    best_last = -1
    for i in range(K):
        if dp[full][i] < best:
            best = dp[full][i]
            best_last = i

    if best > B:
        print("NO")
        return

    order = []
    mask = full
    last = best_last
    while last != -1:
        order.append(last)
        p = parent[mask][last]
        mask ^= (1 << last)
        last = p
    order.reverse()

    blocked = set()
    for a in range(len(order) - 1):
        za = zones[order[a]]
        zb = zones[order[a + 1]]
        cur = za
        while cur != zb:
            best_nxt = -1
            best_w = INF
            for u, v, w in edges:
                if u == cur and dist[v][zb] + w == dist[cur][zb]:
                    if w < best_w:
                        best_w = w
                        best_nxt = v
                elif v == cur and dist[u][zb] + w == dist[cur][zb]:
                    if w < best_w:
                        best_w = w
                        best_nxt = u
            blocked.add((cur, best_nxt))
            cur = best_nxt

    print("YES")
    print(len(blocked))
    for u, v in blocked:
        print(u, v)

solve()