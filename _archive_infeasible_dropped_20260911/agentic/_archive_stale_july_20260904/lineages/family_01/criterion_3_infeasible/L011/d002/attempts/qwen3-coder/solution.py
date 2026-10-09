import sys
from itertools import combinations

def find_triangle():
    n, m = map(int, sys.stdin.readline().split())
    
    # Create adjacency list representation
    adj = [set() for _ in range(n + 1)]
    edges = set()
    
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].add(v)
        adj[v].add(u)
        edges.add((min(u, v), max(u, v)))
    
    # Find all triangles by checking each combination of 3 nodes
    for a in range(1, n - 1):
        for b in range(a + 1, n):
            if b not in adj[a]:
                continue
            for c in range(b + 1, n + 1):
                if c not in adj[a] or c not in adj[b]:
                    continue
                # Found a triangle: a-b, a-c, b-c all exist
                return [a, b, c]
    
    return None

result = find_triangle()
print(' '.join(map(str, result)))