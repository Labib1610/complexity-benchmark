import sys

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
    order = []
    
    for start in range(1, n + 1):
        if color[start] == 0:
            color[start] = 1
            parent[start] = 0
            stack = [start]
            while stack:
                u = stack.pop()
                order.append(u)
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        parent[v] = u
                        stack.append(v)
                    elif color[v] == color[u]:
                        print("NO")
                        return
    
    color = [0] * (n + 1)
    for u in order:
        if color[u] == 0:
            color[u] = 1
    
    print("YES")
    print(' '.join(str(color[i]) for i in range(1, n + 1)))

solve()