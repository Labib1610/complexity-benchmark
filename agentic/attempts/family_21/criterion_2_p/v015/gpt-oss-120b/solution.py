import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); s = int(next(it)) - 1; t = int(next(it)) - 1; B = int(next(it))
    edges_input = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        edges_input.append((u, v, w))

    # Dinic
    class Edge:
        __slots__ = ('to', 'rev', 'cap')
        def __init__(self, to, rev, cap):
            self.to = to
            self.rev = rev
            self.cap = cap

    g = [[] for _ in range(n)]

    def add_edge(fr, to, cap):
        fwd = Edge(to, len(g[to]), cap)
        rev = Edge(fr, len(g[fr]), 0)
        g[fr].append(fwd)
        g[to].append(rev)

    for u, v, w in edges_input:
        add_edge(u, v, w)
        add_edge(v, u, w)   # because original graph is undirected, we need two directed edges with same capacity

    level = [0]*n
    it_ptr = [0]*n

    from collections import deque

    def bfs():
        for i in range(n):
            level[i] = -1
        q = deque()
        level[s] = 0
        q.append(s)
        while q:
            v = q.popleft()
            for e in g[v]:
                if e.cap > 0 and level[e.to] < 0:
                    level[e.to] = level[v] + 1
                    q.append(e.to)
        return level[t] >= 0

    def dfs(v, f):
        if v == t:
            return f
        for i in range(it_ptr[v], len(g[v])):
            e = g[v][i]
            if e.cap > 0 and level[v] < level[e.to]:
                ret = dfs(e.to, min(f, e.cap))
                if ret:
                    e.cap -= ret
                    g[e.to][e.rev].cap += ret
                    return ret
            it_ptr[v] += 1
        return 0

    flow = 0
    INF = 10**18
    while bfs():
        it_ptr = [0]*n
        while True:
            f = dfs(s, INF)
            if not f:
                break
            flow += f

    # after maxflow, find reachable vertices in residual graph
    visited = [False]*n
    stack = [s]
    visited[s] = True
    while stack:
        v = stack.pop()
        for e in g[v]:
            if e.cap > 0 and not visited[e.to]:
                visited[e.to] = True
                stack.append(e.to)

    cut_edges = []
    total = 0
    for u, v, w in edges_input:
        if visited[u] != visited[v]:
            cut_edges.append((u+1, v+1))
            total += w

    if total <= B:
        out = ["YES", str(len(cut_edges))]
        out += [f"{u} {v}" for u, v in cut_edges]
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()