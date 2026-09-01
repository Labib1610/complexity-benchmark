import sys
from collections import deque

def solve():
    n, m = map(int, sys.stdin.readline().split())
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * (n + 1)
    possible = True
    
    for i in range(1, n+1):
        if color[i] == 0:
            q = deque()
            q.append(i)
            color[i] = 1
            while q and possible:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        q.append(v)
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
        print(' '.join(map(str, color[1:])))

solve()