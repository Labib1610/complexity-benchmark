import sys

# Increase recursion depth just in case, though not needed for this iterative solution.
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

    # Adjacency list to store neighbors for each node
    # Nodes are 1-indexed, so we size it n + 1
    adj = [[] for _ in range(n + 1)]
    
    # Adjacency bitmasks. 
    # mask[u] will have the v-th bit set if there is an edge between u and v.
    # Since N <= 2000, integers will have at most ~2000 bits, which fits easily in memory.
    mask = [0] * (n + 1)

    # Parse edges
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
        mask[u] |= (1 << v)
        mask[v] |= (1 << u)

    # Sort adjacency lists.
    # This allows us to iterate neighbors in increasing order, which is key
    # for finding the lexicographically smallest triplet (a, b, c).
    for i in range(1, n + 1):
        adj[i].sort()

    # Iterate through each potential 'a' from 1 to n.
    # We want the smallest 'a' first.
    for a in range(1, n + 1):
        # Iterate through neighbors 'b' of 'a'.
        # Since adj[a] is sorted, we visit 'b' in increasing order.
        # This ensures that for a fixed 'a', we find the smallest 'b' first.
        for b in adj[a]:
            # We require a < b < c.
            # Since we iterate 'a' in increasing order, a is fixed.
            # We need b > a.
            if b <= a:
                continue
            
            # Now we need to find the smallest 'c' such that c > b
            # and c is connected to both a and b.
            # Common neighbors of a and b are bits set in both mask[a] and mask[b].
            common = mask[a] & mask[b]
            
            # We are only interested in c > b.
            # We can shift the common mask to the right by (b + 1).
            # This moves the bit corresponding to node (b + 1) to position 0.
            # If the result is non-zero, there exists at least one common neighbor > b.
            # The lowest set bit in the shifted mask corresponds to the smallest such c.
            
            shifted_common = common >> (b + 1)
            
            if shifted_common:
                # Find the lowest set bit.
                # (x & -x) isolates the lowest set bit of x.
                lsb = shifted_common & -shifted_common
                
                # bit_length() returns the number of bits required to represent an integer.
                # For a power of 2 (2^k), bit_length is k + 1.
                # So the index of the bit is bit_length - 1.
                c_offset = lsb.bit_length() - 1
                
                # The actual node index c is b + 1 + offset.
                c = b + 1 + c_offset
                
                # We found the lexicographically smallest triplet (a, b, c)
                # because:
                # 1. We iterate 'a' from smallest to largest.
                # 2. For a fixed 'a', we iterate 'b' from smallest to largest.
                # 3. For a fixed pair (a, b), we pick the smallest 'c'.
                print(f"{a} {b} {c}")
                return

if __name__ == '__main__':
    solve()