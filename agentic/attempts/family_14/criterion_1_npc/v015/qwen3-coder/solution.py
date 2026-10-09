import sys
import heapq
from collections import defaultdict

def dijkstra(graph, start, end_set):
    if start in end_set:
        return 0
    
    dist = defaultdict(lambda: float('inf'))
    dist[start] = 0
    pq = [(0, start)]
    
    while pq:
        d, u = heapq.heappop(pq)
        
        if d > dist[u]:
            continue
            
        if u in end_set:
            return d
            
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
                
    return float('inf')

def solve():
    n, m, t = map(int, input().split())
    critical = list(map(int, input().split()))
    
    if t <= 1:
        print(0)
        return
        
    graph = defaultdict(list)
    
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # Compute shortest paths between all pairs of critical facilities
    critical_set = set(critical)
    edges = []
    
    for i in range(t):
        for j in range(i+1, t):
            start = critical[i]
            end_set = {critical[j]}
            cost = dijkstra(graph, start, end_set)
            if cost < float('inf'):
                edges.append((cost, i, j))
    
    # Kruskal's algorithm for MST
    edges.sort()
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
    
    for cost, u, v in edges:
        if union(u, v):
            total_cost += cost
            edges_used += 1
            if edges_used == t - 1:
                break
                
    print(total_cost)

solve()