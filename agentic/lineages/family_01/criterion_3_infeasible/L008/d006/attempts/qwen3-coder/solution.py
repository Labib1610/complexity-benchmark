import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n, m = int(data[0]), int(data[1])
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
    
    # For each edge (u,v), look for a third node w such that (u,w) and (v,w) are also edges
    for u, v in edges:
        if u >= v:
            continue
        # Find common neighbors of u and v
        common = adj[u] & adj[v]
        for w in sorted(common):
            if w > v:
                # Found a triangle: u, v, w
                print(u, v, w)
                return

if __name__ == "__main__":
    main()