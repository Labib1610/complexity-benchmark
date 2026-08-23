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

    color = [0] * (n + 1)  # 1 -> value 1, -1 -> value 2

    for i in range(1, n + 1):
        if color[i] != 0:
            continue
        color[i] = 1
        stack = [i]
        while stack:
            u = stack.pop()
            cu = color[u]
            for w in adj[u]:
                if color[w] == 0:
                    color[w] = -cu
                    stack.append(w)
                elif color[w] == cu:
                    sys.stdout.write("NO")
                    return

    res = ['YES']
    res.append(' '.join('1' if c == 1 else '2' for c in color[1:]))
    sys.stdout.write('\n'.join(res))

solve()