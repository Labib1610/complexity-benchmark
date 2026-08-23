import sys

def solve():
    # Use fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Using adjacency lists for iteration and bitsets (ints in Python) for O(1) lookup
    # Since n <= 2000, bitsets are efficient.
    adj_list = [[] for _ in range(n + 1)]
    adj_bitset = [0] * (n + 1)
    
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        idx += 2
        if u > v:
            u, v = v, u
        adj_list[u].append(v)
        adj_bitset[u] |= (1 << v)
        adj_bitset[v] |= (1 << u)

    # To find the lexicographically smallest (a, b, c) with a < b < c:
    # Iterate a from 1 to n
    # Iterate b from a + 1 to n
    # If (a, b) is an edge, check for common neighbors c > b
    
    # To optimize, we only iterate over b that are actually neighbors of a.
    # We sort the adjacency lists to ensure we check b in increasing order.
    for a in range(1, n + 1):
        # Sort neighbors of a to ensure we check b in increasing order
        neighbors_a = sorted(adj_list[a])
        
        for b in neighbors_a:
            if b <= a:
                continue
            
            # We need c such that c > b and c is connected to both a and b.
            # This is the intersection of adj_bitset[a] and adj_bitset[b].
            common = adj_bitset[a] & adj_bitset[b]
            
            # We need the smallest c > b.
            # Mask out bits <= b.
            mask = ~((1 << (b + 1)) - 1)
            candidates = common & mask
            
            if candidates:
                # Find the lowest set bit (the smallest c)
                # candidates.bit_length() is not what we need, we need the trailing zeros.
                # In Python 3.10+, we can use candidates.bit_count() or others, 
                # but (candidates & -candidates).bit_length() - 1 works for the lowest set bit.
                c = (candidates & -candidates).bit_length() - 1
                print(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()