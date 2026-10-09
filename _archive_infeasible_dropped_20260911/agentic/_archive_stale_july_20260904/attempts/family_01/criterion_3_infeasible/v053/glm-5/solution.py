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
    
    # Iterate to find lexicographically smallest triangle
    for a in range(1, n + 1):
        neighbors_a = adj[a]
        # We need b > a and c > b
        # Iterate through neighbors b of a where b > a
        for b in neighbors_a:
            if b <= a:
                continue
            # Check if b has neighbor c > b that is also neighbor of a
            neighbors_b = adj[b]
            for c in neighbors_b:
                if c > b and c in neighbors_a:
                    print(a, b, c)
                    return

if __name__ == "__main__":
    solve()