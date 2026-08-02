import sys

def solve():
    # Use fast I/O
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
        if u > v:
            u, v = v, u
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))
        idx += 2
        
    # To find the lexicographically smallest triple (a, b, c) with a < b < c:
    # We iterate a from 1 to n-2, b from a+1 to n-1, c from b+1 to n.
    # To do this efficiently, we iterate over all edges (u, v) as the potential (a, b).
    # Since we need the lexicographically smallest, we sort the edges.
    
    edges.sort()
    
    # Pre-sort adjacency lists to make intersection faster and output deterministic
    for i in range(1, n + 1):
        adj[i] = sorted(list(adj[i]))
    
    # We look for a triple (a, b, c) where a < b < c.
    # This means a-b, a-c, and b-c are edges.
    # Iterate through all edges (a, b) with a < b.
    # Then iterate through all neighbors c of a that are > b.
    # Check if c is also a neighbor of b.
    
    best_triple = None
    
    for a in range(1, n + 1):
        # Optimization: if we already found a triple, we can prune search
        if best_triple and a > best_triple[0]:
            break
            
        for b in adj[a]:
            if b <= a:
                continue
            
            # Now we need c > b such that c is in adj[a] and adj[b]
            # Since adj[a] and adj[b] are sorted, we can intersect them
            # or just iterate through the smaller list.
            
            # Find common neighbors c > b
            # To be lexicographically smallest, we want smallest a, then b, then c.
            # The current loop structure naturally explores in lexicographical order
            # if we process edges (a, b) in sorted order.
            
            # To get smallest c, we just need the first c > b in the intersection.
            for c in adj[a]:
                if c <= b:
                    continue
                if c in adj[b]:
                    # Found the smallest c for this (a, b)
                    if best_triple is None or (a, b, c) < best_triple:
                        best_triple = (a, b, c)
                    # Since we want the smallest c for this (a, b), we break
                    break
                    
    if best_triple:
        print(f"{best_triple[0]} {best_triple[1]} {best_triple[2]}")

if __name__ == '__main__':
    solve()