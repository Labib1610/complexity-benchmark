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
    
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        index += 2
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # Convert to sorted list for consistent iteration
    for u in adj:
        adj[u] = sorted(adj[u])
    
    # We want the lexicographically smallest triangle
    # So we iterate through all edges and look for a common neighbor
    
    edges_sorted = sorted(edges, key=lambda x: (min(x[0], x[1]), max(x[0], x[1])))
    
    for u, v in edges_sorted:
        if u > v:
            u, v = v, u
        # Now u < v
        # Look for a node w such that w connects to both u and v
        # And we want the lexicographically smallest such triangle
        
        neighbors_u = set(adj[u])
        neighbors_v = set(adj[v])
        common = neighbors_u & neighbors_v
        
        if common:
            # Find the smallest w in common neighbors
            w = min(common)
            # Ensure ordering a < b < c
            a, b, c = sorted([u, v, w])
            print(a, b, c)
            return

if __name__ == "__main__":
    main()