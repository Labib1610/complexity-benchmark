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

    # Adjacency list to iterate neighbors in sorted order
    adj = [[] for _ in range(n + 1)]
    # Bitmask for fast intersection of neighbor sets
    mask = [0] * (n + 1)
    
    # Parse edges
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
        # Set bit v for u, bit u for v
        # We use 1-based indexing for nodes, so bit v corresponds to node v
        mask[u] |= (1 << v)
        mask[v] |= (1 << u)
    
    # Sort adjacency lists to ensure we check neighbors in increasing order
    # This is crucial for lexicographical order of b
    for i in range(1, n + 1):
        adj[i].sort()
        
    # Iterate through each vertex 'a'
    # Since we want the lexicographically smallest triple (a, b, c),
    # we start with the smallest possible 'a'.
    for a in range(1, n + 1):
        # Iterate through neighbors of 'a' as 'b'
        # We need b > a to satisfy a < b < c
        for b in adj[a]:
            if b > a:
                # We need to find a 'c' such that c > b
                # and (a, c) and (b, c) are edges.
                # This means c must be a common neighbor of a and b with c > b.
                
                # Find common neighbors using bitwise AND
                common = mask[a] & mask[b]
                
                # We only care about neighbors > b.
                # We create a mask to clear bits <= b.
                # (1 << (b + 1)) - 1 has bits 0 to b set to 1.
                # ~((1 << (b + 1)) - 1) has bits 0 to b set to 0, and bits > b set to 1.
                mask_low = (1 << (b + 1)) - 1
                common &= ~mask_low
                
                if common:
                    # There exists at least one common neighbor > b.
                    # We want the smallest such 'c' to ensure lexicographical order.
                    # The smallest bit set in 'common' gives the smallest 'c'.
                    
                    # Isolate the lowest set bit
                    lsb = common & -common
                    
                    # Find the index of this bit.
                    # If lsb is 2^k, bit_length() returns k+1.
                    # So index k = bit_length() - 1.
                    c = lsb.bit_length() - 1
                    
                    # Output the result
                    print(f"{a} {b} {c}")
                    return

if __name__ == '__main__':
    solve()