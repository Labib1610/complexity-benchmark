import sys
from collections import defaultdict

def find_triangle():
    n, m = map(int, sys.stdin.readline().split())
    
    # Store edges in adjacency list and edge set for O(1) lookup
    adj = defaultdict(set)
    edges = set()
    
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        if u > v:
            u, v = v, u
        adj[u].add(v)
        adj[v].add(u)
        edges.add((u, v))
    
    # Convert sets to lists for deterministic iteration
    adj_list = {k: sorted(list(v)) for k, v in adj.items()}
    
    # Check all triangles by iterating through all edges
    min_triangle = None
    
    # For each edge (u,v), check if there's a node w that connects to both u and v
    for u in sorted(adj.keys()):
        for v in adj_list[u]:
            if u >= v:
                continue
            # Look for common neighbors of u and v
            neighbors_u = set(adj_list[u])
            neighbors_v = set(adj_list[v])
            
            # Find common neighbors
            common = neighbors_u.intersection(neighbors_v)
            
            for w in sorted(common):
                if u < v < w:
                    triangle = (u, v, w)
                    if min_triangle is None or triangle < min_triangle:
                        min_triangle = triangle
    
    if min_triangle:
        print(min_triangle[0], min_triangle[1], min_triangle[2])

find_triangle()