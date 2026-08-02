import sys

def solve():
    # Read n and m
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Use adjacency sets for O(1) lookup
    adj = [set() for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj[u].add(v)
        adj[v].add(u)
        idx += 2
        
    # To find lexicographically smallest (a, b, c) with a < b < c:
    # Iterate a from 1 to n-2
    # Iterate b from a+1 to n-1
    # Check if there exists c > b such that c is in adj[a] and adj[b]
    
    # Sort adj sets to optimize iteration
    sorted_adj = [sorted(list(adj[i])) for i in range(n + 1)]
    
    for a in range(1, n - 1):
        # Candidates for b must be connected to a and > a
        candidates_b = [x for x in sorted_adj[a] if x > a]
        for b in candidates_b:
            # Candidates for c must be > b AND connected to both a and b
            # We look for the smallest c > b that is in both adj[a] and adj[b]
            # Since sorted_adj[a] is sorted, we can intersect efficiently
            
            # Optimization: iterate through the smaller adjacency list
            if len(sorted_adj[a]) < len(sorted_adj[b]):
                for c in sorted_adj[a]:
                    if c > b and c in adj[b]:
                        print(f"{a} {b} {c}")
                        return
            else:
                for c in sorted_adj[b]:
                    if c > b and c in adj[a]:
                        print(f"{a} {b} {c}")
                        return

solve()