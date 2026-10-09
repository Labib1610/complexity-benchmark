import sys
import heapq
from collections import defaultdict
import itertools

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
    core = list(map(int, input().split()))
    
    if t <= 1:
        print(0)
        return
    
    edges = []
    graph = defaultdict(list)
    
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # Compute shortest paths between all pairs of core languages
    core_dist = defaultdict(lambda: defaultdict(lambda: float('inf')))
    
    for i in range(t):
        for j in range(i+1, t):
            src = core[i]
            dst = core[j]
            # Find shortest path from src to dst
            dist = dijkstra(graph, src, {dst})
            core_dist[src][dst] = dist
            core_dist[dst][src] = dist
    
    # Now we have a complete graph on core languages
    # Find minimum spanning tree
    core_set = set(core)
    
    # Kruskal's algorithm
    edges_sorted = []
    for i in range(t):
        for j in range(i+1, t):
            u, v = core[i], core[j]
            w = core_dist[u][v]
            if w < float('inf'):
                edges_sorted.append((w, u, v))
    
    edges_sorted.sort()
    
    # Union-Find for Kruskal
    parent = {x: x for x in core}
    
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
    
    for w, u, v in edges_sorted:
        if union(u, v):
            total_cost += w
            edges_used += 1
            if edges_used == t - 1:
                break
    
    print(total_cost)

solve()