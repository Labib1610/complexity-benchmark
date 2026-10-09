import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    forbidden = [[False] * (n + 1) for _ in range(n + 1)]
    
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        idx += 2
        edges.append((u, v))
        forbidden[u][v] = True
        forbidden[v][u] = True
    
    # Build adjacency list
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # Sort adjacency lists to help with ordering
    for u in adj:
        adj[u].sort()
    
    # We need to find the lexicographically smallest triple (a,b,c) such that:
    # - a < b < c
    # - (a,b) is forbidden
    # - (a,c) is forbidden
    # - (b,c) is forbidden
    
    # To do this efficiently, we'll iterate through all edges (a,b) with a < b
    # For each such edge, we look for a node c > b such that (a,c) and (b,c) are also edges
    # Since we want the lexicographically smallest triple, we iterate a from 1 to n
    # For each a, we consider its neighbors b where b > a
    # For each such (a,b), we look for c > b that is a neighbor of both a and b
    
    # To make this efficient, for each (a,b), we intersect the neighbor lists of a and b
    # and look for elements > max(a,b) = b (since b > a)
    
    best = None
    
    # Iterate through all nodes a from 1 to n
    for a in range(1, n + 1):
        if a not in adj:
            continue
        # For each neighbor b of a where b > a
        for b in adj[a]:
            if b <= a:
                continue
            # Now we want to find c such that c > b and c is in both adj[a] and adj[b]
            # Let's make sets for fast intersection (but since n can be 2000, let's use sorted lists)
            # We'll merge the sorted lists adj[a] and adj[b] to find common elements > b
            
            # Get neighbors of a and b, sorted
            neigh_a = adj[a]
            neigh_b = adj[b]
            
            i, j = 0, 0
            while i < len(neigh_a) and j < len(neigh_b):
                ca = neigh_a[i]
                cb = neigh_b[j]
                if ca == cb:
                    c = ca
                    if c > b:
                        # Found a valid triple (a, b, c)
                        triple = (a, b, c)
                        if best is None or triple < best:
                            best = triple
                        # Since we're looking for the lexicographically smallest,
                        # and our iteration is in order, the first one we find for this (a,b)
                        # with minimal c is good enough for this (a,b)
                        # But to get the overall minimum, we should check all
                        # However, since we want the global minimum, we keep track
                        # Actually, to get the true lex min, we should break when we find the first c>b
                        # But that's not right because there might be another (a', ...) that's smaller
                        # So we should continue searching all possibilities
                        # But given the constraints, and that we want the global minimum,
                        # we can optimize: once we fix a, and go through b>a,
                        # and for each find the minimal c>b connected to both,
                        # we just need to track the global minimum
                        
                        # But actually, we're iterating a from small to large,
                        # so the first valid triple we find will be the lex min
                        # No, that's not true either, because even for same a,
                        # different b may lead to different c
                        
                        # Correct approach:
                        # We're iterating a=1,2,... For each a, b>a, we find c>b
                        # connected to both. Among all these, we want the lex smallest
                        # So we compare all found triples
                        
                        # But wait, we want the GLOBAL minimum, not per (a,b)
                        
                        # So we should just collect all valid triples and sort them
                        # But that's inefficient
                        
                        # Better: as we generate triples in some order, we keep track of the minimum
                        # What order? We're iterating a small to large, then b>a small to large,
                        # then c>b in sorted order of adj lists intersection
                        # So the first few triples we encounter might not be the minimum
                        
                        # But there's a smarter way:
                        # Once we fix a, and go through b, and for each b find the minimal c>b
                        # connected to both, we get candidate triples (a, b, c)
                        # Among these, the one with smallest b, and for same b, smallest c
                        # But across different a, we still need to compare
                        
                        # Actually, let's think differently:
                        # We want the lexicographically smallest (a,b,c)
                        # So we should:
                        # 1. Try a=1, then a=2, ..., until we find any valid triple
                        # 2. For fixed a, try b=a+1, then a+2, ...
                        # 3. For fixed (a,b), try c=b+1, b+2, ... in increasing order
                        # 4. Return the first triple found
                        
                        # But that would require checking all c>b, which is what we're doing
                        # in the intersection. And we want the minimum over ALL possibilities
                        
                        # So let's just do the intersection properly and keep track of minimum
                        
                        # But wait, there's a better way:
                        # Since we want the global minimum, and we're iterating a from 1 up,
                        # if we find a triple starting with a=x, and later we try a=x' > x,
                        # we don't care about those, because (x,...) < (x',...)
                        
                        # So we can optimize: for each a, we only need to find the lexicographically
                        # smallest triple starting with a, if any, and compare with current best
                        
                        # But even simpler: just iterate through all possibilities and keep track
                        # of the minimum
                        
                        pass  # We'll implement the proper search below instead of this nested logic
                        
                    elif c == b:
                        # This can't happen since c > b in our search condition
                        pass
                    # Move both pointers forward to find next potential match
                    i += 1
                    j += 1
                elif ca < cb:
                    i += 1
                else:
                    j += 1
    
    # Let's re-implement cleanly:
    # For each edge (u,v) with u<v, we want to find w>v such that (u,w) and (v,w) exist
    # Among all such triangles, we want the lexicographically smallest
    
    min_triple = None
    
    # Sort edges to process in a consistent order, but we actually need to check all
    # Let's just work with the adjacency structure
    
    for a in range(1, n+1):
        if a not in adj:
            continue
        # Get neighbors of a
        neighbors_a = set(adj[a])
        for b in adj[a]:
            if b <= a:
                continue
            # Get neighbors of b
            neighbors_b = set(adj[b])
            # Find common neighbors of a and b that are > b
            common = neighbors_a & neighbors_b
            for c in common:
                if c > b:
                    triple = (a, b, c)
                    if min_triple is None or triple < min_triple:
                        min_triple = triple
                    # To find the minimal c for this (a,b), we can break on first
                    # But to get the global minimum, we should check all
                    # Actually, since common is a set, the order is not sorted
                    # So to get the lex min triple, we should check all c in common with c > b
                    
    print(min_triple[0], min_triple[1], min_triple[2])

if __name__ == "__main__":
    main()