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
    
    if t == 1:
        print(0)
        return
    
    graph = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # Compute shortest distances from each critical node to all other nodes
    distances = {}
    for c in critical:
        distances[c] = dijkstra(graph, c, n)
    
    min_cost = float('inf')
    
    # Try each format as the native format
    for native in range(1, n + 1):
        cost = 0
        for c in critical:
            if c != native:
                cost += distances[c][native]
        min_cost = min(min_cost, cost)
    
    print(min_cost)

solve()