import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * (n + 1)
    
    for start in range(1, n + 1):
        if color[start] != 0:
            continue
        
        queue = deque([start])
        color[start] = 1
        
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if color[v] == 0:
                    color[v] = -color[u]
                    queue.append(v)
                elif color[v] == color[u]:
                    print("NO")
                    return
    
    result = [1 if color[i] == 1 else 2 for i in range(1, n + 1)]
    
    print("YES")
    print(' '.join(map(str, result)))

solve()