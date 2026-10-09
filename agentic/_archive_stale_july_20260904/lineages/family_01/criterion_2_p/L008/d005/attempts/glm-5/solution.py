import sys
from sys import stdin

def solve():
    input_data = stdin.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * (n+1)
    
    for start in range(1, n+1):
        if color[start] != 0:
            continue
        # Try coloring start with 1
        color[start] = 1
        stack = [start]
        ok = True
        order = [start]
        while stack and ok:
            u = stack.pop()
            for v in adj[u]:
                if color[v] == 0:
                    color[v] = 3 - color[u]
                    stack.append(v)
                    order.append(v)
                elif color[v] == color[u]:
                    ok = False
                    break
        
        if ok:
            continue
        
        # Reset and try coloring start with 2
        for node in order:
            color[node] = 0
        color[start] = 2
        stack = [start]
        ok = True
        while stack and ok:
            u = stack.pop()
            for v in adj[u]:
                if color[v] == 0:
                    color[v] = 3 - color[u]
                    stack.append(v)
                elif color[v] == color[u]:
                    ok = False
                    break
        
        if not ok:
            print("NO")
            return
    
    print("YES")
    print(' '.join(str(color[i]) for i in range(1, n+1)))

solve()