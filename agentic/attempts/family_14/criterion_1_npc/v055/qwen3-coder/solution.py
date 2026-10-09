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
            
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    
    min_dist = float('inf')
    for end in end_set:
        min_dist = min(min_dist, dist[end])
    
    return min_dist

def solve():
    n, m, t = map(int, input().split())
    primaries = list(map(int, input().split()))
    
    if t <= 1:
        print(0)
        return
    
    graph = defaultdict(list)
    
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # Create a complete graph between primary crystals with shortest path weights
    primary_graph = []
    for i in range(t):
        for j in range(i+1, t):
            start = primaries[i]
            end_set = {primaries[j]}
            weight = dijkstra(graph, start, end_set)
            primary_graph.append((start, primaries[j], weight))
    
    # Find MST of primary graph using Kruskal's algorithm
    def find(parent, x):
        if parent[x] != x:
            parent[x] = find(parent, parent[x])
        return parent[x]
    
    def union(parent, rank, x, y):
        px, py = find(parent, x), find(parent, y)
        if px == py:
            return False
        if rank[px] < rank[py]:
            px, py = py, px
        parent[py] = px
        if rank[px] == rank[py]:
            rank[px] += 1
        return True
    
    # Sort edges by weight
    primary_graph.sort(key=lambda x: x[2])
    
    parent = {p: p for p in primaries}
    rank = {p: 0 for p in primaries}
    
    total_cost = 0
    edges_used = 0
    
    for u, v, w in primary_graph:
        if union(parent, rank, u, v):
            total_cost += w
            edges_used += 1
            if edges_used == t - 1:
                break
    
    print(total_cost)

solve()