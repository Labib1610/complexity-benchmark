import sys

def solve():
    # Read n and m
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [set() for _ in range(n + 1)]
    edges = []
    
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        if u > v:
            u, v = v, u
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))
        idx += 2
        
    # Sort edges to ensure we check in lexicographical order
    edges.sort()
    
    # Iterate through each edge (u, v) and find a common neighbor w
    # We want to minimize (u, v, w) lexicographically.
    # Since we want the smallest (a, b, c) with a < b < c,
    # we iterate through all edges (u, v) where u < v.
    # For a fixed (u, v), any w such that (u, w) and (v, w) exist
    # forms a triple (u, v, w). 
    # To get the lexicographically smallest, we check all triples.
    
    # Optimization: iterate through sorted edges, and for each edge,
    # find all common neighbors w.
    
    best_triple = None
    
    for u, v in edges:
        # Common neighbors of u and v
        # We only care about w such that (u, v, w) is ordered
        # The triple is (min(u, v, w), mid(u, v, w), max(u, v, w))
        
        # Check neighbors of u that are also neighbors of v
        # To optimize, iterate over the smaller adjacency list
        if len(adj[u]) < len(adj[v]):
            common = adj[u].intersection(adj[v])
        else:
            common = adj[v].intersection(adj[u])
            
        for w in common:
            # Current triple elements
            triple = sorted([u, v, w])
            if best_triple is None or triple < best_triple:
                best_triple = triple
                
    if best_triple:
        print(f"{best_triple[0]} {best_triple[1]} {best_triple[2]}")

if __name__ == '__main__':
    solve()