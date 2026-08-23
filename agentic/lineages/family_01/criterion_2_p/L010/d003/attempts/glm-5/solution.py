import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        g[u].append(v)
        g[v].append(u)

    color = [0] * (n + 1)
    for i in range(1, n + 1):
        if color[i] == 0:
            color[i] = 1
            stack = [i]
            while stack:
                u = stack.pop()
                cu = color[u]
                cv = 3 - cu
                for v in g[u]:
                    if color[v] == 0:
                        color[v] = cv
                        stack.append(v)
                    elif color[v] == cu:
                        sys.stdout.write("NO\n")
                        return

    out = ['YES\n', ' '.join(str(color[i]) for i in range(1, n + 1)), '\n']
    sys.stdout.write(''.join(out))

solve()