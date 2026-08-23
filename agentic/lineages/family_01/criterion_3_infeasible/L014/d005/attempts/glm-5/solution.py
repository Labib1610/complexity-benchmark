import sys

def solve():
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
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))
    
    # Sort edges to process in order (u, v) with u < v
    edges.sort()
    
    for u, v in edges:
        # Find common neighbors between u and v
        # Iterate through the smaller adjacency set for efficiency
        if len(adj[u]) > len(adj[v]):
            u, v = v, u
        
        for w in adj[u]:
            if w != v and w in adj[v]:
                # Found triangle (u, v, w)
                # Note: u < v due to sorted edges, but w can be anywhere
                # We need to output a < b < c
                a, b, c = sorted([u, v, w])
                print(a, b, c)
                return

if __name__ == "__main__":
    solve()