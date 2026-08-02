import sys

def solve():
    # Use fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Adjacency set for O(1) lookup
    adj = [set() for _ in range(n + 1)]
    edges = []
    
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj[u].add(v)
        adj[v].add(u)
        edges.append((min(u, v), max(u, v)))
        idx += 2
    
    # To find the lexicographically smallest triplet (a, b, c) with a < b < c:
    # Iterate through all edges (u, v) with u < v. 
    # For each edge, look for a common neighbor w.
    # The triplet is sorted as (min(u,v,w), mid(u,v,w), max(u,v,w)).
    
    best_triplet = None
    
    # Sort edges to help find smallest lexicographical triplet earlier
    edges.sort()
    
    for u, v in edges:
        # We need a third node w such that w is connected to both u and v.
        # To minimize the triplet (a, b, c), we iterate through possible w.
        # u < v.
        
        # We want to check common neighbors of u and v.
        # For efficiency, iterate over the smaller adjacency list.
        if len(adj[u]) < len(adj[v]):
            common = adj[u].intersection(adj[v])
        else:
            common = adj[v].intersection(adj[u])
            
        for w in common:
            # Form triplet and sort
            nodes = [u, v, w]
            nodes.sort()
            a, b, c = nodes
            
            if best_triplet is None or (a, b, c) < best_triplet:
                best_triplet = (a, b, c)
                
    print(f"{best_triplet[0]} {best_triplet[1]} {best_triplet[2]}")

if __name__ == '__main__':
    solve()