import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    n = int(next(iterator))
    m = int(next(iterator))
    
    adj = [set() for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].add(v)
        adj[v].add(u)
    
    # Iterate through all pairs to find the lexicographically smallest triangle
    # We iterate u from 1 to n, v from u+1 to n, w from v+1 to n.
    # The first triangle found in this order is the answer.
    for u in range(1, n + 1):
        # Optimization: if degree of u is less than 2, it cannot be part of a triangle
        if len(adj[u]) < 2:
            continue
        
        # We need to check pairs (v, w) in adj[u] such that v < w and v, w are connected.
        # To ensure lexicographical order, we iterate v from u+1 to n.
        for v in range(u + 1, n + 1):
            if v not in adj[u]:
                continue
            
            # Now we need to find w such that w > v, w in adj[u], and w in adj[v]
            # We iterate w from v+1 to n.
            for w in range(v + 1, n + 1):
                if w in adj[u] and w in adj[v]:
                    print(u, v, w)
                    return

if __name__ == '__main__':
    solve()