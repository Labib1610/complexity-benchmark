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
    anchors = [int(next(it)) - 1 for _ in range(t)]
    
    # adjacency list
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    if t <= 1:
        print(0)
        return
    
    # Dijkstra from each anchor to get pairwise distances
    INF = 10**18
    dist_anchors = [[INF] * t for _ in range(t)]
    
    for i, src in enumerate(anchors):
        dist = [INF] * n
        dist[src] = 0
        pq = [(0, src)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, w in graph[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))
        for j, anchor in enumerate(anchors):
            dist_anchors[i][j] = dist[anchor]
    
    # Prim's algorithm on anchor nodes
    visited = [False] * t
    min_cost = [INF] * t
    min_cost[0] = 0
    total = 0
    
    for _ in range(t):
        u = -1
        best = INF
        for i in range(t):
            if not visited[i] and min_cost[i] < best:
                best = min_cost[i]
                u = i
        visited[u] = True
        total += best
        for v in range(t):
            if not visited[v] and dist_anchors[u][v] < min_cost[v]:
                min_cost[v] = dist_anchors[u][v]
    
    print(total)

if __name__ == "__main__":
    solve()