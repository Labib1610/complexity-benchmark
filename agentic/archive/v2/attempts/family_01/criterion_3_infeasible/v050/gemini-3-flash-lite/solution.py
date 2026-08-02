import sys

def solve():
    # Read n and m
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [set() for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        adj[u].add(v)
        adj[v].add(u)
        idx += 2
        
    # We want the lexicographically smallest (a, b, c) with a < b < c.
    # Iterate a from 1 to n-2, b from a+1 to n-1, c from b+1 to n.
    # To optimize, sort adjacency lists.
    sorted_adj = [sorted(list(adj[i])) for i in range(n + 1)]
    
    # Pre-convert sets for O(1) lookup
    adj_sets = [set(adj[i]) for i in range(n + 1)]
    
    for a in range(1, n + 1):
        neighbors_a = sorted_adj[a]
        # Optimization: only consider neighbors b > a
        neighbors_a = [b for b in neighbors_a if b > a]
        for i in range(len(neighbors_a)):
            b = neighbors_a[i]
            # Now we need c > b such that c is in both adj[a] and adj[b]
            # Intersection of sorted lists neighbors_a and neighbors_b
            # Since we need the smallest c, iterate through neighbors_b
            neighbors_b = sorted_adj[b]
            for c in neighbors_b:
                if c > b:
                    if c in adj_sets[a]:
                        print(f"{a} {b} {c}")
                        return

solve()