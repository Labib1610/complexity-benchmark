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
    parent = [0] * (n + 1)
    order = []
    is_bipartite = True
    
    for i in range(1, n + 1):
        if color[i] == 0:
            color[i] = 1
            parent[i] = 0
            stack = [i]
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
                        is_bipartite = False
                    e = nxt[e]
    
    if not is_bipartite:
        sys.stdout.write("NO\n")
        return
    
    for u in order:
        e = head[u]
        while e != -1:
            v = to[e]
            if parent[v] == u:
                if color[u] == 1:
                    color[u] = 2
            e = nxt[e]
    
    sys.stdout.write("YES\n")
    sys.stdout.write(' '.join(str(color[i]) for i in range(1, n + 1)) + '\n')

if __name__ == "__main__":
    setrecursionlimit(1 << 25)
    solve()