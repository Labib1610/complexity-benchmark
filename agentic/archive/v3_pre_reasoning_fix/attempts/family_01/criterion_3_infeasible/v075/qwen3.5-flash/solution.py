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

    # Adjacency bitmasks
    # adj[i] will have the j-th bit set if there is an edge between i and j
    # We use n + 1 to accommodate 1-based indexing
    adj = [0] * (n + 1)
    
    # Adjacency lists to iterate neighbors in increasing order
    # This is necessary to find the lexicographically smallest (a, b, c)
    adj_list = [[] for _ in range(n + 1)]

    # Read m edges
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        # Set bits in adjacency masks
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
        # Add to adjacency lists
        adj_list[u].append(v)
        adj_list[v].append(u)
        
    # Sort adjacency lists to ensure we iterate neighbors in increasing order
    for i in range(1, n + 1):
        adj_list[i].sort()
        
    # Iterate a from 1 to n to find the smallest 'a'
    for a in range(1, n + 1):
        # Iterate b in neighbors of a
        # Since adj_list[a] is sorted, we check b in increasing order
        for b in adj_list[a]:
            # We need a < b < c
            if b > a:
                # Check if there is a common neighbor c > b
                # Intersection of adjacency bitmasks gives common neighbors
                common = adj[a] & adj[b]
                
                # We want the smallest c > b.
                # The bits in 'common' represent neighbors of both a and b.
                # We need the smallest bit index c such that c > b.
                # We can achieve this by shifting 'common' right by (b + 1).
                # The bit at position (b + 1) in 'common' becomes bit 0 in 'shifted'.
                # If 'shifted' is non-zero, the lowest set bit in 'shifted' corresponds to the smallest c > b.
                
                shifted = common >> (b + 1)
                
                if shifted > 0:
                    # Isolate the lowest set bit
                    lsb = shifted & -shifted
                    
                    # Calculate the 0-based index of the lowest set bit
                    # lsbit.bit_length() returns the number of bits required to represent the integer.
                    # For a power of 2 (2^k), bit_length is k + 1.
                    # Thus, the index is bit_length - 1.
                    # The bit index in 'shifted' is c - (b + 1).
                    c_offset = lsb.bit_length() - 1
                    c = c_offset + b + 1
                    
                    # We found the lexicographically smallest committee
                    print(f"{a} {b} {c}")
                    return

if __name__ == '__main__':
    solve()