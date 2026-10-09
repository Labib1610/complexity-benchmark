import sys
from collections import deque

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    n, m = map(int, input[ptr:ptr+2])
    ptr += 2
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input[ptr:ptr+2])
        ptr += 2
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * n
    possible = True
    
    for i in range(n):
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
        print(*(color[i] for i in range(n)))

if __name__ == '__main__':
    solve()