import sys

# Increase recursion depth just in case, though not strictly needed here
sys.setrecursionlimit(2000)

def solve():
    # Read all input from stdin efficiently
    # Using sys.stdin.read().split() handles all whitespace (newlines, spaces)
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # Adjacency masks
    # Using 1-based indexing for vertices, so size n+1
    # adj_mask[u] will have bit v set if u and v interfere
    # This allows for fast intersection of neighbor sets using bitwise AND
    adj_mask = [0] * (n + 1)
    
    # Adjacency lists for iteration
    # adj_list[u] will contain neighbors of u
    adj_list = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        
        adj_mask[u] |= (1 << v)
        adj_mask[v] |= (1 << u)
        
        adj_list[u].append(v)
        adj_list[v].append(u)
        
    # Sort adjacency lists to ensure we process neighbors in increasing order
    # This is crucial for finding the lexicographically smallest triplet (a, b, c)
    # We want smallest a, then smallest b > a, then smallest c > b
    for i in range(1, n + 1):
        adj_list[i].sort()
        
    # Iterate to find the lexicographically smallest triplet (a, b, c)
    # a < b < c
    # We iterate a from 1 to n
    # Then iterate b in neighbors of a such that b > a
    # Then find smallest c in neighbors of a such that c > b and c is neighbor of b
    
    for a in range(1, n + 1):
        # Optimization: if a has no neighbors, skip
        if not adj_list[a]:
            continue
            
        mask_a = adj_mask[a]
        
        for b in adj_list[a]:
            if b <= a:
                continue
            
            # We need a common neighbor c > b
            # common = adj_mask[a] & adj_mask[b]
            # This gives us a bitmask where bit c is set if c is connected to both a and b
            
            mask_b = adj_mask[b]
            common = mask_a & mask_b
            
            # We only care about bits > b
            # -(1 << (b + 1)) creates a mask with 0s at positions 0..b and 1s elsewhere
            # This effectively clears bits <= b from common
            valid = common & -(1 << (b + 1))
            
            if valid:
                # If valid is non-zero, there exists at least one c > b connected to both a and b.
                # We want the smallest such c.
                # (valid & -valid) isolates the lowest set bit (LSB) in valid.
                # .bit_length() - 1 gives the index of that bit.
                c = (valid & -valid).bit_length() - 1
                print(f"{a} {b} {c}")
                return

if __name__ == '__main__':
    solve()