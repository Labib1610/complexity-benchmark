import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [set() for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u > v:
            u, v = v, u
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))
    
    # Sort edges to process in order (u, v) increasing
    edges.sort()
    
    best_a, best_b, best_c = n + 1, n + 1, n + 1
    
    for u, v in edges:
        # Find common neighbors w where w > v to ensure u < v < w
        # This guarantees we find the lexicographically smallest triangle
        common = adj[u] & adj[v]
        for w in common:
            if w > v:
                if u < best_a or (u == best_a and v < best_b) or (u == best_a and v == best_b and w < best_c):
                    best_a, best_b, best_c = u, v, w
    
    print(best_a, best_b, best_c)

if __name__ == "__main__":
    solve()