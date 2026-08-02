import sys

# Increase recursion depth just in case, though not strictly needed
sys.setrecursionlimit(2000)

def solve():
    # Read all input from standard input efficiently
    # sys.stdin.read().split() reads all tokens at once, which is fast
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
    
    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # adj[u] will store a bitmask where the v-th bit is set if v > u and (u, v) is an edge
    # Using integers as bitmasks is efficient for N <= 2000
    # This structure implicitly handles ordering: adj[u] only has bits for neighbors > u
    adj = [0] * (n + 1)
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        
        # Store edge in the node with smaller index to maintain u < v property
        if u > v:
            u, v = v, u
        
        # Set bit v in adj[u]
        adj[u] |= (1 << v)
        
    # Iterate through each worker a from 1 to n
    # We want the lexicographically smallest triplet (a, b, c) with a < b < c
    for a in range(1, n + 1):
        # We need to find b > a such that (a, b) is an edge.
        # These b's correspond to the bits set in adj[a].
        # We iterate them in increasing order to ensure lexicographical order.
        temp = adj[a]
        while temp:
            # Extract the lowest set bit (smallest b > a)
            lsb = temp & -temp
            b = lsb.bit_length() - 1
            temp ^= lsb
            
            # Now we have a candidate pair (a, b) with a < b.
            # We need to find c > b such that (a, c) and (b, c) are edges.
            # adj[a] contains neighbors of a > a.
            # adj[b] contains neighbors of b > b.
            # The intersection adj[a] & adj[b] contains neighbors common to both.
            # Since these neighbors are in adj[b], they must be > b.
            # So any bit set in 'common' is a valid c > b.
            
            common = adj[a] & adj[b]
            
            if common:
                # There exists at least one c. We want the smallest c.
                # The smallest set bit in 'common' corresponds to the smallest c.
                c_lsb = common & -common
                c = c_lsb.bit_length() - 1
                
                # Found the lexicographically smallest triplet
                print(f"{a} {b} {c}")
                return

if __name__ == '__main__':
    solve()