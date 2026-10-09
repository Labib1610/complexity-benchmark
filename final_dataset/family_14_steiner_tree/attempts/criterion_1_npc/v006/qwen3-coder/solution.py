import sys
import heapq
from collections import defaultdict

def dijkstra(graph, start, end_set):
    # Dijkstra's algorithm to find shortest path from start to any node in end_set
    dist = {}
    pq = [(0, start)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if u in dist:
            continue
        dist[u] = d
        
        if u in end_set:
            return d
            
        for v, w in graph[u]:
            if v not in dist:
                heapq.heappush(pq, (d + w, v))
                
    return float('inf')

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
    
    # Create a complete graph on primary nodes with shortest path distances
    primary_set = set(primaries)
    edges = []
    
    for i in range(t):
        for j in range(i+1, t):
            p1, p2 = primaries[i], primaries[j]
            dist = dijkstra(graph, p1, {p2})
            if dist < float('inf'):
                edges.append((dist, p1, p2))
    
    # Union-Find for Kruskal's algorithm
    parent = {p: p for p in primaries}
    
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
    
    # Sort edges by weight
    edges.sort()
    
    # Kruskal's algorithm to find MST
    total_cost = 0
    edge_count = 0
    
    for w, u, v in edges:
        if union(u, v):
            total_cost += w
            edge_count += 1
            if edge_count == t - 1:
                break
    
    print(total_cost)

solve()