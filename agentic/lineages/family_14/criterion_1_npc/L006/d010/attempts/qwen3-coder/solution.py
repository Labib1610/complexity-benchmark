import sys
import heapq
from collections import defaultdict

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
    targets = list(map(int, sys.stdin.readline().split()))
    
    # If there's only one target, B[x,x] = 1 > 0 always, so cost is 0
    if t == 1:
        print(0)
        return
    
    # Build graph from modifications
    graph = defaultdict(list)
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # Compute shortest paths between all pairs of target vertices
    # We only care about paths between target vertices
    distances = {}
    for target in targets:
        distances[target] = dijkstra(graph, target, n)
    
    # Create a complete graph on target vertices with edge weights as shortest path distances
    # Find minimum spanning tree of this graph
    # This gives us the minimum cost to connect all target vertices
    
    # Prim's algorithm for MST
    if t == 0:
        print(0)
        return
        
    visited = set()
    min_cost = 0
    edges = [(0, targets[0])]  # (cost, vertex)
    
    while len(visited) < t:
        cost, u = heapq.heappop(edges)
        if u in visited:
            continue
        visited.add(u)
        min_cost += cost
        
        # Add edges from u to all unvisited targets
        for v in targets:
            if v not in visited:
                heapq.heappush(edges, (distances[u][v], v))
    
    print(min_cost)

solve()