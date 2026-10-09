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
    adj = defaultdict(set)
    
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
        # We want to find w such that w is connected to both u and v
        # Iterate through neighbors of u, check if they're also neighbors of v
        # Since we want lexicographically smallest trio, iterate through neighbors in sorted order
        candidates = sorted(adj[u] & adj[v])
        for w in candidates:
            if u < v < w:
                print(u, v, w)
                return

if __name__ == "__main__":
    main()