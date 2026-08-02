import sys

# Increase recursion depth just in case
sys.setrecursionlimit(2000)

def solve():
    # Read all input from standard input efficiently
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # Adjacency masks for bitset operations
    # adj_mask[i] is an integer where the j-th bit is set if there is an edge between i and j
    # Using 1-based indexing for nodes 1 to n
    adj_mask = [0] * (n + 1)
    
    # Adjacency lists to iterate over neighbors efficiently
    adj_list = [[] for _ in range(n + 1)]

    for _ in range(m):
        try:
            u = int(next(iterator))
            v = int(next(iterator))
        except StopIteration:
            break
            
        # Update adjacency masks
        adj_mask[u] |= (1 << v)
        adj_mask[v] |= (1 << u)
        
        # Update adjacency lists
        adj_list[u].append(v)
        adj_list[v].append(u)

    # Sort adjacency lists to ensure we process neighbors in increasing order
    # This is crucial for finding the lexicographically smallest triple
    for i in range(1, n + 1):
        adj_list[i].sort()

    # We want the lexicographically smallest triple (a, b, c) with a < b < c.
    # We iterate 'a' from 1 to n-2.
    # For each 'a', we iterate 'b' (neighbor of 'a' with b > a) in increasing order.
    # For each pair (a, b), we find the smallest 'c' (neighbor of both a and b with c > b).
    
    for a in range(1, n - 1):
        mask_a = adj_mask[a]
        
        # Iterate over neighbors b of a
        for b in adj_list[a]:
            if b <= a:
                continue
            
            # Check if there exists a common neighbor c > b
            # common represents bits set for nodes connected to both a and b
            common = mask_a & adj_mask[b]
            
            # We need to find the smallest bit index in 'common' that is strictly greater than 'b'.
            # Shifting 'common' right by (b + 1) effectively removes bits <= b
            # and shifts the remaining bits down.
            # The lowest set bit in the shifted value corresponds to the smallest c > b.
            
            common_shifted = common >> (b + 1)
            
            if common_shifted > 0:
                # Extract the lowest set bit
                low_bit = common_shifted & -common_shifted
                
                # Calculate the index of this bit. 
                # low_bit is 2^k for some k. bit_length() returns k + 1.
                # So the index relative to the shift start is k = bit_length() - 1.
                # The actual index c is k + (b + 1).
                
                c = low_bit.bit_length() - 1 + b + 1
                
                # We found the lexicographically smallest triple
                print(f"{a} {b} {c}")
                return

if __name__ == '__main__':
    solve()