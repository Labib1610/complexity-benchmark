import sys

def solve():
    data = sys.stdin.buffer.read().split()
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
    
    # Sort edges lexicographically to find the smallest triangle
    edges.sort()
    
    for u, v in edges:
        # Find common neighbors w > v to ensure u < v < w
        # Iterate over the smaller adjacency set for efficiency
        if len(adj[u]) <= len(adj[v]):
            small = adj[u]
            big = adj[v]
        else:
            small = adj[v]
            big = adj[u]
        
        for w in small:
            if w > v and w in big:
                print(u, v, w)
                return

if __name__ == "__main__":
    solve()