import sys
from bisect import bisect_right

def solve():
    # Read all input from standard input at once
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # Adjacency bitmasks
    # adj[i] is an integer where the k-th bit is 1 if there is an edge (i, k)
    # Since n <= 2000, these integers will be around 2^2000, which Python handles efficiently.
    adj = [0] * (n + 1)
    
    # Adjacency lists for iteration to ensure we visit edges in order
    adj_list = [[] for _ in range(n + 1)]
    
    # Read edges
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        
        # Mark edge in bitmask
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
        
        # Add to adjacency list
        adj_list[u].append(v)
        adj_list[v].append(u)
        
    # Sort adjacency lists to process neighbors in increasing order
    # This is crucial for finding the lexicographically smallest triplet
    for i in range(1, n + 1):
        adj_list[i].sort()
        
    # Iterate to find the lexicographically smallest triplet (a, b, c)
    # We iterate a from 1 to n.
    # For each a, we iterate b > a from neighbors of a.
    # We want the smallest b, so we iterate b in increasing order.
    # Then we find the smallest c > b such that (a, c) and (b, c) are edges.
    
    for a in range(1, n + 1):
        # We only consider b > a
        # Use bisect to find the start index of neighbors > a
        idx = bisect_right(adj_list[a], a)
        
        # Iterate through valid b's
        for i in range(idx, len(adj_list[a])):
            b = adj_list[a][i]
            
            # We need to find the smallest c > b such that c is connected to both a and b.
            # This is equivalent to finding the smallest bit set in (adj[a] & adj[b])
            # that is at a position > b.
            
            common = adj[a] & adj[b]
            
            # Shift common right by b + 1 to remove bits <= b
            # If common had bit k set (where k > b), shifted will have bit (k - (b + 1)) set.
            shifted = common >> (b + 1)
            
            if shifted:
                # Find the lowest set bit in shifted
                # lsb = shifted & -shifted isolates the lowest set bit
                lsb = shifted & -shifted
                # bit_length() - 1 gives the 0-based index of the lowest set bit
                c_offset = lsb.bit_length() - 1
                
                # Calculate original c index
                c = c_offset + b + 1
                
                # Since we iterate a, then b in increasing order, and find smallest c,
                # the first triplet found is guaranteed to be lexicographically smallest.
                print(f"{a} {b} {c}")
                return

if __name__ == '__main__':
    solve()