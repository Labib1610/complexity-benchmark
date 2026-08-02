import sys

# Increase recursion depth just in case, though not needed for this iterative solution
sys.setrecursionlimit(2000)

def main():
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
    
    # Adjacency bitmasks and lists
    # We use 0-based indexing for workers internally (0 to n-1)
    # adj[i] is an integer where the j-th bit is 1 if there is an edge between i and j
    adj = [0] * n
    adj_list = [[] for _ in range(n)]
    
    # Read m edges
    for _ in range(m):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        
        # Update bitmask: set bit v for u and bit u for v
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
        
        # Update adjacency list
        adj_list[u].append(v)
        adj_list[v].append(u)
        
    # Sort adjacency lists to ensure we process b in increasing order
    # This is crucial for finding the lexicographically smallest triplet
    for i in range(n):
        adj_list[i].sort()
        
    # Iterate to find the lexicographically smallest triplet (a, b, c)
    # a < b < c
    # We iterate a from 0 to n-1 (smallest a first)
    for a in range(n):
        # Iterate over neighbors b of a
        # We only care about b > a to maintain order and avoid duplicates
        for b in adj_list[a]:
            if b <= a:
                continue
            
            # We have edge (a, b). We need to find c > b such that (a, c) and (b, c) are edges.
            # This means c is a common neighbor of a and b.
            # We want the smallest such c.
            
            # Calculate common neighbors using bitwise AND
            # This operation takes O(n/64) time on average for n-bit integers
            common = adj[a] & adj[b]
            
            # We need to find the smallest bit index > b in 'common'.
            # We can shift right by (b + 1) to discard bits 0 to b.
            # Then find the lowest set bit in the shifted value.
            # This corresponds to the smallest c > b.
            
            shifted = common >> (b + 1)
            
            if shifted:
                # Find the lowest set bit (LSB)
                lsb = shifted & -shifted
                
                # Calculate the original index c (1-based)
                # lsb corresponds to bit k in shifted (where k >= 0).
                # Original index (0-based) = k + (b + 1)
                # 1-based index = k + (b + 1) + 1 = k + b + 2
                # bit_length of lsb is k + 1.
                # So 1-based index c = (lsb.bit_length() - 1) + b + 2 = lsb.bit_length() + b + 1.
                
                c = lsb.bit_length() + b + 1
                
                # Print the result and exit immediately as we found the smallest triplet
                print(f"{a + 1} {b + 1} {c}")
                return

if __name__ == '__main__':
    main()