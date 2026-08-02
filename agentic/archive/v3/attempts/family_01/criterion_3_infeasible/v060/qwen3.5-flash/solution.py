import sys

# Increase recursion depth just in case, though not strictly needed for this iterative solution
sys.setrecursionlimit(2000)

def solve():
    # Read all input from stdin efficiently
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # Adjacency masks for fast intersection and neighbor checks
    # adj_mask[u] will be a bitmask where the k-th bit is 1 if u is connected to k
    # We use integers as bitsets. Python handles arbitrarily large integers efficiently.
    adj_mask = [0] * (n + 1)
    
    # Adjacency list for iterating neighbors
    adj = [[] for _ in range(n + 1)]

    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        
        adj_mask[u] |= (1 << v)
        adj_mask[v] |= (1 << u)
        
        adj[u].append(v)
        adj[v].append(u)

    # Sort adjacency lists to ensure we process neighbors in increasing order
    # This helps in finding the lexicographically smallest b
    for i in range(1, n + 1):
        adj[i].sort()

    # Iterate through all possible vertices for 'a'
    # We want to minimize 'a' first, so we iterate from 1 to n.
    for a in range(1, n + 1):
        # Iterate through neighbors of 'a' to find 'b'
        # Since adj[a] is sorted, we check b in increasing order.
        # This ensures we find the smallest valid 'b' for the current 'a'.
        for b in adj[a]:
            if b <= a:
                continue
            
            # Check if 'a' and 'b' are connected (they are, by virtue of being in adj[a])
            # We need to find a common neighbor 'c' such that c > b.
            # Intersection of adjacency masks gives common neighbors.
            # adj_mask[u] has bit v set if u and v are connected.
            
            common = adj_mask[a] & adj_mask[b]
            
            # We are interested in common neighbors with index > b.
            # We can shift the common mask to the right by (b + 1)
            # to ignore bits <= b (since we need c > b, i.e., c >= b + 1).
            shifted = common >> (b + 1)
            
            if shifted:
                # If there are any common neighbors > b, find the smallest one.
                # The lowest set bit in 'shifted' corresponds to the smallest c.
                # We use bitwise AND with two's complement to isolate the lowest set bit.
                lsb = shifted & -shifted
                
                # bit_length() of a power of 2 (2^k) is k + 1.
                # The bit index in 'shifted' is bit_length - 1.
                # The original bit index is (bit_length - 1) + (b + 1) = bit_length + b.
                c = lsb.bit_length() + b
                
                # Since we iterate 'a' from smallest, then 'b' from smallest,
                # and find the smallest 'c', the first triangle we find is the
                # lexicographically smallest (a, b, c).
                print(f"{a} {b} {c}")
                return

if __name__ == '__main__':
    solve()