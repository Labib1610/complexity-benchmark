import sys

def solve():
    # Read n and m
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Use an adjacency list of sets for O(1) lookup
    adj = [set() for _ in range(n + 1)]
    edges = []
    
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        idx += 2
        adj[u].add(v)
        adj[v].add(u)
        if u > v:
            u, v = v, u
        edges.append((u, v))
        
    # To find the lexicographically smallest (a, b, c),
    # we iterate through all edges (u, v) where u < v.
    # For each edge, we look for a node w such that 
    # w is connected to both u and v.
    # To maintain lexicographical order, we ensure the triple is (a, b, c)
    # with a < b < c.
    
    edges.sort()
    
    for a, b in edges:
        # We need a c such that c > b and c is connected to a and b.
        # Or c < a (impossible since a is smallest)
        # Or a < c < b (not possible if we iterate edges in order)
        
        # Intersection of neighbors of a and b
        # To optimize, iterate over the smaller adjacency list
        if len(adj[a]) < len(adj[b]):
            candidates = adj[a]
            target = b
        else:
            candidates = adj[b]
            target = a
            
        for c in candidates:
            if c > b and c in adj[target]:
                print(f"{a} {b} {c}")
                return

if __name__ == '__main__':
    solve()