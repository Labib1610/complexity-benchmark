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
    
    # Create adjacency list as sets for fast lookup
    # We'll iterate through all triplets (i,j,k) with i<j<k
    # and check if all three pairs (i,j), (i,k), (j,k) exist
    
    # To optimize, we can iterate through all edges and for each edge (u,v),
    # look for a third node w such that (u,w) and (v,w) also exist.
    # This means we're looking for triangles in the graph.
    
    # Convert adjacency list to sorted lists for consistent iteration
    adj_list = {}
    for node in adj:
        adj_list[node] = sorted(list(adj[node]))
        
    # Also create a set of edges for O(1) lookup
    edge_set = set(edges)
    for u, v in list(edge_set):
        if u > v:
            edge_set.remove((u, v))
            edge_set.add((v, u))
            
    # Now iterate through all edges (u,v) where u<v
    # For each such edge, iterate through nodes w > v
    # Check if both (u,w) and (v,w) exist
    
    best = None
    
    # Sort nodes for consistent processing
    nodes = sorted(adj.keys())
    
    for idx_u in range(len(nodes)):
        u = nodes[idx_u]
        for idx_v in range(idx_u + 1, len(nodes)):
            v = nodes[idx_v]
            # Check if edge (u,v) exists
            if v not in adj[u]:
                continue
            # Now look for w > v such that (u,w) and (v,w) exist
            # Iterate through neighbors of u that are > v
            for w in adj_list[u]:
                if w <= v:
                    continue
                # Check if (v,w) exists
                if w in adj[v]:
                    candidate = tuple(sorted([u, v, w]))
                    if best is None or candidate < best:
                        best = candidate
                        
    # Since we're iterating in order and checking minimality,
    # the first valid triangle found will be the lexicographically smallest
    print(best[0], best[1], best[2])

if __name__ == "__main__":
    main()