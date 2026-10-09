import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [set() for _ in range(n + 1)]
    edges = []
    
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))
    
    # Sort adjacency lists for lexicographic iteration
    adj_list = [sorted(s) for s in adj]
    
    best = None
    
    # Strategy: iterate over edges (u, v), then check common neighbors w
    # To find lexicographically smallest, we check edges in order (u, v)
    # and neighbors w in sorted order
    
    # Sort edges for consistent processing
    edges_sorted = sorted(edges)
    
    for u, v in edges_sorted:
        # Ensure u < v for consistent ordering
        if u > v:
            u, v = v, u
        
        # Find common neighbors
        # Iterate through smaller adjacency set for efficiency
        if len(adj[u]) <= len(adj[v]):
            neighbors = adj_list[u]
            check = adj[v].__contains__
        else:
            neighbors = adj_list[v]
            check = adj[u].__contains__
        
        for w in neighbors:
            if w == u or w == v:
                continue
            if check(w):
                # Found triangle (u, v, w)
                a, b, c = sorted([u, v, w])
                if best is None or (a, b, c) < best:
                    best = (a, b, c)
                    # Since we process edges and neighbors in sorted order,
                    # first found is lexicographically smallest
                    print(a, b, c)
                    return
    
    # Should always find a triangle per problem guarantee
    if best:
        print(best[0], best[1], best[2])

if __name__ == "__main__":
    solve()