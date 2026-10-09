import sys
from itertools import combinations

def find_min_penalty(n, m, t, priorities, conditions):
    if t <= 1:
        return 0
    
    # Build a graph with minimum edge weights
    graph = {}
    for u, v, w in conditions:
        if (u, v) not in graph or graph[(u, v)] > w:
            graph[(u, v)] = w
        if (v, u) not None and graph.get((v, u), float('inf')) > w:
            graph[(v, u)] = w
    
    # Use Floyd-Warshall to find shortest paths between all nodes
    dist = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dist[i][i] = 0
    
    for (u, v), w in graph.items():
        dist[u][v] = min(dist[u][v], w)
        dist[v][u] = min(dist[v][u], w)
    
    # Floyd-Warshall algorithm
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    # Find minimum spanning tree for the priority nodes
    # We want to connect all priority nodes with minimal cost
    # This is essentially a Steiner tree problem, but we'll use a simpler approach:
    # Find the minimum cost to connect all priority nodes
    
    # For small t (<= 10), we can try all possible ways to connect them
    # But let's use a more efficient approach: 
    # Find the minimum spanning tree in the complete graph formed by priority nodes
    # where edge weights are the shortest path distances
    
    if len(priorities) <= 1:
        return 0
        
    # Create a complete graph of priority nodes with shortest path distances
    edges = []
    for i in range(len(priorities)):
        for j in range(i + 1, len(priorities)):
            u, v = priorities[i], priorities[j]
            if dist[u][v] < float('inf'):
                edges.append((dist[u][v], u, v))
    
    # Sort edges by weight
    edges.sort()
    
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
    
    # Kruskal's algorithm to find MST
    total_cost = 0
    edges_used = 0
    
    for weight, u, v in edges:
        if union(u, v):
            total_cost += weight
            edges_used += 1
            if edges_used == len(priorities) - 1:
                break
    
    return total_cost

# Read input
line1 = list(map(int, sys.stdin.readline().split()))
n, m, t = line1[0], line1[1], line1[2]

priorities = list(map(int, sys.stdin.readline().split()))

conditions = []
for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    conditions.append((u, v, w))

# Solve and print result
result = find_min_penalty(n, m, t, priorities, conditions)
print(result)