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
    adj = [set() for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        index += 2
        if u > v:
            u, v = v, u
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # Sort edges to help with lexicographical ordering
    edges.sort()
    
    # For each edge (u,v), look for a node w such that (u,w) and (v,w) are also edges
    for u, v in edges:
        # We want to find w such that w in adj[u] and w in adj[v]
        # To maintain lexicographical order, we need u < v < w
        common_neighbors = adj[u] & adj[v]
        for w in sorted(common_neighbors):
            if w > v:
                print(u, v, w)
                return

if __name__ == "__main__":
    main()