import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    adj = defaultdict(list)
    edge_set = set()
    
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        idx += 2
        if u > v:
            u, v = v, u
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
        edge_set.add((u, v))
    
    # Sort adjacency lists for consistent ordering
    for key in adj:
        adj[key].sort()
    
    best = None
    
    # Iterate through all edges
    for u, v in edges:
        # Find common neighbors of u and v
        neighbors_u = set(adj[u])
        neighbors_v = set(adj[v])
        common = neighbors_u & neighbors_v
        
        for w in common:
            # Ensure all three nodes are distinct and form a triangle
            nodes = sorted([u, v, w])
            triangle = (nodes[0], nodes[1], nodes[2])
            if best is None or triangle < best:
                best = triangle
    
    print(best[0], best[1], best[2])

if __name__ == "__main__":
    main()