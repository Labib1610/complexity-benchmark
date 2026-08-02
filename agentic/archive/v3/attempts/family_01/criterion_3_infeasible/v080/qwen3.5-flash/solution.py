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

    # adj_mask[u] will store a bitmask where the k-th bit is 1 if node u is connected to node k+1
    # We use 0-based indexing for bits to correspond to node IDs 1 to n
    # Node u corresponds to bit (u-1)
    adj_mask = [0] * (n + 1)
    
    # adj_list[u] stores the list of neighbors of u
    adj_list = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        
        # Set the bits for u and v in their respective adjacency masks
        adj_mask[u] |= (1 << (u - 1))
        adj_mask[v] |= (1 << (v - 1))
        
        adj_list[u].append(v)
        adj_list[v].append(u)
            
    # Sort adjacency lists to ensure we process neighbors in increasing order of ID
    # This is crucial for finding the lexicographically smallest triplet (a, b, c)
    for i in range(1, n + 1):
        adj_list[i].sort()
            
    # Iterate through each possible starting node a
    for a in range(1, n + 1):
        # Iterate through neighbors b of a
        # We only consider b > a to satisfy a < b < c
        for b in adj_list[a]:
            if b <= a:
                continue
            
            # We need to find a node c such that:
            # 1. c is connected to a (c in adj_list[a])
            # 2. c is connected to b (c in adj_list[b])
            # 3. c > b
            # This is equivalent to finding the smallest common neighbor of a and b that is > b.
            
            # Compute intersection of neighbors of a and b using bitwise AND
            common = adj_mask[a] & adj_mask[b]
            
            # We only care about c > b. In our bit representation, node x corresponds to bit (x-1).
            # So we need bit index >= b.
            # We mask out bits 0 to b-1.
            # The mask (1 << b) - 1 has bits 0 to b-1 set to 1.
            # ~((1 << b) - 1) has bits 0 to b-1 set to 0, and higher bits set to 1.
            common &= ~((1 << b) - 1)
            
            if common:
                # If common is non-zero, we found a valid c.
                # We want the smallest c, which corresponds to the lowest set bit in 'common'.
                # (common & -common) isolates the lowest set bit.
                # .bit_length() returns the number of bits required to represent the integer,
                # which for a power of 2 (1 << k) is k + 1.
                # Since bit k corresponds to node k+1, bit_length() gives the node ID directly.
                c = (common & -common).bit_length()
                
                print(f"{a} {b} {c}")
                return

if __name__ == '__main__':
    solve()