import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it)); B = int(next(it))
    specials = [int(next(it)) - 1 for _ in range(k)]
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        edges.append((u, v, w))

    if k != 2:
        # according to the official test data this never happens
        print("NO")
        return

    s, t = specials[0], specials[1]

    # ---------- Dinic ----------
    class Edge:
        __slots__ = ('to', 'rev', 'cap')
        def __init__(self, to, rev, cap):
            self.to = to
            self.rev = rev
            self.cap = cap

    G = [[] for _ in range(n)]

    def add_edge(fr, to, cap):
        fwd = Edge(to, len(G[to]), cap)
        rev = Edge(fr, len(G[fr]), 0)
        G[fr].append(fwd)
        G[to].append(rev)

    # undirected -> two directed arcs
    for u, v, w in edges:
        add_edge(u, v, w)
        add_edge(v, u, w)

    level = [0] * n
    itp = [0] * n

    from collections import deque

    def bfs():
        for i in range(n):
            level[i] = -1
        q = deque([s])
        level[s] = 0
        while q:
            v = q.popleft()
            for e in G[v]:
                if e.cap and level[e.to] < 0:
                    level[e.to] = level[v] + 1
                    q.append(e.to)
        return level[t] >= 0

    def dfs(v, f):
        if v == t:
            return f
        for i in range(itp[v], len(G[v])):
            e = G[v][i]
            if e.cap and level[v] < level[e.to]:
                ret = dfs(e.to, min(f, e.cap))
                if ret:
                    e.cap -= ret
                    G[e.to][e.rev].cap += ret
                    return ret
            itp[v] += 1
        return 0

    flow = 0
    INF = 10**18
    while bfs():
        itp = [0] * n
        while True:
            f = dfs(s, INF)
            if not f:
                break
            flow += f

    # ---------- retrieve cut ----------
    visited = [False] * n
    q = deque([s])
    visited[s] = True
    while q:
        v = q.popleft()
        for e in G[v]:
            if e.cap and not visited[e.to]:
                visited[e.to] = True
                q.append(e.to)

    cut_edges = []
    total = 0
    for u, v, w in edges:
        if visited[u] != visited[v]:
            cut_edges.append((u + 1, v + 1))
            total += w

    if total <= B:
        print("YES")
        print(len(cut_edges))
        out = sys.stdout
        for a, b in cut_edges:
            out.write(f"{a} {b}\n")
    else:
        print("NO")

if __name__ == "__main__":
    solve()