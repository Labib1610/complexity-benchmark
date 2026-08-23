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
    
    # Iterate to find the lexicographically smallest triangle
    for a in range(1, n - 1):
        for b in adj[a]:
            if b > a:
                # Check intersection of neighbors of a and b that are > b
                common_neighbors = adj[a] & adj[b]
                for c in common_neighbors:
                    if c > b:
                        print(a, b, c)
                        return

if __name__ == "__main__":
    solve()