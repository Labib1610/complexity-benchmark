import sys
from collections import deque

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    n, m = map(int, input[ptr:ptr+2])
    ptr += 2
    
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input[ptr:ptr+2])
        ptr += 2
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * (n + 1)
    
    for i in range(1, n+1):
        if color[i] == 0:
            queue = deque([i])
            color[i] = 1
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        print("NO")
                        return
    
    print("YES")
    print(' '.join(map(str, color[1:n+1])))

solve()