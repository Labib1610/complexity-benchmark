import sys

# Increase recursion depth just in case, though not strictly needed here
sys.setrecursionlimit(2000)

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

    # adj_list[u] will store neighbors v of u such that u < v
    # This ensures we only iterate forward and maintain u < v < w order implicitly
    adj_list = [[] for _ in range(n + 1)]
    # adj_bitmask[u] will be a bitmask where the v-th bit is set if edge (u, v) exists (with u < v)
    # We use Python's arbitrary-precision integers for bitmasks, which act as bitsets
    adj_bitmask = [0] * (n + 1)

    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        
        # Ensure u < v for directed storage logic. 
        # We only store edges from smaller index to larger index.
        if u > v:
            u, v = v, u
        
        # Check distinctness, though problem guarantees u != v
        if u == v:
            continue
            
        adj_list[u].append(v)
        adj_bitmask[u] |= (1 << v)
        
    # Sort adjacency lists to ensure lexicographical order for b
    # Also remove duplicates if any (though input likely simple graph)
    for i in range(1, n + 1):
        if adj_list[i]:
            # Using set to remove duplicates, then sort
            adj_list[i] = sorted(list(set(adj_list[i])))
            
    # Iterate over a to find the lexicographically smallest triplet
    # Since we want smallest a, then smallest b, then smallest c:
    # We iterate a from 1 to n.
    # For each a, we iterate b in adj_list[a] (sorted), so b increases.
    # For each pair (a, b), we find the smallest valid c.
    for a in range(1, n + 1):
        # Iterate over neighbors b of a
        # Since we stored edges only for u < v, b > a is guaranteed.
        for b in adj_list[a]:
            # We need to find c such that c > b and (a, c) and (b, c) exist.
            # In our directed storage:
            # adj_bitmask[b] contains neighbors of b that are > b (since we only store u -> v where u < v).
            # adj_bitmask[a] contains neighbors of a that are > a.
            # The intersection of these two bitmasks will contain exactly the neighbors c
            # such that c is a neighbor of b (so c > b) and also a neighbor of a.
            # Since c > b > a, edge (a, c) implies bit c is set in adj_bitmask[a].
            
            common = adj_bitmask[a] & adj_bitmask[b]
            
            if common:
                # We need the smallest c. This corresponds to the lowest set bit in common.
                # common & -common isolates the lowest set bit.
                lowest_bit = common & -common
                
                # bit_length() returns the number of bits required to represent the integer.
                # For a power of 2, 2^k, bit_length is k + 1.
                # We want k, so we subtract 1.
                c = lowest_bit.bit_length() - 1
                
                print(f"{a} {b} {c}")
                return

if __name__ == '__main__':
    solve()