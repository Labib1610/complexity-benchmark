import sys
from bisect import bisect_right

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

    # Adjacency list and adjacency matrix
    # 1-based indexing for convenience
    adj = [[] for _ in range(n + 1)]
    # Using bytearray for memory efficiency and speed
    # mat[u][v] == 1 means edge exists between u and v
    mat = [bytearray(n + 1) for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
        mat[u][v] = 1
        mat[v][u] = 1
        
    # Sort adjacency lists to ensure we process neighbors in increasing order
    # This is crucial for finding the lexicographically smallest triple
    for i in range(1, n + 1):
        adj[i].sort()
        
    # Iterate to find the lexicographically smallest triangle (a, b, c)
    # Order: a < b < c
    # We iterate a from 1 to n
    for a in range(1, n + 1):
        if not adj[a]:
            continue
            
        # Iterate neighbors b of a such that b > a
        # Since adj[a] is sorted, we just iterate and skip b <= a
        for b in adj[a]:
            if b <= a:
                continue
            
            # We need to find a common neighbor c such that c > b
            # We want the smallest such c to satisfy lexicographical order
            # To optimize, we iterate over the neighbor list with fewer candidates > b
            
            # Candidates for c are in adj[a] and adj[b]
            # We check existence using mat
            
            # Calculate number of candidates > b in adj[a]
            # b is guaranteed to be in adj[a]
            idx_a = bisect_right(adj[a], b)
            count_a = len(adj[a]) - idx_a
            
            # Calculate number of candidates > b in adj[b]
            # b is not in adj[b] (no self loops), but bisect_right handles it correctly
            idx_b = bisect_right(adj[b], b)
            count_b = len(adj[b]) - idx_b
            
            if count_a <= count_b:
                # Iterate through adj[a] starting from idx_a
                for i in range(idx_a, len(adj[a])):
                    c = adj[a][i]
                    # Check if c is connected to b
                    if mat[b][c]:
                        print(f"{a} {b} {c}")
                        return
            else:
                # Iterate through adj[b] starting from idx_b
                for i in range(idx_b, len(adj[b])):
                    c = adj[b][i]
                    # Check if c is connected to a
                    if mat[a][c]:
                        print(f"{a} {b} {c}")
                        return

if __name__ == '__main__':
    solve()