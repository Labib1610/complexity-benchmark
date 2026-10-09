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
    
    # Sort edges lexicographically to find the lexicographically smallest triangle
    edges.sort()
    
    for u, v in edges:
        # Find common neighbors w > v to ensure u < v < w
        # Iterate over the smaller adjacency set for efficiency
        if len(adj[u]) <= len(adj[v]):
            small, large = adj[u], adj[v]
        else:
            small, large = adj[v], adj[u]
        
        for w in small:
            if w > v and w in large:
                print(f"{u} {v} {w}")
                return

solve()