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
    
    # We'll iterate through all edges and for each edge (u,v), 
    # we look for a third node w such that (u,w) and (v,w) are also edges.
    # This forms a triangle.
    
    # To make it efficient, for each edge, we check the adjacency list of the node 
    # with smaller degree to find common neighbors.
    
    # First, let's sort the edges so that for each edge (u,v), deg[u] <= deg[v]
    # But since we don't want to modify the original list too much,
    # we will just process accordingly.
    
    # Let's build degree list
    deg = [len(adj[i]) for i in range(n + 1)]
    
    best = None
    
    for u, v in edges:
        # We want to iterate over the adjacency list of the node with smaller degree
        if deg[u] > deg[v]:
            u, v = v, u
        
        # Now iterate through neighbors of u and check if they are also neighbors of v
        for w in adj[u]:
            if w != v and w in adj[v]:
                # Found a triangle: u, v, w
                # Sort them to get canonical form
                triple = tuple(sorted([u, v, w]))
                if best is None or triple < best:
                    best = triple
    
    # It's guaranteed that at least one exists
    a, b, c = best
    print(a, b, c)

if __name__ == "__main__":
    main()