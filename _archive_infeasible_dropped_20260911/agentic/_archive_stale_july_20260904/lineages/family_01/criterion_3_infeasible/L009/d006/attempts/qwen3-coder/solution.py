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
    
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        idx += 2
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # We need to find a triangle (three nodes all connected to each other)
    # That satisfies the reactive symmetry property.
    # In a triangle, every node is connected to the other two,
    # so the reactive symmetry is automatically satisfied.
    # So we just need to find any triangle.
    
    # To find the lexicographically smallest triangle:
    # We can iterate through all edges and for each edge (u,v),
    # look for a common neighbor w such that u < v < w.
    
    # First, let's sort adjacency lists for consistent iteration
    for i in range(1, n + 1):
        adj[i] = sorted(list(adj[i]))
    
    best = None
    
    # Iterate through all edges
    for u, v in edges:
        if u >= v:
            continue
        # Look for a common neighbor w such that v < w
        # Convert to sets for fast intersection
        neighbors_u = set(adj[u])
        neighbors_v = set(adj[v])
        common_neighbors = neighbors_u & neighbors_v
        
        for w in sorted(common_neighbors):
            if v < w:
                candidate = (u, v, w)
                if best is None or candidate < best:
                    best = candidate
    
    if best:
        print(best[0], best[1], best[2])

if __name__ == "__main__":
    main()