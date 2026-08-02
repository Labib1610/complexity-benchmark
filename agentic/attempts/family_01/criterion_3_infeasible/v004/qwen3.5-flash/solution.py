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

    # Adjacency list to store neighbors for iteration in sorted order
    # Using sets to avoid duplicate edges if any
    adj = [set() for _ in range(n + 1)]
    
    # Adjacency masks for fast bitset operations
    # masks[u] will have the v-th bit set if (u, v) is an edge
    masks = [0] * (n + 1)
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].add(v)
        adj[v].add(u)
        masks[u] |= (1 << v)
        masks[v] |= (1 << u)
    
    # Sort adjacency lists to ensure we process neighbors in increasing order
    # This is crucial for finding the lexicographically smallest triple
    for i in range(1, n + 1):
        adj[i] = sorted(list(adj[i]))
    
    # Iterate through all possible 'a' from 1 to n
    # We want to minimize 'a' first
    for a in range(1, n + 1):
        # Iterate through all neighbors 'b' of 'a'
        # We want b > a for the triple (a, b, c) with a < b < c
        # Since adj[a] is sorted, we process b in increasing order
        for b in adj[a]:
            if b <= a:
                continue
            
            # Find common neighbors of a and b
            # This represents nodes 'c' such that (a, c) and (b, c) are edges
            common = masks[a] & masks[b]
            
            # We need c > b.
            # We shift right by (b + 1) to discard bits <= b.
            # The bit at position c (where c > b) will move to position c - (b + 1).
            shifted = common >> (b + 1)
            
            if shifted:
                # Find the smallest set bit in 'shifted'
                # This corresponds to the smallest c > b
                # x & -x extracts the lowest set bit
                lsb = shifted & -shifted
                
                # Calculate the index of the bit.
                # If lsb = 2^k, then bit_length is k + 1. So k = bit_length - 1.
                # The position in the original mask was k + (b + 1).
                k = lsb.bit_length() - 1
                c = k + b + 1
                
                # We found the lexicographically smallest triple (a, b, c)
                # because we iterate a increasing, b increasing, and find smallest c.
                print(f"{a} {b} {c}")
                return

if __name__ == '__main__':
    solve()