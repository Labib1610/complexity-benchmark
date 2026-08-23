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
        if u > v:
            u, v = v, u
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # Sort adjacency lists for consistent ordering
    for key in adj:
        adj[key] = sorted(adj[key])
    
    # Create edge set for fast lookup
    edge_set = set(edges)
    
    # We'll iterate through all edges and try to find a triangle
    # For each edge (u,v), we look for a node w such that (u,w) and (v,w) exist
    found = False
    result = None
    
    # To get lexicographically smallest, we should iterate u from 1 to n,
    # and for each u, iterate through its neighbors v where v > u,
    # and for each such v, iterate through neighbors w of u where w > v
    for u in range(1, n+1):
        if u not in adj:
            continue
        neighbors_u = adj[u]
        # Only consider neighbors greater than u
        candidates_v = [v for v in neighbors_u if v > u]
        # Now for each pair (u,v), check for common neighbor w > v
        for i in range(len(candidates_v)):
            v = candidates_v[i]
            if v <= u:
                continue
            # Get neighbors of v that are greater than v
            neighbors_v = adj[v]
            candidates_w_from_v = [w for w in neighbors_v if w > v]
            # Get neighbors of u that are greater than v
            candidates_w_from_u = [w for w in neighbors_u if w > v]
            
            # Convert to sets for intersection
            set_w_u = set(candidates_w_from_u)
            set_w_v = set(candidates_w_from_v)
            common = set_w_u & set_w_v
            
            if common:
                # Found a triangle: u, v, and some w in common
                w = min(common)
                print(u, v, w)
                return

if __name__ == "__main__":
    main()