import sys

def solve() -> None:
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [set() for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].add(v)
        adj[v].add(u)
    
    # Iterate a from 1 to n
    for a in range(1, n + 1):
        neighbors_a = adj[a]
        # We need to find b, c in neighbors_a such that c is in adj[b]
        # To satisfy the tie-breaking (minimize b, then c), we iterate b and c in increasing order.
        # Since neighbors_a is a set, we sort it.
        sorted_neighbors = sorted(neighbors_a)
        for b in sorted_neighbors:
            if b < a: 
                continue
            # Check potential c values. 
            # c must be > b to satisfy a < b < c.
            # We iterate through neighbors of b that are also neighbors of a.
            neighbors_b = adj[b]
            common = neighbors_b.intersection(neighbors_a)
            for c in sorted(common):
                if c > b:
                    # Found the deadlock (a, b, c)
                    print(a, b, c)
                    return

if __name__ == '__main__':
    solve()