import sys
from collections import defaultdict

def find_triangle(edges, adj):
    # For each edge (u,v), check if there exists a node w such that
    # (u,w) and (v,w) are also edges.
    edge_set = set(edges)
    
    for u in sorted(adj.keys()):
        for v in sorted(adj[u]):
            if u >= v:
                continue
            # Check neighbors of u and v for common neighbor
            for w in adj[u]:
                if w <= v:
                    continue
                if w in adj[v]:
                    return (u, v, w)
    return None

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    m = int(data[idx+1])
    idx += 2
    
    edges = []
    adj = defaultdict(set)
    
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        idx += 2
        if u > v:
            u, v = v, u
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # Sort adjacency lists for consistent ordering
    for key in adj:
        adj[key] = sorted(adj[key])
        
    result = find_triangle(edges, adj)
    print(result[0], result[1], result[2])

if __name__ == "__main__":
    main()