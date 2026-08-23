import sys
from collections import deque

def solve():
    it = iter(sys.stdin.read().split())
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
    
    assignment = [-1] * (n + 1)
    
    for start in range(1, n + 1):
        if assignment[start] != -1:
            continue
        
        assignment[start] = 1
        queue = deque([start])
        
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                required = 3 - assignment[u]
                if assignment[v] == -1:
                    assignment[v] = required
                    queue.append(v)
                elif assignment[v] != required:
                    print("NO")
                    return
    
    print("YES")
    print(" ".join(map(str, assignment[1:])))

solve()