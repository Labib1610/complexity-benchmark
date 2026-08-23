import sys

def solve():
    data = sys.stdin.buffer.read().split()
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
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # Sort edges lexicographically so we find the lexicographically smallest triangle.
    edges.sort()
    
    # For each edge (u, v), find the smallest w > v such that w is adjacent to both u and v.
    # Since edges are sorted, the first such triangle is lexicographically smallest.
    for u, v in edges:
        # Iterate over the smaller adjacency list to find common neighbors.
        if len(adj[u]) > len(adj[v]):
            u, v = v, u
        # Now adj[u] is the smaller set. We need w > v to maintain sorted order (u < v < w).
        # Actually, we need w such that u < v < w and w is in both adj[u] and adj[v].
        # Since we swapped, u might be > v now, but we need to check the original order.
        # Let's restore original order for the check.
        if u > v:
            u, v = v, u
        
        # Find common neighbors w where w > v
        # Iterate through the smaller adjacency set
        for w in adj[u]:
            if w > v and w in adj[v]:
                print(f"{u} {v} {w}")
                return
    
    # Should not reach here since problem guarantees a triangle exists
    print("-1")

solve()