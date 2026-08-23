import sys

def solve():
    # Use fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Represent the graph as an adjacency list of sets or bitsets for fast lookup
    # Since n <= 2000, bitsets (using Python's large integers) are efficient
    adj = [0] * (n + 1)
    edges = []
    
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        idx += 2
        if u > v:
            u, v = v, u
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
        edges.append((u, v))
    
    # We want the lexicographically smallest (a, b, c) with a < b < c.
    # Lexicographically smallest means smallest a, then smallest b, then smallest c.
    # Sort edges primarily by u, then by v.
    edges.sort()
    
    # Iterate through all possible a, b, c
    # To minimize (a, b, c), we iterate a from 1 to n, b from a+1 to n, etc.
    # A triplet (a, b, c) exists if b is a neighbor of a, c is a neighbor of a,
    # and c is a neighbor of b.
    
    for a in range(1, n + 1):
        # Get neighbors of a that are greater than a
        neighbors_a = []
        bitmask_a = adj[a]
        for b in range(a + 1, n + 1):
            if (bitmask_a >> b) & 1:
                neighbors_a.append(b)
        
        # Now check if any two neighbors b, c are connected
        for i in range(len(neighbors_a)):
            b = neighbors_a[i]
            # Check if there exists c in neighbors_a[i+1:] such that c is neighbor of b
            # Intersection of neighbors of a and neighbors of b
            common = adj[a] & adj[b]
            # We only care about c > b
            for c in range(b + 1, n + 1):
                if (common >> c) & 1:
                    print(f"{a} {b} {c}")
                    return

solve()