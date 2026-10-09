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
    
    # For each edge, check if it forms a triangle with any previous edge
    for i in range(m):
        u, v = edges[i]
        # Check for common neighbors
        common = adj[u] & adj[v]
        if common:
            # There exists a triangle: u, v, and some w in common
            w = min(common)
            # Output the sorted triplet
            triple = sorted([u, v, w])
            print(triple[0], triple[1], triple[2])
            return

if __name__ == "__main__":
    main()