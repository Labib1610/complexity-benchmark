import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Using bitsets for adjacency lists. Node indices are 1-based.
    adj = [0] * (n + 1)
    
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        idx += 2
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
        
    for a in range(1, n + 1):
        # We only consider neighbors b > a
        # To iterate over set bits in adj[a] that are > a:
        # We can mask out bits <= a
        mask_a = adj[a] & ~((1 << (a + 1)) - 1)
        
        b = a + 1
        while mask_a:
            # Get the lowest set bit in mask_a
            # This corresponds to the smallest b > a adjacent to a
            lowest_bit = mask_a & -mask_a
            b = lowest_bit.bit_length() - 1
            
            # We need c > b such that c is adjacent to both a and b
            # So we look at adj[b] & adj[a], and mask out bits <= b
            common = adj[b] & adj[a] & ~((1 << (b + 1)) - 1)
            
            if common:
                # The smallest c is the lowest set bit in common
                c = (common & -common).bit_length() - 1
                print(f"{a} {b} {c}")
                return
            
            # Remove b from mask_a to continue searching for the next b
            mask_a &= ~lowest_bit

if __name__ == "__main__":
    solve()