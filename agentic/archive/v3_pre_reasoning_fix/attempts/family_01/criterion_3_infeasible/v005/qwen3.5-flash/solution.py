import sys
from bisect import bisect_right

# Increase recursion depth just in case, though not needed here
sys.setrecursionlimit(2000)

def solve():
    # Read all input from standard input
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # Adjacency list and matrix
    # Workers are 1-indexed
    adj = [[] for _ in range(n + 1)]
    # Using a list of lists for adjacency matrix for O(1) access
    # Initialize with False
    mat = [[False] * (n + 1) for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
        mat[u][v] = True
        mat[v][u] = True
        
    # Sort adjacency lists to allow binary search and ordered iteration
    for i in range(1, n + 1):
        adj[i].sort()
        
    # Iterate to find the lexicographically smallest triple (a, b, c)
    # a < b < c
    for a in range(1, n + 1):
        # Iterate over neighbors b of a
        # We want b > a. Since adj[a] is sorted, we can find the start.
        # But simply iterating and checking is fine.
        
        # To optimize, we can find the index of the first element > a
        # using bisect_right, but iterating is also O(d(a))
        # Let's iterate with index to be able to use Case 1 optimization
        
        # adj[a] contains neighbors. We need b > a.
        # We can iterate through the list.
        
        # Optimization: if degree is small, we might not find a triangle starting with a
        # But we must check a.
        
        # We iterate b in adj[a].
        # We need to keep track of index to avoid bisect in Case 1.
        
        # Let's enumerate to get index
        for idx_b, b in enumerate(adj[a]):
            if b <= a:
                continue
            
            # We have edge (a, b) with a < b.
            # Now we look for c > b such that (a, c) and (b, c) are edges.
            # We want smallest c.
            
            # Strategy: iterate over the smaller adjacency list between a and b
            # to find common neighbor c > b.
            
            len_adj_a = len(adj[a])
            len_adj_b = len(adj[b])
            
            if len_adj_a < len_adj_b:
                # Iterate over adj[a]
                # We need c in adj[a] such that c > b.
                # Since adj[a] is sorted and b is at idx_b,
                # all neighbors > b are at indices > idx_b.
                # So we iterate k from idx_b + 1 to len_adj_a.
                
                # This avoids bisect and is very efficient.
                # We check if mat[b][c] is true.
                
                # Local variable optimization
                mat_b = mat[b]
                for k in range(idx_b + 1, len_adj_a):
                    c = adj[a][k]
                    if mat_b[c]:
                        print(f"{a} {b} {c}")
                        return
            else:
                # Iterate over adj[b]
                # We need c in adj[b] such that c > b.
                # Use bisect_right to find the first index where element > b.
                # adj[b] does not contain b, so bisect_right returns index of first element > b.
                
                start_idx = bisect_right(adj[b], b)
                
                mat_a = mat[a]
                for k in range(start_idx, len_adj_b):
                    c = adj[b][k]
                    if mat_a[c]:
                        print(f"{a} {b} {c}")
                        return

if __name__ == '__main__':
    solve()