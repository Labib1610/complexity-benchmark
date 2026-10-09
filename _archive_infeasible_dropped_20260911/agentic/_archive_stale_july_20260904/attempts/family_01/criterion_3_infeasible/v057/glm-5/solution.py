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
        if u > v:
            u, v = v, u
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))
    
    # Sort edges to process in lexicographical order
    edges.sort()
    
    # For each edge (u, v), check for common neighbors w where w > v
    # This ensures u < v < w and we find lexicographically smallest triangle
    for u, v in edges:
        # Find intersection of neighbors of u and v that are > v
        # Iterate over the smaller set for efficiency
        if len(adj[u]) > len(adj[v]):
            u, v = v, u
        
        for w in adj[u]:
            if w > v and w in adj[v]:
                # Found triangle (original_u, original_v, w)
                # Need to get original u, v values
                # Since we might have swapped, let's recalculate
                # Actually, we need the original u, v from the edge
                # Let's restructure to avoid confusion
                pass
    
    # Let me rewrite more carefully
    for u, v in edges:
        # u < v already guaranteed by sorting
        # Find w such that w > v and w is neighbor of both u and v
        # Iterate through neighbors of u that are > v
        for w in adj[u]:
            if w > v and w in adj[v]:
                print(u, v, w)
                return
    
    # If not found with w > v, check all common neighbors
    # (This handles cases where the triangle might not have w > v)
    for u, v in edges:
        for w in adj[u]:
            if w != v and w in adj[v]:
                result = sorted([u, v, w])
                print(result[0], result[1], result[2])
                return

solve()