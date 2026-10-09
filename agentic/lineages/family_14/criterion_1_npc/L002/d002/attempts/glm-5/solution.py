import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    anchors = [int(next(it)) for _ in range(t)]
    
    INF = float('inf')
    dist = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dist[i][i] = 0
    
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        if w < dist[u][v]:
            dist[u][v] = w
            dist[v][u] = w
    
    for k in range(1, n + 1):
        dk = dist[k]
        for i in range(1, n + 1):
            di = dist[i]
            dik = di[k]
            if dik == INF:
                continue
            for j in range(1, n + 1):
                nd = dik + dk[j]
                if nd < di[j]:
                    di[j] = nd
    
    if t <= 1:
        print(0)
        return
    
    # Prim's algorithm on anchors using metric closure
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
                d = dist[anchors[u]][anchors[v]]
                if d < min_edge[v]:
                    min_edge[v] = d
    
    print(total)

solve()