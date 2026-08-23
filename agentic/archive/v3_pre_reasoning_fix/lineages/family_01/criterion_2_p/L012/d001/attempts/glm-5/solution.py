import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
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
    
    mode = [0] * (n + 1)
    
    for start in range(1, n + 1):
        if mode[start] != 0:
            continue
        mode[start] = 1
        queue = deque([start])
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if mode[v] == 0:
                    mode[v] = 3 - mode[u]
                    queue.append(v)
                elif mode[v] + mode[u] != 3:
                    print("NO")
                    return
    
    print("YES")
    print(" ".join(map(str, mode[1:])))

solve()