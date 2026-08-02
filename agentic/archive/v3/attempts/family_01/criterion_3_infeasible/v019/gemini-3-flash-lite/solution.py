import sys

def solve():
    # Read n and m
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Use bitsets (Python integers) for fast intersection checks
    adj = [0] * (n + 1)
    
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
        
    # To find the lexicographically smallest triplet (a, b, c) with a < b < c:
    # Iterate a from 1 to n-2, b from a+1 to n-1, c from b+1 to n.
    # Check if a, b, c are mutually incompatible.
    # Condition: b is in adj[a], c is in adj[a], and c is in adj[b].
    
    for a in range(1, n + 1):
        adj_a = adj[a]
        # Get all neighbors of a that are > a
        # We only care about neighbors b where b > a
        # To optimize, iterate through potential b's
        for b in range(a + 1, n + 1):
            if (adj_a >> b) & 1:
                # b is a neighbor of a. Now check for c > b
                # c must be a neighbor of both a and b
                common = adj_a & adj[b]
                # We need the smallest c > b
                # Shift right by (b + 1) to ignore indices <= b
                c_candidates = common >> (b + 1)
                if c_candidates > 0:
                    # Find the index of the lowest set bit
                    # (c_candidates & -c_candidates) gives the lowest bit
                    # bit_length() - 1 gives the index
                    c = (c_candidates & -c_candidates).bit_length() + b
                    print(f"{a} {b} {c}")
                    return

if __name__ == '__main__':
    solve()