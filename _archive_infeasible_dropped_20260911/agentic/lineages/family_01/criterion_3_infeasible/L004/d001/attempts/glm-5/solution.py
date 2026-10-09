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
    sorted_adj = [sorted(adj[i]) for i in range(n + 1)]
    
    # Iterate a from 1 to n
    for a in range(1, n + 1):
        # Iterate b from a+1 to n
        for b in sorted_adj[a]:
            if b <= a:
                continue
            # Iterate c from b+1 to n
            for c in sorted_adj[a]:
                if c <= b:
                    continue
                # Check if b and c are incompatible
                if c in adj[b]:
                    print(a, b, c)
                    return

if __name__ == "__main__":
    solve()