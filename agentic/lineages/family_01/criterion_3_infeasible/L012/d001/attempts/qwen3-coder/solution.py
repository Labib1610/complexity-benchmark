import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # Build adjacency list using sets for O(1) lookup
    adj = [set() for _ in range(n + 1)]
    edges = []
    
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))
        idx += 2
    
    # Sort edges to process in order
    edges.sort()
    
    # To find the lexicographically smallest triangle, we iterate through all edges
    # and for each edge (u,v), we look for a third node w such that (u,w) and (v,w) exist
    # We want the smallest such triplet (u,v,w) in lexicographical order
    
    best_triad = None
    
    # Try all edges as the first edge of the triangle
    for u, v in edges:
        if u > v:
            u, v = v, u  # Ensure u < v
            
        # We want to find w such that (u,w) and (v,w) exist and u < v < w
        # Iterate through neighbors of u that are greater than v
        for w in adj[u]:
            if w > v:
                if w in adj[v]:
                    # Found a triangle (u, v, w)
                    triad = (u, v, w)
                    if best_triad is None or triad < best_triad:
                        best_triad = triad
        
        # Also check neighbors of v that are greater than v
        for w in adj[v]:
            if w > v:
                if w in adj[u]:
                    # Found a triangle (u, v, w)
                    triad = (u, v, w)
                    if best_triad is None or triad < best_triad:
                        best_triad = triad
                        
    # Since we're guaranteed a solution, best_triad will be found
    print(best_triad[0], best_triad[1], best_triad[2])

if __name__ == "__main__":
    main()