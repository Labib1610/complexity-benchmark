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
        idx += 2
        if u > v:
            u, v = v, u
        adj[u].add(v)
        edges.append((u, v))
    
    # Sort edges to ensure we process in lexicographical order
    edges.sort()
    
    # Iterate through each edge (a, b) and look for a common neighbor c
    # To find lexicographically smallest (a, b, c), we iterate through
    # sorted edges (a, b) and then through sorted neighbors of a.
    
    # Pre-sort adjacency lists for faster searching and lexicographical order
    sorted_adj = [sorted(list(adj[i])) for i in range(n + 1)]
    
    # To find the lexicographically smallest (a, b, c):
    # We iterate a from 1 to n-2.
    # For each a, we look at neighbors b > a.
    # Then we check if there exists c > b such that c is in adj[a] and adj[b].
    
    for a in range(1, n + 1):
        neighbors_a = sorted_adj[a]
        for i in range(len(neighbors_a)):
            b = neighbors_a[i]
            if b <= a:
                continue
            
            # We have a < b. Now look for smallest c > b such that c is in adj[a] and adj[b]
            # Since sorted_adj[a] is sorted, we can iterate through its elements
            # greater than b.
            for c in neighbors_a[i+1:]:
                if c > b:
                    if c in adj[b]:
                        print(f"{a} {b} {c}")
                        return

solve()