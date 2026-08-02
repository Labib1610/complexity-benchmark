import sys

# Increase recursion depth just in case, though not used here.
sys.setrecursionlimit(2000)

def solve():
    # Read all input from stdin efficiently
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # Adjacency bitmasks
    # adj_mask[u] has bit v set if there is an edge between u and v
    # We use 1-based indexing for bits to match node numbers (1 to n)
    adj_mask = [0] * (n + 1)
    
    # Adjacency lists to iterate neighbors
    adj_list = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        
        # Update bitmasks
        adj_mask[u] |= (1 << v)
        adj_mask[v] |= (1 << u)
        
        # Update adjacency lists
        adj_list[u].append(v)
        adj_list[v].append(u)
        
    # Sort adjacency lists to ensure we process smaller indices first.
    # This is crucial for finding the lexicographically smallest triple (a, b, c).
    # We iterate a from 1 to n, then b from neighbors of a (sorted), then c.
    for i in range(1, n + 1):
        adj_list[i].sort()
        
    # Iterate through all possible values of a
    for a in range(1, n + 1):
        # Iterate through neighbors of a (potential b's)
        # We only consider b > a to satisfy a < b < c
        for b in adj_list[a]:
            if b <= a:
                continue
            
            # We need to find a c such that c > b, and edges (a, c) and (b, c) exist.
            # This means c must be in the intersection of neighbors of a and neighbors of b.
            # We can find common neighbors using bitwise AND of their masks.
            
            common = adj_mask[a] & adj_mask[b]
            
            # We need the smallest common neighbor c > b.
            # We can shift the common mask to the right by (b + 1) to discard bits <= b.
            # The new mask will have bit k set if original mask had bit k + b + 1 set.
            shifted = common >> (b + 1)
            
            if shifted:
                # Find the lowest set bit in shifted
                # This corresponds to the smallest c > b
                lowest_bit = shifted & -shifted
                
                # Calculate the bit index (node number)
                # bit_length() of 2^k is k + 1. So k = bit_length() - 1.
                # The bit index in 'shifted' is relative to the shift amount.
                # The actual node index is (bit_index_in_shifted) + (b + 1).
                c_idx = (lowest_bit.bit_length() - 1) + (b + 1)
                
                # We found the lexicographically smallest triple
                print(f"{a} {b} {c_idx}")
                return

if __name__ == '__main__':
    solve()