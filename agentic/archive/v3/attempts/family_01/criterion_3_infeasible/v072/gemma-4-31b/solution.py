import sys

def solve():
    # Use fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Adjacency list and adjacency matrix for fast lookup
    # Since n <= 2000, a bitset-like approach or a boolean matrix is feasible.
    # Python's 'int' can act as a bitset.
    adj_bitset = [0] * (n + 1)
    adj_list = [[] for _ in range(n + 1)]
    
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        idx += 2
        if u > v:
            u, v = v, u
        adj_list[u].append(v)
        adj_bitset[u] |= (1 << v)
        adj_bitset[v] |= (1 << u)

    # Sort adjacency lists to ensure lexicographical order
    for i in range(1, n + 1):
        adj_list[i].sort()

    # To find the lexicographically smallest (a, b, c) with a < b < c:
    # Iterate a from 1 to n
    # Iterate b from adj_list[a] (where b > a)
    # Find the smallest c > b such that c is connected to both a and b.
    
    for a in range(1, n + 1):
        # Only consider neighbors b of a where b > a
        for b in adj_list[a]:
            if b <= a:
                continue
            
            # We need c > b such that c is connected to both a and b.
            # The set of common neighbors is the bitwise AND of their adjacency bitsets.
            common = adj_bitset[a] & adj_bitset[b]
            
            if common:
                # We need the smallest c > b.
                # Mask out bits <= b.
                # mask = ~((1 << (b + 1)) - 1)
                # common &= mask
                # However, since we need the smallest c, we can use bit_length and 
                # trailing zeros or simply check from b+1.
                # But the most efficient way in Python is to find the lowest set bit 
                # that is greater than b.
                
                # Mask to keep only bits > b
                mask = ~((1 << (b + 1)) - 1)
                candidates = common & mask
                
                if candidates:
                    # Find the position of the lowest set bit
                    # LSB = candidates & -candidates
                    # c = (candidates & -candidates).bit_length() - 1
                    # But bit_length() is for the highest set bit.
                    # For the lowest set bit:
                    lsb = candidates & -candidates
                    c = lsb.bit_length() - 1
                    print(f"{a} {b} {c}")
                    return

if __name__ == "__main__":
    solve()