import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    index = 2
    edges = []
    adj = defaultdict(set)
    
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        index += 2
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # Convert edges to a set for O(1) lookup
    edge_set = set()
    for u, v in edges:
        if u > v:
            u, v = v, u
        edge_set.add((u, v))
    
    # We want to find a triangle (a,b,c) such that a<b<c and all three edges exist
    # Enumerate all possible pairs (a,b) with a < b
    # For each such pair, check if there exists a c > b such that (a,c) and (b,c) also exist
    
    # Sort adjacency lists for deterministic iteration
    for u in adj:
        adj[u] = sorted(adj[u])
    
    best = None
    
    # Try all pairs (a, b) where a < b
    for a in sorted(adj.keys()):
        for b in adj[a]:
            if b <= a:
                continue
            # Now look for c > b such that both (a,c) and (b,c) exist
            # Iterate through neighbors of b that are greater than b
            for c in adj[b]:
                if c <= b:
                    continue
                # Check if (a, c) exists
                if c in adj[a]:
                    candidate = tuple(sorted([a, b, c]))
                    if best is None or candidate < best:
                        best = candidate
    
    if best:
        print(best[0], best[1], best[2])

if __name__ == "__main__":
    main()