import sys

def solve():
    # Read n and m
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [[] for _ in range(n + 1)]
    # Using a bitset approach for O(1) adjacency checks
    # In Python, large integers act as bitsets.
    adj_bitset = [0] * (n + 1)
    
    ptr = 2
    for _ in range(m):
        u = int(input_data[ptr])
        v = int(input_data[ptr+1])
        ptr += 2
        adj[u].append(v)
        adj[v].append(u)
        adj_bitset[u] |= (1 << v)
        adj_bitset[v] |= (1 << u)

    # To find the lexicographically smallest (a, b, c) with a < b < c:
    # We iterate a from 1 to n.
    # For a fixed a, we iterate b from a+1 to n.
    # If (a, b) is an edge, we look for c > b such that (a, c) and (b, c) are edges.
    
    # Optimization: Only check nodes b that are actually connected to a.
    for a in range(1, n + 1):
        # Sort neighbors of a to process b in increasing order
        neighbors_a = sorted([v for v in adj[a] if v > a])
        
        for b in neighbors_a:
            # We need c > b such that c is a neighbor of both a and b.
            # The set of common neighbors is the bitwise AND of their bitsets.
            common = adj_bitset[a] & adj_bitset[b]
            
            # We need the smallest c > b.
            # Mask out bits <= b.
            mask = ~((1 << (b + 1)) - 1)
            candidates = common & mask
            
            if candidates:
                # Find the lowest set bit in candidates
                # Using (candidates & -candidates).bit_length() - 1
                # or simply iterating if the number of set bits is small.
                # Since we need the smallest c, we can use bit_length() on the lowest bit.
                c = (candidates & -candidates).bit_length() - 1
                print(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()