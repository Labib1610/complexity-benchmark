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
    
    # For each edge, look for a third node that connects to both endpoints
    for i in range(m):
        u, v = edges[i]
        # Get common neighbors of u and v
        common = adj[u] & adj[v]
        if common:
            # Find the smallest neighbor
            w = min(common)
            # Output the triplet in sorted order
            triple = sorted([u, v, w])
            print(triple[0], triple[1], triple[2])
            return

if __name__ == "__main__":
    main()