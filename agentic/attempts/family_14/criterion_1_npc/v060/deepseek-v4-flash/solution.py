import sys
import heapq

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    
    vital = [int(next(it)) - 1 for _ in range(t)]
    
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
    
    # Floyd-Warshall for all-pairs shortest paths
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
    
    # Build complete graph among vital nodes
    vital_count = t
    vital_dist = [[0] * vital_count for _ in range(vital_count)]
    for i in range(vital_count):
        for j in range(vital_count):
            vital_dist[i][j] = dist[vital[i]][vital[j]]
    
    # Prim's algorithm for MST on vital nodes
    visited = [False] * vital_count
    min_edge = [INF] * vital_count
    min_edge[0] = 0
    total = 0
    
    for _ in range(vital_count):
        u = -1
        best = INF
        for i in range(vital_count):
            if not visited[i] and min_edge[i] < best:
                best = min_edge[i]
                u = i
        if u == -1:
            break
        visited[u] = True
        total += best
        for v in range(vital_count):
            if not visited[v] and vital_dist[u][v] < min_edge[v]:
                min_edge[v] = vital_dist[u][v]
    
    print(total)

if __name__ == "__main__":
    solve()