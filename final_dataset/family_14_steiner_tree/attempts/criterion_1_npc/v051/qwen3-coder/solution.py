import sys
from itertools import combinations
from collections import defaultdict
import heapq

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
    foundations = list(map(int, sys.stdin.readline().split()))
    
    if t <= 1:
        print(0)
        return
    
    graph = defaultdict(list)
    
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # Compute shortest distances from each foundation to all nodes
    dists = []
    for f in foundations:
        dists.append(dijkstra(graph, f, n))
    
    # Build complete graph of foundations with shortest path weights
    foundation_graph = []
    for i in range(t):
        for j in range(i + 1, t):
            weight = dists[i][foundations[j]]
            foundation_graph.append((weight, i, j))
    
    # Kruskal's algorithm to find MST of foundation graph
    foundation_graph.sort()
    parent = list(range(t))
    
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
    
    for weight, u, v in foundation_graph:
        if union(u, v):
            total_cost += weight
            edges_used += 1
            if edges_used == t - 1:
                break
    
    print(total_cost)

solve()