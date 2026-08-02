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
        
    # To find the lexicographically smallest (a, b, c) with a < b < c:
    # Iterate a from 1 to n-2
    # Iterate b from a+1 to n-1
    # Check if b is in adj[a]
    # If so, check if any c > b exists such that c in adj[a] and c in adj[b]
    
    for a in range(1, n + 1):
        # Candidates for b are neighbors of a
        neighbors_a = sorted([x for x in adj[a] if x > a])
        for b in neighbors_a:
            # Candidates for c must be in both adj[a] and adj[b]
            # And c > b
            # Intersection of adj[a] and adj[b]
            # Since n <= 2000, we can intersect efficiently
            
            # To optimize: only check c > b
            # Using set intersection
            common = adj[a].intersection(adj[b])
            for c in sorted(common):
                if c > b:
                    print(f"{a} {b} {c}")
                    return

solve()