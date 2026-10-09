import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
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
    
    # Sort edges lexicographically
    edges.sort()
    
    # For each edge (u, v), find the smallest w > v such that
    # w is adjacent to both u and v
    for u, v in edges:
        # We need w > v, w in adj[u] and w in adj[v]
        # Iterate through the smaller adjacency set
        if len(adj[u]) > len(adj[v]):
            set_to_iterate = adj[v]
            other = adj[u]
        else:
            set_to_iterate = adj[u]
            other = adj[v]
        
        for w in set_to_iterate:
            if w > v and w in other:
                print(u, v, w)
                return
    
    # Should not reach here as problem guarantees a solution
    print(-1, -1, -1)

if __name__ == "__main__":
    solve()