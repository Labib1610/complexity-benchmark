import sys
from bisect import bisect_right

def solve():
    # Read all input from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    n = int(next(iterator))
    m = int(next(iterator))
    
    # Adjacency list for the graph
    adj = [[] for _ in range(n + 1)]
    # Adjacency matrix for O(1) edge existence checks
    is_edge = [[False] * (n + 1) for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
        is_edge[u][v] = True
        is_edge[v][u] = True

    # Sort adjacency lists to facilitate lexicographical search and binary search
    for i in range(1, n + 1):
        adj[i].sort()
        
    # Iterate through all possible values for 'a' from smallest to largest
    for a in range(1, n + 1):
        # Iterate through neighbors 'b' of 'a'
        # Since adj[a] is sorted, we encounter b in increasing order
        for b in adj[a]:
            if b <= a:
                continue
            
            # We need to find a 'c' such that c > b, and edges (a, c) and (b, c) exist.
            # To optimize, we iterate over the adjacency list of the vertex with the smaller degree
            # between a and b. This ensures we check fewer candidates.
            
            # We want to find the intersection of neighbors of a and neighbors of b
            # restricted to c > b.
            
            if len(adj[a]) <= len(adj[b]):
                # Iterate over neighbors of a
                # We only care about c > b
                # Use bisect to find the index of the first element > b
                idx = bisect_right(adj[a], b)
                for i in range(idx, len(adj[a])):
                    c = adj[a][i]
                    # Check if c is a neighbor of b
                    if is_edge[b][c]:
                        print(f"{a} {b} {c}")
                        return
            else:
                # Iterate over neighbors of b
                # We only care about c > b
                idx = bisect_right(adj[b], b)
                for i in range(idx, len(adj[b])):
                    c = adj[b][i]
                    # Check if c is a neighbor of a
                    if is_edge[a][c]:
                        print(f"{a} {b} {c}")
                        return

if __name__ == '__main__':
    solve()