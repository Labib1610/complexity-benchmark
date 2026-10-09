import sys
from collections import deque

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * (n + 1)  # 0 = unvisited, 1 or 2 = assigned value
    
    for start in range(1, n + 1):
        if color[start] != 0:
            continue
        color[start] = 1
        queue = deque([start])
        while queue:
            u = queue.popleft()
            cu = color[u]
            for v in adj[u]:
                if color[v] == 0:
                    color[v] = 3 - cu  # opposite: 1->2, 2->1
                    queue.append(v)
                elif color[v] == cu:
                    print("NO")
                    return
    
    print("YES")
    print(' '.join(str(color[i]) for i in range(1, n + 1)))

solve()