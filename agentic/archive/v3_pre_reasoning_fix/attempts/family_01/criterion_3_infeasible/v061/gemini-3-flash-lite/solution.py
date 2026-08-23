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
        
    # To find the lexicographically smallest (a, b, c),
    # we iterate a from 1 to n, b from a+1 to n, and c from b+1 to n.
    # To optimize, we only consider b such that b is connected to a,
    # and c such that c is connected to both a and b.
    
    # Pre-sort adjacency lists to help iteration
    adj_list = [sorted(list(s)) for s in adj]
    
    for a in range(1, n + 1):
        neighbors_a = adj_list[a]
        # Only consider b > a that are neighbors of a
        for b in neighbors_a:
            if b <= a:
                continue
            
            # Now we need c > b such that c is in adj[a] and adj[b]
            # Since both adj_list[a] and adj_list[b] are sorted,
            # we can find the intersection efficiently.
            
            # Find intersection of neighbors_a and neighbors_b
            # Optimization: only check c > b
            
            # Convert to set for O(1) lookup if needed, 
            # but given constraints and structure, simple intersection is fine
            set_b = adj[b]
            for c in neighbors_a:
                if c > b and c in set_b:
                    print(f"{a} {b} {c}")
                    return

if __name__ == '__main__':
    solve()