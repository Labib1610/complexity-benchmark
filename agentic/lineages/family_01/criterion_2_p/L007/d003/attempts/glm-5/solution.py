import sys
from sys import stdin

def solve():
    input_data = stdin.read().split()
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
    
    color = [0] * (n + 1)
    
    for start in range(1, n+1):
        if color[start] != 0:
            continue
        color[start] = 1
        stack = [start]
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
    print(' '.join(str(color[i]) for i in range(1, n+1)))

solve()