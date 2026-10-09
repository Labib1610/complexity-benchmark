import sys
from collections import deque

def solve():
    input_data = sys.stdin.buffer.read().split()
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
        
        # Try assigning start = 1
        color[start] = 1
        queue = deque([start])
        component = [start]
        ok = True
        
        while queue and ok:
            u = queue.popleft()
            for v in adj[u]:
                if color[v] == 0:
                    color[v] = 3 - color[u]
                    queue.append(v)
                    component.append(v)
                elif color[v] == color[u]:
                    ok = False
                    break
        
        if ok:
            continue
        
        # Try assigning start = 2
        for v in component:
            color[v] = 0
        color[start] = 2
        queue = deque([start])
        ok = True
        
        while queue and ok:
            u = queue.popleft()
            for v in adj[u]:
                if color[v] == 0:
                    color[v] = 3 - color[u]
                    queue.append(v)
                elif color[v] == color[u]:
                    ok = False
                    break
        
        if not ok:
            print("NO")
            return
    
    print("YES")
    print(' '.join(str(color[i]) for i in range(1, n+1)))

solve()