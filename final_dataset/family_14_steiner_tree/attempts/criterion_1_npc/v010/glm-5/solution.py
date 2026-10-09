import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    primary = [int(next(it)) for _ in range(t)]
    primary_set = set(primary)
    
    INF = 10**18
    dist = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dist[i][i] = 0
    
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        if w < dist[u][v]:
            dist[u][v] = w
            dist[v][u] = w
    
    # Floyd-Warshall
    for k in range(1, n + 1):
        dk = dist[k]
        for i in range(1, n + 1):
            dik = dist[i][k]
            if dik == INF:
                continue
            di = dist[i]
            for j in range(1, n + 1):
                nd = dik + dk[j]
                if nd < di[j]:
                    di[j] = nd
    
    if t <= 1:
        print(0)
        return
    
    # Prim's algorithm on primary facilities using shortest path distances
    in_mst = [False] * (n + 1)
    min_edge = [INF] * (n + 1)
    start = primary[0]
    min_edge[start] = 0
    total = 0
    
    for _ in range(t):
        # find the primary facility not in MST with smallest min_edge
        u = -1
        best = INF
        for p in primary:
            if not in_mst[p] and min_edge[p] < best:
                best = min_edge[p]
                u = p
        if u == -1:
            break
        in_mst[u] = True
        total += best
        for p in primary:
            if not in_mst[p] and dist[u][p] < min_edge[p]:
                min_edge[p] = dist[u][p]
    
    print(total)

solve()