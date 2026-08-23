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
    
    # Sort adjacency lists for deterministic iteration and early termination
    for i in range(1, n + 1):
        adj_list = list(adj[i])
        adj_list.sort()
        adj[i] = adj_list
    
    # Iterate through all edges (u, v) and look for a common neighbor w
    edges.sort()
    for u, v in edges:
        # We want u < v < w, so we iterate through neighbors of u that are > v
        for w in adj[u]:
            if w <= v:
                continue
            # Check if v and w are connected
            if w in adj[v]:
                print(u, v, w)
                return

if __name__ == "__main__":
    main()