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

    # Adjacency list to store neighbors
    adj = [[] for _ in range(n + 1)]
    # Adjacency matrix using bytearray for O(1) edge check and memory efficiency
    # adj_mat[u][v] == 1 if edge exists, 0 otherwise
    adj_mat = [bytearray(n + 1) for _ in range(n + 1)]

    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
        adj_mat[u][v] = 1
        adj_mat[v][u] = 1

    # Sort adjacency lists to allow for ordered iteration and efficient slicing/indexing
    for i in range(1, n + 1):
        adj[i].sort()

    # Iterate through all possible vertices for 'a'
    for a in range(1, n + 1):
        # Iterate through neighbors of 'a' for 'b'
        # We use enumerate to keep track of the index in adj[a]
        for idx_b, b in enumerate(adj[a]):
            # We require a < b < c, so b must be greater than a
            if b <= a:
                continue
            
            # We need to find a vertex c such that c > b and edges (a, c) and (b, c) exist.
            # This means c must be in the intersection of adj[a] and adj[b].
            # To minimize the number of checks, we iterate over the smaller adjacency list.
            # The condition is: find smallest c > b in intersection.
            
            # If adj[a] is smaller or equal in size to adj[b]
            if len(adj[a]) <= len(adj[b]):
                # Iterate over neighbors of a that are strictly greater than b.
                # Since adj[a] is sorted and b is at index idx_b, the elements after idx_b are > b.
                # We iterate from idx_b + 1 to the end of adj[a].
                # This avoids using bisect_right on adj[a] and slicing, saving overhead.
                for idx_c in range(idx_b + 1, len(adj[a])):
                    c = adj[a][idx_c]
                    # Check if c is connected to b
                    if adj_mat[b][c]:
                        # Found the lexicographically smallest triple (a, b, c)
                        print(f"{a} {b} {c}")
                        return
            else:
                # If adj[b] is smaller, iterate over neighbors of b.
                # We need c > b. Since adj[b] is sorted, we find the first element > b using bisect_right.
                idx_c = bisect_right(adj[b], b)
                for k in range(idx_c, len(adj[b])):
                    c = adj[b][k]
                    # Check if c is connected to a
                    if adj_mat[a][c]:
                        print(f"{a} {b} {c}")
                        return

if __name__ == '__main__':
    solve()