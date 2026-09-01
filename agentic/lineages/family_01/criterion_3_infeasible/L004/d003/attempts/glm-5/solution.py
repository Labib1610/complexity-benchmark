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
    
    # Sort adjacency lists to iterate neighbors in order.
    # This helps in finding the lexicographically smallest triangle efficiently.
    sorted_adj = [sorted(list(s)) for s in adj]
    
    # We iterate u from 1 to n to find the smallest u in a triangle.
    # Once we find a triangle with the smallest u, we need to find the 
    # lexicographically smallest triangle (u, v, w) for that u.
    # Since we iterate v and w in increasing order, the first valid (v, w) found
    # will be the smallest.
    
    for u in range(1, n + 1):
        neighbors_u = sorted_adj[u]
        # We need to check pairs (v, w) from neighbors_u such that v < w and edge (v, w) exists.
        # To find the smallest such pair, we iterate v from smallest to largest,
        # and for each v, iterate w from smallest to largest in neighbors_u.
        # Since neighbors_u is sorted, this yields pairs in lexicographical order.
        
        len_neighbors = len(neighbors_u)
        for i in range(len_neighbors):
            v = neighbors_u[i]
            if v <= u: 
                continue # We want u < v < w for unique ordered triplet
            
            # For a fixed v, we check w > v.
            # The set of neighbors of v is adj[v].
            # We iterate through potential w from neighbors_u.
            # Since neighbors_u is sorted, we can start checking from index i + 1.
            for j in range(i + 1, len_neighbors):
                w = neighbors_u[j]
                if w <= v:
                    continue # Should not happen if sorted and distinct, but safety check
                
                if w in adj[v]:
                    # Found the lexicographically smallest triangle for this u
                    print(u, v, w)
                    return

if __name__ == '__main__':
    solve()