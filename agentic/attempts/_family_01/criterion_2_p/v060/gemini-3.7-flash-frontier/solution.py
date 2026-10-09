import sys
from collections import deque

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
        
    color = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if color[i] != 0:
            continue
        
        color[i] = 1
        q = deque([i])
        
        while q:
            u = q.popleft()
            c = color[u]
            next_c = 3 - c
            
            for v in adj[u]:
                if color[v] == 0:
                    color[v] = next_c
                    q.append(v)
                elif color[v] == c:
                    print("NO")
                    return

    print("YES")
    print(*(color[1:]))

if __name__ == '__main__':
    solve()