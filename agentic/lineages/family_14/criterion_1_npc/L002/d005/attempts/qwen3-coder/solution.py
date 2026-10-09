import sys
from itertools import combinations

def find_root(parent, x):
    if parent[x] != x:
        parent[x] = find_root(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    root_x = find_root(parent, x)
    root_y = find_root(parent, y)
    if root_x != root_y:
        if rank[root_x] < rank[root_y]:
            root_x, root_y = root_y, root_x
        parent[root_y] = root_x
        if rank[root_x] == rank[root_y]:
            rank[root_x] += 1

def kruskal(n, edges):
    parent = list(range(n))
    rank = [0] * n
    edges.sort(key=lambda x: x[2])
    cost = 0
    for u, v, w in edges:
        if find_root(parent, u) != find_root(parent, v):
            union(parent, rank, u, v)
            cost += w
    return cost

def solve():
    n, m, t = map(int, sys.stdin.readline().split())
    critical_indices = list(map(int, sys.stdin.readline().split()))
    
    # Convert to 0-based indexing
    critical_indices = [x - 1 for x in critical_indices]
    
    # If there's only one critical index, no pairs exist, so cost is 0
    if t <= 1:
        print(0)
        return
    
    # Generate all required pairs of critical indices
    required_pairs = list(combinations(critical_indices, 2))
    
    # Read available functionals
    available_edges = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        available_edges.append((u-1, v-1, w))  # Convert to 0-based indexing
    
    # For each required pair, find the minimum cost to connect them
    # This is equivalent to finding the minimum spanning tree that connects all critical nodes
    # We can use a Steiner tree approach, but since t is small (<= 10), we can try all combinations
    
    # Build a graph with only critical nodes and paths between them using available edges
    # Use Floyd-Warshall to find shortest paths between all pairs of critical nodes
    INF = float('inf')
    dist = [[INF] * n for _ in range(n)]
    
    # Initialize distances for direct edges
    for i in range(n):
        dist[i][i] = 0
    
    for u, v, w in available_edges:
        dist[u][v] = min(dist[u][v], w)
        dist[v][u] = min(dist[v][u], w)
    
    # Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    # Now we have shortest paths between all nodes
    # Create a complete graph on critical nodes with these distances
    # Then find the minimum spanning tree of this graph
    critical_dist = []
    for i in range(len(critical_indices)):
        for j in range(i+1, len(critical_indices)):
            u = critical_indices[i]
            v = critical_indices[j]
            if dist[u][v] < INF:
                critical_dist.append((u, v, dist[u][v]))
    
    # Find MST of the critical nodes using Kruskal's algorithm
    result = kruskal(n, critical_dist)
    print(result)

solve()