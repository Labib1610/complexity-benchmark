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
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
                
    return dist

def solve():
    n, m, t = map(int, sys.stdin.readline().split())
    primary = list(map(int, sys.stdin.readline().split()))
    
    if t <= 1:
        print(0)
        return
    
    graph = defaultdict(list)
    
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # Create a complete graph among primary turbines
    # where edge weights are shortest path distances
    primary_set = set(primary)
    primary_distances = {}
    
    for p in primary:
        dist = dijkstra(graph, p, range(1, n+1))
        primary_distances[p] = {p2: dist[p2] for p2 in primary if p2 != p}
    
    # Now we need to find MST of this complete graph
    # Using Prim's algorithm
    included = {primary[0]}
    edges = []
    
    for p in primary[1:]:
        heapq.heappush(edges, (primary_distances[primary[0]][p], primary[0], p))
    
    total_cost = 0
    
    while len(included) < len(primary):
        cost, u, v = heapq.heappop(edges)
        if v in included:
            continue
            
        included.add(v)
        total_cost += cost
        
        for p in primary:
            if p not in included:
                heapq.heappush(edges, (primary_distances[v][p], v, p))
    
    print(total_cost)

solve()