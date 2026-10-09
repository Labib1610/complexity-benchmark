import sys
from sys import setrecursionlimit

def solve():
    input_data = sys.stdin.buffer.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    head = [-1] * (n + 1)
    to = [0] * (2 * m)
    nxt = [0] * (2 * m)
    for i in range(m):
        u = int(next(it))
        v = int(next(it))
        to[2*i] = v
        nxt[2*i] = head[u]
        head[u] = 2*i
        to[2*i+1] = u
        nxt[2*i+1] = head[v]
        head[v] = 2*i+1
    
    color = [0] * (n + 1)
    parent = [0] * (n + 1)
    order = []
    possible = True
    
    for start in range(1, n + 1):
        if color[start] == 0:
            color[start] = 1
            parent[start] = 0
            stack = [start]
            while stack:
                u = stack.pop()
                order.append(u)
                e = head[u]
                while e != -1:
                    v = to[e]
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        parent[v] = u
                        stack.append(v)
                    elif color[v] == color[u]:
                        nonlocal possible
                        possible = False
                    e = nxt[e]
    
    if not possible:
        sys.stdout.write("NO\n")
        return
    
    # Greedy: process in DFS order, flip if parent has same color
    for u in order:
        p = parent[u]
        if p != 0 and color[u] == color[p]:
            color[u] = 3 - color[u]
    
    sys.stdout.write("YES\n")
    sys.stdout.write(' '.join(str(color[i]) for i in range(1, n + 1)) + '\n')

solve()