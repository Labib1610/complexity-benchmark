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
    
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        idx += 2
        edges.append((u, v))
        graph[u].add(v)
        graph[v].add(u)
    
    # We need to find a triangle in the graph
    # That is, three nodes a, b, c such that all three edges (a,b), (b,c), (a,c) exist
    
    # To ensure lexicographical minimality, we iterate through all triplets (a,b,c) with a < b < c
    # But to optimize, we'll check for each edge (u,v), and see if there's a node w such that
    # both (u,w) and (v,w) exist, and u < v < w
    
    # First, let's sort the adjacency list for consistent iteration
    for i in range(1, n + 1):
        graph[i] = sorted(graph[i])
    
    # Iterate through all edges
    for u, v in edges:
        if u > v:
            u, v = v, u  # Ensure u < v
        # Now look for a common neighbor w of u and v such that v < w
        # Since we want u < v < w
        neighbors_u = set(graph[u])
        for w in graph[v]:
            if w > v and w in neighbors_u:
                # Found a triangle u, v, w with u < v < w
                print(u, v, w)
                return

if __name__ == "__main__":
    main()