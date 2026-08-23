import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [set() for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].add(v)
        adj[v].add(u)
    
    # Iterate to find lexicographically smallest triangle
    for a in range(1, n - 1):
        neighbors_a = adj[a]
        # We need b > a and c > b.
        # Iterate through neighbors of a that are > a.
        # Sort them to ensure we check smaller b first.
        potential_b = sorted([x for x in neighbors_a if x > a])
        
        for b in potential_b:
            # We need c > b such that c is in neighbors_a AND c is in adj[b].
            # So c must be in the intersection of neighbors_a and adj[b].
            # Also c > b.
            neighbors_b = adj[b]
            
            # Iterate through potential c from neighbors_a (which is sorted)
            # Since potential_b is sorted, and we iterate it in order,
            # and we pick c > b from neighbors_a, the first valid c found
            # will be the smallest possible for this (a, b) pair.
            for c in potential_b: # potential_b contains elements > a
                if c > b and c in neighbors_b:
                    print(a, b, c)
                    return

if __name__ == '__main__':
    solve()