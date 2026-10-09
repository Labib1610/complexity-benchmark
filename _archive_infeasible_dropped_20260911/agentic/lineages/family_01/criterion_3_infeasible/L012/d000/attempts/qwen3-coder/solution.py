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
    
    # Sort edges to process in order
    edges.sort()
    
    # For each edge (u,v), look for a neighbor of u that is also a neighbor of v
    for u, v in edges:
        if u >= v:
            continue
        # Get neighbors of u and v
        neighbors_u = adj[u]
        neighbors_v = adj[v]
        # Find common neighbors
        common = neighbors_u & neighbors_v
        if common:
            # Find the smallest common neighbor
            w = min(common)
            if u < v < w:
                print(u, v, w)
                return
            elif u < w < v:
                print(u, w, v)
                return
            elif w < u < v:
                print(w, u, v)
                return

if __name__ == "__main__":
    main()