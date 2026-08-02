import sys

# Increase recursion depth just in case, though not used here
sys.setrecursionlimit(2000)

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

    # Adjacency matrix for O(1) edge existence check.
    # Vertices are 1-indexed, so size is n + 1.
    # Using list of lists of booleans/ints.
    adj = [[False] * (n + 1) for _ in range(n + 1)]
    
    # Adjacency lists to iterate over neighbors efficiently.
    adj_lists = [[] for _ in range(n + 1)]
    
    # Read edges
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u][v] = True
        adj[v][u] = True
        adj_lists[u].append(v)
        adj_lists[v].append(u)
    
    # Sort adjacency lists. This is crucial to ensure we process neighbors
    # in increasing order of their indices, which helps in finding the
    # lexicographically smallest trio (a, b, c) with a < b < c.
    for i in range(1, n + 1):
        adj_lists[i].sort()
        
    # Iterate through each vertex 'a' to be the smallest vertex in the trio.
    for a in range(1, n + 1):
        # We need to find a triangle involving 'a'.
        # The other two vertices 'b' and 'c' must be neighbors of 'a'
        # and satisfy a < b < c.
        # So we collect all neighbors of 'a' that are greater than 'a'.
        # Since adj_lists[a] is sorted, we can filter them.
        s_a = [v for v in adj_lists[a] if v > a]
        
        # If 'a' has fewer than 2 neighbors with index > a, it cannot be part
        # of a triangle with the smallest vertex condition.
        if len(s_a) < 2:
            continue
            
        # Now we need to find two vertices b, c in s_a such that (b, c) is an edge.
        # Since s_a is sorted, iterating i < j ensures b < c.
        # We want the lexicographically smallest (a, b, c), so we iterate b (s_a[i])
        # from smallest to largest, and c (s_a[j]) from smallest to largest.
        # The first valid triangle found will be the answer.
        for i in range(len(s_a)):
            b = s_a[i]
            for j in range(i + 1, len(s_a)):
                c = s_a[j]
                # Check if edge (b, c) exists using the adjacency matrix.
                if adj[b][c]:
                    print(f"{a} {b} {c}")
                    return

if __name__ == '__main__':
    solve()