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
    parent = [0] * (n + 1)
    depth = [0] * (n + 1)
    stack = []
    conflict = False

    for s in range(1, n + 1):
        if color[s] != 0:
            continue
        color[s] = 1
        depth[s] = 0
        stack.append(s)
        while stack:
            u = stack.pop()
            for v in adj[u]:
                if color[v] == 0:
                    color[v] = 3 - color[u]
                    depth[v] = depth[u] + 1
                    parent[v] = u
                    stack.append(v)
                elif color[v] == color[u]:
                    if conflict:
                        continue
                    a, b = u, v
                    if depth[a] < depth[b]:
                        a, b = b, a
                    while depth[a] > depth[b]:
                        a = parent[a]
                    while a != b:
                        a = parent[a]
                        b = parent[b]
                    cycle_len = depth[u] + depth[v] - 2 * depth[a] + 1
                    if cycle_len % 2 == 1:
                        conflict = True

    if conflict:
        sys.stdout.write("NO\n")
        return

    color = [0] * (n + 1)
    for u in range(1, n + 1):
        if color[u] == 0:
            color[u] = 1
            stack.append(u)
            while stack:
                x = stack.pop()
                for y in adj[x]:
                    if color[y] == 0:
                        color[y] = 3 - color[x]
                        stack.append(y)

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(str(color[i]) for i in range(1, n + 1)) + "\n")

solve()