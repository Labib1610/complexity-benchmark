import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    graph = [set() for _ in range(n + 1)]
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        index += 2
        if u > v:
            u, v = v, u
        edges.append((u, v))
        graph[u].add(v)
        graph[v].add(u)
    
    # Sort edges to process in order
    edges.sort()
    
    # Create adjacency set for fast lookup
    adj = [set() for _ in range(n+1)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    
    # We want to find a triangle (a,b,c) such that all three edges (a,b), (b,c), (a,c) exist
    # Iterate through all edges and find a common neighbor
    found = False
    result = None
    
    # For each edge (u,v), check for a node w such that (u,w) and (v,w) also exist
    for u, v in edges:
        if found:
            break
        # Find common neighbors of u and v
        for w in adj[u]:
            if w != v and w in adj[v]:
                # Found a triangle: u, v, w
                triple = sorted([u, v, w])
                result = triple
                found = True
                break
    
    print(result[0], result[1], result[2])

if __name__ == "__main__":
    main()