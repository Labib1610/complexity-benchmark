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

    # Use bytearray for adjacency matrix for O(1) access and lower memory usage
    # Indices are 1 to n, so we need size n + 1
    adj = [bytearray(n + 1) for _ in range(n + 1)]
    
    # Adjacency lists to iterate over neighbors
    adj_list = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u][v] = 1
        adj[v][u] = 1
        adj_list[u].append(v)
        adj_list[v].append(u)
        
    # Sort adjacency lists and remove duplicates to facilitate iteration
    for i in range(1, n + 1):
        if adj_list[i]:
            adj_list[i] = sorted(set(adj_list[i]))
            
    # Array to mark elements in L for O(1) membership check
    # We reuse this array. We will only set True for elements in L and reset afterwards.
    in_L = [False] * (n + 1)
    
    # Iterate through each worker 'a' to be the first element of the triple
    # We want the lexicographically smallest triple, so we iterate 'a' from 1 to n.
    for a in range(1, n + 1):
        # Get neighbors of 'a' that are greater than 'a'.
        # Since adj_list[a] is sorted, we can find the slice efficiently.
        # bisect_right returns the index where all elements to the left are <= a.
        idx_a = bisect_right(adj_list[a], a)
        L = adj_list[a][idx_a:]
        
        if not L:
            continue
        
        # Mark elements of L in in_L for fast lookup
        for x in L:
            in_L[x] = True
            
        len_L = len(L)
        
        # Iterate through 'b' in L.
        # Since L is sorted, iterating in order ensures we find the smallest 'b' first.
        for i in range(len_L):
            b = L[i]
            
            # We need to find the smallest 'c' such that c > b, c is in L, and (b, c) is an edge.
            # To optimize, we iterate over the smaller set of neighbors of 'a' (which is L)
            # OR neighbors of 'b' (adj_list[b]).
            # We want the intersection of L and adj_list[b] restricted to c > b.
            
            deg_b = len(adj_list[b])
            
            if deg_b < len_L:
                # Iterate over neighbors of b.
                # We need c > b and c in L.
                # Find first neighbor > b using binary search.
                idx_b = bisect_right(adj_list[b], b)
                
                # Iterate through the slice. 
                # Slicing creates a copy, but since deg_b < len_L, it's efficient enough.
                for c in adj_list[b][idx_b:]:
                    if in_L[c]:
                        # Found the lexicographically smallest triple
                        print(f"{a} {b} {c}")
                        return
            else:
                # Iterate over neighbors in L that are > b.
                # Since L is sorted, these are L[i+1:].
                # We iterate using index to avoid slicing L.
                for j in range(i + 1, len_L):
                    c = L[j]
                    if adj[b][c]:
                        # Found the lexicographically smallest triple
                        print(f"{a} {b} {c}")
                        return
        
        # Clean up in_L for the next iteration of 'a'
        for x in L:
            in_L[x] = False

if __name__ == '__main__':
    solve()