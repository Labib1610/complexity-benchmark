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

    # Adjacency list to store neighbors for iteration order
    # Using 1-based indexing for convenience
    adj_list = [[] for _ in range(n + 1)]
    
    # Adjacency bitmasks for fast intersection
    # adj_mask[u] has the k-th bit set if there is an edge (u, k)
    adj_mask = [0] * (n + 1)
    
    # Parse edges
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        
        adj_list[u].append(v)
        adj_list[v].append(u)
        
        # Update bitmasks
        # We use 1 << v because v is up to n. 
        # Python handles arbitrarily large integers efficiently.
        adj_mask[u] |= (1 << v)
        adj_mask[v] |= (1 << u)
        
    # Sort adjacency lists to ensure we check neighbors in increasing order.
    # This is crucial for finding the lexicographically smallest triple (a, b, c).
    # We want smallest 'a', then smallest 'b', then smallest 'c'.
    for i in range(1, n + 1):
        adj_list[i].sort()
        
    # Iterate through all possible 'a'
    for a in range(1, n + 1):
        # Iterate through neighbors 'b' of 'a'
        for b in adj_list[a]:
            # We enforce a < b < c.
            # Since we iterate 'a' in increasing order, we just need to ensure b > a.
            # If b <= a, it would be a duplicate pair (since graph is undirected)
            # or an order violation.
            if b <= a:
                continue
            
            # Check for a common neighbor 'c' such that c > b.
            # Intersection of neighbors of a and b gives all common neighbors.
            # Using bitmasks, this is a bitwise AND operation.
            common = adj_mask[a] & adj_mask[b]
            
            # We need the smallest bit set in 'common' that is at a position > b.
            # Bits in 'common' correspond to node indices.
            # We shift the mask right by (b + 1) to discard bits <= b.
            shifted = common >> (b + 1)
            
            if shifted:
                # If shifted is non-zero, there is at least one common neighbor c > b.
                # We want the smallest such c.
                # In 'shifted', the least significant bit (LSB) corresponds to the smallest c > b.
                # The position of the LSB in 'shifted' (0-indexed) corresponds to c - (b + 1).
                
                # Isolate the LSB
                lsb = shifted & -shifted
                
                # Find the index of the LSB. 
                # For a power of 2, bit_length() - 1 gives the 0-based index.
                c_idx = lsb.bit_length() - 1
                
                # Reconstruct the node index c
                c = c_idx + b + 1
                
                # Since we iterate 'a' and 'b' in lexicographical order,
                # the first valid triangle we find is the lexicographically smallest.
                print(f"{a} {b} {c}")
                return

if __name__ == '__main__':
    solve()