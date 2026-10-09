import sys

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
    edge_count = 0
    
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        to[edge_count] = v
        nxt[edge_count] = head[u]
        head[u] = edge_count
        edge_count += 1
        
        to[edge_count] = u
        nxt[edge_count] = head[v]
        head[v] = edge_count
        edge_count += 1
    
    color = [0] * (n + 1)
    parent = [0] * (n + 1)
    stack = []
    
    for start in range(1, n + 1):
        if color[start] != 0:
            continue
        color[start] = 1
        stack.append(start)
        while stack:
            u = stack.pop()
            e = head[u]
            while e != -1:
                v = to[e]
                if color[v] == 0:
                    color[v] = 3 - color[u]
                    parent[v] = u
                    stack.append(v)
                elif color[v] == color[u] and v != parent[u]:
                    print("NO")
                    return
                e = nxt[e]
    
    print("YES")
    sys.stdout.write(' '.join(str(color[i]) for i in range(1, n + 1)))
    sys.stdout.write('\n')

solve()