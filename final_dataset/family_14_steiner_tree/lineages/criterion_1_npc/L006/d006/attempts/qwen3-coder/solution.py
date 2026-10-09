import sys
from collections import defaultdict
import heapq

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

def minimum_cost_to_connect_core_variables(n, m, t, core_vars, edges):
    # We need to connect all core variables in one component with minimum cost
    # This is essentially a Steiner tree problem, but since t is small (<= 10),
    # we can use a different approach.
    
    # Since we're looking for minimum cost to connect all core variables,
    # we can try all possible subsets of edges and check if they connect all core variables.
    # But with m up to n(n-1)/2, this is too much.
    
    # Better approach: Use a modified Kruskal's algorithm
    # We only care about connecting the core variables, not all vertices
    
    # For small t, we can compute the minimum spanning tree of the complete graph
    # induced by the core variables, where edge weights are the shortest path distances
    # between pairs of core variables in the original graph.
    
    if t <= 1:
        return 0
    
    # Build a graph with the given edges
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # Compute shortest paths between all pairs of core variables
    # Using Dijkstra from each core variable
    core_set = set(core_vars)
    dist = {}  # dist[(i, j)] = shortest distance from i to j
    
    def dijkstra(start):
        distance = {node: float('inf') for node in range(1, n+1)}
        distance[start] = 0
        pq = [(0, start)]
        
        while pq:
            d, u = heapq.heappop(pq)
            if d > distance[u]:
                continue
                
            for v, w in graph[u]:
                if distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w
                    heapq.heappush(pq, (distance[v], v))
        
        return distance
    
    # Calculate shortest distances between all pairs of core variables
    core_dists = []
    for i in range(t):
        distances = dijkstra(core_vars[i])
        for j in range(i+1, t):
            core_dists.append((distances[core_vars[j]], core_vars[i], core_vars[j]))
    
    # Sort edges by weight for Kruskal's algorithm
    core_dists.sort()
    
    # Apply Kruskal's algorithm to connect all core variables
    parent = {v: v for v in core_vars}
    rank = {v: 0 for v in core_vars}
    cost = 0
    components = t
    
    for weight, u, v in core_dists:
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            cost += weight
            components -= 1
            if components == 1:
                break
    
    return cost

# Read input
line = sys.stdin.readline().split()
n, m, t = int(line[0]), int(line[1]), int(line[2])

core_vars = list(map(int, sys.stdin.readline().split()))

edges = []
for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    edges.append((u, v, w))

# Solve and print result
result = minimum_cost_to_connect_core_variables(n, m, t, core_vars, edges)
print(result)