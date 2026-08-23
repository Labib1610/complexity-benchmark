import sys

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

    # Precompute powers of 2 for bit manipulation to speed up adjacency updates
    # Indices 0 to n, where index i corresponds to node i
    POW2 = [1 << i for i in range(n + 1)]
    
    # Adjacency bitmasks
    # adj[u] will have the v-th bit set if there is an edge between u and v
    adj = [0] * (n + 1)
    edges = []
    
    # Read edges
    for _ in range(m):
        try:
            u = int(next(iterator))
            v = int(next(iterator))
        except StopIteration:
            break
        
        # Normalize edge so that u < v for consistent processing
        if u > v:
            u, v = v, u
        
        # Update adjacency bitmasks
        adj[u] |= POW2[v]
        adj[v] |= POW2[u]
        
        edges.append((u, v))
    
    # Sort edges to process in lexicographical order of (u, v)
    # This ensures we find the lexicographically smallest triplet (a, b, c)
    # by minimizing a, then b, then c.
    edges.sort()
    
    for u, v in edges:
        # Find common neighbors c > v.
        # Common neighbors are the intersection of neighbors of u and v.
        common = adj[u] & adj[v]
        
        # We need c > v. Shift right by v + 1 to remove bits corresponding to nodes <= v.
        shifted_common = common >> (v + 1)
        
        if shifted_common > 0:
            # Find the lowest set bit in shifted_common, which corresponds to the smallest c > v.
            # (x & -x) isolates the lowest set bit.
            lsb = shifted_common & -shifted_common
            
            # bit_length() returns the number of bits required to represent an integer.
            # For a power of 2 (2^k), bit_length is k + 1.
            # The index of the bit in the shifted number is bit_length - 1.
            # The original node index c is this index plus the shift amount (v + 1).
            c = lsb.bit_length() - 1 + (v + 1)
            
            print(f"{u} {v} {c}")
            return

if __name__ == '__main__':
    solve()