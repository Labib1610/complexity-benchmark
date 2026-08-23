import sys

# Increase recursion depth just in case
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

    # adj_mask[u] will store a bitmask where the v-th bit is set if (u, v) is an edge
    # We use 1-based indexing for transmitters, so bits 1..n are used.
    adj_mask = [0] * (n + 1)
    
    # adj_list[u] will store the list of neighbors of u
    adj_list = [[] for _ in range(n + 1)]

    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        
        # Update masks
        adj_mask[u] |= (1 << v)
        adj_mask[v] |= (1 << u)
        
        # Update lists
        adj_list[u].append(v)
        adj_list[v].append(u)

    # Sort adjacency lists to ensure we process neighbors in increasing order.
    # This is important for finding the lexicographically smallest triplet (a, b, c)
    # where we minimize a, then b, then c.
    for i in range(1, n + 1):
        adj_list[i].sort()

    # Iterate through each transmitter 'a' as the first element of the triplet
    for a in range(1, n + 1):
        # Iterate through neighbors 'b' of 'a'
        # We require b > a for the triplet (a, b, c)
        neighbors = adj_list[a]
        for b in neighbors:
            if b <= a:
                continue
            
            # At this point, we have an edge (a, b) with a < b.
            # We need to find the smallest 'c' > 'b' such that (a, c) and (b, c) exist.
            # This means c must be a common neighbor of a and b, and c > b.
            
            # Find common neighbors using bitwise AND of masks
            common = adj_mask[a] & adj_mask[b]
            
            # We want the smallest bit set in 'common' that is greater than b.
            # We can achieve this by shifting 'common' right by (b + 1).
            # If the result is non-zero, the lowest set bit corresponds to the smallest c > b.
            val = common >> (b + 1)
            
            if val == 0:
                continue
            
            # Isolate the lowest set bit of val
            lsb = val & -val
            
            # Calculate the index c.
            # If lsb is 2^k, then the bit at position k in val is set.
            # This corresponds to bit position k + b + 1 in common.
            # The index of the bit k (0-indexed) is bit_length(k) - 1? 
            # No, lsb.bit_length() returns k + 1.
            # So c = (k + 1) + b.
            c = lsb.bit_length() + b
            
            # We found the lexicographically smallest triplet
            print(f"{a} {b} {c}")
            return

if __name__ == '__main__':
    solve()