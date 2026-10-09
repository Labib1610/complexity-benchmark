import sys

def solve() -> None:
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
    
    # Sort adjacency lists for lexicographical iteration
    sorted_adj = [sorted(s) for s in adj]
    
    # Iterate a from 1 to n
    for a in range(1, n + 1):
        neighbors_a = sorted_adj[a]
        # Iterate b in neighbors of a where b > a
        for b in neighbors_a:
            if b <= a:
                continue
            # Iterate c in neighbors of a where c > b
            for c in neighbors_a:
                if c <= b:
                    continue
                # Check if b and c are connected
                if c in adj[b]:
                    print(a, b, c)
                    return

if __name__ == "__main__":
    solve()