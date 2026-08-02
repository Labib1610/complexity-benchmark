import sys

def solve():
    # Use fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Adjacency list and adjacency matrix (bitsets for efficiency)
    # Since n <= 2000, we can use bitmasks to speed up the intersection
    adj = [[] for _ in range(n + 1)]
    # Using Python's arbitrary precision integers as bitsets
    bit_adj = [0] * (n + 1)
    
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        idx += 2
        
        # Ensure u < v for easier processing
        if u > v:
            u, v = v, u
        
        adj[u].append(v)
        bit_adj[u] |= (1 << v)
        bit_adj[v] |= (1 << u)

    # Sort neighbors to ensure we check candidates in increasing order
    for i in range(1, n + 1):
        adj[i].sort()

    # We want the lexicographically smallest (a, b, c) where a < b < c
    # Iterate a from 1 to n
    for a in range(1, n + 1):
        # For a fixed a, we look for b and c among neighbors of a that are > a
        neighbors_a = [v for v in adj[a] if v > a]
        
        # Iterate through neighbors of a to find b
        for i in range(len(neighbors_a)):
            b = neighbors_a[i]
            
            # We need a third unit c such that c > b and c is a neighbor of both a and b
            # Candidates for c are neighbors of a that are > b
            # We can use bitwise AND between bit_adj[a] and bit_adj[b]
            # Then find the smallest set bit that is > b
            
            common = bit_adj[a] & bit_adj[b]
            
            # Mask out bits <= b
            # mask = ~((1 << (b + 1)) - 1)
            # However, bit_length() and trailing zeros are faster
            
            # We only care about c > b.
            # Shift common right by b+1 and find the lowest set bit.
            shifted = common >> (b + 1)
            if shifted:
                # Find the position of the lowest set bit in shifted
                # (shifted & -shifted).bit_length() - 1 gives the index of the lowest 1
                # The actual unit c is (index + b + 1)
                low_bit = shifted & -shifted
                c = low_bit.bit_length() - 1 + b + 1
                print(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()