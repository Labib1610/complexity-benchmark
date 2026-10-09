import sys
import heapq

input = sys.stdin.readline

def solve():
    n, m, t = map(int, input().split())
    core = list(map(int, input().split()))
    core_set = set(core)
    
    # Build graph
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    if t <= 1:
        print(0)
        return
    
    # Dijkstra from each core node to get distances to all other core nodes
    core_index = {node: i for i, node in enumerate(core)}
    dist_matrix = [[float('inf')] * t for _ in range(t)]
    
    for i, start in enumerate(core):
        dist = [float('inf')] * (n + 1)
        dist[start] = 0
        pq = [(0, start)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, w in graph[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))
        for j, node in enumerate(core):
            dist_matrix[i][j] = dist[node]
    
    # Prim's algorithm on core nodes
    visited = [False] * t
    min_cost = [float('inf')] * t
    min_cost[0] = 0
    total = 0
    
    for _ in range(t):
        u = -1
        best = float('inf')
        for i in range(t):
            if not visited[i] and min_cost[i] < best:
                best = min_cost[i]
                u = i
        visited[u] = True
        total += best
        for v in range(t):
            if not visited[v] and dist_matrix[u][v] < min_cost[v]:
                min_cost[v] = dist_matrix[u][v]
    
    print(total)

if __name__ == "__main__":
    solve()