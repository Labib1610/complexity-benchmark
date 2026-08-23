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
    
    # Sort edges to ensure we process them in order
    edges.sort()
    
    # For each edge (u,v), look for a common neighbor w
    # such that (u,w) and (v,w) are also edges
    for u, v in edges:
        # We want to find w such that w is connected to both u and v
        # and u < v < w to maintain a < b < c
        for w in adj[u]:
            if w > v and w in adj[v]:
                print(u, v, w)
                return

if __name__ == "__main__":
    main()