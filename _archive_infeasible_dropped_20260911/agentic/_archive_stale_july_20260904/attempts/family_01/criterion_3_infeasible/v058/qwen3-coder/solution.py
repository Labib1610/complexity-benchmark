import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    adj = [set() for _ in range(n + 1)]
    
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        index += 2
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # We need to find a triangle (triad) in the graph.
    # A brute-force approach checking all triplets would be too slow.
    # Instead, we iterate through each edge and check for a common neighbor.
    
    # To ensure lexicographical order, we'll process nodes in order.
    # For each edge (u,v), we look for a node w such that (u,w) and (v,w) exist,
    # and u < v < w to maintain the order and avoid duplicates.
    
    # First, let's sort adjacency lists for consistent processing
    for i in range(1, n+1):
        adj[i] = sorted(list(adj[i]))
    
    best = None
    
    # Iterate through all edges
    for u, v in edges:
        if u >= v:
            continue  # Ensure u < v
        
        # Find common neighbors of u and v that are > v
        # Convert to sets for intersection
        neighbors_u = set(adj[u])
        neighbors_v = set(adj[v])
        
        # Get common neighbors
        common = neighbors_u & neighbors_v
        
        # Filter those that are greater than v to maintain u < v < w
        candidates = [w for w in common if w > v]
        
        if candidates:
            w = min(candidates)
            triplet = (u, v, w)
            if best is None or triplet < best:
                best = triplet
    
    if best:
        print(best[0], best[1], best[2])

if __name__ == "__main__":
    main()