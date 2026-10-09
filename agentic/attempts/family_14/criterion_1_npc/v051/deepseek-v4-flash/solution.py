import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    
    terminals = [int(next(it)) - 1 for _ in range(t)]
    
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
    
    # Build complete graph among terminals
    tdist = [[0] * t for _ in range(t)]
    for i in range(t):
        for j in range(t):
            tdist[i][j] = dist[terminals[i]][terminals[j]]
    
    # Prim's algorithm for MST on terminals
    visited = [False] * t
    min_edge = [INF] * t
    min_edge[0] = 0
    total_cost = 0
    
    for _ in range(t):
        u = -1
        best = INF
        for i in range(t):
            if not visited[i] and min_edge[i] < best:
                best = min_edge[i]
                u = i
        visited[u] = True
        total_cost += best
        for v in range(t):
            if not visited[v] and tdist[u][v] < min_edge[v]:
                min_edge[v] = tdist[u][v]
    
    print(total_cost)

if __name__ == "__main__":
    main()