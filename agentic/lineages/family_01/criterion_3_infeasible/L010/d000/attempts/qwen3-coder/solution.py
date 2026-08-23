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
        if u > v:
            u, v = v, u
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # Sort edges to process in order
    edges.sort()
    
    # For each edge (u,v), look for a neighbor of u that is also a neighbor of v
    for u, v in edges:
        # Get common neighbors of u and v
        common = adj[u] & adj[v]
        if common:
            # Found a triangle
            w = min(common)
            # Output the triple in sorted order
            triple = sorted([u, v, w])
            print(triple[0], triple[1], triple[2])
            return

if __name__ == "__main__":
    main()