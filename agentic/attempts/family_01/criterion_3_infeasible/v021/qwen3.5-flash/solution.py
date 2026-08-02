import sys
from bisect import bisect_right

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

    # Initialize adjacency list and matrix
    # 1-based indexing
    adj = [[] for _ in range(n + 1)]
    # Using bytearray for adjacency matrix for memory efficiency and speed
    # has_edge[u][v] = 1 if edge exists, 0 otherwise
    has_edge = [bytearray(n + 1) for _ in range(n + 1)]

    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
        has_edge[u][v] = 1
        has_edge[v][u] = 1

    # Sort adjacency lists to process in increasing order
    # This is crucial for finding the lexicographically smallest triplet
    for i in range(1, n + 1):
        adj[i].sort()

    # Iterate to find lexicographically smallest triangle (a, b, c) with a < b < c
    # We iterate a from 1 to n.
    # For each a, we iterate b > a that is a neighbor of a.
    # For each pair (a, b), we find the smallest c > b that is a neighbor of both a and b.
    
    for a in range(1, n + 1):
        # Iterate neighbors b of a
        # We use enumerate to keep track of index i for optimization
        for i, b in enumerate(adj[a]):
            if b <= a:
                continue
            
            # We need to find smallest c > b such that c is in adj[a] and adj[b].
            # Since c must be > b, we only consider neighbors > b.
            # From adj[a], candidates are elements after b (since b is at index i and sorted).
            # From adj[b], candidates are elements > b.
            
            # Optimization: iterate over the smaller set of candidates to minimize checks.
            
            # Count of candidates from adj[a]
            # adj[a][i] is b. So elements > b start at i+1.
            # Count = length - (i + 1)
            count_a = len(adj[a]) - (i + 1)
            
            # Count of candidates from adj[b]
            # We need elements > b in adj[b].
            # Using bisect_right to find the index of first element > b.
            # Note: adj[b] does not contain b (simple graph), so bisect_right works correctly.
            idx_b = bisect_right(adj[b], b)
            count_b = len(adj[b]) - idx_b
            
            # Choose the list with fewer candidates to iterate
            if count_a < count_b:
                # Iterate adj[a] starting from i+1
                # We check if c is a neighbor of b using the adjacency matrix.
                row_b = has_edge[b]
                for k in range(i + 1, len(adj[a])):
                    c = adj[a][k]
                    # Since adj[a] is sorted, c >= b. 
                    # We rely on has_edge[b][b] being 0 to skip c=b case (no self loops).
                    if row_b[c]:
                        print(a, b, c)
                        return
            else:
                # Iterate adj[b] starting from idx_b
                row_a = has_edge[a]
                for k in range(idx_b, len(adj[b])):
                    c = adj[b][k]
                    if row_a[c]:
                        print(a, b, c)
                        return

if __name__ == '__main__':
    solve()