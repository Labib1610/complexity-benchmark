import sys
from collections import defaultdict

def main():
    n, m = map(int, sys.stdin.readline().split())
    
    # Build adjacency list and set for O(1) lookup
    adj = defaultdict(set)
    edges = []
    
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        if u > v:
            u, v = v, u
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))
    
    # Sort vertices by degree descending for optimization
    vertices = list(range(1, n + 1))
    vertices.sort(key=lambda x: len(adj[x]), reverse=True)
    
    # For each edge, check if there's a common neighbor
    for u, v in edges:
        if u > v:
            u, v = v, u
            
        # Check neighbors of the node with smaller degree
        if len(adj[u]) > len(adj[v]):
            u, v = v, u
            
        for w in adj[u]:
            if w != v and w in adj[v]:
                # Found a triangle
                result = sorted([u, v, w])
                print(result[0], result[1], result[2])
                return

if __name__ == "__main__":
    main()