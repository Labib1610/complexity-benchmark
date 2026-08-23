import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n + 1)]
    possible = True
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u == v:
            possible = False
        else:
            adj[u].append(v)
            adj[v].append(u)
    if not possible:
        sys.stdout.write("NO")
        return
    color = [0] * (n + 1)
    for i in range(1, n + 1):
        if color[i] != 0:
            continue
        color[i] = 1
        stack = [i]
        while stack:
            v = stack.pop()
            cv = color[v]
            nv = 3 - cv
            for w in adj[v]:
                if color[w] == 0:
                    color[w] = nv
                    stack.append(w)
                elif color[w] == cv:
                    sys.stdout.write("NO")
                    return
    out = ["YES"]
    out.append(" ".join(str(color[i]) for i in range(1, n + 1)))
    sys.stdout.write("\n".join(out))

solve()