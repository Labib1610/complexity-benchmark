import sys

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    
    adj = [set() for _ in range(n + 1)]
    edges = []
    
    for _ in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        if u > v:
            u, v = v, u
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))
    
    # Sort edges lexicographically so we find the lexicographically smallest triangle first
    edges.sort()
    
    for u, v in edges:
        # Find common neighbors w where u < v < w (to ensure a < b < c)
        # Iterate over the smaller adjacency set
        if len(adj[u]) <= len(adj[v]):
            small = adj[u]
            large = adj[v]
        else:
            small = adj[v]
            large = adj[u]
        
        for w in small:
            if w > v and w in large:
                print(f"{u} {v} {w}")
                return

solve()