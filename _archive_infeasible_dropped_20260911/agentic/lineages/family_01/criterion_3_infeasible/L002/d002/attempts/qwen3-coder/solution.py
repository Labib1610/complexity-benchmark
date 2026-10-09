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
    
    # Sort edges to help with ordering
    edges.sort()
    
    # For each edge (u,v), look for a common neighbor w
    best = None
    
    # We'll iterate through all edges and for each edge (u,v), 
    # we check neighbors of u and see if they are also neighbors of v
    for u, v in edges:
        # Get neighbors of u and v
        neigh_u = adj[u]
        neigh_v = adj[v]
        
        # Find common neighbors
        common = neigh_u & neigh_v
        
        for w in common:
            # Create the trio
            trio = tuple(sorted([u, v, w]))
            if best is None or trio < best:
                best = trio
    
    print(best[0], best[1], best[2])

if __name__ == "__main__":
    main()