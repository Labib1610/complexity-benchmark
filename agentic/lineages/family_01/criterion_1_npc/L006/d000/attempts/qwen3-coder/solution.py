import sys
from itertools import product

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n, m = int(data[0]), int(data[1])
    edges = []
    idx = 2
    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx+1]) - 1
        edges.append((u, v))
        idx += 2
    
    # We need to find a 3-coloring that is lexicographically smallest
    # We can do this by backtracking with constraint propagation
    
    # Build adjacency list
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # colors[i] will store the color of node i (0-based), or -1 if unassigned
    colors = [-1] * n
    
    def is_safe(node, color):
        for neighbor in adj[node]:
            if colors[neighbor] == color:
                return False
        return True
    
    def backtrack(pos):
        if pos == n:
            return True
        # Try colors 0, 1, 2 in order (corresponding to hoppers 1, 2, 3)
        for c in range(3):
            if is_safe(pos, c):
                colors[pos] = c
                if backtrack(pos + 1):
                    return True
                colors[pos] = -1
        return False
    
    if backtrack(0):
        print("YES")
        print(' '.join(str(c + 1) for c in colors))
    else:
        print("NO")

solve()