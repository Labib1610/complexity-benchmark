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
    
    color = [0] * (n + 1)
    
    for start in range(1, n + 1):
        if color[start] != 0:
            continue
        
        success = False
        for init_c in (1, 2):
            color[start] = init_c
            assigned = [start]
            queue = deque([start])
            ok = True
            
            while queue and ok:
                u = queue.popleft()
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        assigned.append(v)
                        queue.append(v)
                    elif color[v] == color[u]:
                        ok = False
                        break
            
            if ok:
                success = True
                break
            else:
                for node in assigned:
                    color[node] = 0
        
        if not success:
            print("NO")
            return
    
    print("YES")
    print(' '.join(str(color[i]) for i in range(1, n + 1)))

solve()