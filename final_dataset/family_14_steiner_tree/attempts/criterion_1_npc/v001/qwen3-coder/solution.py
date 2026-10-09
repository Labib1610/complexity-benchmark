import sys
import heapq
from collections import defaultdict
import math

def dijkstra(graph, start, end_set, n):
    dist = [math.inf] * (n + 1)
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
                
    min_dist = math.inf
    for node in end_set:
        if node != start and dist[node] < min_dist:
            min_dist = dist[node]
            
    return min_dist if min_dist != math.inf else 0

def solve():
    n, m, t = map(int, sys.stdin.readline().split())
    mandatory = list(map(int, sys.stdin.readline().split()))
    
    if t <= 1:
        print(0)
        return
    
    graph = defaultdict(list)
    
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # Create a complete graph of mandatory facilities with shortest path distances
    mandatory_graph = []
    
    for i in range(t):
        for j in range(i + 1, t):
            src = mandatory[i]
            dst = mandatory[j]
            
            # Find shortest path between src and dst
            dist = [math.inf] * (n + 1)
            dist[src] = 0
            pq = [(0, src)]
            
            while pq:
                d, u = heapq.heappop(pq)
                if u == dst:
                    distance = d
                    break
                if d > dist[u]:
                    continue
                    
                for v, w in graph[u]:
                    if dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
                        heapq.heappush(pq, (dist[v], v))
            else:
                distance = dist[dst]
            
            mandatory_graph.append((distance, src, dst))
    
    # Now find MST of mandatory facilities
    # Sort edges by weight
    mandatory_graph.sort()
    
    # Union-Find for Kruskal's algorithm
    parent = list(range(n + 1))
    
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
    
    for weight, u, v in mandatory_graph:
        if union(u, v):
            total_cost += weight
            edges_used += 1
            if edges_used == t - 1:
                break
    
    print(total_cost)

solve()