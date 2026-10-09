import sys
from sys import stdin

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    
    adj = [set() for _ in range(n+1)]
    edges = set()
    for _ in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        adj[u].add(v)
        adj[v].add(u)
        edges.add((min(u,v), max(u,v)))
    
    best = None
    # For each vertex, check pairs of neighbors
    for c in range(1, n+1):
        neighbors = sorted(adj[c])
        for i in range(len(neighbors)):
            for j in range(i+1, len(neighbors)):
                a, b = neighbors[i], neighbors[j]
                if b in adj[a]:  # edge a-b exists
                    trio = tuple(sorted([a, b, c]))
                    if best is None or trio < best:
                        best = trio
    
    print(best[0], best[1], best[2])

solve()