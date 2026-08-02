import sys

def solve():
    # Read n and m
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Use an adjacency list and adjacency sets for O(1) lookup
    adj = [set() for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        adj[u].add(v)
        adj[v].add(u)
        idx += 2
        
    # Convert sets to sorted lists for deterministic iteration
    adj_list = [sorted(list(s)) for s in adj]
    
    # We want the lexicographically smallest (a, b, c) with a < b < c.
    # Iterate a from 1 to n, b from a+1 to n, c from b+1 to n.
    # To optimize, iterate a, then b in adj[a], then check if c is in adj[a] and adj[b].
    for a in range(1, n + 1):
        neighbors_a = adj_list[a]
        # Only consider b > a
        for b in neighbors_a:
            if b <= a:
                continue
            
            # Find common neighbors of a and b that are > b
            # This ensures we find c > b.
            # We intersect neighbors_a and neighbors_b.
            # Since neighbors are sorted, we can use two pointers.
            neighbors_b = adj_list[b]
            
            ptr_a = 0
            ptr_b = 0
            len_a = len(neighbors_a)
            len_b = len(neighbors_b)
            
            while ptr_a < len_a and ptr_b < len_b:
                val_a = neighbors_a[ptr_a]
                val_b = neighbors_b[ptr_b]
                
                if val_a == val_b:
                    if val_a > b:
                        print(f"{a} {b} {val_a}")
                        return
                    ptr_a += 1
                    ptr_b += 1
                elif val_a < val_b:
                    ptr_a += 1
                else:
                    ptr_b += 1

solve()