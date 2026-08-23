import sys

# Increase recursion depth just in case, though not strictly needed
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

    # Adjacency list to maintain order of neighbors
    adj = [[] for _ in range(n + 1)]
    # Adjacency mask for fast intersection using bitwise operations
    # We use an integer as a bitset where the k-th bit represents node k.
    adj_mask = [0] * (n + 1)
    
    # Read edges
    for _ in range(m):
        try:
            u = int(next(iterator))
            v = int(next(iterator))
        except StopIteration:
            break
        
        adj[u].append(v)
        adj[v].append(u)
        adj_mask[u] |= (1 << v)
        adj_mask[v] |= (1 << u)
        
    # Sort adjacency lists to ensure we check neighbors in increasing order
    # This is crucial for finding the lexicographically smallest result.
    for i in range(1, n + 1):
        adj[i].sort()
        
    # Iterate through each node 'a' as the first element of the triple
    # Since we want the lexicographically smallest triple (a, b, c),
    # we iterate 'a' from 1 upwards.
    for a in range(1, n + 1):
        # Iterate through neighbors 'b' of 'a'
        # Since adj[a] is sorted, 'b' will be encountered in increasing order.
        # This ensures that for a fixed 'a', we check the smallest possible 'b' first.
        for b in adj[a]:
            # We require a < b < c
            if b > a:
                # We need to find 'c' such that c is connected to both 'a' and 'b'
                # and c > b.
                # Using adjacency masks, common neighbors are found by bitwise AND.
                common_mask = adj_mask[a] & adj_mask[b]
                
                # We only care about neighbors 'c' > b.
                # Shifting the mask right by (b + 1) removes bits for nodes <= b.
                # The bit for node 'c' (where c > b) will be at position (c - (b + 1)).
                shifted_mask = common_mask >> (b + 1)
                
                # If shifted_mask is non-zero, there exists at least one such 'c'.
                if shifted_mask > 0:
                    # We want the smallest such 'c', which corresponds to the 
                    # lowest set bit in shifted_mask.
                    # (x & -x) isolates the lowest set bit in an integer.
                    lowest_bit = shifted_mask & -shifted_mask
                    
                    # bit_length() returns the number of bits required to represent the integer.
                    # For a power of 2 (2^k), bit_length() is k + 1.
                    # Thus, the exponent k = bit_length() - 1.
                    # Here, k = c - (b + 1), so c = k + b + 1.
                    c = lowest_bit.bit_length() - 1 + b + 1
                    
                    # Since we iterate 'a' increasing, then 'b' increasing,
                    # and find smallest 'c', this is the lexicographically smallest triple.
                    print(f"{a} {b} {c}")
                    return

if __name__ == '__main__':
    solve()