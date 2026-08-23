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
    
    # Sort adjacency lists for consistent ordering
    adj_list = [sorted(s) for s in adj]
    
    # Iterate over all triples in lexicographical order
    for a in range(1, n - 1):
        for b in range(a + 1, n):
            if b not in adj[a]:
                continue
            for c in range(b + 1, n + 1):
                if c in adj[a] and c in adj[b]:
                    print(a, b, c)
                    return

if __name__ == "__main__":
    solve()