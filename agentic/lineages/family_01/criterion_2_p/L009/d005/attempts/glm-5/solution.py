import sys
from collections import deque

def solve():
    input_data = sys.stdin.buffer.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    p = [0] * n
    visited = [False] * n
    
    for start in range(n):
        if visited[start]:
            continue
        visited[start] = True
        p[start] = 1
        queue = deque([start])
        comp = [start]
        
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    p[v] = 3 - p[u]
                    queue.append(v)
                    comp.append(v)
        
        for u in comp:
            du = len(adj[u])
            s = 0
            for v in adj[u]:
                s += p[v] * p[v]
            if s + 3 * du * p[u] != 7 * du:
                print("NO")
                return
    
    print("YES")
    print(' '.join(map(str, p)))

solve()