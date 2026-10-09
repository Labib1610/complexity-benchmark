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
    
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        idx += 2
        if u > v:
            u, v = v, u
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # Sort edges to help with finding the lexicographically smallest triangle
    edges.sort()
    
    # For each edge (u,v), look for a common neighbor w
    for u, v in edges:
        if u > v:
            u, v = v, u
        # Iterate through neighbors of u
        for w in adj[u]:
            if w != v and w > v:
                # Check if v and w are connected
                if w in adj[v]:
                    print(u, v, w)
                    return

if __name__ == "__main__":
    main()