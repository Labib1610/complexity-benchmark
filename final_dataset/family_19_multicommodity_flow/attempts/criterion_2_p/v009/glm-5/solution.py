import sys
from collections import deque

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    _ = int(data[idx]); idx += 1  # the '1'
    s = int(data[idx]); idx += 1
    t = int(data[idx]); idx += 1
    d = int(data[idx]); idx += 1

    u = [0] * m
    v = [0] * m
    cap = [0] * m
    for i in range(m):
        u[i] = int(data[idx]); idx += 1
        v[i] = int(data[idx]); idx += 1
        cap[i] = int(data[idx]); idx += 1

    # Build adjacency list
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        adj[u[i]].append(i)
        adj[v[i]].append(i)

    # Dinic's algorithm
    head = [-1] * (n + 1)
    to = [0] * (2 * m)
    nxt = [0] * (2 * m)
    cap_edge = [0] * (2 * m)

    for i in range(m):
        # forward edge index 2*i
        head[u[i]] = 0 if head[u[i]] == -1 else head[u[i]]
        to[2*i] = v[i]
        nxt[2*i] = head[u[i]]
        head[u[i]] = 2*i
        cap_edge[2*i] = cap[i]

        # backward edge index 2*i+1
        head[v[i]] = 0 if head[v[i]] == -1 else head[v[i]]
        to[2*i+1] = u[i]
        nxt[2*i+1] = head[v[i]]
        head[v[i]] = 2*i+1
        cap_edge[2*i+1] = 0

    level = [0] * (n + 1)
    ptr = [0] * (n + 1)

    def bfs():
        for i in range(n + 1):
            level[i] = -1
        level[s] = 0
        q = deque([s])
        while q:
            node = q.popleft()
            e = head[node]
            while e != -1:
                if cap_edge[e] > 0 and level[to[e]] < 0:
                    level[to[e]] = level[node] + 1
                    q.append(to[e])
                e = nxt[e]
        return level[t] >= 0

    def dfs(node, f):
        if node == t:
            return f
        e = ptr[node]
        while e != -1:
            if cap_edge[e] > 0 and level[to[e]] == level[node] + 1:
                pushed = dfs(to[e], min(f, cap_edge[e]))
                if pushed > 0:
                    cap_edge[e] -= pushed
                    cap_edge[e ^ 1] += pushed
                    return pushed
            e = nxt[e]
            ptr[node] = e
        return 0

    flow = 0
    while flow < d and bfs():
        for i in range(n + 1):
            ptr[i] = head[i]
        while True:
            pushed = dfs(s, d - flow)
            if pushed == 0:
                break
            flow += pushed

    if flow < d:
        sys.stdout.write("NO\n")
        return

    # Extract flow on each original edge
    result = [0] * m
    for i in range(m):
        # flow on edge i = original cap - remaining cap on forward edge
        result[i] = cap[i] - cap_edge[2*i]

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, result)) + "\n")

solve()