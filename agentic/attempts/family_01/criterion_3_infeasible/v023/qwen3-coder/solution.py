import sys
from collections import defaultdict

def find_feedback_cascade():
    n, m = map(int, sys.stdin.readline().split())
    
    # Build adjacency list and edge set for O(1) lookup
    adj = defaultdict(set)
    edges = set()
    
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].add(v)
        adj[v].add(u)
        edges.add((min(u, v), max(u, v)))
    
    # Convert to sorted lists for deterministic iteration
    nodes = sorted(adj.keys())
    
    # Look for triangles (feedback cascades)
    best = None
    
    # For each potential triangle a-b-c where a < b < c
    for i, a in enumerate(nodes):
        for j in range(i + 1, len(nodes)):
            b = nodes[j]
            if b <= a:
                continue
            if (a, b) not in edges:
                continue
                
            # Check common neighbors of a and b
            common_neighbors = adj[a] & adj[b]
            
            for c in sorted(common_neighbors):
                if c <= b:
                    continue
                    
                # Verify triangle: a-b, a-c, b-c all exist
                if (a, c) in edges and (b, c) in edges:
                    candidate = (a, b, c)
                    if best is None or candidate < best:
                        best = candidate
                        break  # Since we want lexicographically smallest
            
            if best is not None:
                break
                
        if best is not None:
            break
    
    print(*best)

find_feedback_cascade()