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

    # adj_mask[u] is a bitmask where the v-th bit is set if u and v are incompatible.
    # We use 0-based indexing for nodes internally (0 to n-1).
    # Since n <= 2000, integers with 2000 bits are manageable in Python.
    adj_mask = [0] * n
    
    # adj_list[u] stores the list of neighbors of u.
    adj_list = [[] for _ in range(n)]

    for _ in range(m):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        
        adj_mask[u] |= (1 << v)
        adj_mask[v] |= (1 << u)
        
        adj_list[u].append(v)
        adj_list[v].append(u)

    # Sort adjacency lists to ensure we process neighbors in increasing order.
    # This is crucial for finding the lexicographically smallest triplet.
    for i in range(n):
        adj_list[i].sort()

    # Iterate a from 0 to n-1. Since we want lexicographically smallest (a, b, c),
    # we start with the smallest possible a.
    for a in range(n):
        # Iterate neighbors b of a. Since adj_list[a] is sorted, b will be in increasing order.
        # We only care about b > a because we want a < b < c.
        for b in adj_list[a]:
            if b <= a:
                continue
            
            # We need to find a neighbor c of both a and b such that c > b.
            # We want the smallest such c.
            # We can find common neighbors by bitwise AND of their masks.
            common = adj_mask[a] & adj_mask[b]
            
            # We need the smallest bit set in 'common' that is > b.
            # This corresponds to bits >= b + 1.
            # We can mask out bits < b + 1 using -(1 << (b + 1)).
            # In Python, -(1 << k) is a negative number with 0s at bits 0..k-1 and 1s at bits >= k.
            # This effectively keeps bits >= b + 1 from 'common' and clears bits <= b.
            
            candidates = common & -(1 << (b + 1))
            
            if candidates:
                # If candidates is non-zero, there exists at least one c > b.
                # We need the smallest such c, which corresponds to the lowest set bit.
                # (candidates & -candidates) isolates the lowest set bit.
                lsb = candidates & -candidates
                c = lsb.bit_length() - 1
                
                # Output the result (converting back to 1-based indexing)
                print(f"{a + 1} {b + 1} {c + 1}")
                return

if __name__ == '__main__':
    solve()