import sys

def solve():
    # Read all input from standard input
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
    
    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # Adjacency masks. adj_masks[u] stores the bitmask of neighbors of u.
    # Indices are 1-based.
    adj_masks = [0] * (n + 1)
    edges = []
    
    # Parse edges
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        
        # Ensure u < v for consistent processing
        if u > v:
            u, v = v, u
        
        edges.append((u, v))
        
        # Set bits in adjacency masks
        # Node indices 1..n map to bits 1..n
        adj_masks[u] |= (1 << v)
        adj_masks[v] |= (1 << u)
    
    # Sort edges to process in lexicographical order of pairs (u, v)
    # This ensures we find the lexicographically smallest triangle first.
    edges.sort()
    
    # Iterate through sorted edges to find the first valid triangle
    for u, v in edges:
        # We are looking for c > v such that (u, c) and (v, c) are edges.
        # This forms a triangle (u, v, c) with u < v < c.
        
        # Find common neighbors
        common = adj_masks[u] & adj_masks[v]
        
        # Filter neighbors to be > v
        # Mask with bits 0..v set is (1 << (v + 1)) - 1
        # We want to clear these bits. In Python, ~x acts as infinite 1s to the left.
        mask_clear = (1 << (v + 1)) - 1
        potential_c = common & ~mask_clear
        
        if potential_c:
            # Find the smallest valid c.
            # This is the lowest set bit in potential_c.
            lowest_bit = potential_c & -potential_c
            c = lowest_bit.bit_length() - 1
            
            print(f"{u} {v} {c}")
            return

if __name__ == '__main__':
    solve()