import sys

def solve():
    # Use fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Use adjacency matrix for O(1) lookup. 
    # Given n <= 2000, a bitset-like approach or a 2D array is feasible.
    # In Python, a list of integers (bitsets) is often faster for intersection.
    adj_bitsets = [0] * (n + 1)
    adj_list = [[] for _ in range(n + 1)]
    
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        idx += 2
        if u > v:
            u, v = v, u
        adj_bitsets[u] |= (1 << v)
        adj_bitsets[v] |= (1 << u)
        adj_list[u].append(v)
        adj_list[v].append(u)

    # To find the lexicographically smallest (a, b, c) with a < b < c:
    # We iterate a from 1 to n, then b from a+1 to n.
    # For a fixed a and b, we need c > b such that c is connected to both a and b.
    # This is equivalent to finding the smallest bit set in (adj_bitsets[a] & adj_bitsets[b]) that is > b.
    
    # Pre-sort adjacency lists to iterate b in increasing order
    for i in range(1, n + 1):
        adj_list[i].sort()

    for a in range(1, n + 1):
        # Only consider neighbors of a that are greater than a
        neighbors_a = [v for v in adj_list[a] if v > a]
        
        # To optimize, we can use the bitset of a
        bitset_a = adj_bitsets[a]
        
        for b in neighbors_a:
            # We need c > b such that c is connected to both a and b
            # common_neighbors = bitset_a & adj_bitsets[b]
            common = bitset_a & adj_bitsets[b]
            
            # We need the smallest c > b. 
            # Mask out bits <= b
            mask = ~((1 << (b + 1)) - 1)
            candidates = common & mask
            
            if candidates:
                # Find the lowest set bit in candidates
                # This is the smallest c > b
                c = (candidates & -candidates).bit_length() - 1
                # Since we are iterating a and b in increasing order, 
                # the first triplet found is the lexicographically smallest.
                print(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()