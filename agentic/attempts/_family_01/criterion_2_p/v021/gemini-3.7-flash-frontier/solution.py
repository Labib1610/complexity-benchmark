import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
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
            next_c = 2 if c == 1 else 1
            
            for v in adj[u]:
                if color[v] == 0:
                    color[v] = next_c
                    q.append(v)
                elif color[v] != next_c:
                    print("NO")
                    return

    print("YES")
    print(*(color[1:]))

if __name__ == '__main__':
    solve()