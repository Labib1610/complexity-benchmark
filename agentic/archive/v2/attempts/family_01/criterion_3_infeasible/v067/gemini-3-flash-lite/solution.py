import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [set() for _ in range(n + 1)]
    edges = []
    
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj[u].add(v)
        adj[v].add(u)
        edges.append((min(u, v), max(u, v)))
        idx += 2
        
    # Sort edges to help find the lexicographical smallest triad
    # We want smallest a, then smallest b, then smallest c.
    # Triad is (a, b, c) with a < b < c.
    # Iterate through all possible 'a' from 1 to n-2
    for a in range(1, n + 1):
        # Get neighbors of 'a' that are greater than 'a'
        neighbors_a = sorted([v for v in adj[a] if v > a])
        
        # We need to find b, c in neighbors_a such that b < c and b is connected to c
        # To ensure lexicographical order, we iterate b then c
        for i in range(len(neighbors_a)):
            b = neighbors_a[i]
            # Optimization: if we already found a triad, we don't need to look further
            # But the loop structure handles the lexicographical order naturally.
            # Check intersection of neighbors of a and neighbors of b
            for j in range(i + 1, len(neighbors_a)):
                c = neighbors_a[j]
                if c in adj[b]:
                    print(f"{a} {b} {c}")
                    return

solve()