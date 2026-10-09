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
    
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        idx += 2
        if u > v:
            u, v = v, u
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # Convert sets to lists for faster intersection
    adj_list = {k: list(v) for k, v in adj.items()}
    
    min_trio = None
    
    # For each edge (u,v), look for a common neighbor w
    # which forms a triangle (clique of size 3)
    for u, v in edges:
        # Get neighbors of u and v
        neigh_u = adj_list.get(u, [])
        neigh_v = adj_list.get(v, [])
        
        # Use set for the smaller list for efficiency
        set_u = set(neigh_u)
        
        # Check for common neighbors
        for w in neigh_v:
            if w in set_u:
                # Found a triangle: u, v, w
                trio = tuple(sorted([u, v, w]))
                if min_trio is None or trio < min_trio:
                    min_trio = trio
    
    print(min_trio[0], min_trio[1], min_trio[2])

if __name__ == "__main__":
    main()