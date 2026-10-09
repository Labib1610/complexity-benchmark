import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    t = int(data[idx]); idx += 1
    centers = [int(data[idx+i]) for i in range(t)]
    idx += t
    edges = []
    for _ in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        w = int(data[idx]); idx += 1
        edges.append((u, v, w))
    
    if t <= 1:
        print(0)
        return
    
    INF = float('inf')
    dist = [[INF] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        dist[i][i] = 0
    for u, v, w in edges:
        if w < dist[u][v]:
            dist[u][v] = w
            dist[v][u] = w
    for k in range(1, n+1):
        dk = dist[k]
        for i in range(1, n+1):
            dik = dist[i][k]
            if dik == INF:
                continue
            di = dist[i]
            for j in range(1, n+1):
                nd = dik + dk[j]
                if nd < di[j]:
                    di[j] = nd
    
    best = INF
    for k in range(1, n+1):
        s = 0
        ok = True
        for c in centers:
            if dist[c][k] == INF:
                ok = False
                break
            s += dist[c][k]
        if ok and s < best:
            best = s
    print(best)

solve()