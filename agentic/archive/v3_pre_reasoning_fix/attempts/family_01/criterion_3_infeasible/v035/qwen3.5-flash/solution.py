import sys

# Increase recursion depth just in case, though not needed for this iterative solution
sys.setrecursionlimit(2000)

def solve():
    # Efficiently read all input from standard input
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
    
    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return
    
    # Adjacency masks and lists
    # Using 0-indexed internally
    # adj_masks[i] will have the j-th bit set if there is an edge between i and j
    adj_masks = [0] * n
    # adj_lists[i] will store the neighbors of i
    adj_lists = [[] for _ in range(n)]
    
    for _ in range(m):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        
        adj_masks[u] |= (1 << v)
        adj_masks[v] |= (1 << u)
        
        adj_lists[u].append(v)
        adj_lists[v].append(u)
    
    # Sort adjacency lists to ensure we process neighbors in increasing order.
    # This is crucial for finding the lexicographically smallest triplet.
    for i in range(n):
        adj_lists[i].sort()
    
    # Iterate over each vertex 'a' as the first vertex of the triplet
    # We want the smallest 'a', so we iterate from 0 to n-1.
    for a in range(n):
        # Iterate over neighbors 'b' of 'a'.
        # Since adj_lists[a] is sorted, we encounter b in increasing order.
        # This ensures that for a fixed 'a', we find the smallest valid 'b' first.
        for b in adj_lists[a]:
            # We need a < b < c.
            # Since we iterate a from 0, we need b > a.
            if b <= a:
                continue
            
            # We need to find a vertex 'c' such that:
            # 1. c is connected to a (c in adj_masks[a])
            # 2. c is connected to b (c in adj_masks[b])
            # 3. c > b
            #
            # Condition 1 & 2 means c is in the intersection of neighbors of a and b.
            # Condition 3 means c > b.
            
            # Bitwise intersection gives all potential c's.
            # This operation is efficient using Python's arbitrary precision integers as bitsets.
            common = adj_masks[a] & adj_masks[b]
            
            # We need to filter for c > b.
            # Mask to clear bits 0 to b:
            # (1 << (b + 1)) - 1 creates a mask of 1s from bit 0 to b.
            mask_clear_le_b = (1 << (b + 1)) - 1
            
            # We want to keep bits > b.
            # In Python, ~x is -x-1, which has infinite 1s to the left.
            # Since common is bounded (bits 0 to n-1), common & ~mask_clear_le_b
            # correctly clears bits 0 to b and keeps higher bits.
            candidates = common & ~mask_clear_le_b
            
            if candidates != 0:
                # We found valid candidates for c.
                # We want the smallest c, which corresponds to the lowest set bit.
                # candidates & -candidates isolates the lowest set bit.
                lowest_bit = candidates & -candidates
                
                # bit_length() returns the number of bits required to represent the integer.
                # For a power of 2, 2^k has bit_length k+1.
                # So index is bit_length - 1.
                c = lowest_bit.bit_length() - 1
                
                # Output the result (converting back to 1-based indexing)
                print(f"{a + 1} {b + 1} {c + 1}")
                return

if __name__ == '__main__':
    solve()