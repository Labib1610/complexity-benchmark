```python
import sys
from collections import defaultdict

def find_triangle():
    n, m = map(int, sys.stdin.readline().split())
    
    # Build adjacency list and set for O(1) lookup
    adj = defaultdict(set)
    edges = []
    
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        if u > v:
            u, v = v, u
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))
    
    # Sort