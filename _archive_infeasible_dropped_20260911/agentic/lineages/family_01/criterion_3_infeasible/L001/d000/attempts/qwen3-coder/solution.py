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
        if u > v:
            u, v = v, u
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # Sort adjacency lists for deterministic behavior
    for key in adj:
        adj[key] = sorted(adj[key])
    
    # Create a set of edges for O(1) lookup
    edge_set = set(edges)
    
    # We'll iterate through all edges and try to find a triangle
    # For each edge (u,v), we look for a node w such that (u,w) and (v,w) also exist
    
    found = False
    result = None
    
    # To get lexicographically smallest, we iterate u from 1 to n,
    # for each u, v from neighbors of u with v > u,
    # and for each such (u,v), we check w from neighbors of u with w > v
    # and verify if (v,w) exists.
    
    for u in range(1, n+1):
        if u not in adj:
            continue
        neighbors_u = adj[u]
        len_u = len(neighbors_u)
        for i in range(len_u):
            v = neighbors_u[i]
            if v <= u:
                continue
            # Now look for w in neighbors of u such that w > v and (v,w) exists
            for j in range(i+1, len_u):
                w = neighbors_u[j]
                if w <= v:
                    continue
                # Check if (v,w) is an edge
                if w in adj[v]:
                    print(u, v, w)
                    return

if __name__ == "__main__":
    main()