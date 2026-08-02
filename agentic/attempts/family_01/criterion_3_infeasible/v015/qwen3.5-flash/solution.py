import sys

# Increase recursion depth just in case, though not used here.
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

    # Adjacency list to store neighbors
    adj = [[] for _ in range(n + 1)]
    
    # Adjacency matrix using bytearray for O(1) edge check.
    # is_edge[u][v] will store 1 if edge exists, 0 otherwise.
    # Using bytearray is memory efficient (1 byte per entry) and fast.
    is_edge = [bytearray(n + 1) for _ in range(n + 1)]
    
    # Read edges
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
        is_edge[u][v] = 1
        is_edge[v][u] = 1
        
    # Process adjacency lists
    # We filter to keep only neighbors with index > u.
    # This helps in ensuring a < b < c logic (since we iterate a, then b > a, then c > b)
    # and reduces list sizes, improving performance.
    for u in range(1, n + 1):
        # Filter neighbors > u using list comprehension
        adj[u] = [v for v in adj[u] if v > u]
        # Sort to ensure lexicographical order of iteration for b and c
        adj[u].sort()
        
    # Iterate to find the lexicographically smallest triangle
    # We want to find a < b < c such that (a,b), (b,c), (a,c) are edges.
    # We iterate a from 1 to n.
    # For each a, we iterate b in adj[a] (so b > a).
    # For each b, we iterate c in adj[b] (so c > b).
    # We check if (a, c) is an edge.
    # The first valid triplet found will be lexicographically smallest because:
    # 1. a is increasing.
    # 2. b is increasing for fixed a (since adj[a] is sorted).
    # 3. c is increasing for fixed a, b (since adj[b] is sorted).
    
    for a in range(1, n + 1):
        if not adj[a]:
            continue
            
        # Cache the row for 'a' to avoid repeated lookups in the matrix
        row_a = is_edge[a]
        
        for b in adj[a]:
            # b > a is guaranteed by filtering
            if not adj[b]:
                continue
                
            # Iterate c in adj[b] (so c > b)
            # Check if a is connected to c
            for c in adj[b]:
                if row_a[c]:
                    print(f"{a} {b} {c}")
                    return

if __name__ == '__main__':
    solve()