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
        u = int(input_data[idx]); v = int(input_data[idx+1])
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * (n + 1)
    
    for start in range(1, n + 1):
        if color[start] != 0:
            continue
        # BFS to 2-color this component, assigning color 1 to the smallest node
        color[start] = 1
        q = deque([start])
        while q:
            u = q.popleft()
            cu = color[u]
            for v in adj[u]:
                if color[v] == 0:
                    color[v] = 3 - cu
                    q.append(v)
                elif color[v] == cu:
                    print("NO")
                    return
    
    print("YES")
    print(' '.join(str(color[i]) for i in range(1, n + 1)))

solve()