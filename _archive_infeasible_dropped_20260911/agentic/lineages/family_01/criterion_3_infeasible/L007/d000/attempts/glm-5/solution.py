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
    
    best = None
    
    # Method 1: Check for triangles containing an edge (u, v)
    # For each edge, check if there's a common neighbor w
    for u, v in edges:
        # We want to find w such that u-w and v-w are edges
        # To optimize, iterate over the smaller adjacency set
        if len(adj[u]) > len(adj[v]):
            u, v = v, u
        
        for w in adj[u]:
            if w > v and w in adj[v]:
                # Found triangle (u, v, w) with u < v < w
                cand = (u, v, w)
                if best is None or cand < best:
                    best = cand
    
    # Method 2: Check for triangles where the smallest vertex is isolated
    # from the other two (i.e., no edge between the two larger vertices)
    # This handles cases where the edge between larger vertices might be missing
    # from our edge list processing above (though the above should catch all)
    # Actually, the above method catches all triangles where u < v < w
    # because we iterate over all edges (u,v) and find w > v
    
    # But we need to be careful: what if the triangle is (a, b, c) with a < b < c
    # but the edge (b, c) is not in our edges list?
    # That's impossible since we iterate over ALL edges
    
    # However, there's a subtle case: what if the triangle is found via
    # an edge (u, v) where u is not the smallest?
    # Let's trace: triangle (a, b, c) with a < b < c
    # Edges: (a,b), (a,c), (b,c)
    # When we process edge (a,b), we look for w > b in adj[a], find c, check c in adj[b] -> yes
    # When we process edge (a,c), we look for w > c in adj[a], find nothing (since c is largest)
    # When we process edge (b,c), we look for w > c in adj[b], find nothing
    # So we find the triangle exactly once via edge (a,b)
    
    # But wait, what if we swap u,v during processing?
    # For edge (a,b): if len(adj[a]) > len(adj[b]), we swap to (b,a)
    # Then we iterate over adj[b] looking for w > a
    # But we need w > b (since we want a < b < w)
    # After swap, u=b, v=a, so we need w > v = a
    # But we want w > b (the original larger vertex)
    # This is a bug!
    
    # Let me reconsider: after swap, u is the one with smaller adj, v is the other
    # We iterate over adj[u] and check if w > v and w in adj[v]
    # For triangle (a,b,c) with a < b < c:
    # Original edge (a,b): u=a, v=b (or swapped based on adj sizes)
    # We want to find w such that w > max(u,v) = b and w is common neighbor
    # After potential swap, we check w > v
    # If original (a,b) stays as u=a, v=b: we check w > b, correct
    # If swapped to u=b, v=a: we check w > a, but we want w > b
    # So we might find w=c where c > a but c might not be > b
    # But c > b since c is largest in triangle, so c > b > a, so c > a is true
    # And we check w in adj[v] = adj[a], which is true
    # So we find the triangle, but the condition w > v might not give us sorted order
    
    # Actually, let me re-examine:
    # After swap, u and v are such that len(adj[u]) <= len(adj[v])
    # We iterate over adj[u] and check if w > v and w in adj[v]
    # For triangle (a,b,c) with a < b < c:
    # Case 1: edge (a,b) processed, no swap: u=a, v=b, check w > b, find c, correct
    # Case 2: edge (a,b) processed, swapped: u=b, v=a, check w > a, find c (since c > a)
    #         But then cand = (b, a, c) which is not sorted!
    #         We need to sort: min(b,a,c), mid, max = (a, b, c)
    
    # So the fix is: when we find u, v, w, we need to sort them
    # Let me update the code
    
    # Actually, looking at my code again:
    # I have: if w > v and w in adj[v]
    # After swap, v might be smaller than u
    # So w > v doesn't guarantee w > u
    # The triangle vertices are u, v, w but not necessarily sorted
    
    # Let me rewrite more carefully:
    
    # Reset and redo
    best = None
    
    for u, v in edges:
        # u < v already from input processing
        # Find common neighbors w where w > v (to ensure u < v < w)
        # Iterate over smaller adjacency set for efficiency
        if len(adj[u]) < len(adj[v]):
            for w in adj[u]:
                if w > v and w in adj[v]:
                    cand = (u, v, w)
                    if best is None or cand < best:
                        best = cand
        else:
            for w in adj[v]:
                if w > v and w in adj[u]:
                    cand = (u, v, w)
                    if best is None or cand < best:
                        best = cand
    
    # Now we also need to check for triangles where the smallest vertex a
    # has edges to b and c, but b and c are not directly connected
    # Wait, that's not a triangle then!
    # A triangle requires all three edges: (a,b), (a,c), (b,c)
    
    # So the above should find all triangles
    # But let me also add a fallback O(n^3) check for very small n
    
    if best is None:
        # Fallback: check all triples
        for a in range(1, n - 1):
            for b in range(a + 1, n):
                if b not in adj[a]:
                    continue
                for c in range(b + 1, n + 1):
                    if c in adj[a] and c in adj[b]:
                        cand = (a, b, c)
                        if best is None or cand < best:
                            best = cand
                        break  # Found smallest c for this (a,b)
                if best and best[0] == a:
                    break  # Found smallest triangle starting with a
            if best:
                break  # Found the overall smallest
    
    if best:
        print(f"{best[0]} {best[1]} {best[2]}")

solve()