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
    for i in range(1, n + 1):
        if color[i] == 0:
            stack = [i]
            color[i] = 1
            while stack:
                u = stack.pop()
                cu = color[u]
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - cu
                        stack.append(v)
                    elif color[v] == cu:
                        sys.stdout.write("NO")
                        return
    
    out = ["YES"]
    out.append(" ".join(str(color[i]) for i in range(1, n + 1)))
    sys.stdout.write("\n".join(out))

solve()