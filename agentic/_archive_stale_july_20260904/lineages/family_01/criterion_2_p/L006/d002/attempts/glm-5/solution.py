import sys
from sys import stdin

def solve():
    input = stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    
    adj = [[] for _ in range(n+1)]
    idx = 2
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx+1])
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * (n+1)
    possible = True
    
    for i in range(1, n+1):
        if color[i] == 0:
            color[i] = 1
            stack = [i]
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        stack.append(v)
                    elif color[v] == color[u]:
                        possible = False
                        break
                if not possible:
                    break
        if not possible:
            break
    
    if not possible:
        print("NO")
    else:
        print("YES")
        print(' '.join(str(color[i]) for i in range(1, n+1)))

solve()