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
        
    # We need the lexicographically smallest (a, b, c) with a < b < c.
    # Iterate a from 1 to n, b from a+1 to n, then check if there exists c > b
    # such that c is connected to both a and b.
    
    # To optimize: for a fixed a and b, check if there is any c > b in (adj[a] & adj[b])
    
    for a in range(1, n + 1):
        adj_a = adj[a]
        # Sort neighbors to potentially speed up finding b
        sorted_neighbors_a = sorted([x for x in adj_a if x > a])
        for b in sorted_neighbors_a:
            adj_b = adj[b]
            # Find common neighbors c such that c > b
            # Intersection of adj[a] and adj[b]
            # Since adj[a] and adj[b] are sets, this is O(min(deg(a), deg(b)))
            common = adj_a.intersection(adj_b)
            
            # Filter for c > b
            candidates = [c for c in common if c > b]
            if candidates:
                print(f"{a} {b} {min(candidates)}")
                return

if __name__ == '__main__':
    solve()