import sys

def solve():
    # Read n and m
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Use adjacency sets for fast lookup
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
        edges.append((u, v))
    
    # To find lexicographically smallest (a, b, c),
    # we iterate through possible a, b, c in order.
    # A triple (a, b, c) with a < b < c exists if:
    # (a, b) is edge, (a, c) is edge, (b, c) is edge.
    
    # Sort edges to help iterate effectively
    edges.sort()
    
    # To optimize: iterate through a, then through neighbors b of a, then check intersection
    # Only iterate through a from 1 to n
    for a in range(1, n + 1):
        neighbors_a = sorted(list(adj[a]))
        # Need to find b, c in neighbors_a such that (b, c) is an edge
        # b must be < c. Also need to ensure a < b < c.
        for i in range(len(neighbors_a)):
            b = neighbors_a[i]
            # We need a < b. Since a < b is always true if b is in neighbors_a (as b > a)
            # wait, neighbors_a contains nodes > a and nodes < a.
            # Let's ensure b > a.
            if b < a:
                continue
            
            # Now we need c such that c > b and c is in neighbors_a and c is in adj[b]
            # Intersect neighbors of a and neighbors of b
            # To be efficient, only look at neighbors of b that are > b
            neighbors_b = adj[b]
            
            # We want the smallest c > b that is in both sets
            # The intersection of neighbors_a and neighbors_b
            # Since we want lexicographical smallest, iterate c in sorted order
            for c in sorted(list(neighbors_a)):
                if c > b and c in neighbors_b:
                    print(f"{a} {b} {c}")
                    return

if __name__ == '__main__':
    solve()