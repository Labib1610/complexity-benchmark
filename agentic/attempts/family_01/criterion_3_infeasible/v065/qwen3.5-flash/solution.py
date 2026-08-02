import sys
from bisect import bisect_right

# Increase recursion depth just in case, though not strictly needed here
sys.setrecursionlimit(2000)

def solve():
    # Fast I/O
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # Adjacency matrix for O(1) lookups
    # n <= 2000, so a 2D array is manageable (approx 4MB for booleans)
    adj_matrix = [[False] * (n + 1) for _ in range(n + 1)]
    
    # Adjacency lists to iterate over neighbors
    adj_list = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj_matrix[u][v] = True
        adj_matrix[v][u] = True
        adj_list[u].append(v)
        adj_list[v].append(u)
        
    # Sort adjacency lists to facilitate finding the smallest c
    # This allows us to use binary search and iterate in increasing order
    for i in range(1, n + 1):
        adj_list[i].sort()
        
    # Iterate to find the lexicographically smallest triad (a, b, c) with a < b < c
    # We iterate a from 1 to n.
    # Since we want the lexicographically smallest (a, b, c), the first valid triad we find
    # by iterating a, then b, then c will be the answer.
    for a in range(1, n + 1):
        neighbors_a = adj_list[a]
        len_a = len(neighbors_a)
        
        # Enumerate to get index i for optimization
        for i, b in enumerate(neighbors_a):
            if b <= a:
                continue
            
            # We have a < b. Now we need to find smallest c > b such that c is neighbor of a and b.
            # Candidates for c must be in adj_list[a] (since c > b > a) AND in adj_list[b].
            # We iterate over the smaller neighbor set to minimize checks (O(m * sqrt(m)) optimization).
            
            if len_a < len(adj_list[b]):
                # Iterate neighbors of a.
                # Since neighbors_a is sorted and b is neighbors_a[i],
                # all neighbors after index i are > b.
                # We check if such a neighbor is connected to b.
                for idx_c in range(i + 1, len_a):
                    c = neighbors_a[idx_c]
                    if adj_matrix[b][c]:
                        print(f"{a} {b} {c}")
                        return
            else:
                # Iterate neighbors of b.
                # We need c > b. adj_list[b] is sorted.
                # Use binary search to find the first element > b.
                neighbors_b = adj_list[b]
                start_idx = bisect_right(neighbors_b, b)
                for idx_c in range(start_idx, len(neighbors_b)):
                    c = neighbors_b[idx_c]
                    if adj_matrix[a][c]:
                        print(f"{a} {b} {c}")
                        return

if __name__ == '__main__':
    solve()