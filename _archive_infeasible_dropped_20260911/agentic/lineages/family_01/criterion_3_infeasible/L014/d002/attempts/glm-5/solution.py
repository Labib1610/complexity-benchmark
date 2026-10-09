import sys

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    
    adj = [set() for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        if u > v:
            u, v = v, u
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))
    
    # Sort edges by (u, v) so we process in lexicographic order
    edges.sort()
    
    # For each edge (a, b), find smallest c > b such that both (a,c) and (b,c) are edges.
    # Since we process edges in sorted order, the first triangle found is the answer.
    for a, b in edges:
        # Iterate over common neighbors c > b
        # Choose smaller adjacency set to iterate
        if len(adj[a]) <= len(adj[b]):
            smaller = adj[a]
            larger = adj[b]
        else:
            smaller = adj[b]
            larger = adj[a]
        
        for c in smaller:
            if c > b and c in larger:
                print(f"{a} {b} {c}")
                return

solve()