import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    nL = int(data[idx])
    idx += 1
    nR = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    
    edges = []
    deg_L = [0] * (nL + 1)
    deg_R = [0] * (nR + 1)
    
    for _ in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        edges.append((u, v))
        deg_L[u] += 1
        deg_R[v] += 1
    
    delta = max(max(deg_L[1:]), max(deg_R[1:]))
    
    # Build adjacency list for graph matching
    adj = [[] for _ in range(nL + 1)]
    for i, (u, v) in enumerate(edges):
        adj[u].append((v, i))
    
    # For each left node, sort its edges by right node id for consistency
    for u in range(1, nL + 1):
        adj[u].sort()
    
    # We'll simulate a greedy edge coloring approach using BFS-like assignment
    # Each color represents a cycle. We want to use at most delta colors.
    result = [0] * m
    used_colors_L = [set() for _ in range(nL + 1)]
    used_colors_R = [set() for _ in range(nR + 1)]
    
    # For each edge, assign the smallest available color not used by either endpoint
    for i, (u, v) in enumerate(edges):
        c = 1
        while c in used_colors_L[u] or c in used_colors_R[v]:
            c += 1
        result[i] = c
        used_colors_L[u].add(c)
        used_colors_R[v].add(c)
    
    print("YES")
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()