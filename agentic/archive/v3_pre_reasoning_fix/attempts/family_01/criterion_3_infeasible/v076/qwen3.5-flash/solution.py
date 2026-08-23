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

    # Adjacency masks for fast intersection
    # adj_mask[u] will have the v-th bit set if u and v are connected.
    # We use 1-based indexing for vertices 1..n.
    # adj_mask[u] is an integer where the k-th bit is 1 if edge (u, k) exists.
    adj_mask = [0] * (n + 1)
    
    # Adjacency lists to iterate neighbors in sorted order
    # This allows us to process b in increasing order for lexicographical requirement
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        
        # Update adjacency masks
        # Note: u and v are 1-based indices
        adj_mask[u] |= (1 << v)
        adj_mask[v] |= (1 << u)
        
        # Add to adjacency lists
        adj[u].append(v)
        adj[v].append(u)
        
    # Sort adjacency lists to ensure we check b in increasing order
    # Sorting takes O(m log n) in total
    for i in range(1, n + 1):
        adj[i].sort()
        
    # Iterate to find the lexicographically smallest triangle (a, b, c)
    # We want to minimize a, then b, then c.
    # So we iterate a from 1 to n.
    for a in range(1, n + 1):
        # Iterate over neighbors b of a
        # Since adj[a] is sorted, b will be iterated in increasing order.
        # We only care about b > a to satisfy the condition a < b < c later.
        for b in adj[a]:
            if b <= a:
                continue
            
            # We need to find the smallest c > b such that (a, c) and (b, c) are edges.
            # This corresponds to finding the smallest bit index c > b in (adj_mask[a] & adj_mask[b]).
            
            # Compute intersection of neighbors of a and b
            common = adj_mask[a] & adj_mask[b]
            
            # We are interested in bits strictly greater than b.
            # Shift right by (b + 1) to discard bits <= b.
            # If common has bit x set (x > b), it becomes bit x - (b + 1) in shifted.
            shifted = common >> (b + 1)
            
            if shifted > 0:
                # Find the lowest set bit in shifted
                # (shifted & -shifted) isolates the lowest set bit
                low_bit = shifted & -shifted
                
                # bit_length() returns the number of bits required to represent an integer.
                # For a power of 2 (2^k), bit_length() is k + 1.
                # So the index of the bit (0-based) is bit_length() - 1.
                # This index is relative to the shifted mask.
                # The actual bit index (vertex c) is (index relative to shifted) + (b + 1).
                # c = (low_bit.bit_length() - 1) + (b + 1) = low_bit.bit_length() + b
                
                c = low_bit.bit_length() + b
                
                # Found the solution. Since we iterate a, then b, then smallest c,
                # this is guaranteed to be the lexicographically smallest.
                print(f"{a} {b} {c}")
                return

if __name__ == '__main__':
    solve()