import sys
from bisect import bisect_right

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

    # adj_mask[u] will store a bitmask where the v-th bit is 1 if guild v is a neighbor of u.
    # We use 1-based indexing for guilds, so we need size n + 1.
    adj_mask = [0] * (n + 1)
    
    # adj[u] will store a list of neighbors of u.
    # Using sets initially to handle potential duplicate edges and then sort them.
    adj = [set() for _ in range(n + 1)]
    
    # Precompute powers of 2 for bit manipulation.
    # pow2[v] is 1 << v.
    # This avoids recomputing large integers repeatedly.
    pow2 = [1 << i for i in range(n + 1)]
    
    # Process edges
    for _ in range(m):
        try:
            u = int(next(iterator))
            v = int(next(iterator))
        except StopIteration:
            break
        
        adj[u].add(v)
        adj[v].add(u)
        
        adj_mask[u] |= pow2[v]
        adj_mask[v] |= pow2[u]
        
    # Sort adjacency lists to ensure we iterate neighbors in increasing order (lexicographical requirement)
    for i in range(1, n + 1):
        adj[i] = sorted(list(adj[i]))
        
    # Iterate to find the lexicographically smallest triangle (a, b, c) with a < b < c
    # We iterate 'a' from 1 to n to find the smallest 'a'.
    for a in range(1, n + 1):
        # We only consider neighbors b > a.
        # Since adj[a] is sorted, we can use binary search to find the start index.
        # bisect_right returns the insertion point after all elements <= a.
        idx = bisect_right(adj[a], a)
        
        # Iterate over neighbors b > a
        for i in range(idx, len(adj[a])):
            b = adj[a][i]
            
            # Find common neighbors c of a and b.
            # The common neighbors are indicated by the bits set in (adj_mask[a] & adj_mask[b]).
            common = adj_mask[a] & adj_mask[b]
            
            # We need c > b.
            # We can shift the common mask right by (b + 1) bits.
            # This shifts the bit corresponding to b+1 to position 0, and discards bits <= b.
            # If 'common' has bits set at positions > b, 'shifted' will be non-zero.
            shifted = common >> (b + 1)
            
            if shifted:
                # If shifted is non-zero, there exists at least one c > b.
                # To find the smallest such c (lexicographically smallest triple),
                # we need the lowest set bit in 'shifted'.
                # (shifted & -shifted) isolates the lowest set bit.
                # .bit_length() returns the number of bits required to represent the integer.
                # For a power of 2 (2^k), bit_length() is k + 1.
                # So the index k is bit_length() - 1.
                # The actual guild index c is k + (b + 1) because we shifted right by b + 1.
                
                lowest_bit = shifted & -shifted
                c = lowest_bit.bit_length() - 1 + b + 1
                
                print(f"{a} {b} {c}")
                return

if __name__ == '__main__':
    solve()