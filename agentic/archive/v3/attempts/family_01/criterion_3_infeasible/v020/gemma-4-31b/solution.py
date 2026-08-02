import sys

def solve():
    # Use fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Adjacency list for graph traversal
    adj = [[] for _ in range(n + 1)]
    # Bitsets for fast intersection check (using Python's arbitrary precision integers)
    bitsets = [0] * (n + 1)
    
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        idx += 2
        if u > v:
            u, v = v, u
        adj[u].append(v)
        bitsets[u] |= (1 << v)
        bitsets[v] |= (1 << u)

    # To find the lexicographically smallest (a, b, c) with a < b < c:
    # We iterate a from 1 to n, then b from a+1 to n.
    # For a fixed a and b, if they are connected, we look for the smallest c > b
    # such that c is connected to both a and b.
    
    # Sort adjacency lists to iterate through b in increasing order
    for i in range(1, n + 1):
        adj[i].sort()

    for a in range(1, n - 1):
        # We only care about neighbors of a that are greater than a
        # Since adj[a] is sorted, we can iterate through it
        for b in adj[a]:
            if b <= a:
                continue
            
            # We need c > b such that c is connected to both a and b.
            # This is the intersection of neighbors of a and neighbors of b,
            # filtered for values > b.
            
            # common_neighbors = bitsets[a] & bitsets[b]
            # To find the smallest c > b, we mask out bits <= b.
            # Mask for bits > b is ~((1 << (b + 1)) - 1)
            
            common = bitsets[a] & bitsets[b]
            if common:
                # Mask to keep only bits > b
                mask = ~((1 << (b + 1)) - 1)
                candidates = common & mask
                if candidates:
                    # Find the lowest set bit in candidates
                    # (candidates & -candidates).bit_length() - 1 gives the index of the lowest set bit
                    c = (candidates & -candidates).bit_length() - 1
                    print(f"{a} {b} {c}")
                    return

if __name__ == "__main__":
    solve()