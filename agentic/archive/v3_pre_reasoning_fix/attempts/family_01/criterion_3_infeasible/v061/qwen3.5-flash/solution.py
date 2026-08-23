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

    # Using integer as bitmask for adjacency matrix
    # adj_mask[i] will store the bitmask of neighbors of node i
    # Since n <= 2000, integers will have up to 2000 bits, which fits comfortably in memory
    adj_mask = [0] * n
    
    # Adjacency list for iterating neighbors
    adj_list = [[] for _ in range(n)]
    
    for _ in range(m):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        
        # Update bitmasks
        adj_mask[u] |= (1 << v)
        adj_mask[v] |= (1 << u)
        
        # Update adjacency lists
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    # Sort adjacency lists to ensure we check b in increasing order
    # This is crucial for finding the lexicographically smallest triplet
    for i in range(n):
        adj_list[i].sort()
        
    # Iterate through each node 'a' from smallest index to largest
    for a in range(n):
        # Iterate through neighbors 'b' of 'a'
        # Since adj_list[a] is sorted, we process neighbors in increasing order
        for b in adj_list[a]:
            # We are looking for a triangle (a, b, c) with 1 <= a < b < c <= n
            # In 0-based indexing: 0 <= a < b < c <= n-1
            # So we must have b > a
            if b <= a:
                continue
            
            # We need to find if there exists a common neighbor 'c' of a and b
            # such that c > b.
            
            # Calculate common neighbors using bitwise AND
            common = adj_mask[a] & adj_mask[b]
            
            # We are interested in bits at positions > b.
            # Shifting right by (b + 1) removes all bits <= b.
            # This effectively filters for c > b.
            shifted = common >> (b + 1)
            
            if shifted:
                # If shifted is non-zero, there exists at least one c > b
                # We want the smallest c, which corresponds to the lowest set bit in 'shifted'.
                
                # Isolate the lowest set bit (e.g., 01100 -> 00100)
                lowest_bit = shifted & -shifted
                
                # Find the position of the lowest set bit (0-based index)
                # bit_length() returns the number of bits required to represent the integer
                # For a power of 2 like 2^k, bit_length() is k + 1.
                # So the index k = bit_length() - 1.
                # This index is relative to the shifted mask (0 corresponds to index b+1).
                
                c_idx_shifted = lowest_bit.bit_length() - 1
                
                # The actual index in the original graph is c_idx_shifted + (b + 1)
                c = c_idx_shifted + b + 1
                
                # Found the lexicographically smallest triplet
                # Convert back to 1-based indexing for output
                print(f"{a + 1} {b + 1} {c + 1}")
                return

if __name__ == '__main__':
    solve()