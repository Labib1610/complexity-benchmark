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
    
    # We need to find a triangle (mutually incompatible triad)
    # We'll iterate through all edges and for each edge (u,v), 
    # we look for a node w such that (u,w) and (v,w) are also edges.
    
    # To make it efficient and find the lexicographically smallest,
    # we'll process nodes in order and build adjacency sets.
    
    # Let's restructure: for each node, keep a set of neighbors
    # Then for each edge (u,v), find common neighbors
    
    # To ensure lexicographical order, we'll check triangles systematically
    
    # Convert to list and sort neighbors for deterministic behavior
    for i in range(1, n + 1):
        adj[i] = list(adj[i])
        adj[i].sort()
    
    # Iterate through all edges
    for u, v in sorted(edges):
        if u > v:
            u, v = v, u
        # For each edge, check for a common neighbor that forms a triangle
        # We want the lexicographically smallest triangle
        # So we iterate through neighbors of u and see if they're also neighbors of v
        # and form a valid triangle with u < v < w
        set_v = set(adj[v])
        for w in adj[u]:
            if w > v and w in set_v:
                print(u, v, w)
                return

if __name__ == "__main__":
    main()