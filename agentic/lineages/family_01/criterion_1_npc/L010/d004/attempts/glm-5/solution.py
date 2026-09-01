import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    adj = [[] for _ in range(n)]
    idx = 2
    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx+1]) - 1
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * n
    order = []
    visited = [False] * n
    
    for start in range(n):
        if visited[start]:
            continue
        comp = []
        stack = [start]
        visited[start] = True
        while stack:
            u = stack.pop()
            comp.append(u)
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    stack.append(v)
        order.append(comp)
    
    for comp in order:
        color[comp[0]] = 1
        stack = [comp[0]]
        while stack:
            u = stack.pop()
            for v in adj[u]:
                if color[v] == 0:
                    color[v] = 3 - color[u]
                    stack.append(v)
                elif color[v] == color[u]:
                    print("NO")
                    return
    
    print("YES")
    print(' '.join(str(c) for c in color))

solve()