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
    
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        idx += 2
        if u > v:
            u, v = v, u
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # Sort adjacency lists for consistent ordering
    for key in adj:
        adj[key] = sorted(adj[key])
    
    # Create a set of edges for O(1) lookup
    edge_set = set(edges)
    
    # Iterate through all edges
    for u, v in edges:
        # Find common neighbors of u and v
        neighbors_u = set(adj[u])
        neighbors_v = set(adj[v])
        common_neighbors = neighbors_u & neighbors_v
        
        if common_neighbors:
            # Found a triangle
            w = min(common_neighbors)
            # Output the lexicographically smallest triple
            triple = sorted([u, v, w])
            print(triple[0], triple[1], triple[2])
            return

if __name__ == "__main__":
    main()