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
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # Sort edges to ensure we find lexicographically smallest triangle
    edges.sort()
    
    for u, v in edges:
        # Find common neighbors of u and v
        # Iterate through the smaller set for efficiency
        if len(adj[u]) > len(adj[v]):
            u, v = v, u
        
        for w in adj[u]:
            if w > v and w in adj[v]:
                # Found triangle (u, v, w) with u < v < w
                print(u, v, w)
                return
    
    # Should not reach here as problem guarantees a solution exists
    print(-1)

if __name__ == "__main__":
    solve()