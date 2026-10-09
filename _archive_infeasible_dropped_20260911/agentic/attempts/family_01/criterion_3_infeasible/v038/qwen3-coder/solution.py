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
    index = 2
    edges = []
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        index += 2
        if u > v:
            u, v = v, u
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))
    
    # Sort adjacency lists for consistent iteration
    for u in adj:
        adj[u] = sorted(list(adj[u]))
    
    # For each edge (u,v), look for a common neighbor w
    # This ensures triangle {u,v,w}
    found = False
    result = None
    
    # Try all edges, and for each edge (u,v), try all neighbors of u to see if 
    # they connect to v as well
    for u in range(1, n+1):
        if u not in adj:
            continue
        for v in adj[u]:
            if v <= u:
                continue
            # Now we have edge u-v with u < v
            # Look for a node w connected to both u and v
            # To find the lexicographically smallest, iterate through neighbors of u
            for w in adj[u]:
                if w <= v:
                    continue
                if w in adj[v]:
                    # Found triangle u-v-w with u < v < w
                    print(u, v, w)
                    return

if __name__ == "__main__":
    main()