import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # Build adjacency list using sets for O(1) lookup
    adj = defaultdict(set)
    edges = []
    
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        index += 2
        if u > v:
            u, v = v, u
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))
    
    # For each edge (u,v), look for a common neighbor w
    # such that u-v, u-w, v-w all exist
    # We want the lexicographically smallest triple
    
    # Convert adjacency list to sorted lists for consistent iteration
    for u in range(1, n+1):
        adj[u] = sorted(list(adj[u]))
    
    # Iterate through all edges
    for u, v in sorted(edges):
        if u > v:
            u, v = v, u
        # Find common neighbors of u and v
        # Since we want lexicographically smallest, we iterate in order
        for w in adj[u]:
            if w > v and w in adj[v]:
                # Found a triangle: u < v < w
                print(u, v, w)
                return

if __name__ == "__main__":
    main()