import sys
from collections import defaultdict

def find_critical_interference():
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # Build adjacency list
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
    
    # Sort vertices for consistent processing
    vertices = sorted(adj.keys())
    
    # For each edge, check if it forms a triangle with any common neighbor
    best_cluster = None
    
    # Process edges in a consistent order
    for u, v in sorted(edges):
        # Find common neighbors of u and v
        if u in adj and v in adj:
            common_neighbors = adj[u] & adj[v]
            for w in common_neighbors:
                # Form the triangle
                triangle = tuple(sorted([u, v, w]))
                
                # Check if this is better than our current best
                if best_cluster is None:
                    best_cluster = triangle
                else:
                    # Compare based on the criteria
                    # First by smallest first element
                    if triangle[0] < best_cluster[0]:
                        best_cluster = triangle
                    elif triangle[0] == best_cluster[0]:
                        # Then by smallest second element
                        if triangle[1] < best_cluster[1]:
                            best_cluster = triangle
                        elif triangle[1] == best_cluster[1]:
                            # Then by smallest third element
                            if triangle[2] < best_cluster[2]:
                                best_cluster = triangle
    
    print(' '.join(map(str, best_cluster)))

find_critical_interference()