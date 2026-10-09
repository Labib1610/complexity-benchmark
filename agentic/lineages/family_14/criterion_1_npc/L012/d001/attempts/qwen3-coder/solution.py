import sys
import heapq
from collections import defaultdict
import itertools

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
    priorities = list(map(int, sys.stdin.readline().split()))
    
    graph = defaultdict(list)
    
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # Compute shortest distances from each priority language to all nodes
    dist_from_priority = {}
    for p in priorities:
        dist_from_priority[p] = dijkstra(graph, p, n)
    
    # Try each possible source language
    min_cost = float('inf')
    
    for source in range(1, n + 1):
        # Calculate cost to connect all priority languages from this source
        total_cost = 0
        reachable = True
        
        # We need to connect all priority languages to form a connected component containing source
        # Find minimum spanning tree connecting source and all priority languages
        
        # Special case: if source is itself a priority language
        is_source_priority = source in priorities
        
        # Create a complete graph among source and priority languages
        # Node indices: 0 for source, 1..t for priorities (if source is not a priority)
        # If source is a priority, we exclude it from priorities in the nodes list
        nodes = []
        node_map = {}
        
        if is_source_priority:
            # Source is already a priority - we don't need to connect to it separately
            temp_priorities = [p for p in priorities if p != source]
            if not temp_priorities:  # Only the source is priority
                min_cost = min(min_cost, 0)
                continue
            nodes = [source] + temp_priorities
        else:
            nodes = [source] + priorities
            
        # For each node, we know the min distance to every other node via Dijkstra
        # But we want to find the minimum cost to connect all these nodes
        
        # Use Prim's algorithm on the induced subgraph with nodes = [source] + priorities
        # But we need to compute the minimum distance between any two nodes in our subset
        # Distance between two nodes is the shortest path in the full graph
        
        # Actually, let's think differently:
        # We want to choose a source language and connect all priority languages to it
        # The cost is the sum of shortest paths from source to each priority language
        # But we also have the option to translate between priority languages at no extra cost once we reach one
        
        # So the real approach:
        # 1. Choose a source language
        # 2. Find minimum cost to connect all priority languages
        # 3. This means finding a Steiner tree with terminals = priorities and source
        
        # Simplification: try each node as potential source
        # For each source, compute cost to connect all priorities
        # Cost = sum of shortest paths from source to each priority (but accounting for connectivity)
        
        # Even simpler approach:
        # Try each language as source
        # For each source, compute minimum cost to make all priorities reachable
        # This is a MST on the metric closure
        
        if source in priorities and len(priorities) == 1:
            min_cost = min(min_cost, 0)
            continue
            
        # Compute distances from source to all priorities
        dist_from_source = dijkstra(graph, source, n)
        
        # Check if all priorities are reachable
        unreachable = False
        cost = 0
        for p in priorities:
            if dist_from_source[p] == float('inf'):
                unreachable = True
                break
            cost += dist_from_source[p]
            
        if not unreachable:
            min_cost = min(min_cost, cost)
    
    print(min_cost)

solve()