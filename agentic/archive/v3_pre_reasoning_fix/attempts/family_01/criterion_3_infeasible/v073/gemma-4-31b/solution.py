import sys

def solve():
    # Read n and m from the first line
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Adjacency list for graph
    adj = [[] for _ in range(n + 1)]
    ptr = 2
    for _ in range(m):
        u = int(input_data[ptr])
        v = int(input_data[ptr + 1])
        adj[u].append(v)
        adj[v].append(u)
        ptr += 2
        
    # To find the lexicographically smallest triple (a, b, c),
    # we iterate a from 1 to n, b from a+1 to n, and check for c.
    # To optimize, we use bitsets (represented as integers in Python) 
    # to find the intersection of neighbors of a and b.
    
    # Precompute adjacency bitsets for all nodes
    bitsets = [0] * (n + 1)
    for i in range(1, n + 1):
        for neighbor in adj[i]:
            bitsets[i] |= (1 << neighbor)
            
    # Sort adjacency lists to iterate b in increasing order
    for i in range(1, n + 1):
        adj[i].sort()

    # Iterate through possible values of a
    for a in range(1, n - 1):
        # To minimize b, we only check neighbors of a that are > a
        # Sort neighbors of a to iterate b in increasing order
        neighbors_a = [v for v in adj[a] if v > a]
        
        for b in neighbors_a:
            # Find common neighbors of a and b that are > b
            # Intersection of bitsets[a] and bitsets[b]
            common = bitsets[a] & bitsets[b]
            
            # We need the smallest c such that c > b and c is a common neighbor
            # Mask out all bits <= b
            mask = ~((1 << (b + 1)) - 1)
            candidates = common & mask
            
            if candidates:
                # Find the lowest set bit (the smallest c)
                # Using bit_length() and bin() is slow, use (candidates & -candidates).bit_length()
                # or simply iterate since we need the smallest c.
                # In Python, (candidates & -candidates).bit_length() gives the position of the first 1.
                low_bit = candidates & -candidates
                c = low_bit.bit_length() - 1
                print(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()