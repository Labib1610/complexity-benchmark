import sys
from collections import defaultdict
import heapq

def find_ternary_cascade():
    n, m = map(int, sys.stdin.readline().split())
    
    # Build adjacency list and set for O(1) lookup
    adj_list = defaultdict(set)
    adj_set = set()
    
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        if u > v:
            u, v = v, u
        adj_list[u].add(v)
        adj_list[v].add(u)
        adj_set.add((u, v))
        edges.append((u, v))
    
    # Sort vertices by degree (ascending)
    vertices = list(range(1, n + 1))
    vertices.sort(key=lambda x: len(adj_list[x]))
    
    best = None
    
    # For each edge, check for common neighbors
    for u, v in edges:
        if u > v:
            u, v = v, u
            
        # Get common neighbors of u and v
        common_neighbors = adj_list[u] & adj_list[v]
        
        for w in common_neighbors:
            # Ensure we have three distinct nodes
            if w == u or w == v:
                continue
                
            # Create sorted triplet
            triplet = tuple(sorted([u, v, w]))
            
            # Check if this forms a triangle (all pairs must exist)
            u_w = (min(u, w), max(u, w))
            v_w = (min(v, w), max(v, w))
            
            if u_w in adj_set and v_w in adj_set:
                if best is None or triplet < best:
                    best = triplet
    
    if best:
        print(best[0], best[1], best[2])

find_ternary_cascade()