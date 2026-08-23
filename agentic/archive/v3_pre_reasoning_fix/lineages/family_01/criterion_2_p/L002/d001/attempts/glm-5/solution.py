import sys

def solve():
    data = sys.stdin.read().split()
    ptr = 0
    n = int(data[ptr]); ptr += 1
    m = int(data[ptr]); ptr += 1
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(data[ptr]) - 1; ptr += 1
        v = int(data[ptr]) - 1; ptr += 1
        adj[u].append(v)
        adj[v].append(u)
    
    color = [-1] * n  # -1: unvisited, 0: value 1, 1: value 2
    
    for start in range(n):
        if color[start] != -1:
            continue
        
        stack = [start]
        color[start] = 0  # Assign smallest value (1) to smallest node
        
        while stack:
            u = stack.pop()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 1 - color[u]
                    stack.append(v)
                elif color[v] == color[u]:
                    print("NO")
                    return
    
    print("YES")
    print(" ".join(str(c + 1) for c in color))

solve()