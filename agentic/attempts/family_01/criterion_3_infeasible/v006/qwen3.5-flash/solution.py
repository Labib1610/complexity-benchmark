import sys

# Increase recursion depth just in case, though not needed here
sys.setrecursionlimit(2000)

def solve():
    # Read all input from standard input
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # Adjacency mask for fast intersection
    # adj_mask[u] will have the v-th bit set if u and v are connected
    adj_mask = [0] * (n + 1)
    
    # Adjacency list for iteration
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        
        adj_mask[u] |= (1 << v)
        adj_mask[v] |= (1 << u)
        
        adj[u].append(v)
        adj[v].append(u)
    
    # Sort adjacency lists to ensure we process neighbors in increasing order
    for u in range(1, n + 1):
        adj[u].sort()
    
    # Iterate to find the lexicographically smallest triple (a, b, c)
    # We want smallest a, then smallest b, then smallest c
    # Conditions: a < b < c, and edges (a,b), (a,c), (b,c) exist
    
    for a in range(1, n + 1):
        # Iterate over neighbors b of a such that b > a
        for b in adj[a]:
            if b <= a:
                continue
            
            # We need to find smallest c > b such that (a, c) and (b, c) are edges
            # Intersection of neighbors of a and neighbors of b
            # adj_mask[a] & adj_mask[b] gives the bitmask of common neighbors
            
            common = adj_mask[a] & adj_mask[b]
            
            # We only care about c > b
            # Shift right by b + 1 to remove bits <= b
            # Note: vertices are 1-based. Bit k corresponds to vertex k.
            # We want to check bits b+1, b+2, ...
            # So we shift common by b + 1.
            
            common >>= (b + 1)
            
            if common > 0:
                # Find the lowest set bit in common
                # This corresponds to the smallest c > b
                low_bit = common & -common
                
                # Calculate the index of the bit
                # bit_length() returns the number of bits required to represent an integer
                # For a power of 2, bit_length is the position of the bit + 1 (since 2^0 has length 1)
                # So the index is bit_length - 1
                # Since we shifted by b + 1, the original index was (bit_length - 1) + b + 1
                
                c = low_bit.bit_length() - 1 + b + 1
                
                # We found the triple (a, b, c)
                # Since we iterate a then b, and find smallest c for each b,
                # this is guaranteed to be the lexicographically smallest triple.
                print(f"{a} {b} {c}")
                return

if __name__ == '__main__':
    solve()