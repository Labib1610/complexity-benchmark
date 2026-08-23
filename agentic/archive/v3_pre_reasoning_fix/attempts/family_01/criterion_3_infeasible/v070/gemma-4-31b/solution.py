import sys

def solve():
    # Use fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Adjacency matrix for O(1) lookup
    # Using a list of sets or bitsets for efficiency. 
    # Given n=2000, a bitset (integer in Python) is very efficient.
    adj = [0] * (n + 1)
    
    ptr = 2
    for _ in range(m):
        u = int(input_data[ptr])
        v = int(input_data[ptr+1])
        ptr += 2
        # Store edges such that we can easily iterate through neighbors
        # Use bitmask to represent adjacency for fast intersection
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)

    # To find the lexicographically smallest (a, b, c) with a < b < c:
    # We iterate a from 1 to n, then b from a+1 to n.
    # For each (a, b) that are connected, we look for c > b such that
    # c is connected to both a and b.
    # The smallest such c will be the first bit set in (adj[a] & adj[b]) that is > b.
    
    for a in range(1, n + 1):
        # Optimization: only check b's that are neighbors of a and > a
        # Get neighbors of a that are > a
        neighbors_a = adj[a] >> (a + 1)
        if neighbors_a == 0:
            continue
        
        # We need to iterate through set bits of neighbors_a
        # To ensure lexicographical order, we check b in increasing order.
        # However, since we need the smallest b, we can just iterate from a+1 to n.
        for b in range(a + 1, n + 1):
            if (adj[a] >> b) & 1:
                # We found a pair (a, b). Now find smallest c > b.
                # c must be a neighbor of both a and b.
                common = adj[a] & adj[b]
                # Mask out bits <= b
                common &= ~((1 << (b + 1)) - 1)
                
                if common:
                    # Find the lowest set bit (the smallest c)
                    # c = (common & -common).bit_length() - 1 is not quite right for large ints
                    # Use .bit_length() on (common & -common) or simply:
                    c = (common & -common).bit_length() - 1
                    # Wait, (common & -common) gives a power of 2. 
                    # Example: common = 0b10100 (bits 2 and 4 set), common & -common = 0b00100 (bit 2).
                    # bit_length of 0b100 is 3. So c = 3-1 = 2.
                    # Let's verify: if common = 8 (1000), bit_length is 4, c=3.
                    # Since we need the index of the bit, bit_length() - 1 works for powers of 2.
                    
                    # Let's use a safer way to find the lowest set bit:
                    # c = (common & -common).bit_length() - 1
                    # Actually, Python's bit_length() is perfect here.
                    print(f"{a} {b} {c}")
                    return

if __name__ == "__main__":
    solve()