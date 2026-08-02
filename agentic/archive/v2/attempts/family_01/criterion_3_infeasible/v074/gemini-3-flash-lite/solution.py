import sys

def solve():
    # Read n and m
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Use bitsets for adjacency to check for cliques efficiently
    # adj[i] will store a bitmask of workers incompatible with i
    # Since n <= 2000, we can use Python's arbitrary precision integers as bitsets
    adj = [0] * (n + 1)
    
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
        
    # We need the lexicographically smallest (a, b, c) with a < b < c
    # Iterate a from 1 to n-2
    for a in range(1, n - 1):
        # Candidates for b must be > a and incompatible with a
        # b_candidates is a bitmask of nodes > a that are neighbors of a
        b_candidates = adj[a] >> (a + 1)
        if b_candidates == 0:
            continue
            
        # Iterate b from a+1 to n-1
        for b in range(a + 1, n):
            if (adj[a] & (1 << b)):
                # Now we need c > b such that c is neighbor of a AND c is neighbor of b
                # common_neighbors is (adj[a] & adj[b])
                # We only care about bits > b
                common_mask = (adj[a] & adj[b]) >> (b + 1)
                if common_mask > 0:
                    # Find the smallest c > b
                    # (common_mask & -common_mask) gives the lowest set bit
                    # bit_length() gives the position
                    c = (common_mask & -common_mask).bit_length() + b
                    print(f"{a} {b} {c}")
                    return

if __name__ == '__main__':
    solve()