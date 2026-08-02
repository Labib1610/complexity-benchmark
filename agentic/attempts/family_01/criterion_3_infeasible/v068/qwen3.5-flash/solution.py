import sys
import bisect

# Increase recursion depth just in case, though not needed here
sys.setrecursionlimit(2000)

def solve():
    # Read all input at once for speed
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return
    
    adj = [[] for _ in range(n + 1)]
    # Using bytearray for adjacency matrix for O(1) access and low memory usage
    # n <= 2000, so 2000*2000 bytes = 4MB, well within 256MB limit
    adj_mat = [bytearray(n + 1) for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
        adj_mat[u][v] = 1
        adj_mat[v][u] = 1
        
    # Sort adjacency lists to facilitate iteration in increasing order
    for i in range(1, n + 1):
        adj[i].sort()
        
    # Iterate a from 1 to n to find the lexicographically smallest triple (a, b, c)
    for a in range(1, n + 1):
        # Iterate b in adj[a]. Since adj[a] is sorted, b will be increasing.
        # This ensures we find the smallest b for the current a.
        for idx_b, b in enumerate(adj[a]):
            if b <= a:
                continue
            
            # We have a pair (a, b) with a < b.
            # We want to find the smallest c > b such that (a, c) and (b, c) are edges.
            # This means c must be in adj[a] and adj[b].
            # To optimize, we iterate through the adjacency list with fewer neighbors.
            # This ensures the complexity is bounded by O(m * sqrt(m)).
            
            deg_a = len(adj[a])
            deg_b = len(adj[b])
            
            if deg_a < deg_b:
                # Iterate c in adj[a]
                # We need c > b. Since b is in adj[a] at index idx_b,
                # any c > b must be at an index > idx_b in the sorted list adj[a].
                # We iterate from idx_b + 1 to the end.
                for idx_c in range(idx_b + 1, deg_a):
                    c = adj[a][idx_c]
                    # Check if edge (b, c) exists using the adjacency matrix
                    if adj_mat[b][c]:
                        print(f"{a} {b} {c}")
                        return
            else:
                # Iterate c in adj[b]
                # We need c > b.
                # Since b is not in adj[b] (no self-loops), we can use bisect_right
                # to find the index of the first element > b.
                start_idx = bisect.bisect_right(adj[b], b)
                for idx_c in range(start_idx, deg_b):
                    c = adj[b][idx_c]
                    # Check if edge (a, c) exists using the adjacency matrix
                    if adj_mat[a][c]:
                        print(f"{a} {b} {c}")
                        return

if __name__ == '__main__':
    solve()