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
    
    # We need to find a triangle: x-y-z where x-y, y-z, z-x all exist
    # That means we need three nodes that are all connected to each other
    
    # For each edge (u,v), check if there's a node w such that (u,w) and (v,w) also exist
    # This forms a triangle u-v-w
    
    # Convert edges to a set for O(1) lookup
    edge_set = set()
    for u, v in edges:
        if u > v:
            u, v = v, u
        edge_set.add((u, v))
    
    # Also create adjacency sets for fast lookup
    adj_list = {i: set() for i in range(1, n+1)}
    for u, v in edges:
        adj_list[u].add(v)
        adj_list[v].add(u)
    
    best = None
    
    # Iterate through all edges
    for u, v in edges:
        if u > v:
            continue  # To avoid duplicate checking
        # Check for common neighbors
        neighbors_u = adj_list[u]
        neighbors_v = adj_list[v]
        common = neighbors_u & neighbors_v
        for w in common:
            # Found triangle u, v, w
            triple = sorted([u, v, w])
            if best is None or triple < best:
                best = triple
    
    if best:
        print(' '.join(map(str, best)))

if __name__ == "__main__":
    main()