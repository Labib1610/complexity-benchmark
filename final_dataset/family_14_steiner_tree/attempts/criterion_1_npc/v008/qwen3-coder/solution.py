import sys
import heapq
from collections import defaultdict

def dijkstra(graph, start, required):
    # Dijkstra's algorithm modified to stop when all required nodes are reached
    dist = {start: 0}
    pq = [(0, start)]
    visited = set()
    required_reached = set()
    
    if start in required:
        required_reached.add(start)
    
    while pq and len(required_reached) < len(required):
        d, u = heapq.heappop(pq)
        if u in visited:
            continue
        visited.add(u)
        
        for v, weight in graph[u]:
            if v not in dist or dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))
                if v in required:
                    required_reached.add(v)
    
    return dist

def solve():
    n, m, t = map(int, sys.stdin.readline().split())
    required = list(map(int, sys.stdin.readline().split()))
    
    if t <= 1:
        print(0)
        return
    
    graph = defaultdict(list)
    
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # Prim's algorithm for Steiner tree approximation
    # We'll use a modified approach: build MST of required nodes using distances
    
    # Calculate shortest paths between all required nodes
    required_set = set(required)
    required_indices = {req: i for i, req in enumerate(required)}
    
    # Create a complete graph on required nodes with shortest path weights
    required_graph = [[float('inf')] * len(required) for _ in range(len(required))]
    
    for i, req in enumerate(required):
        dist = dijkstra(graph, req, required_set)
        for j, other_req in enumerate(required):
            if req == other_req:
                required_graph[i][j] = 0
            elif other_req in dist:
                required_graph[i][j] = dist[other_req]
    
    # Now find MST of this complete graph using Prim's algorithm
    if len(required) <= 1:
        print(0)
        return
    
    # Prim's algorithm on the required graph
    visited = [False] * len(required)
    min_edge = [float('inf')] * len(required)
    min_edge[0] = 0
    total_cost = 0
    
    for _ in range(len(required)):
        # Find the vertex with minimum edge weight not yet included
        u = -1
        for v in range(len(required)):
            if not visited[v] and (u == -1 or min_edge[v] < min_edge[u]):
                u = v
        
        visited[u] = True
        total_cost += min_edge[u]
        
        # Update min_edge for vertices adjacent to u
        for v in range(len(required)):
            if not visited[v] and required_graph[u][v] < min_edge[v]:
                min_edge[v] = required_graph[u][v]
    
    print(total_cost)

solve()