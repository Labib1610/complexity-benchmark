import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    index = 2
    edges = []
    adj = defaultdict(set)
    
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        index += 2
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # Convert to sorted list for consistent iteration
    nodes = sorted(adj.keys())
    
    # For each edge (u,v), look for a common neighbor w
    # such that u-v-w forms a triangle
    triangles = []
    
    # To make it efficient, we'll iterate through all edges
    # and for each edge (u,v), we'll check for nodes that are
    # neighbors of both u and v
    for u, v in edges:
        if u > v:
            u, v = v, u  # Ensure u < v for consistency
        # Get common neighbors of u and v
        common = adj[u] & adj[v]
        for w in common:
            if w != u and w != v:
                # Sort the triplet to ensure a < b < c
                a, b, c = sorted([u, v, w])
                triangles.append((a, b, c))
    
    # Remove duplicates by converting to set then back to list
    unique_triangles = list(set(triangles))
    
    # Sort lexicographically
    unique_triangles.sort()
    
    # Output the first one
    result = unique_triangles[0]
    print(result[0], result[1], result[2])

if __name__ == "__main__":
    main()