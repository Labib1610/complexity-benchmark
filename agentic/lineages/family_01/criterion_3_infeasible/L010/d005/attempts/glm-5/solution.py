import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [set() for _ in range(n + 1)]
    edges = set()
    
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].add(v)
        adj[v].add(u)
        if u > v:
            u, v = v, u
        edges.add((u, v))
    
    # Sort adjacency lists for lexicographic order
    adj_list = [sorted(s) for s in adj]
    
    for a in range(1, n + 1):
        for b in adj_list[a]:
            if b <= a:
                continue
            # Check if there exists c > b such that (a,c) and (b,c) are edges
            # Using set intersection
            common = adj[a] & adj[b]
            for c in common:
                if c > b:
                    print(a, b, c)
                    return

if __name__ == "__main__":
    solve()