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

    edges = []
    adj = [[] for _ in range(n + 1)]
    for j in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        cap = int(data[idx]); idx += 1
        edges.append((u, v, cap))
        adj[u].append((v, j))
        adj[v].append((u, j))  # for BFS on undirected connectivity

    # Check undirected connectivity between s and t
    visited = [False] * (n + 1)
    visited[s] = True
    q = deque([s])
    while q:
        u = q.popleft()
        if u == t:
            break
        for v, _ in adj[u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)
    if not visited[t]:
        print("NO")
        return

    # Build flow network: node 0 = source, node 1 = sink, nodes 2..n+1 = routers
    N = n + 2
    S = 0
    T = 1
    head = [-1] * N
    to = []
    cap_arr = []
    nxt = []

    def add_edge(a, b, c):
        to.append(b); cap_arr.append(c); nxt.append(head[a]); head[a] = len(to) - 1
        to.append(a); cap_arr.append(0); nxt.append(head[b]); head[b] = len(to) - 1

    # source -> origin with capacity d
    add_edge(S, s + 1, d)
    # destination -> sink with capacity d
    add_edge(t + 1, T, d)
    # original edges
    for u, v, c in edges:
        add_edge(u + 1, v + 1, c)

    # Dinic
    level = [0] * N
    def bfs():
        for i in range(N):
            level[i] = -1
        level[S] = 0
        qd = deque([S])
        while qd:
            u = qd.popleft()
            e = head[u]
            while e != -1:
                if cap_arr[e] > 0 and level[to[e]] < 0:
                    level[to[e]] = level[u] + 1
                    qd.append(to[e])
                e = nxt[e]
        return level[T] >= 0

    def dfs(u, f):
        if u == T:
            return f
        e = ptr[u]
        while e != -1:
            v = to[e]
            if cap_arr[e] > 0 and level[v] == level[u] + 1:
                pushed = dfs(v, min(f, cap_arr[e]))
                if pushed > 0:
                    cap_arr[e] -= pushed
                    cap_arr[e ^ 1] += pushed
                    ptr[u] = e
                    return pushed
            e = nxt[e]
        ptr[u] = -1
        return 0

    flow = 0
    while bfs():
        ptr = list(head)
        while True:
            pushed = dfs(S, d - flow)
            if pushed == 0:
                break
            flow += pushed
            if flow == d:
                break

    if flow < d:
        print("NO")
        return

    # Extract flow on original edges
    # Original edge j corresponds to add_edge call index (2 + j*2), forward edge
    ans = []
    for j in range(m):
        e = 2 + j * 2 + 1  # reverse edge holds the flow used
        ans.append(cap_arr[e])

    print("YES")
    print(' '.join(map(str, ans)))

solve()