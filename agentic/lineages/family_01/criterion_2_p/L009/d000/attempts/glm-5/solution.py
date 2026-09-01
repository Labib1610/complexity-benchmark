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
    edge_cnt = 0
    
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        to[edge_cnt] = v
        nxt[edge_cnt] = head[u]
        head[u] = edge_cnt
        edge_cnt += 1
        
        to[edge_cnt] = u
        nxt[edge_cnt] = head[v]
        head[v] = edge_cnt
        edge_cnt += 1
    
    color = [0] * (n + 1)
    possible = True
    
    for start in range(1, n + 1):
        if color[start] == 0:
            color[start] = 1
            stack = [start]
            while stack:
                u = stack.pop()
                e = head[u]
                while e != -1:
                    v = to[e]
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        stack.append(v)
                    elif color[v] == color[u]:
                        print("NO")
                        return
                    e = nxt[e]
    
    print("YES")
    print(' '.join(str(color[i]) for i in range(1, n + 1)))

solve()