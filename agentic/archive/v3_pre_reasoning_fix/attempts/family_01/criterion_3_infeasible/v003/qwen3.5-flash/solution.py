import sys
import bisect

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

    # Adjacency list to store neighbors
    adj = [[] for _ in range(n + 1)]
    
    # Adjacency matrix for O(1) edge lookup
    # Using bytearray for memory efficiency and speed.
    # mat[u][v] will be 1 if an edge exists, 0 otherwise.
    mat = [bytearray(n + 1) for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
        mat[u][v] = 1
        mat[v][u] = 1
        
    # Sort adjacency lists to facilitate binary search and ordered iteration
    for i in range(1, n + 1):
        adj[i].sort()
        
    # Iterate a from 1 to n to find the lexicographically smallest triple (a, b, c)
    # with a < b < c.
    for a in range(1, n + 1):
        # We need b to be a neighbor of a such that b > a.
        # Since adj[a] is sorted, we can find the starting index using bisect.
        idx_a_start = bisect.bisect_right(adj[a], a)
        
        # Iterate through potential b's
        for i in range(idx_a_start, len(adj[a])):
            b = adj[a][i]
            
            # We need to find c > b such that (b, c) is an edge.
            # Also, c must be a neighbor of a (since (a, c) must be an edge).
            # So c must be in N(a) AND N(b) and c > b.
            # We want the smallest such c.
            
            # To optimize, we iterate over the smaller of the two adjacency lists (N(a) or N(b)).
            # We filter for elements > b using binary search.
            
            len_a = len(adj[a])
            len_b = len(adj[b])
            
            if len_a < len_b:
                # Iterate c in adj[a]
                # Find the first index where element > b
                idx_c = bisect.bisect_right(adj[a], b)
                for j in range(idx_c, len_a):
                    c = adj[a][j]
                    # Check if c is connected to b
                    if mat[b][c]:
                        print(f"{a} {b} {c}")
                        return
            else:
                # Iterate c in adj[b]
                # Find the first index where element > b
                idx_c = bisect.bisect_right(adj[b], b)
                for j in range(idx_c, len_b):
                    c = adj[b][j]
                    # Check if c is connected to a
                    if mat[a][c]:
                        print(f"{a} {b} {c}")
                        return

if __name__ == '__main__':
    solve()