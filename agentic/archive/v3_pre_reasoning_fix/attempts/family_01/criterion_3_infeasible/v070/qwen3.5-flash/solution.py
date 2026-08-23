import sys

# Increase recursion depth just in case, though not used for this iterative solution
sys.setrecursionlimit(2000)

def solve():
    # Read all input from standard input efficiently
    # Using sys.stdin.read().split() handles all whitespace (newlines, spaces)
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # Adjacency bitmasks
    # adj[u] will have the v-th bit set if there is an edge between u and v
    # We use 1-based indexing for nodes, so bit v corresponds to node v.
    # Since n <= 2000, integers in Python can easily hold these bitmasks.
    adj = [0] * (n + 1)
    
    # Adjacency lists for efficient iteration over neighbors
    adj_list = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    # Sort adjacency lists to ensure we iterate b in increasing order
    # This is crucial for finding the lexicographically smallest triplet
    for i in range(1, n + 1):
        adj_list[i].sort()
        
    # Iterate to find the lexicographically smallest triplet (a, b, c)
    # with a < b < c
    # We iterate a from 1 to n to minimize a.
    for a in range(1, n + 1):
        # Iterate over neighbors b of a
        for b in adj_list[a]:
            # We require a < b < c
            if b <= a:
                continue
            
            # Check if there exists a common neighbor c > b
            # We look for c such that (a, c) and (b, c) are edges.
            # This corresponds to bits set in adj[a] & adj[b].
            common = adj[a] & adj[b]
            
            # We are interested in bits > b.
            # Shift common to the right by b + 1 to align the (b+1)-th bit to position 0.
            # If bit k (where k > b) was set in 'common', it moves to position k - (b + 1) in 'shifted'.
            shifted = common >> (b + 1)
            
            if shifted > 0:
                # Find the lowest set bit in shifted.
                # This corresponds to the smallest c > b because we want lexicographically smallest.
                lsb = shifted & -shifted
                
                # bit_length() gives the number of bits required to represent an integer.
                # For a number with only one bit set, say 2^k, bit_length is k + 1.
                # The index of the bit (0-based) in 'shifted' is bit_length - 1.
                # The actual value of c is b + 1 + (bit_length - 1) = b + bit_length.
                c = b + lsb.bit_length()
                
                # Since we iterate a from 1..n, then b from neighbors (sorted),
                # the first valid triplet found is guaranteed to be the lexicographically smallest.
                print(f"{a} {b} {c}")
                return

if __name__ == '__main__':
    solve()