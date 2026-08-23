import sys

def solve():
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
        
    # To find the lexicographically smallest triple (a, b, c) with a < b < c:
    # Iterate a from 1 to n-2
    # Iterate b from a+1 to n-1
    # Check if b is connected to a
    # Iterate c from b+1 to n
    # Check if c is connected to a and b
    
    # Pre-sorting adjacency lists to help iteration or just using set lookups
    # Given n=2000, O(n^3) might be slow, but the constraint says 2s.
    # Actually, we can optimize by intersecting adj[a] and adj[b].
    
    for a in range(1, n + 1):
        # We only care about b > a
        neighbors_a = sorted([x for x in adj[a] if x > a])
        for b in neighbors_a:
            # We need c > b such that c is in adj[a] and adj[b]
            # Intersection of neighbors_a and neighbors_b
            # Since neighbors_a is sorted, we can find common elements efficiently
            # or just iterate through smaller set.
            
            # Using set intersection is usually fast in Python
            common = adj[a].intersection(adj[b])
            c_candidates = sorted([x for x in common if x > b])
            
            if c_candidates:
                print(f"{a} {b} {c_candidates[0]}")
                return

solve()