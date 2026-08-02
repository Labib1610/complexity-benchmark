import sys

# Increase recursion depth just in case, though not needed for this iterative solution
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
    # adj[u] will have the v-th bit set if there is an edge between u and v.
    # Using bitmasks allows for O(n/64) intersection operations.
    adj = [0] * (n + 1)
    
    # Adjacency lists for ordered iteration to find lexicographically smallest triplet
    adj_lists = [[] for _ in range(n + 1)]
    
    # Read edges
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        
        # Set bits in adjacency masks
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
        
        # Store neighbors in lists
        adj_lists[u].append(v)
        adj_lists[v].append(u)
    
    # Sort and deduplicate adjacency lists.
    # Sorting ensures we visit neighbors in increasing order, which is crucial
    # for finding the lexicographically smallest triplet.
    for i in range(1, n + 1):
        if adj_lists[i]:
            adj_lists[i] = sorted(list(set(adj_lists[i])))
    
    # Iterate to find the lexicographically smallest triplet (a, b, c).
    # We iterate 'a' from 1 to n.
    # For each 'a', we iterate 'b' through its neighbors in increasing order.
    # We only consider 'b' > 'a' to satisfy a < b < c and avoid duplicates.
    # For each valid pair (a, b), we check for the smallest 'c' > 'b'
    # such that (a, c) and (b, c) are edges.
    # The first such triplet found is guaranteed to be the lexicographically smallest.
    
    for a in range(1, n + 1):
        for b in adj_lists[a]:
            if b > a:
                # Check intersection of neighbors of a and b
                common = adj[a] & adj[b]
                
                # We need c > b. So we clear all bits <= b in common.
                # Bit v corresponds to node v.
                # We want to clear bits 0, 1, ..., b.
                # Mask with 1s at 0..b is (1 << (b + 1)) - 1.
                # We want to keep bits > b, so we AND with the inverse.
                # In Python, ~x is -x-1.
                # So we can use -(1 << (b + 1)) which is equivalent to clearing bits 0..b
                # and keeping higher bits (infinite 1s to the left in two's complement).
                common &= -(1 << (b + 1))
                
                if common:
                    # Find the smallest set bit in common (this corresponds to smallest c > b)
                    # common & -common isolates the lowest set bit (a power of 2)
                    lowest_bit = common & -common
                    
                    # bit_length() returns the number of bits required to represent an integer.
                    # For a power of 2 (1 << k), bit_length() is k + 1.
                    # The index of the bit is k.
                    c = lowest_bit.bit_length() - 1
                    
                    # Output the result
                    print(f"{a} {b} {c}")
                    return

if __name__ == '__main__':
    solve()