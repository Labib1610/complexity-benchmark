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
    
    # Build adjacency list as sets for fast lookup
    # We need to find a triangle (3-cycle) in the graph
    
    # To find the lexicographically smallest triangle:
    # We'll iterate through all edges and for each edge (u,v),
    # we look for a node w such that (u,w) and (v,w) are also edges.
    # Among all such triangles, we want the lexicographically smallest.
    
    # First, let's sort the adjacency lists to help with ordering
    for i in range(1, n+1):
        adj[i] = sorted(adj[i])
    
    best_triangle = None
    
    # Iterate over all edges
    for u, v in edges:
        if u > v:
            continue  # To avoid double checking
        # We want to find w such that (u,w) and (v,w) exist
        # Iterate through neighbors of u and check if they are also neighbors of v
        for w in adj[u]:
            if w <= v:
                continue  # Ensuring u < v < w for lex order
            if w in adj[v]:
                # Found a triangle u-v-w
                triangle = tuple(sorted([u, v, w]))
                if best_triangle is None or triangle < best_triangle:
                    best_triangle = triangle
    
    if best_triangle:
        print(' '.join(map(str, best_triangle)))

if __name__ == "__main__":
    main()