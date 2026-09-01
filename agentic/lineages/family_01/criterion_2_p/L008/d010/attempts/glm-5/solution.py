import sys
from collections import deque

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(input_data[idx]) - 1; idx += 1
        v = int(input_data[idx]) - 1; idx += 1
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * n  # 0 = unassigned, 1 = state 1, 2 = state 2
    
    for start in range(n):
        if color[start] != 0:
            continue
        color[start] = 1
        queue = deque([start])
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
    print(' '.join(str(color[i]) for i in range(n)))

solve()