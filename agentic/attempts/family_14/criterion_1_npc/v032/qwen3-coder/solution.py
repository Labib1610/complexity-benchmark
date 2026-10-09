import sys
import heapq
from itertools import combinations

def dijkstra(graph, start, n):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    
    return dist

def solve():
    n, m, t = map(int, sys.stdin.readline().split())
    critical = list(map(int, sys.stdin.readline().split()))
    
    if t <= 1:
        print(0)
        return
    
    graph = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # Compute shortest paths between all pairs of critical modules
    distances = {}
    for c in critical:
        distances[c] = dijkstra(graph, c, n)
    
    # Create a complete graph of critical modules with edge weights as shortest paths
    critical_graph = []
    for i in range(t):
        for j in range(i + 1, t):
            u, v = critical[i], critical[j]
            critical_graph.append((distances[u][v], u, v))
    
    # Kruskal's algorithm to find MST of critical modules
    critical_graph.sort()
    parent = {c: c for c in critical}
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py
            return True
        return False
    
    total_cost = 0
    edges_used = 0
    
    for w, u, v in critical_graph:
        if union(u, v):
            total_cost += w
            edges_used += 1
            if edges_used == t - 1:
                break
    
    print(total_cost)

solve()