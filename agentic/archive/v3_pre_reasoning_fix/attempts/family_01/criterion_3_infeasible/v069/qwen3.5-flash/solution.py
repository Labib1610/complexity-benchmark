import sys

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

    # adj_mask[u] will store a bitmask where the v-th bit is set if u and v are connected
    # Using 1-based indexing for convenience, so size n + 1
    adj_mask = [0] * (n + 1)
    
    # adj_list[u] will store a list of neighbors v where v > u
    # This helps in iterating b > a efficiently
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
        
        # Populate adj_list for forward edges (u < v)
        # We only store v in adj_list[u] if v > u
        # This ensures that when we iterate 'b' in adj_list[a], b > a
        if v > u:
            adj_list[u].append(v)
        else:
            adj_list[v].append(u)
            
    # Sort adjacency lists to ensure we process 'b' in increasing order
    # This is crucial for finding the lexicographically smallest triple
    for i in range(1, n + 1):
        adj_list[i].sort()
        
    # Iterate through each node 'a' to be the first element of the triple
    for a in range(1, n + 1):
        # Iterate through neighbors 'b' of 'a' such that b > a
        for b in adj_list[a]:
            # We need to find a neighbor 'c' of both 'a' and 'b' such that c > b
            # This corresponds to a bit in (adj_mask[a] & adj_mask[b]) that is at position > b
            
            # Find common neighbors
            common_neighbors = adj_mask[a] & adj_mask[b]
            
            # Check if there is any common neighbor with index > b
            # We shift right by (b + 1) to discard bits <= b
            shifted = common_neighbors >> (b + 1)
            
            if shifted > 0:
                # There exists at least one such 'c'.
                # We want the smallest such 'c', which corresponds to the lowest set bit in 'shifted'.
                # (shifted & -shifted) isolates the lowest set bit.
                lowest_bit = shifted & -shifted
                
                # Calculate the index of this bit.
                # bit_length() returns the number of bits required to represent the integer.
                # For a power of 2 (2^k), bit_length() is k + 1.
                # So the index (0-based) is bit_length() - 1.
                # Since we shifted by (b + 1), the actual index is (b + 1) + (bit_length - 1).
                c = b + 1 + lowest_bit.bit_length() - 1
                
                # We found the lexicographically smallest triple (a, b, c)
                print(f"{a} {b} {c}")
                return

if __name__ == '__main__':
    solve()