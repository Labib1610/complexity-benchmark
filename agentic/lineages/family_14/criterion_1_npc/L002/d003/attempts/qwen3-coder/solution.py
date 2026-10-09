import sys
import heapq
from collections import defaultdict

def dijkstra(graph, start, nodes):
    dist = {node: float('inf') for node in nodes}
    dist[start] = 0
    pq = [(0, start)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
            
        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
                
    return dist

def solve():
    n, m, t = map(int, sys.stdin.readline().split())
    primaries = list(map(int, sys.stdin.readline().split()))
    
    if t <= 1:
        print(0)
        return
        
    graph = defaultdict(list)
    
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
        
    nodes = list(range(1, n + 1))
    all_distances = {}
    
    # Compute shortest paths from each primary node
    for p in primaries:
        all_distances[p] = dijkstra(graph, p, nodes)
        
    # Build a complete graph of primary nodes with shortest path weights
    # Then find the minimum spanning tree of this graph
    edges = []
    for i in range(len(primaries)):
        for j in range(i + 1, len(primaries)):
            u, v = primaries[i], primaries[j]
            weight = all_distances[u][v]
            edges.append((weight, u, v))
            
    # Kruskal's algorithm for MST
    edges.sort()
    parent = {node: node for node in primaries}
    
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
    for weight, u, v in edges:
        if union(u, v):
            total_cost += weight
            
    print(total_cost)

solve()