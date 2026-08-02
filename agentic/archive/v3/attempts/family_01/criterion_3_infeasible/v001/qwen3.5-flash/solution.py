import sys
from bisect import bisect_right

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

    # Use sets to avoid duplicate edges and then sort
    adj = [set() for _ in range(n + 1)]
    # Mask array to store neighbors as bitmask
    # n <= 2000, so integers will have ~2000 bits, which is manageable
    mask = [0] * (n + 1)
    
    # Read edges
    for _ in range(m):
        try:
            u = int(next(iterator))
            v = int(next(iterator))
            adj[u].add(v)
            adj[v].add(u)
            # Set bits for mask
            mask[u] |= (1 << v)
            mask[v] |= (1 << u)
        except StopIteration:
            break
            
    # Convert sets to sorted lists for efficient iteration
    for i in range(1, n + 1):
        adj[i] = sorted(list(adj[i]))
        
    # Iterate to find the lexicographically smallest triple (a, b, c)
    # a < b < c
    # We iterate a from 1 to n
    for a in range(1, n + 1):
        # We need to find b in neighbors of a such that b > a
        # Since adj[a] is sorted, we can use bisect to find the start index
        idx = bisect_right(adj[a], a)
        
        # Iterate over b > a without slicing to avoid copy overhead
        for i in range(idx, len(adj[a])):
            b = adj[a][i]
            
            # Check if there exists a common neighbor c > b
            # Common neighbors are neighbors of a AND neighbors of b
            # mask[a] & mask[b] gives the set of common neighbors
            common = mask[a] & mask[b]
            
            # We are interested in bits > b
            # Shift right by b + 1 to ignore bits <= b
            temp = common >> (b + 1)
            
            if temp != 0:
                # Found at least one common neighbor > b
                # We want the smallest c, which corresponds to the lowest set bit in temp
                # (temp & -temp) isolates the lowest set bit
                # .bit_length() - 1 gives the index of that bit (0-based)
                p = (temp & -temp).bit_length() - 1
                c = b + 1 + p
                
                # Since we iterate a, then b, then find smallest c, this is the lexicographically smallest triple
                print(f"{a} {b} {c}")
                return

if __name__ == '__main__':
    solve()