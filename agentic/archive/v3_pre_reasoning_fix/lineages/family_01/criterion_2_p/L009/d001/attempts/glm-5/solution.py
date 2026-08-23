import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        if u == v:
            print("NO")
            return
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * (n+1)
    
    for start in range(1, n+1):
        if color[start] == 0:
            queue = deque([start])
            color[start] = 1
            
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
    print(' '.join(map(str, color[1:])))

solve()