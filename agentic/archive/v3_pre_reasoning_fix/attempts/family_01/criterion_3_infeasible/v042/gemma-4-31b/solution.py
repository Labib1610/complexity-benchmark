import sys

def solve():
    # Read n and m
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Use adjacency lists to store the graph
    # adj[u] will store all neighbors v of u such that v > u
    adj = [[] for _ in range(n + 1)]
    # Use a bitset-like approach for fast intersection check
    # Since n <= 2000, we can use Python's large integers as bitsets
    bitsets = [0] * (n + 1)
    
    ptr = 2
    for _ in range(m):
        u = int(input_data[ptr])
        v = int(input_data[ptr+1])
        ptr += 2
        if u > v:
            u, v = v, u
        adj[u].append(v)
        bitsets[u] |= (1 << v)
        bitsets[v] |= (1 << u)

    # Sort neighbors to ensure we find the lexicographically smallest triple
    for i in range(1, n + 1):
        adj[i].sort()

    # To find the lexicographically smallest (a, b, c) where a < b < c:
    # Iterate a from 1 to n
    # Iterate b from the sorted neighbors of a that are > a
    # Check if there is a c > b such that c is a neighbor of both a and b
    for a in range(1, n + 1):
        neighbors_a = adj[a]
        # We only care about neighbors b > a
        # Since adj[a] is sorted, we can iterate through them
        for b in neighbors_a:
            # We need c > b. We can intersect the bitsets of a and b
            # and find the smallest bit set that is greater than b.
            common = bitsets[a] & bitsets[b]
            if common:
                # We need the smallest c > b. 
                # Mask out bits <= b.
                # common & ~((1 << (b + 1)) - 1) clears bits 0 to b.
                mask = ~((1 << (b + 1)) - 1)
                candidates = common & mask
                if candidates:
                    # Find the lowest set bit (the smallest c > b)
                    # c = (candidates & -candidates).bit_length() - 1
                    # However, in Python, candidates.bit_length() is not enough.
                    # We can use (candidates & -candidates).bit_length() - 1
                    # But simpler:
                    c = (candidates & -candidates).bit_length() - 1
                    print(f"{a} {b} {c}")
                    return

if __name__ == "__main__":
    solve()