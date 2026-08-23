import sys

def solve():
    # Set recursion limit if necessary, though not needed for this approach
    # Read n and m
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [set() for _ in range(n + 1)]
    ptr = 2
    for _ in range(m):
        u = int(input_data[ptr])
        v = int(input_data[ptr+1])
        adj[u].add(v)
        adj[v].add(u)
        ptr += 2
    
    # To find the lexicographically smallest (a, b, c) with a < b < c:
    # We iterate a from 1 to n.
    # For a fixed a, we look for b > a such that (a, b) is an edge.
    # We want the smallest such b.
    # For a fixed a and b, we look for c > b such that (a, c) and (b, c) are edges.
    # We want the smallest such c.
    
    # Pre-sort adjacency lists to iterate in increasing order
    sorted_adj = [sorted(list(adj[i])) for i in range(n + 1)]
    
    # To optimize, we can use bitsets for fast intersection, but with n=2000, 
    # a simple nested loop with set intersection might be slow in Python.
    # However, we only need to iterate through neighbors of a that are > a.
    
    # Use bitmasks for faster intersection checks
    # Since n is up to 2000, we can use Python's arbitrary precision integers as bitsets.
    bitsets = [0] * (n + 1)
    for i in range(1, n + 1):
        mask = 0
        for neighbor in adj[i]:
            mask |= (1 << neighbor)
        bitsets[i] = mask

    for a in range(1, n + 1):
        # Neighbors of a that are greater than a
        neighbors_a = [v for v in sorted_adj[a] if v > a]
        
        for b in neighbors_a:
            # We need c > b such that c is a neighbor of both a and b.
            # The common neighbors are bitsets[a] & bitsets[b].
            common = bitsets[a] & bitsets[b]
            
            # We need the smallest c > b.
            # We can find this by checking bits of 'common' starting from b+1.
            # Since we need the smallest c, we can use the bit_length or a loop.
            # However, the most efficient way to find the lowest set bit > b:
            # Mask out bits <= b.
            mask_gt_b = ~((1 << (b + 1)) - 1)
            candidates = common & mask_gt_b
            
            if candidates:
                # Find the lowest set bit
                # (candidates & -candidates).bit_length() - 1 gives the index of the lowest set bit
                # because candidates is positive, candidates & -candidates extracts the lowest bit.
                low_bit = candidates & -candidates
                c = low_bit.bit_length() - 1
                print(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()