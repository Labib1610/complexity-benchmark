import sys

# Increase integer string conversion limit just in case, though not strictly needed as we don't print large ints.
# This is available in Python 3.11+, so we wrap in try-except.
try:
    sys.set_int_max_str_digits(100000)
except AttributeError:
    pass

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

    # Adjacency lists to iterate over neighbors in order
    # Adjacency bitmasks to perform fast intersection checks
    adj = [[] for _ in range(n + 1)]
    adj_mask = [0] * (n + 1)
    
    # Read edges
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        
        adj[u].append(v)
        adj[v].append(u)
        
        # Set bit v in adj_mask[u] and bit u in adj_mask[v]
        # Facilities are 1-indexed, so bit k corresponds to facility k
        adj_mask[u] |= (1 << v)
        adj_mask[v] |= (1 << u)
    
    # Sort adjacency lists to ensure we iterate neighbors b in increasing order
    # This is crucial for lexicographical requirement
    for i in range(1, n + 1):
        adj[i].sort()
    
    # Iterate through each facility a as the first element of the triple
    for a in range(1, n + 1):
        # Iterate through neighbors b of a
        # We only care about b > a to satisfy a < b
        for b in adj[a]:
            if b <= a:
                continue
            
            # We need to find a common neighbor c such that c > b
            # This means c must be connected to both a and b.
            # We use bitwise AND of adjacency masks to find common neighbors.
            common = adj_mask[a] & adj_mask[b]
            
            # We need the smallest c > b.
            # Shift the common mask right by (b + 1) to remove all bits <= b.
            # The lowest set bit in the shifted mask corresponds to the smallest c > b.
            shifted = common >> (b + 1)
            
            if shifted > 0:
                # Find the index of the lowest set bit.
                # (shifted & -shifted) isolates the lowest set bit.
                # .bit_length() - 1 gives the 0-based index of that bit.
                lsb = shifted & -shifted
                offset = lsb.bit_length() - 1
                
                # Reconstruct c. The bit was at index 'offset' after shifting,
                # so original index was 'offset + (b + 1)'.
                c = b + 1 + offset
                
                # Since we iterate a, then b (in increasing order), and pick the smallest valid c,
                # this is guaranteed to be the lexicographically smallest triple.
                print(f"{a} {b} {c}")
                return

if __name__ == '__main__':
    solve()