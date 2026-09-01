import sys
from sys import stdin

def solve():
    input_data = stdin.buffer.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * (n+1)
    parent = [0] * (n+1)
    order = []
    
    for s in range(1, n+1):
        if color[s] != 0:
            continue
        color[s] = 1
        parent[s] = 0
        stack = [s]
        while stack:
            u = stack.pop()
            order.append(u)
            for v in adj[u]:
                if color[v] == 0:
                    color[v] = 3 - color[u]
                    parent[v] = u
                    stack.append(v)
                elif color[v] == color[u]:
                    print("NO")
                    return
    
    # Greedy: process in BFS/DFS order, flip if parent has same color
    for u in order:
        p = parent[u]
        if p != 0 and color[u] == color[p]:
            color[u] = 3 - color[u]
    
    print("YES")
    print(' '.join(str(color[i]) for i in range(1, n+1)))

solve()