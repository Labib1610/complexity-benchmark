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

    # Adjacency matrix using bytearray for memory efficiency and O(1) lookup
    # Indices are 1-based, so size is n + 1
    adj = [bytearray(n + 1) for _ in range(n + 1)]
    
    # Adjacency lists for iterating over neighbors
    adj_list = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        
        adj[u][v] = 1
        adj[v][u] = 1
        
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    # Sort adjacency lists to allow efficient iteration and checks
    for i in range(1, n + 1):
        adj_list[i].sort()
        
    # Iterate to find the lexicographically smallest triple (a, b, c)
    # We want the smallest a, then smallest b, then smallest c.
    for a in range(1, n + 1):
        neighbors_a = adj_list[a]
        len_na = len(neighbors_a)
        
        # Iterate over neighbors b of a
        # We use enumerate to get the index i of b in neighbors_a
        for i, b in enumerate(neighbors_a):
            if b <= a:
                continue
            
            # We have a valid edge (a, b) with a < b.
            # We need to find c such that c > b and c is connected to both a and b.
            # We want the smallest such c.
            # We iterate over the smaller of the two neighbor lists to minimize operations.
            # The complexity of this approach is O(m * sqrt(m)), which fits within the time limit.
            
            len_nb = len(adj_list[b])
            
            if len_na <= len_nb:
                # We iterate through neighbors of a.
                # Since we need c > b, and neighbors_a is sorted,
                # we can start checking from the element after b.
                # b is at index i in neighbors_a.
                # So we iterate j from i + 1 to end.
                
                # Optimization: cache adj[b]
                row_b = adj[b]
                
                for j in range(i + 1, len_na):
                    c = neighbors_a[j]
                    # Check if c is a neighbor of b
                    if row_b[c]:
                        # Found the triple
                        print(f"{a} {b} {c}")
                        return
            else:
                # We iterate through neighbors of b.
                # We need c > b and c is connected to a.
                # Since neighbors_b is sorted, we can skip elements <= b using binary search.
                
                # Optimization: cache adj[a]
                row_a = adj[a]
                neighbors_b = adj_list[b]
                
                # Find the starting index of elements > b in neighbors_b
                start_idx = bisect.bisect_right(neighbors_b, b)
                
                # Iterate c in neighbors_b starting from start_idx
                for k in range(start_idx, len_nb):
                    c = neighbors_b[k]
                    if row_a[c]:
                        print(f"{a} {b} {c}")
                        return

if __name__ == '__main__':
    solve()