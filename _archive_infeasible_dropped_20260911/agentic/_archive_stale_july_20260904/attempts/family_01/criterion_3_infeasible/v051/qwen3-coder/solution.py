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
    
    # Sort edges to process in order
    edges.sort()
    
    # For each edge (u,v), look for a common neighbor w
    for u, v in edges:
        if u >= v:
            continue
        # Get neighbors of u and v
        neighbors_u = adj[u]
        neighbors_v = adj[v]
        
        # Find common neighbors
        common = neighbors_u & neighbors_v
        
        if common:
            # Convert to sorted list to get the smallest lexicographically
            common_list = sorted(common)
            for w in common_list:
                if w > v:  # Ensure a < b < c
                    # Found a triangle: u < v < w
                    print(u, v, w)
                    return

if __name__ == "__main__":
    main()