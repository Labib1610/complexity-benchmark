import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
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
    
    # Sort edges to process in lexicographic order
    edges.sort()
    
    # For each edge (u, v), find the smallest w such that w > v,
    # w is adjacent to both u and v.
    # This ensures u < v < w, and we process edges in sorted order,
    # so the first triangle found is lexicographically smallest.
    
    for u, v in edges:
        # We need w > v, and w adjacent to both u and v
        # Iterate through neighbors of u that are > v
        # To find the smallest such w, we can iterate sorted neighbors
        # But for efficiency, we iterate and track minimum
        # Since we need smallest w > v, we can check neighbors of u
        # and see if they are > v and also neighbor of v
        
        # Choose the smaller degree vertex to iterate
        if len(adj[u]) > len(adj[v]):
            u, v = v, u
        
        min_w = n + 1
        for w in adj[u]:
            if w > v and w in adj[v]:
                if w < min_w:
                    min_w = w
        
        if min_w <= n:
            # Found triangle (u, v, min_w) with u < v < min_w
            # Since we process edges in sorted order and find smallest w,
            # this is the lexicographically smallest triangle
            print(u, v, min_w)
            return
    
    # Should not reach here as problem guarantees a solution
    print(-1, -1, -1)

if __name__ == "__main__":
    solve()