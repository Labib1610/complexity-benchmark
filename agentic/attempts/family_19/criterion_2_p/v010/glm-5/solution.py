import sys
from collections import deque

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    s = int(next(it))
    t = int(next(it))
    d = int(next(it))

    edges = []
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        u = int(next(it))
        v = int(next(it))
        cap = int(next(it))
        edges.append((u, v, cap))
        adj[u].append((v, i))
        adj[v].append((u, i))

    # BFS to find augmenting path
    def bfs():
        parent_edge = [-1] * (n + 1)
        visited = [False] * (n + 1)
        q = deque()
        q.append(s)
        visited[s] = True
        while q:
            u = q.popleft()
            if u == t:
                break
            for v, idx in adj[u]:
                if not visited[v]:
                    if u == edges[idx][0]:
                        # forward edge
                        if flow[idx] < edges[idx][2]:
                            visited[v] = True
                            parent_edge[v] = idx
                            q.append(v)
                    else:
                        # backward edge
                        if flow[idx] > 0:
                            visited[v] = True
                            parent_edge[v] = ~idx
                            q.append(v)
        if not visited[t]:
            return None
        path = []
        u = t
        while u != s:
            pe = parent_edge[u]
            if pe >= 0:
                path.append((pe, 1))
                u = edges[pe][0]
            else:
                idx = ~pe
                path.append((idx, -1))
                u = edges[idx][1]
        path.reverse()
        return path

    flow = [0] * m
    total = 0
    while total < d:
        path = bfs()
        if path is None:
            break
        # find bottleneck
        bottleneck = d - total
        for idx, direction in path:
            u, v, cap = edges[idx]
            if direction == 1:
                avail = cap - flow[idx]
            else:
                avail = flow[idx]
            if avail < bottleneck:
                bottleneck = avail
        for idx, direction in path:
            flow[idx] += direction * bottleneck
        total += bottleneck

    if total < d:
        sys.stdout.write("NO\n")
        return

    # Verify feasibility
    balance = [0] * (n + 1)
    for i in range(m):
        u, v, cap = edges[i]
        if flow[i] < 0 or flow[i] > cap:
            sys.stdout.write("NO\n")
            return
        balance[u] -= flow[i]
        balance[v] += flow[i]

    ok = True
    for i in range(1, n + 1):
        if i == s:
            if balance[i] != d:
                ok = False
                break
        elif i == t:
            if balance[i] != -d:
                ok = False
                break
        else:
            if balance[i] != 0:
                ok = False
                break

    if not ok:
        sys.stdout.write("NO\n")
        return

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(str(x) for x in flow) + "\n")

solve()