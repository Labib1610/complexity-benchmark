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
    
    level = [0] * (n + 1)
    
    for start in range(1, n + 1):
        if level[start] != 0:
            continue
        level[start] = 1
        queue = deque([start])
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if level[v] == 0:
                    level[v] = 3 - level[u]
                    queue.append(v)
                elif level[v] == level[u]:
                    sys.stdout.write("NO\n")
                    return
    
    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(str(level[i]) for i in range(1, n + 1)) + "\n")

solve()