import sys
from collections import deque

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    n, m = map(int, input[ptr:ptr+2])
    ptr +=2
    
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input[ptr:ptr+2])
        ptr +=2
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0]*(n+1)
    possible = True
    
    for i in range(1, n+1):
        if color[i] == 0:
            queue = deque()
            queue.append(i)
            color[i] = 1
            while queue and possible:
                current = queue.popleft()
                for neighbor in adj[current]:
                    if color[neighbor] == 0:
                        color[neighbor] = 3 - color[current]
                        queue.append(neighbor)
                    elif color[neighbor] == color[current]:
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
        print(' '.join(map(str, color[1:n+1])))

solve()