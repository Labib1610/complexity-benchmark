import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
    
    tier = [0] * (n + 1)
    
    for start in range(1, n + 1):
        if tier[start] != 0:
            continue
        
        queue = deque([start])
        tier[start] = 1
        
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if tier[v] == 0:
                    tier[v] = 3 - tier[u]
                    queue.append(v)
                elif tier[v] == tier[u]:
                    print("NO")
                    return
    
    print("YES")
    print(' '.join(str(tier[i]) for i in range(1, n + 1)))

solve()