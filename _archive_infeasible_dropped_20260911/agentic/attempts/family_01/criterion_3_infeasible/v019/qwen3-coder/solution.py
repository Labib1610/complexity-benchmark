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
    
    # Sort edges to process in order
    edges.sort()
    
    # For each edge (u,v), we look for a node w such that (u,w) and (v,w) are also edges
    for u, v in edges:
        # To maintain lexicographical order, we want u < v < w
        # So we search for w in adj[u] and adj[v] such that w > v
        # We can iterate through neighbors of u and check if they are also neighbors of v
        # and also greater than v
        set_u = adj[u]
        set_v = adj[v]
        common = set_u & set_v
        candidates = [w for w in common if w > v]
        if candidates:
            w = min(candidates)
            print(u, v, w)
            return

if __name__ == "__main__":
    main()