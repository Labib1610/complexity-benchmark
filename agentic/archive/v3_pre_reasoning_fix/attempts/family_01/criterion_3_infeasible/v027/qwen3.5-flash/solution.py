import sys

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

    # adj_mask[u] is a bitmask where the v-th bit is 1 if (u, v) is a prohibited pair.
    # This allows O(1) edge checks and fast intersection operations.
    adj_mask = [0] * (n + 1)
    
    # adj_list[u] stores neighbors v of u such that v > u, sorted in increasing order.
    # This allows us to iterate b > a in lexicographical order.
    adj_list = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        
        # Set bits in masks for both u and v
        adj_mask[u] |= (1 << v)
        adj_mask[v] |= (1 << u)
        
        # Store neighbors in list only if v > u to ensure a < b order later
        if u < v:
            adj_list[u].append(v)
        else:
            adj_list[v].append(u)
            
    # Sort the adjacency lists to ensure we iterate b in increasing order
    for i in range(1, n + 1):
        adj_list[i].sort()
        
    # Iterate through all possible smallest elements 'a'
    for a in range(1, n + 1):
        # Iterate through neighbors 'b' of 'a' such that b > a (lexicographical order)
        for b in adj_list[a]:
            # We need to find the smallest 'c' > b such that (a, c) and (b, c) are prohibited pairs.
            # This corresponds to finding the smallest bit set in the intersection of masks of a and b,
            # at a position greater than b.
            
            # Intersection of neighbors
            common = adj_mask[a] & adj_mask[b]
            
            # Shift right to ignore bits <= b
            # We want the smallest bit at index c > b.
            # In the shifted value, the bit at index 0 corresponds to c = b + 1.
            shifted = common >> (b + 1)
            
            if shifted > 0:
                # Find the position of the lowest set bit in 'shifted'
                # (shifted & -shifted) isolates the lowest set bit (as a power of 2)
                # .bit_length() returns the number of bits required to represent the integer
                # For a power of 2, say 2^k, bit_length is k + 1.
                # The bit index in 'shifted' is k.
                # So c = (b + 1) + k = b + 1 + (bit_length - 1) = b + bit_length
                c = (shifted & -shifted).bit_length() + b
                
                # Output the result and terminate
                print(f"{a} {b} {c}")
                return

if __name__ == '__main__':
    solve()