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
    
    # We'll iterate through all edges and for each edge (u,v), 
    # we'll look for a common neighbor w such that u-v-w forms a triangle.
    # To ensure lexicographical minimality, we'll process nodes in order.
    
    # First, sort the edges to help with ordering
    edges.sort()
    
    min_triad = None
    
    for u, v in edges:
        if u > v:
            u, v = v, u
        # Now u < v
        # Find common neighbors of u and v
        neighbors_u = adj[u]
        neighbors_v = adj[v]
        common = neighbors_u & neighbors_v
        
        for w in sorted(common):
            if w > u and w > v:
                # We have a triangle u-v-w with u < v < w
                triad = (u, v, w)
                if min_triad is None or triad < min_triad:
                    min_triad = triad
            elif w < u:
                # w < u < v
                triad = (w, u, v)
                if min_triad is None or triad < min_triad:
                    min_triad = triad
            elif u < w < v:
                # u < w < v
                triad = (u, w, v)
                if min_triad is None or triad < min_triad:
                    min_triad = triad
    
    if min_triad:
        print(min_triad[0], min_triad[1], min_triad[2])

if __name__ == "__main__":
    main()