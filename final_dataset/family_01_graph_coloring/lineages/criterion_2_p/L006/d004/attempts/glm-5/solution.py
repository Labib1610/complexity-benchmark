import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * (n + 1)
    stack = []
    
    for start in range(1, n + 1):
        if color[start] != 0:
            continue
        color[start] = 1
        stack.append(start)
        while stack:
            u = stack.pop()
            for w in adj[u]:
                if color[w] == 0:
                    color[w] = 3 - color[u]
                    stack.append(w)
    
    for u in range(1, n + 1):
        for w in adj[u]:
            if color[w] == color[u]:
                print("NO")
                return
    
    print("YES")
    print(' '.join(str(color[i]) for i in range(1, n + 1)))

solve()