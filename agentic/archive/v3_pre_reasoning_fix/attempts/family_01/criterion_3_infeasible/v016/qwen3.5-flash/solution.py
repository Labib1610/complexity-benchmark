import sys

# Increase recursion depth just in case, though not needed here
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
    
    # Adjacency list to store neighbors for iteration
    # We use 1-based indexing for convenience to match problem statement
    adj = [[] for _ in range(n + 1)]
    
    # Adjacency mask to store neighbors as bits in an integer
    # This allows for efficient intersection and finding common neighbors
    adj_mask = [0] * (n + 1)
    
    # Reading m edges
    for _ in range(m):
        try:
            u = int(next(iterator))
            v = int(next(iterator))
        except StopIteration:
            break
            
        adj[u].append(v)
        adj[v].append(u)
        
        # Set the bit corresponding to the node index
        # Using 1-based indexing for bits as well (bit k corresponds to node k)
        adj_mask[u] |= (1 << v)
        adj_mask[v] |= (1 << u)
        
    # Sort adjacency lists to ensure we process neighbors in increasing order.
    # This is crucial for finding the lexicographically smallest triple.
    # We need to iterate 'a' from 1 to n, then 'b' (neighbor of a) in increasing order.
    for i in range(1, n + 1):
        adj[i].sort()
        
    # Iterate through each employee 'a' as the first element of the triple
    for a in range(1, n + 1):
        # Iterate through neighbors 'b' of 'a'
        # Since adj[a] is sorted, we encounter b's in increasing order.
        # We want to find the smallest valid triple (a, b, c) with a < b < c.
        # By iterating a increasing, then b increasing, the first valid c we find
        # for the smallest valid b will give the lexicographically smallest triple.
        for b in adj[a]:
            # We require a < b < c. So we only consider neighbors b > a.
            if b <= a:
                continue
            
            # We need to find the smallest c > b such that (a, c) and (b, c) are edges.
            # This means c must be a common neighbor of a and b.
            # We can find common neighbors using bitwise AND of their adjacency masks.
            common = adj_mask[a] & adj_mask[b]
            
            # We need the smallest bit set in 'common' that corresponds to a node index > b.
            # We can mask out bits <= b.
            # The mask ~((1 << (b + 1)) - 1) has 0s at positions 0 to b and 1s elsewhere.
            # This effectively clears all bits corresponding to nodes <= b.
            mask = ~((1 << (b + 1)) - 1)
            candidates = common & mask
            
            if candidates:
                # If candidates is non-zero, there exists at least one c > b forming a triangle.
                # Since candidates is a bitmask, we want the lowest set bit to get the smallest c.
                # The expression (candidates & -candidates) isolates the lowest set bit.
                lowest_bit = candidates & -candidates
                
                # bit_length() returns the number of bits required to represent the integer.
                # For a power of 2 (which lowest_bit is), bit_length() is (index + 1).
                # So the index of the bit (which corresponds to node c) is bit_length() - 1.
                c = lowest_bit.bit_length() - 1
                
                # We found the lexicographically smallest triple
                print(f"{a} {b} {c}")
                return

if __name__ == '__main__':
    solve()