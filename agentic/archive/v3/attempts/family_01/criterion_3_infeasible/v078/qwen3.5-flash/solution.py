import sys

# Increase recursion depth just in case, though not strictly needed for this iterative solution
sys.setrecursionlimit(2000)

def solve():
    # Read all input from standard input at once for efficiency
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # Adjacency matrix for O(1) edge checking
    # Using 1-based indexing to match problem statement
    adj = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Adjacency lists for efficient iteration over neighbors
    adj_list = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u][v] = 1
        adj[v][u] = 1
        adj_list[u].append(v)
        adj_list[v].append(u)
        
    # Sort adjacency lists to facilitate ordered iteration
    # This ensures we process neighbors in increasing order
    for i in range(1, n + 1):
        adj_list[i].sort()
        
    # We need to find the lexicographically smallest triple (a, b, c) with a < b < c
    # such that (a, b), (a, c), and (b, c) are all edges.
    # To achieve lexicographical minimality (minimize a, then b, then c),
    # we iterate a from 1 to n. For each a, we look for valid b and c.
    
    for a in range(1, n - 1):
        # We only care about neighbors of a that are greater than a
        # Since adj_list[a] is sorted, we can filter efficiently.
        # Using a list comprehension creates a new list of relevant neighbors.
        neighbors_a = [x for x in adj_list[a] if x > a]
        
        # If a has no neighbors > a, it cannot be the smallest element of a triangle
        if not neighbors_a:
            continue
            
        len_na = len(neighbors_a)
        
        # We iterate over pairs (b, c) from neighbors_a.
        # Since neighbors_a is sorted, picking indices i < j ensures b < c.
        # Iterating i from 0 to end and j from i+1 to end ensures we find
        # the smallest b first, and for that b, the smallest c.
        for i in range(len_na):
            b = neighbors_a[i]
            for j in range(i + 1, len_na):
                c = neighbors_a[j]
                # Check if b and c are connected
                # Accessing adj[b][c] is O(1)
                if adj[b][c]:
                    print(f"{a} {b} {c}")
                    return

if __name__ == '__main__':
    solve()