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
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # Sort edges lexicographically by (u, v)
    edges.sort()
    
    # For each edge (u, v), find the smallest w > v such that both (u, w) and (v, w) are edges.
    # The first such triple (u, v, w) in lexicographic order is the answer.
    for u, v in edges:
        # We need w > v, and w adjacent to both u and v.
        # Iterate over the smaller adjacency list between adj[u] and adj[v].
        if len(adj[u]) <= len(adj[v]):
            smaller = adj[u]
            other = adj[v]
        else:
            smaller = adj[v]
            other = adj[u]
        
        best_w = n + 1
        for w in smaller:
            if w > v and w in other:
                if w < best_w:
                    best_w = w
        if best_w <= n:
            print(u, v, best_w)
            return

if __name__ == "__main__":
    solve()