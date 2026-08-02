import sys

def solve():
    # Use fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Adjacency list using sets for O(1) lookup
    adj = [set() for _ in range(n + 1)]
    # Store edges as sorted pairs to iterate efficiently
    edges = []
    
    ptr = 2
    for _ in range(m):
        u = int(input_data[ptr])
        v = int(input_data[ptr+1])
        ptr += 2
        if u > v:
            u, v = v, u
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))

    # To find the lexicographically smallest triple (a, b, c) where a < b < c:
    # We want the smallest a, then smallest b, then smallest c.
    # We can iterate through all pairs (a, b) where a < b and they are connected.
    # Then we look for a common neighbor c such that b < c.
    
    # To optimize, we only check pairs (a, b) that are actually edges.
    # Since we need the lexicographically smallest, we should iterate a from 1 to n.
    # For a fixed a, we iterate b from a+1 to n.
    
    # Pre-calculating adjacency lists as sorted lists for faster iteration
    sorted_adj = [sorted(list(adj[i])) for i in range(n + 1)]
    
    for a in range(1, n + 1):
        # For a fixed a, we check its neighbors b > a
        # To ensure lexicographical order, we check b in increasing order
        neighbors_a = sorted_adj[a]
        for b in neighbors_a:
            if b <= a:
                continue
            
            # Now we need a c such that c > b and c is connected to both a and b.
            # We can iterate through the smaller of the two adjacency lists.
            # Since we want the smallest c, we can intersect the sets.
            
            # To find the smallest c > b:
            # We look at neighbors of b that are also neighbors of a.
            # Since we need c > b, we only check neighbors of b that are > b.
            
            # Optimization: Only iterate through neighbors of b that are > b
            # and check if they are in adj[a].
            for c in sorted_adj[b]:
                if c <= b:
                    continue
                if c in adj[a]:
                    print(f"{a} {b} {c}")
                    return

if __name__ == "__main__":
    solve()