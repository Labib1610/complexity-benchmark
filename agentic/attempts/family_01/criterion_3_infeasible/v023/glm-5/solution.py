import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    n = int(next(iterator))
    m = int(next(iterator))
    
    adj = [set() for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].add(v)
        adj[v].add(u)
    
    # Sort adjacency lists for lexicographical iteration
    sorted_adj = [sorted(s) for s in adj]
    
    # We want the lexicographically smallest triple (a, b, c).
    # We iterate a from 1 to n, then b from a+1 to n, then c from b+1 to n.
    # To check if (a, b, c) is a triangle, we need to verify edges (a,b), (a,c), (b,c).
    # We can optimize by iterating a, then iterating b in adj[a] (where b > a),
    # then checking intersection of adj[a] and adj[b] for some c > b.
    
    # Iterate a in increasing order
    for a in range(1, n + 1):
        # Iterate b in increasing order from neighbors of a
        for b in sorted_adj[a]:
            if b <= a:
                continue
            
            # We have edge (a, b). We need c such that c > b, and c in adj[a] and c in adj[b].
            # To find the smallest valid c, we iterate through neighbors of a greater than b
            # and check if they are in adj[b].
            # We iterate neighbors of 'a' because 'a' is the smallest node in the triple,
            # so its degree might be smaller (heuristic).
            for c in sorted_adj[a]:
                if c <= b:
                    continue
                if c in adj[b]:
                    # Found the lexicographically smallest triple
                    print(a, b, c)
                    return

if __name__ == '__main__':
    solve()