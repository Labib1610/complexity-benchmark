import sys
import heapq

def main():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    
    core = [int(next(it)) - 1 for _ in range(t)]
    
    # Initialize adjacency matrix with infinity
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
    
    # Floyd-Warshall to get all-pairs shortest paths
    for k in range(n):
        for i in range(n):
            if dist[i][k] == INF:
                continue
            for j in range(n):
                if dist[k][j] == INF:
                    continue
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    # Build MST on core sites
    core_set = set(core)
    visited = [False] * n
    min_edge = [INF] * n
    start = core[0]
    min_edge[start] = 0
    total_cost = 0
    
    for _ in range(t):
        u = -1
        best = INF
        for c in core:
            if not visited[c] and min_edge[c] < best:
                best = min_edge[c]
                u = c
        visited[u] = True
        total_cost += best
        for v in core:
            if not visited[v] and dist[u][v] < min_edge[v]:
                min_edge[v] = dist[u][v]
    
    print(total_cost)

if __name__ == "__main__":
    main()