import sys
from collections import defaultdict

def find_triangle():
    n, m = map(int, sys.stdin.readline().split())
    
    # Build adjacency list
    adj = defaultdict(set)
    edges = []
    
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        if u > v:
            u, v = v, u
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))
    
    # Sort adjacency lists for consistent processing
    for node in adj:
        adj[node] = sorted(list(adj[node]))
    
    # For each edge, check if there's a common neighbor forming a triangle
    found = False
    result = None
    
    # Process edges in lexicographical order
    edges.sort()
    
    for u, v in edges:
        if found:
            break
        # Check neighbors of u and v for common elements
        # We want to find w such that u-w and v-w exist
        neighbors_u = set(adj[u])
        neighbors_v = set(adj[v])
        
        # Remove the edge between u and v from consideration
        neighbors_u.discard(v)
        neighbors_v.discard(u)
        
        # Find common neighbors
        common = neighbors_u.intersection(neighbors_v)
        
        for w in sorted(common):
            # Found triangle u-v-w
            a, b, c = sorted([u, v, w])
            if not found or (a, b, c) < result:
                result = (a, b, c)
                found = True
                break
    
    if result is None:
        # Fallback - brute force search for small cases
        nodes = sorted(adj.keys())
        for i in range(len(nodes)):
            for j in range(i+1, len(nodes)):
                for k in range(j+1, len(nodes)):
                    u, v, w = nodes[i], nodes[j], nodes[k]
                    if v in adj[u] and w in adj[u] and w in adj[v]:
                        a, b, c = u, v, w
                        print(a, b, c)
                        return
    
    print(result[0], result[1], result[2])

find_triangle()