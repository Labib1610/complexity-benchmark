import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    adj = defaultdict(set)
    
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        index += 2
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # We need to find a triangle (3-cycle) in the graph.
    # The graph is undirected.
    # We want the lexicographically smallest triangle.

    # Create adjacency list as sets for fast lookup
    # For each edge (u,v), check for a common neighbor w
    # That would make a triangle u-v-w-u
    
    # To get the lex smallest triangle, we can iterate through
    # all edges and for each edge (u,v) with u<v,
    # look for the smallest w > v such that (u,w) and (v,w) exist.
    
    # First, sort adjacency lists for consistent iteration
    for node in adj:
        adj[node] = sorted(adj[node])
    
    best_triangle = None
    
    # Iterate through all edges
    for u, v in edges:
        if u > v:
            u, v = v, u  # Ensure u < v
        
        # Get neighbors of u and v
        neigh_u = set(adj[u])
        neigh_v = set(adj[v])
        
        # Find common neighbors greater than v to ensure u < v < w
        common = [w for w in neigh_u if w in neigh_v and w > v]
        
        if common:
            w = min(common)
            triangle = tuple(sorted([u, v, w]))
            if best_triangle is None or triangle < best_triangle:
                best_triangle = triangle
    
    print(best_triangle[0], best_triangle[1], best_triangle[2])

if __name__ == "__main__":
    main()