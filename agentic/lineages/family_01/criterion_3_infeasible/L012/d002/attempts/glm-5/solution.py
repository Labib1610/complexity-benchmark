import sys

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    
    adj = [[] for _ in range(n + 1)]
    edges = set()
    
    for _ in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        adj[u].append(v)
        adj[v].append(u)
        if u > v:
            u, v = v, u
        edges.add((u, v))
    
    # Sort adjacency lists for deterministic iteration
    for i in range(1, n + 1):
        adj[i].sort()
    
    # For each vertex a (ascending), check pairs of neighbors (b, c) with b < c
    # If edge (b, c) exists, we found a triangle (a, b, c)
    # First found is lexicographically smallest
    for a in range(1, n + 1):
        neighbors = adj[a]
        L = len(neighbors)
        for i in range(L):
            b = neighbors[i]
            if b < a:
                continue
            for j in range(i + 1, L):
                c = neighbors[j]
                if c < a:
                    continue
                # Check if edge (b, c) exists
                if b < c:
                    key = (b, c)
                else:
                    key = (c, b)
                if key in edges:
                    # Found triangle
                    result = sorted([a, b, c])
                    print(f"{result[0]} {result[1]} {result[2]}")
                    return
    
    # Should never reach here per problem guarantee
    print("-1 -1 -1")

solve()