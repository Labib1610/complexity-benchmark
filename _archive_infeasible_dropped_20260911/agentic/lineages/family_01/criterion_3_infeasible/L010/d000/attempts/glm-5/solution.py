import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [set() for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u > v:
            u, v = v, u
        adj[u].add(v)
        adj[v].add(u)
    
    # Iterate in lexicographic order: a < b < c
    for a in range(1, n - 1):
        adj_a = adj[a]
        # b must be > a and adjacent to a
        for b in adj_a:
            if b <= a:
                continue
            adj_b = adj[b]
            # c must be > b, adjacent to a and adjacent to b
            # Iterate over the smaller of the two adjacency sets for efficiency
            if len(adj_a) <= len(adj_b):
                for c in adj_a:
                    if c > b and c in adj_b:
                        print(a, b, c)
                        return
            else:
                for c in adj_b:
                    if c > b and c in adj_a:
                        print(a, b, c)
                        return

if __name__ == "__main__":
    solve()