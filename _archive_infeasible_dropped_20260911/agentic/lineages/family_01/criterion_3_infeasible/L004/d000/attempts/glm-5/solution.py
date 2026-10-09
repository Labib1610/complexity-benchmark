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
    
    # Sort adjacency lists for deterministic iteration order
    adj_lists = [sorted(s) for s in adj]
    
    # We want lexicographically smallest triple (a, b, c)
    # Iterate a from 1 to n-2
    for a in range(1, n - 1):
        # b must be > a and conflict with a
        for b in adj_lists[a]:
            if b <= a:
                continue
            # c must be > b and conflict with both a and b
            # Check intersection of adj[a] and adj[b] for values > b
            # Since lists are sorted, we can iterate efficiently
            for c in adj_lists[b]:
                if c <= b:
                    continue
                if c in adj[a]:
                    print(a, b, c)
                    return

if __name__ == "__main__":
    solve()