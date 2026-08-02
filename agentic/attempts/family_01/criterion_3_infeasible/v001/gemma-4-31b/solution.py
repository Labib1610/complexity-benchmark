import sys

def solve():
    # Increase recursion depth just in case, though not needed for this approach
    sys.setrecursionlimit(2000)
    
    # Read n and m
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # We need to find the lexicographically smallest triple (a, b, c)
    # such that a < b < c and all pairs are connected.
    # Since n is up to 2000, an O(n^3) approach is too slow.
    # However, we can iterate through all pairs (a, b) and check common neighbors.
    # To get the lexicographically smallest, we iterate a from 1 to n,
    # then b from a+1 to n, then c from b+1 to n.
    
    adj = [set() for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj[u].add(v)
        adj[v].add(u)
        idx += 2

    # To optimize, we use bitsets. In Python, large integers act as bitsets.
    # bit_adj[i] will be a bitmask where the j-th bit is 1 if i and j are connected.
    bit_adj = [0] * (n + 1)
    for i in range(1, n + 1):
        mask = 0
        for neighbor in adj[i]:
            mask |= (1 << neighbor)
        bit_adj[i] = mask

    # We want lexicographically smallest (a, b, c) with a < b < c.
    # Iterate a from 1 to n.
    for a in range(1, n + 1):
        # To find b and c, they must both be neighbors of a and b < c.
        # Get all neighbors of a that are > a.
        neighbors_of_a = sorted([v for v in adj[a] if v > a])
        
        # Iterate through pairs of neighbors of a.
        for i in range(len(neighbors_of_a)):
            b = neighbors_of_a[i]
            # We need to find the smallest c > b such that c is a neighbor of both a and b.
            # The candidates for c are neighbors of a that are > b.
            # We can use bitwise AND to find common neighbors of a and b.
            
            # common_neighbors = bit_adj[a] & bit_adj[b]
            # We only care about neighbors > b.
            # A mask for bits > b is ~((1 << (b + 1)) - 1)
            
            common_mask = bit_adj[a] & bit_adj[b]
            # We need the smallest bit set in common_mask that is > b.
            # To efficiently find the smallest bit > b:
            # We can clear bits <= b and then find the lowest set bit.
            
            # Clear bits 0 to b
            valid_c_mask = common_mask & ~((1 << (b + 1)) - 1)
            
            if valid_c_mask:
                # Find the lowest set bit (LSB)
                # LSB is (valid_c_mask & -valid_c_mask).bit_length() - 1
                # But Python's bit_length is for the highest bit.
                # The lowest set bit can be found by:
                lsb = (valid_c_mask & -valid_c_mask).bit_length() - 1
                print(f"{a} {b} {lsb}")
                return

if __name__ == "__main__":
    solve()