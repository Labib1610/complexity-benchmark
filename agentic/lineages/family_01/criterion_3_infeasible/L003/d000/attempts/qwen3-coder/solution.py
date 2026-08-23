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
        if u > v:
            u, v = v, u
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # Sort edges to help with finding lexicographically smallest triple
    edges.sort()
    
    # For each edge (u,v), look for a node w such that (u,w) and (v,w) are also edges
    for u, v in edges:
        if u >= v:
            continue
        # Check common neighbors of u and v
        neighbors_u = adj[u]
        neighbors_v = adj[v]
        
        # Iterate through the smaller set for efficiency
        if len(neighbors_u) > len(neighbors_v):
            neighbors_u, neighbors_v = neighbors_v, neighbors_u
            
        for w in neighbors_u:
            if w in neighbors_v:
                # Found a triangle: u, v, w
                triple = sorted([u, v, w])
                print(triple[0], triple[1], triple[2])
                return

if __name__ == "__main__":
    main()