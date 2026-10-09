import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n + 1)]
    edges = []
    for i in range(m):
        u = int(next(it))
        v = int(next(it))
        edges.append((u, v))
        adj[u].append((v, i))
        adj[v].append((u, i))

    color = [0] * m
    visited = [False] * (n + 1)

    for s in range(1, n + 1):
        if visited[s]:
            continue
        stack = [(s, 0)]
        visited[s] = True
        while stack:
            u, pu = stack.pop()
            for v, ei in adj[u]:
                if ei == pu:
                    continue
                if not visited[v]:
                    visited[v] = True
                    color[ei] = 1
                    stack.append((v, ei))
                else:
                    if color[ei] == 0:
                        color[ei] = 2
        cnt = [0, 0, 0, 0]
        for v, ei in adj[s]:
            cnt[color[ei]] += 1
        if cnt[1] == 2:
            stack = [s]
            while stack:
                u = stack.pop()
                c1 = c2 = 0
                for v, ei in adj[u]:
                    if color[ei] == 1:
                        c1 += 1
                    elif color[ei] == 2:
                        c2 += 1
                if c1 == 2:
                    for v, ei in adj[u]:
                        if color[ei] == 1:
                            color[ei] = 2
                            stack.append(v)
                elif c2 == 2:
                    for v, ei in adj[u]:
                        if color[ei] == 2:
                            color[ei] = 1
                            stack.append(v)

    out = ['YES']
    out.append(' '.join(str(color[i]) for i in range(m)))
    sys.stdout.write('\n'.join(out))

solve()