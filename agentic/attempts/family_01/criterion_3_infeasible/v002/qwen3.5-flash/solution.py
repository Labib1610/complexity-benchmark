import sys

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

    # Use adjacency bitmasks for fast intersection checks
    # adj[i] is an integer where the j-th bit is set if station i interferes with station j
    adj = [0] * (n + 1)
    
    # Use adjacency lists to iterate through neighbors
    # Sorting these lists allows us to process neighbors in increasing order
    adj_list = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
        
        adj_list[u].append(v)
        adj_list[v].append(u)
        
    # Sort adjacency lists to ensure we check neighbors in increasing order
    # This is crucial to find the lexicographically smallest triple
    for i in range(1, n + 1):
        adj_list[i].sort()
        
    # Iterate through each possible value for the first station 'a'
    for a in range(1, n + 1):
        mask_a = adj[a]
        # Iterate through neighbors of 'a' to find 'b'
        # Since adj_list[a] is sorted, we encounter b in increasing order
        for b in adj_list[a]:
            # We need b > a to maintain order a < b < c
            if b <= a:
                continue
            
            # Find common neighbors of 'a' and 'b'
            # This is the bitwise AND of their adjacency masks
            common = mask_a & adj[b]
            
            # We need to find a common neighbor 'c' such that c > b
            # Shift the common mask right by (b + 1) to filter out neighbors <= b
            shifted = common >> (b + 1)
            
            if shifted:
                # If shifted is non-zero, there exists at least one common neighbor > b
                # We need the smallest such 'c'
                # lsb = shifted & -shifted isolates the lowest set bit in shifted
                lsb = shifted & -shifted
                
                # Calculate the index of the bit. 
                # bit_length() - 1 gives the index of the lowest set bit relative to 0.
                # We add (b + 1) to get the original index.
                c = lsb.bit_length() - 1 + (b + 1)
                
                # Since we iterate a, then b, then find smallest c, this is the lexicographically smallest triple
                print(f"{a} {b} {c}")
                return

if __name__ == '__main__':
    solve()