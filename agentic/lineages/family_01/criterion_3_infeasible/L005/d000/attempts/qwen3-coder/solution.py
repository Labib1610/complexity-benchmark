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
    
    # Convert sets to lists for faster intersection
    for u in adj:
        adj[u] = list(adj[u])
    
    # We'll iterate through all edges and try to find a triangle
    # To get the lexicographically smallest, we can iterate through
    # edges in a way that ensures we check smaller nodes first.
    
    # First, sort the adjacency lists so we process smaller neighbors first
    for u in adj:
        adj[u].sort()
    
    # Sort edges primarily by first node, then by second
    edges.sort()
    
    best = None
    
    # For each edge (u,v), we look for a common neighbor w
    # which would form triangle u-v-w
    for u, v in edges:
        if u >= v:
            continue
        # Iterate through neighbors of u and v to find common ones
        # Use the sorted lists for efficiency
        i = j = 0
        while i < len(adj[u]) and j < len(adj[v]):
            w1 = adj[u][i]
            w2 = adj[v][j]
            if w1 == w2:
                w = w1
                if w != u and w != v:
                    # Found a triangle u, v, w
                    # Ensure they are in increasing order
                    triple = tuple(sorted([u, v, w]))
                    if best is None or triple < best:
                        best = triple
                i += 1
                j += 1
            elif w1 < w2:
                i += 1
            else:
                j += 1
        if best is not None:
            break  # Since edges are sorted, first found will be lex smallest
            
    if best is None:
        # Should not happen as per problem statement
        # But just in case, let's do brute force
        candidates = set()
        for u, v in edges:
            for w in adj[u]:
                if w in adj[v] and w != u and w != v:
                    triple = tuple(sorted([u, v, w]))
                    candidates.add(triple)
        best = min(candidates)
        
    print(best[0], best[1], best[2])

if __name__ == "__main__":
    main()