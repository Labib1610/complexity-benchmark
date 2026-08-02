import sys

def solve():
    # Use fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Use adjacency lists and a bitset-like approach for fast intersection
    # Since n <= 2000, we can use Python's large integers as bitsets.
    # adj_bitset[i] will be a bitmask where the j-th bit is 1 if port i and j are connected.
    adj_bitset = [0] * (n + 1)
    adj_list = [[] for _ in range(n + 1)]
    
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        idx += 2
        
        # Ensure u < v for consistent adjacency list ordering
        if u > v:
            u, v = v, u
        
        adj_bitset[u] |= (1 << v)
        adj_bitset[v] |= (1 << u)
        adj_list[u].append(v)
        adj_list[v].append(u)

    # To find the lexicographically smallest (a, b, c) with a < b < c:
    # Iterate a from 1 to n
    # Iterate b from a+1 to n
    # If a and b are connected, check for common neighbors c > b
    
    # Sort adjacency lists to iterate b in increasing order
    for i in range(1, n + 1):
        adj_list[i].sort()

    for a in range(1, n - 1):
        # Only consider neighbors of a that are > a
        neighbors_of_a = [v for v in adj_list[a] if v > a]
        
        for b in neighbors_of_a:
            # We need a common neighbor c of a and b such that c > b
            # The intersection of neighbors of a and neighbors of b gives common neighbors
            # We mask the result to only keep bits > b
            common = adj_bitset[a] & adj_bitset[b]
            
            # Mask to remove bits <= b
            # (1 << (b + 1)) - 1 creates a mask of 1s from bit 0 to b
            # Bitwise NOT (~) and ANDing will clear bits 0 to b
            mask = ~((1 << (b + 1)) - 1)
            candidates = common & mask
            
            if candidates:
                # Find the lowest set bit in candidates (the smallest c > b)
                # c = (candidates & -candidates).bit_length() - 1 is not quite right for Python's arbitrary precision
                # Use bit_length of (candidates & -candidates) or simply find first set bit
                # Since we need the smallest c, we can use (candidates & -candidates).bit_length() - 1 
                # but a simpler way is:
                c = (candidates & -candidates).bit_length() - 1
                print(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()