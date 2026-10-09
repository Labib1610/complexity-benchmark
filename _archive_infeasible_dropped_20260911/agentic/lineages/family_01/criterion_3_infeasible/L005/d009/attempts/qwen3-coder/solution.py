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
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # Convert edges to a set for O(1) lookup
    edge_set = set(edges)
    rev_edge_set = set()
    for u, v in edges:
        rev_edge_set.add((v, u))
    full_edge_set = edge_set | rev_edge_set
    
    # We need to find three edges such that each node appears an even number of times
    # That means we're looking for a cycle of length 3 (triangle) in the graph
    # Because in a triangle, each node appears in exactly 2 edges => even count
    
    # To find a triangle, we can iterate over all edges and for each edge (u,v),
    # look for a common neighbor w of u and v.
    # The triangle would be u-v-w-u
    
    # To make it efficient, for each edge (u,v), we look through the neighbors of 
    # the node with smaller degree to find a common neighbor
    
    deg = {i: len(adj[i]) for i in range(1, n+1)}
    
    best = None
    
    for u, v in edges:
        # Iterate through the adjacency list of the node with smaller degree
        if deg[u] > deg[v]:
            u, v = v, u
        
        # Look for a common neighbor
        for w in adj[u]:
            if w == v:
                continue
            # Check if w is also connected to v
            if (v, w) in full_edge_set or (w, v) in full_edge_set:
                # Found a triangle: u-v-w-u
                nodes = sorted([u, v, w])
                candidate = tuple(nodes)
                if best is None or candidate < best:
                    best = candidate
    
    print(best[0], best[1], best[2])

if __name__ == "__main__":
    main()