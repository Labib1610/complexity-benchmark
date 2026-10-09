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
    required = list(map(int, input().split()))
    
    if t <= 1:
        print(0)
        return
    
    graph = defaultdict(list)
    
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # Create a complete graph of required nodes with shortest path distances
    required_graph = []
    required_set = set(required)
    
    for i in range(t):
        for j in range(i+1, t):
            # Find shortest path between required[i] and required[j]
            dist = dijkstra(graph, required[i], {required[j]})
            required_graph.append((dist, required[i], required[j]))
    
    # Kruskal's algorithm to find MST of required graph
    required_graph.sort()
    
    parent = {}
    def find(x):
        if x not in parent:
            parent[x] = x
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
    
    for cost, u, v in required_graph:
        if union(u, v):
            total_cost += cost
            edges_used += 1
            if edges_used == t - 1:
                break
    
    print(total_cost)

solve()