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
        if u > v:
            u, v = v, u
        adj[u].add(v)
    
    # We want to find a < b < c such that (a,b), (a,c), (b,c) are all edges.
    # Iterate a from 1 to n-2.
    # For each a, iterate b in adj[a] where b > a.
    # For each such b, iterate c in adj[b] where c > b.
    # Check if c is in adj[a].
    
    for a in range(1, n - 1):
        # adj[a] contains neighbors v where v > a
        for b in adj[a]:
            # b > a is guaranteed by construction
            for c in adj[b]:
                # c > b is guaranteed
                if c in adj[a]:
                    print(a, b, c)
                    return

if __name__ == '__main__':
    solve()