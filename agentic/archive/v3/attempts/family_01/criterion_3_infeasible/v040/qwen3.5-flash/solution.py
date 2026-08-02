import sys

# Increase recursion depth just in case, though not used here
sys.setrecursionlimit(2000)

def solve():
    # Read all input from standard input
    # Using sys.stdin.read().split() is efficient for large inputs
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # adj[i] stores the bitmask of neighbors for vertex i (0-indexed)
    # We use Python's arbitrary precision integers as bitsets for efficient intersection
    adj = [0] * n
    
    # adj_list[i] stores the list of neighbors for vertex i (0-indexed)
    # We will sort this list to iterate neighbors in increasing order of vertex index
    adj_list = [[] for _ in range(n)]

    for _ in range(m):
        try:
            u = int(next(iterator)) - 1
            v = int(next(iterator)) - 1
        except StopIteration:
            break
        
        # Update bitmasks
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
        
        # Update adjacency lists
        adj_list[u].append(v)
        adj_list[v].append(u)

    # Sort adjacency lists to ensure we iterate neighbors in increasing order
    for i in range(n):
        adj_list[i].sort()

    # Iterate through each vertex a as the first member of the triple
    # We want the lexicographically smallest triple (a, b, c) with a < b < c.
    # So we iterate a from smallest to largest.
    for a in range(n):
        # Iterate over neighbors b of a.
        # Since adj_list[a] is sorted, we encounter b in increasing order.
        # We only care about b > a.
        for b in adj_list[a]:
            if b <= a:
                continue
            
            # We need to find c > b such that c is connected to both a and b.
            # c must be in the intersection of neighbors of a and neighbors of b.
            # Compute intersection using bitwise AND.
            common = adj[a] & adj[b]
            
            # We need c > b.
            # In 0-indexed terms, we need bit index > b.
            # Mask out bits 0 to b.
            # The mask to keep bits > b is ~((1 << (b + 1)) - 1)
            # Note: (1 << (b + 1)) - 1 has bits 0..b set to 1.
            # Inverting it gives 0s at 0..b and 1s elsewhere (conceptually infinite 1s to left).
            # Since common is positive and limited to n bits, this works correctly.
            mask = ~((1 << (b + 1)) - 1)
            common &= mask
            
            if common:
                # Find the smallest bit set in common.
                # This corresponds to the smallest vertex c > b.
                # common & -common gives the lowest set bit as a power of 2.
                lowbit = common & -common
                
                # bit_length() returns the number of bits required to represent the integer.
                # For 2^k, bit_length is k+1.
                # So the index k is bit_length() - 1.
                c_idx = lowbit.bit_length() - 1
                
                # Convert back to 1-based indexing for output
                print(a + 1, b + 1, c_idx + 1)
                return

if __name__ == '__main__':
    solve()