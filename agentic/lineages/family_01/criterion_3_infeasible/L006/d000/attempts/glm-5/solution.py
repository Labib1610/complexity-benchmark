import sys

def solve():
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
    
    # We need to find the lexicographically smallest triangle.
    # Iterate a from 1 to n, b from a+1 to n, c from b+1 to n.
    # Check if (a,b), (a,c), (b,c) are all edges.
    # To speed up, we iterate a, then b > a such that (a,b) is an edge.
    # Then for c > b, check if (a,c) and (b,c) are edges.
    
    for a in range(1, n + 1):
        # We need b > a. 
        # Since we want lexicographically smallest, we check b in increasing order.
        # We only care about b that are neighbors of a.
        neighbors_a = adj[a]
        # We iterate b from a+1 to n.
        for b in range(a + 1, n + 1):
            if b in neighbors_a:
                # (a, b) is an edge.
                # Now we need c > b such that (a, c) and (b, c) are edges.
                neighbors_b = adj[b]
                # Iterate c from b+1 to n.
                for c in range(b + 1, n + 1):
                    if c in neighbors_a and c in neighbors_b:
                        print(a, b, c)
                        return

if __name__ == '__main__':
    solve()