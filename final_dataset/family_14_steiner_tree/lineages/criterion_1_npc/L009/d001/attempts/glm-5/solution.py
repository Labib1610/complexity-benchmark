import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    t = int(data[idx]); idx += 1
    hubs = [int(data[idx + i]) - 1 for i in range(t)]
    idx += t

    INF = float('inf')
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0

    for _ in range(m):
        u = int(data[idx]) - 1; idx += 1
        v = int(data[idx]) - 1; idx += 1
        w = int(data[idx]); idx += 1
        if w < dist[u][v]:
            dist[u][v] = w
            dist[v][u] = w

    # Floyd-Warshall
    for k in range(n):
        dk = dist[k]
        for i in range(n):
            di = dist[i]
            dik = di[k]
            if dik == INF:
                continue
            for j in range(n):
                nd = dik + dk[j]
                if nd < di[j]:
                    di[j] = nd

    if t <= 1:
        print(0)
        return

    # Prim's MST on the t hubs using all-pairs shortest paths
    in_mst = [False] * t
    min_edge = [INF] * t
    min_edge[0] = 0
    total = 0

    for _ in range(t):
        u = -1
        best = INF
        for i in range(t):
            if not in_mst[i] and min_edge[i] < best:
                best = min_edge[i]
                u = i
        in_mst[u] = True
        total += best
        for v in range(t):
            if not in_mst[v]:
                d = dist[hubs[u]][hubs[v]]
                if d < min_edge[v]:
                    min_edge[v] = d

    print(total)

solve()