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

    # Precompute powers of 2 for bit manipulation
    # pows[i] corresponds to bit i (1-based index for nodes)
    pows = [0] * (n + 1)
    for i in range(1, n + 1):
        pows[i] = 1 << i
        
    # Adjacency bitmasks and lists
    adj = [0] * (n + 1)
    adj_list = [[] for _ in range(n + 1)]
    
    # Read edges
    for _ in range(m):
        try:
            u = int(next(iterator))
            v = int(next(iterator))
        except StopIteration:
            break
            
        adj[u] |= pows[v]
        adj[v] |= pows[u]
        adj_list[u].append(v)
        adj_list[v].append(u)
        
    # Sort adjacency lists to process neighbors in increasing order
    # This is crucial for finding the lexicographically smallest triple
    for i in range(1, n + 1):
        adj_list[i].sort()
        
    # Iterate a from 1 to n
    for a in range(1, n + 1):
        # Iterate neighbors b of a
        # Since adj_list is sorted, we encounter b in increasing order
        for b in adj_list[a]:
            if b > a:
                # Check if there is a common neighbor c > b
                # Intersect adjacency bitmasks of a and b
                common = adj[a] & adj[b]
                
                # We need smallest c in common such that c > b
                # Shift right by b + 1 to remove bits <= b
                shifted = common >> (b + 1)
                
                if shifted:
                    # Find lowest set bit in shifted
                    # lsb_mask = shifted & -shifted gives the lowest set bit as a power of 2
                    # bit_length() - 1 gives the 0-based index of that bit
                    lsb_mask = shifted & -shifted
                    c = b + 1 + lsb_mask.bit_length() - 1
                    
                    # We found the lexicographically smallest triple (a, b, c)
                    # because we iterate a, then b, then find smallest c.
                    print(f"{a} {b} {c}")
                    return

if __name__ == '__main__':
    solve()