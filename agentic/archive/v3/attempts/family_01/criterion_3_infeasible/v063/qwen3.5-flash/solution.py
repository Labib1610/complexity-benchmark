import sys

def solve():
    # Read all input from stdin efficiently
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
    # adj[i] is an integer where the j-th bit is 1 if edge (i, j) exists
    # Using bitmasks allows O(1) edge checks and fast intersection
    adj = [0] * (n + 1)
    adj_list = [[] for _ in range(n + 1)]
    
    # Read m edges
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
        adj_list[u].append(v)
        adj_list[v].append(u)
        
    # Sort adjacency lists to iterate neighbors in increasing order
    # This ensures we find the lexicographically smallest b for a fixed a
    for i in range(1, n + 1):
        adj_list[i].sort()
        
    # Iterate through each node a to act as the first vertex of the triplet
    # We want the smallest a, then smallest b > a, then smallest c > b
    for a in range(1, n + 1):
        # Iterate through neighbors b of a
        for b in adj_list[a]:
            if b <= a:
                continue
            
            # We need to find a neighbor c such that c > b and c is connected to both a and b
            # mask represents common neighbors of a and b
            mask = adj[a] & adj[b]
            
            # We only care about neighbors c > b.
            # Shift the mask right by (b + 1) to ignore bits <= b.
            # The bit at position k in 'mask' (where k > b) moves to position k - (b + 1) in 'shifted'.
            shifted = mask >> (b + 1)
            
            if shifted > 0:
                # Find the smallest bit set in shifted.
                # This corresponds to the smallest c > b.
                # We isolate the lowest set bit using (shifted & -shifted)
                # Then we find its position using bit_length().
                # If lowest set bit is 2^k, bit_length is k+1.
                # The index in shifted is k.
                # The original index c is (b + 1) + k = b + 1 + (bit_length - 1) = b + bit_length
                
                low_bit = shifted & -shifted
                c = b + low_bit.bit_length()
                
                # Since we iterate a increasing, then b increasing, and find smallest c,
                # this is the lexicographically smallest triplet.
                print(f"{a} {b} {c}")
                return

if __name__ == '__main__':
    solve()