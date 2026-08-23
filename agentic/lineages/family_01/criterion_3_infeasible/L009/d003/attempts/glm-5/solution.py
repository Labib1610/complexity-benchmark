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
    
    # Sort adjacency lists for lexicographic iteration
    sorted_adj = [sorted(s) for s in adj]
    
    # Iterate over all pairs (u, v) with u < v
    for u in range(1, n + 1):
        neighbors_u = sorted_adj[u]
        # We need v > u, so we iterate through neighbors and filter
        for v in neighbors_u:
            if v <= u:
                continue
            
            # Check for common neighbor w such that w > v
            # Iterate through neighbors of u that are > v
            for w in neighbors_u:
                if w > v:
                    if w in adj[v]:
                        print(u, v, w)
                        return
    
    # Should not reach here as per problem statement
    print(-1)

if __name__ == '__main__':
    solve()