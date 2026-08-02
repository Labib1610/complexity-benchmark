import sys

def solve():
    # Use fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Use adjacency sets for O(1) edge lookups
    adj = [set() for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj[u].add(v)
        adj[v].add(u)
        idx += 2
        
    # Convert sets to sorted lists for efficient iteration
    adj_sorted = [sorted(list(adj[i])) for i in range(n + 1)]
    
    # We want lexicographically smallest (a, b, c) with a < b < c
    # Iterate through all possible a, b, c
    # Since n <= 2000, we can optimize the search.
    # For a fixed a, we only check neighbors b > a.
    # For fixed a and b, we check if there exists c > b such that c is in adj[a] and adj[b].
    
    for a in range(1, n + 1):
        neighbors_a = adj_sorted[a]
        # Filter neighbors > a
        b_candidates = [b for b in neighbors_a if b > a]
        for b in b_candidates:
            # We need smallest c > b such that c is in adj[a] and adj[b]
            # Since adj[a] and adj[b] are sorted, we can find intersection efficiently
            # However, with n=2000, checking the intersection is fast enough
            # if we iterate through the smaller neighbor list.
            
            # Identify intersection of neighbors of a and b that are > b
            set_a = adj[a]
            set_b = adj[b]
            
            # Check for common neighbors c > b
            # Iterate through the smaller neighbor list to find c
            if len(set_a) < len(set_b):
                for c in neighbors_a:
                    if c > b and c in set_b:
                        print(f"{a} {b} {c}")
                        return
            else:
                for c in adj_sorted[b]:
                    if c > b and c in set_a:
                        print(f"{a} {b} {c}")
                        return

solve()