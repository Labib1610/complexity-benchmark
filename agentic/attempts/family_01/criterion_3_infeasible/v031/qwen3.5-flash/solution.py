import sys

# Increase recursion depth just in case, though not used here
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

    # Adjacency list and masks
    # adj[i] stores neighbors of node i
    # masks[i] is a bitmask where the j-th bit is 1 if node j is a neighbor of i
    # We use 1-based indexing for nodes, so size is n + 1
    adj = [[] for _ in range(n + 1)]
    masks = [0] * (n + 1)
    
    # Process edges
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
        # Set bits corresponding to neighbors
        masks[u] |= (1 << v)
        masks[v] |= (1 << u)
            
    # Sort adjacency lists to ensure we iterate b in increasing order
    # This is crucial for finding the lexicographically smallest triple
    for i in range(1, n + 1):
        adj[i].sort()
            
    # Iterate a from 1 to n to minimize 'a'
    for a in range(1, n + 1):
        # Iterate b in adj[a] to minimize 'b'
        # Since adj[a] is sorted, we encounter smaller b first.
        for b in adj[a]:
            if b <= a:
                continue
            
            # We need to find the smallest c > b such that (a, c) and (b, c) are edges.
            # This corresponds to finding a common neighbor of a and b with index > b.
            # Intersection of neighbors: masks[a] & masks[b]
            common = masks[a] & masks[b]
            
            # Filter bits <= b. We want bits > b.
            # Mask with bits 0..b set to 1 is (1 << (b + 1)) - 1.
            # Inverting it gives 0s for 0..b and 1s for > b (conceptually).
            # Python's ~ operator works with infinite bits (2's complement).
            mask_le_b = (1 << (b + 1)) - 1
            valid = common & ~mask_le_b
            
            if valid:
                # Find the smallest set bit in valid.
                # valid & -valid isolates the lowest set bit.
                # bit_length() returns the number of bits required to represent an integer.
                # For 2^k, bit_length is k+1. So index is bit_length - 1.
                lowest_bit = valid & -valid
                c = lowest_bit.bit_length() - 1
                print(f"{a} {b} {c}")
                return

if __name__ == '__main__':
    solve()