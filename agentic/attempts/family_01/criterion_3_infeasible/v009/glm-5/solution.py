import sys

def solve() -> None:
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
    
    # Sort edges to process in lexicographical order
    edges.sort()
    
    # For each edge (u, v), check for common neighbors w > v
    # This ensures u < v < w and we find the lexicographically smallest triangle
    for u, v in edges:
        # We need w such that w > v and w is neighbor of both u and v
        # Iterate through neighbors of u that are > v
        neighbors_u = adj[u]
        neighbors_v = adj[v]
        
        # Find common neighbors > v
        # Since we process edges in sorted order, the first common neighbor > v
        # gives us the smallest valid triangle for this edge
        for w in neighbors_u:
            if w > v and w in neighbors_v:
                print(u, v, w)
                return

if __name__ == "__main__":
    solve()