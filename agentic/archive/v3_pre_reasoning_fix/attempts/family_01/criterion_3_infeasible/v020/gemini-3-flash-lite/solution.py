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
        if u > v:
            u, v = v, u
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))
        idx += 2
        
    # Sort edges primarily by u then by v
    edges.sort()
    
    # We want to find the lexicographically smallest (a, b, c) with a < b < c
    # Iterate through all possible a, then all neighbors b of a, 
    # then check if there is a c that is a neighbor of both a and b.
    # To keep it efficient, iterate through sorted vertices.
    
    # To find lexicographical minimum, iterate a from 1 to n
    for a in range(1, n + 1):
        neighbors_a = sorted([v for v in adj[a] if v > a])
        # For each b in sorted neighbors of a
        for i in range(len(neighbors_a)):
            b = neighbors_a[i]
            # We need to find c such that c > b, c is neighbor of a, c is neighbor of b
            # To be lexicographically smallest, we check neighbors of b that are also neighbors of a
            # and pick the smallest one > b
            
            # Intersection of adj[a] and adj[b]
            # Since n is up to 2000, we can use set intersection
            common = adj[a].intersection(adj[b])
            valid_c = [c for c in common if c > b]
            
            if valid_c:
                print(f"{a} {b} {min(valid_c)}")
                return

solve()