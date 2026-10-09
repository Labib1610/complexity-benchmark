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
    
    # Sort edges to process in lexicographic order
    edges.sort()
    
    # For each edge (a, b), check if there exists c such that
    # a-c and b-c edges exist, with a < b < c
    for a, b in edges:
        # We need c > b (since a < b and we want a < b < c)
        # Check neighbors of a that are > b
        for c in adj[a]:
            if c > b and c in adj[b]:
                print(a, b, c)
                return
    
    # If not found, check for c < a (so c < a < b)
    # We need to find c < a such that a-c and b-c exist
    for a, b in edges:
        for c in adj[a]:
            if c < a and c in adj[b]:
                print(c, a, b)
                return
    
    # Should not reach here as problem guarantees a solution exists
    print(-1, -1, -1)

if __name__ == "__main__":
    solve()