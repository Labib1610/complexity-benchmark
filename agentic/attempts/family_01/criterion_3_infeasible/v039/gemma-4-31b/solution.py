import sys

def solve():
    # Increase recursion depth just in case, though not needed for this iterative approach
    sys.setrecursionlimit(2000)
    
    # Read n and m
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Use adjacency lists for neighbors and a bitset-like approach for fast intersection
    # In Python, integers can act as bitsets.
    # adj_bitsets[i] will be a bitmask where the j-th bit is 1 if i and j interfere.
    adj_bitsets = [0] * (n + 1)
    # Also keep sorted adjacency lists to iterate over smaller indices first
    adj_lists = [[] for _ in range(n + 1)]
    
    ptr = 2
    for _ in range(m):
        u = int(input_data[ptr])
        v = int(input_data[ptr+1])
        ptr += 2
        
        # Ensure u < v for consistent processing
        if u > v:
            u, v = v, u
        
        adj_bitsets[u] |= (1 << v)
        adj_bitsets[v] |= (1 << u)
        adj_lists[u].append(v)
        adj_lists[v].append(u)
    
    # Sort adjacency lists to ensure lexicographical order
    for i in range(1, n + 1):
        adj_lists[i].sort()
        
    # To find the lexicographically smallest triple (a, b, c):
    # We iterate a from 1 to n, then b from a+1 to n, then c from b+1 to n.
    # Optimization: Only iterate over b that are neighbors of a.
    for a in range(1, n + 1):
        # We only care about neighbors of a that are > a
        neighbors_a = [v for v in adj_lists[a] if v > a]
        
        # We want to find the smallest b among neighbors_a, and then the smallest c.
        # Since neighbors_a is sorted, we iterate through b in increasing order.
        for b in neighbors_a:
            # We need c > b such that c is a neighbor of both a and b.
            # This is the intersection of adj_bitsets[a] and adj_bitsets[b].
            common = adj_bitsets[a] & adj_bitsets[b]
            
            # We need the smallest c > b.
            # We can mask out all bits <= b.
            # The mask for bits > b is ~((1 << (b + 1)) - 1)
            mask = ~((1 << (b + 1)) - 1)
            candidates = common & mask
            
            if candidates:
                # Find the index of the lowest set bit
                # (candidates & -candidates).bit_length() - 1 gives the index of the LSB
                lsb = candidates & -candidates
                c = lsb.bit_length() - 1
                print(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()