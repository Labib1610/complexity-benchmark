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
        v = int(input_data[idx + 1])
        idx += 2
        if u > v:
            u, v = v, u
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))
    
    # To find the lexicographically smallest trio (a, b, c) with a < b < c:
    # We iterate a from 1 to n, b from a+1 to n, and check if c exists.
    # To optimize, sort neighbors of a and b.
    
    for a in range(1, n + 1):
        # Candidates for b must be neighbors of a
        neighbors_a = sorted([x for x in adj[a] if x > a])
        for b in neighbors_a:
            # Candidates for c must be neighbors of both a and b
            # Intersection of neighbors_a and neighbors_b
            # We want the smallest c > b
            neighbors_b = adj[b]
            
            # Optimization: check intersection
            # Only need to check if there exists c > b such that c in neighbors_a and c in neighbors_b
            # Using set intersection is efficient
            common = neighbors_a_set = None
            
            # Since we need the smallest c, we can iterate through the smaller set
            if len(neighbors_a) < len(neighbors_b):
                for c in neighbors_a:
                    if c > b and c in neighbors_b:
                        print(f"{a} {b} {c}")
                        return
            else:
                for c in neighbors_b:
                    if c > b and c in adj[a]:
                        print(f"{a} {b} {c}")
                        return

solve()