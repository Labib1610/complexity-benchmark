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
    
    # Sort edges lexicographically
    edges.sort()
    
    # For each edge (a, b) with a < b, find smallest c > b such that c is adjacent to both a and b
    for a, b in edges:
        # Find common neighbors c > b
        # Iterate over the smaller adjacency set
        if len(adj[a]) > len(adj[b]):
            small, large = adj[b], adj[a]
        else:
            small, large = adj[a], adj[b]
        
        for c in small:
            if c > b and c in large:
                print(a, b, c)
                return
    
    # Should not reach here per problem guarantee
    print(-1)

solve()