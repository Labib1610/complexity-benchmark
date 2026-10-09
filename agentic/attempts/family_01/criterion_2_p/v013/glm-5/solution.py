import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx+1]); idx += 2
        if u == v:
            continue
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * (n + 1)
    for i in range(1, n + 1):
        if color[i] == 0:
            color[i] = 1
            stack = [i]
            while stack:
                u = stack.pop()
                for w in adj[u]:
                    if color[w] == 0:
                        color[w] = 3 - color[u]
                        stack.append(w)
                    elif color[w] == color[u]:
                        print("NO")
                        return
    
    out = ["YES"]
    out.append(" ".join(str(color[i]) for i in range(1, n + 1)))
    sys.stdout.write("\n".join(out))

solve()