import sys
from collections import defaultdict

def find_volatile_triad():
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # Build adjacency list representation of the graph
    adj = defaultdict(set)
    edges = []
    
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        index += 2
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))
    
    # Sort the edges to process them in order
    edges.sort()
    
    # For each edge (u,v), check if there exists a node w such that 
    # (u,w) and (v,w) are also edges. That forms a triangle.
    for u, v in edges:
        if u >= v:
            continue
        # Find common neighbors of u and v
        for w in adj[u]:
            if w > v and w in adj[v]:
                print(u, v, w)
                return

find_volatile_triad()