import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
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
        # Iterate b in sorted order of a's neighbors, b > a
        for b in sorted_adj[a]:
            if b <= a:
                continue
            # Iterate c in sorted order of a's neighbors, c > b
            for c in sorted_adj[a]:
                if c <= b:
                    continue
                # Check if b and c conflict
                if c in adj[b]:
                    print(a, b, c)
                    return

if __name__ == "__main__":
    solve()