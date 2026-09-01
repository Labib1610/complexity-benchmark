import sys
from collections import defaultdict

def find_trilateral_impasse():
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # Build adjacency list representation of the graph
    adj = defaultdict(set)
    edges = []
    
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))
        index += 2
    
    # Convert to sorted lists for consistent iteration
    for node in adj:
        adj[node] = sorted(list(adj[node]))
    
    # We'll check all combinations systematically to find the lexicographically smallest triangle
    # Instead of checking all triplets, we can optimize by checking neighbors of each edge
    
    best_triangle = None
    
    # For each edge, check if any common neighbor forms a triangle
    for u, v in edges:
        if u >= v:
            continue
            
        # Find common neighbors of u and v
        neighbors_u = set(adj[u])
        neighbors_v = set(adj[v])
        common_neighbors = neighbors_u & neighbors_v
        
        for w in common_neighbors:
            if w <= u or w <= v:
                continue  # Ensure u < v < w for lexicographic ordering
            
            triangle = (u, v, w)
            if best_triangle is None or triangle < best_triangle:
                best_triangle = triangle
    
    # Since the problem guarantees a solution exists, best_triangle will not be None
    print(best_triangle[0], best_triangle[1], best_triangle[2])

find_trilateral_impasse()