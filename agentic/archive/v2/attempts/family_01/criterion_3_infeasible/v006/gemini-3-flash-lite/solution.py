import sys

def solve():
    # Read n and m
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [set() for _ in range(n + 1)]
    edges = []
    
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        
        # Ensure u < v for adjacency storage
        if u > v:
            u, v = v, u
        adj[u].add(v)
        edges.append((u, v))
    
    # Sort edges to iterate in lexicographical order (u, v)
    edges.sort()
    
    # We want to find the lexicographically smallest (a, b, c) with a < b < c.
    # This means we want the smallest a, then smallest b, then smallest c.
    # Iterate through all edges (u, v) as the first two members of the triple.
    # Since we want the lexicographically smallest (a, b, c), we iterate
    # through all possible edges (a, b) and check for a common neighbor c > b.
    
    for a in range(1, n + 1):
        # Sort neighbors of a to check potential c's in order
        neighbors_a = sorted(list(adj[a]))
        for i in range(len(neighbors_a)):
            b = neighbors_a[i]
            # We are looking for c such that (a, b, c) is a clique
            # c must be a neighbor of a and a neighbor of b
            # To ensure a < b < c, we only look at neighbors of b that are > b
            # and also in neighbors_a
            
            # Optimization: intersection of neighbors
            # Since b > a, b is already in neighbors_a.
            # We look for c in (neighbors_a intersect neighbors_b) where c > b.
            
            # To find the lexicographically smallest triple, we check b's
            # and then c's.
            if b < a: continue
            
            # To make it efficient:
            # We need to intersect adj[a] and adj[b]
            # Since we want the smallest c, we can iterate through the smaller set
            set_a = adj[a]
            set_b = adj[b]
            
            # To ensure we find the absolute smallest (a, b, c),
            # we iterate a from 1 to n, b from sorted neighbors of a,
            # then c from sorted intersection.
            
            common = sorted(list(set_a.intersection(set_b)))
            for c in common:
                if c > b:
                    print(f"{a} {b} {c}")
                    return

solve()