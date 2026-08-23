import sys
from collections import defaultdict

def find_coherent_ternary_subsystem():
    n, m = map(int, sys.stdin.readline().split())
    
    # Build adjacency list representation of the graph
    adj = defaultdict(set)
    edges = []
    
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))
    
    # Sort vertices by their degree in descending order for optimization
    vertices = list(range(1, n + 1))
    vertices.sort(key=lambda x: len(adj[x]), reverse=True)
    
    # For each edge, check if there exists a third vertex that connects to both endpoints
    best_result = None
    
    # Process edges in an order that might help us find the lexicographically smallest solution faster
    edge_list = [(u, v) for u, v in edges]
    edge_list.sort()
    
    for u, v in edge_list:
        if u > v:
            u, v = v, u
            
        # Find common neighbors of u and v
        neighbors_u = adj[u]
        neighbors_v = adj[v]
        
        # Check each vertex to see if it forms a triangle with u and v
        for w in vertices:
            if w == u or w == v:
                continue
            if w in neighbors_u and w in neighbors_v:
                # Found a triangle: u, v, w
                result = sorted([u, v, w])
                if best_result is None or result < best_result:
                    best_result = result
                break  # Since we process in sorted order, first found will be lex smallest for this edge
    
    print(' '.join(map(str, best_result)))

find_coherent_ternary_subsystem()