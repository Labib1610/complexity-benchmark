import sys

def solve():
    # Use fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Use adjacency lists to store the graph
    adj = [[] for _ in range(n + 1)]
    # Use a bitset-like approach or a set for fast lookup
    # Given n=2000, a bitset (integer in Python) can represent the adjacency matrix
    # bitset[i] will have the j-th bit set if i and j are incompatible
    adj_bitset = [0] * (n + 1)
    
    ptr = 2
    for _ in range(m):
        u = int(input_data[ptr])
        v = int(input_data[ptr + 1])
        ptr += 2
        if u > v:
            u, v = v, u
        adj[u].append(v)
        adj_bitset[u] |= (1 << v)
        adj_bitset[v] |= (1 << u)

    # To find the lexicographically smallest (a, b, c), 
    # we iterate through a from 1 to n, then b from a+1 to n, then c from b+1 to n.
    # However, a naive O(n^3) is too slow. 
    # We can optimize by iterating through a and b, and then finding c using bitwise AND.
    
    # Pre-sort adjacency lists to ensure we process potential 'b' values in increasing order
    for i in range(1, n + 1):
        adj[i].sort()

    for a in range(1, n - 1):
        # We only care about neighbors of a that are > a
        neighbors_of_a = [v for v in adj[a] if v > a]
        
        # To find the smallest b, we iterate through neighbors_of_a
        for i in range(len(neighbors_of_a)):
            b = neighbors_of_a[i]
            
            # We need a technician c such that c > b, c is a neighbor of a, and c is a neighbor of b.
            # This is equivalent to finding the smallest set bit in (adj_bitset[a] & adj_bitset[b]) 
            # that is greater than b.
            
            common = adj_bitset[a] & adj_bitset[b]
            
            # Clear bits <= b to find the smallest c > b
            # mask = ~((1 << (b + 1)) - 1)
            # common &= mask
            
            # A faster way to clear bits 0 to b:
            common >>= (b + 1)
            if common:
                # Find the index of the lowest set bit
                # low_bit = common & -common
                # c = low_bit.bit_length() + b
                # Since Python's bit_length() is efficient:
                c = (common & -common).bit_length() + b
                print(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()