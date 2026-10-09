import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0]); m = int(data[1])
    edges = []
    idx = 2
    for i in range(m):
        u = int(data[idx]); v = int(data[idx+1]); idx += 2
        edges.append((u, v))

    deg = [0] * (n + 1)
    adj = [[] for _ in range(n + 1)]
    for i, (u, v) in enumerate(edges):
        adj[u].append((v, i))
        adj[v].append((u, i))
        deg[u] += 1
        deg[v] += 1

    color = [0] * m
    removed = [False] * (n + 1)
    stack = []
    for v in range(1, n + 1):
        if deg[v] <= 1:
            stack.append(v)

    order = []
    while stack:
        v = stack.pop()
        if removed[v] or deg[v] > 1:
            continue
        removed[v] = True
        order.append(v)
        for to, eid in adj[v]:
            if not removed[to]:
                deg[to] -= 1
                if deg[to] <= 1:
                    stack.append(to)

    for v in range(1, n + 1):
        if not removed[v]:
            if deg[v] != 2:
                print("NO")
                return

    for v in order:
        used = set()
        for to, eid in adj[v]:
            if removed[to] and color[eid] != 0:
                used.add(color[eid])
        for c in (1, 2, 3):
            if c not in used:
                for to, eid in adj[v]:
                    if removed[to] and color[eid] == 0:
                        color[eid] = c
                        break
                break

    for v in range(1, n + 1):
        if not removed[v]:
            used = set()
            for to, eid in adj[v]:
                if color[eid] != 0:
                    used.add(color[eid])
            for c in (1, 2, 3):
                if c not in used:
                    for to, eid in adj[v]:
                        if color[eid] == 0:
                            color[eid] = c
                            break
                    break

    for v in range(1, n + 1):
        seen = set()
        for to, eid in adj[v]:
            c = color[eid]
            if c == 0 or c in seen:
                print("NO")
                return
            seen.add(c)

    print("YES")
    print(' '.join(map(str, color)))

solve()