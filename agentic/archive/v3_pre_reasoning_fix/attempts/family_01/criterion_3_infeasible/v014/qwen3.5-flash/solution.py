import sys
from bisect import bisect_right

# Increase recursion depth just in case, though not needed for this iterative solution
sys.setrecursionlimit(2000)

def solve():
    # Read all input from stdin efficiently
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
    
    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # Adjacency list
    adj = [[] for _ in range(n + 1)]
    # Adjacency matrix as bitmasks for O(1) edge checks
    # adj_matrix[u] is an integer where the v-th bit is set if (u, v) exists
    # This allows checking existence of edge (u, v) with (adj_matrix[u] >> v) & 1
    adj_matrix = [0] * (n + 1)
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
        adj_matrix[u] |= (1 << v)
        adj_matrix[v] |= (1 << u)
        
    # Sort adjacency lists to facilitate lexicographical search
    # This ensures that when we iterate neighbors, we encounter them in increasing order
    for i in range(1, n + 1):
        adj[i].sort()
        
    # Iterate a from 1 to n to find the lexicographically smallest triplet (a, b, c)
    # We want to minimize a, then b, then c.
    for a in range(1, n + 1):
        # We only consider neighbors b such that b > a
        # Find the starting index in adj[a] for elements > a
        idx_start_b = bisect_right(adj[a], a)
        len_adj_a = len(adj[a])
        
        # Iterate over valid b in increasing order
        for k_b in range(idx_start_b, len_adj_a):
            b = adj[a][k_b]
            # Now we have edge (a, b) with a < b
            
            # We need to find c > b such that (a, c) and (b, c) exist.
            # We want the smallest such c.
            # To optimize, we iterate over the neighbor list with smaller degree.
            # We also need to ensure c > b.
            
            if len(adj[a]) < len(adj[b]):
                # Iterate neighbors of a
                # Find index for first element > b
                idx_c = bisect_right(adj[a], b)
                # Iterate c in increasing order
                for k_c in range(idx_c, len_adj_a):
                    c = adj[a][k_c]
                    # Check if edge (b, c) exists
                    if (adj_matrix[b] >> c) & 1:
                        print(f"{a} {b} {c}")
                        return
            else:
                # Iterate neighbors of b
                # Find index for first element > b
                idx_c = bisect_right(adj[b], b)
                len_adj_b = len(adj[b])
                # Iterate c in increasing order
                for k_c in range(idx_c, len_adj_b):
                    c = adj[b][k_c]
                    # Check if edge (a, c) exists
                    if (adj_matrix[a] >> c) & 1:
                        print(f"{a} {b} {c}")
                        return

if __name__ == '__main__':
    solve()