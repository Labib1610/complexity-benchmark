import sys

def solve():
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
        idx += 2
        adj[u].add(v)
        adj[v].add(u)
        if u > v:
            u, v = v, u
        edges.append((u, v))
    
    # Sort edges to help find the lexicographically smallest triple
    edges.sort()
    
    # To find the lexicographically smallest (a, b, c) with a < b < c:
    # We iterate through all edges (u, v) as potential (a, b).
    # Then we check if there exists a node c > b such that c is in adj[a] and adj[b].
    
    best = (n + 1, n + 1, n + 1)
    
    # Optimization: iterate through sorted edges (a, b)
    for a, b in edges:
        # We need a < b. edges are stored as (u, v) with u < v.
        # So a is always < b here.
        
        # We need to find c > b such that c is in adj[a] and adj[b].
        # To ensure lexicographical smallest, we want to check possible c's.
        
        # Intersection of neighbors
        common = adj[a].intersection(adj[b])
        
        for c in common:
            if c > b:
                triple = (a, b, c)
                if triple < best:
                    best = triple
                    
    print(f"{best[0]} {best[1]} {best[2]}")

if __name__ == '__main__':
    solve()