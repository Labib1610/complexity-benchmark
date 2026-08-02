import sys

def solve():
    # Use fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [set() for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        adj[u].add(v)
        adj[v].add(u)
        idx += 2
        
    # Convert sets to sorted lists for iteration
    adj_list = [sorted(list(s)) for s in adj]
    
    # We need the lexicographically smallest triplet (a, b, c) with a < b < c
    # Iterate a from 1 to n
    for a in range(1, n + 1):
        neighbors_a = adj_list[a]
        # Only consider neighbors b > a
        for i in range(len(neighbors_a)):
            b = neighbors_a[i]
            if b <= a:
                continue
            
            # To find c, check intersection of neighbors of a and neighbors of b
            # Both neighbors_a and neighbors_b are sorted
            neighbors_b = adj_list[b]
            
            # Use two pointers to find common neighbors c > b
            ptr_a = i + 1
            ptr_b = 0
            
            # Optimization: since we only need the smallest c for this (a, b),
            # we can use the sorted property
            while ptr_a < len(neighbors_a) and ptr_b < len(neighbors_b):
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