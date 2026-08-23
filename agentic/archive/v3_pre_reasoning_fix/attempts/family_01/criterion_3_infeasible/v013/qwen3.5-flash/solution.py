import sys
import bisect

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

    # Adjacency list to store neighbors (for iteration order)
    adj_list = [[] for _ in range(n + 1)]
    # Adjacency mask to store neighbors as bits (for fast intersection)
    adj_mask = [0] * (n + 1)
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        
        adj_list[u].append(v)
        adj_list[v].append(u)
        
        # Set the bit corresponding to the neighbor index
        adj_mask[u] |= (1 << v)
        adj_mask[v] |= (1 << u)
    
    # Sort adjacency lists to ensure we process neighbors in increasing order.
    # This is necessary to find the lexicographically smallest triplet (a, b, c).
    for i in range(1, n + 1):
        adj_list[i].sort()
    
    # Iterate through each node 'a' to find the smallest 'a' in the triplet (a, b, c)
    for a in range(1, n + 1):
        # We iterate over neighbors 'b' of 'a'.
        # Since adj_list[a] is sorted, we will encounter 'b' in increasing order.
        # We only care about 'b' such that a < b.
        # Use bisect to find the starting index of neighbors > a to skip smaller neighbors efficiently.
        idx = bisect.bisect_right(adj_list[a], a)
        
        # Iterate over neighbors b > a
        for b in adj_list[a][idx:]:
            # We have a < b. Now we need to find the smallest c > b such that
            # (a, c) and (b, c) are edges.
            # This means c must be a common neighbor of a and b.
            # We use bitwise intersection to find common neighbors efficiently.
            common = adj_mask[a] & adj_mask[b]
            
            # We are looking for the smallest c > b.
            # In the bitmask, this corresponds to the lowest set bit at a position > b.
            # We can shift the common mask to the right by (b + 1) positions.
            # This removes all bits at positions <= b.
            shifted = common >> (b + 1)
            
            if shifted > 0:
                # There is at least one common neighbor > b.
                # We need the smallest one, which corresponds to the lowest set bit in 'shifted'.
                lsb = shifted & -shifted
                
                # bit_length() returns the number of bits required to represent an integer.
                # For a power of 2 (2^k), bit_length is k + 1.
                # So the index of the bit is bit_length - 1.
                c_idx = lsb.bit_length() - 1
                
                # The actual index c is shifted index + offset (b + 1)
                c = c_idx + b + 1
                
                # We found the lexicographically smallest triplet (a, b, c)
                print(f"{a} {b} {c}")
                return

if __name__ == '__main__':
    solve()