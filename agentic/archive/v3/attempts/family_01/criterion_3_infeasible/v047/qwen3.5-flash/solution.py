import sys
from bisect import bisect_right
from itertools import islice

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

    # Adjacency list using 1-based indexing
    adj = [[] for _ in range(n + 1)]
    
    # Adjacency matrix for O(1) edge checks
    # Since n <= 2000, n^2 = 4,000,000, which fits in memory easily.
    is_connected = [[False] * (n + 1) for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        
        adj[u].append(v)
        adj[v].append(u)
        is_connected[u][v] = True
        is_connected[v][u] = True
        
    # Sort adjacency lists to facilitate lexicographical search
    # This ensures we process neighbors in increasing order
    for i in range(1, n + 1):
        adj[i].sort()
        
    # Iterate to find the lexicographically smallest triplet (a, b, c) with a < b < c
    for a in range(1, n + 1):
        # We need to find b > a such that (a, b) is an edge.
        # adj[a] is sorted. bisect_right finds the first index where elements > a start.
        start_b_idx = bisect_right(adj[a], a)
        
        # Iterate through neighbors b of a such that b > a
        for b in islice(adj[a], start_b_idx, None):
            # We have a < b. Now we need to find c > b such that (a, c) and (b, c) are edges.
            # We want the smallest such c.
            # This corresponds to finding the smallest element in the intersection of adj[a] and adj[b] that is > b.
            # To optimize, we iterate over the smaller of the two neighbor lists.
            
            L1 = adj[a]
            L2 = adj[b]
            
            if len(L1) < len(L2):
                # Iterate L1 (adj[a])
                # We need c > b. Since b is in L1, bisect_right gives index after b.
                start_c_idx = bisect_right(L1, b)
                
                # Check connectivity to b for each candidate c
                row_b = is_connected[b]
                for c in islice(L1, start_c_idx, None):
                    if row_b[c]:
                        # Found the smallest c for this (a, b).
                        # Since we iterate a increasing, b increasing, and c increasing,
                        # this is the lexicographically first triplet.
                        print(f"{a} {b} {c}")
                        return
            else:
                # Iterate L2 (adj[b])
                # We need c > b.
                start_c_idx = bisect_right(L2, b)
                
                # Check connectivity to a for each candidate c
                row_a = is_connected[a]
                for c in islice(L2, start_c_idx, None):
                    if row_a[c]:
                        print(f"{a} {b} {c}")
                        return

if __name__ == '__main__':
    solve()