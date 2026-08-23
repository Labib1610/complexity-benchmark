import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    idx = 0
    n, m = int(data[idx]), int(data[idx+1])
    idx += 2
    
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = int(data[idx]), int(data[idx+1])
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * (n+1)  # 0: unvisited, 1: team 1, 2: team 2
    
    for start in range(1, n+1):
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
    print(" ".join(str(color[i]) for i in range(1, n+1)))

solve()