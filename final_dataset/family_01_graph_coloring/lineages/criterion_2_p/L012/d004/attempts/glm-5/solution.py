import sys
from sys import setrecursionlimit

def solve():
    input_data = sys.stdin.buffer.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * (n + 1)
    parent = [0] * (n + 1)
    depth = [0] * (n + 1)
    stack = []
    
    for start in range(1, n + 1):
        if color[start] != 0:
            continue
        color[start] = 1
        parent[start] = 0
        depth[start] = 0
        stack.append(start)
        while stack:
            u = stack.pop()
            for v in adj[u]:
                if color[v] == 0:
                    color[v] = 3 - color[u]
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    stack.append(v)
                elif v != parent[u]:
                    if color[u] == color[v]:
                        print("NO")
                        return
    
    print("YES")
    print(' '.join(str(color[i]) for i in range(1, n + 1)))

solve()