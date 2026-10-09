import sys
sys.setrecursionlimit(1 << 25)

class Edge:
    __slots__ = ('to', 'rev', 'cap')
    def __init__(self, to, rev, cap):
        self.to = to
        self.rev = rev
        self.cap = cap

def add_edge(g, fr, to, cap):
    g[fr].append(Edge(to, len(g[to]), cap))
    g[to].append(Edge(fr, len(g[fr]) - 1, cap))   # undirected: same capacity back

def bfs(level, g, s, t):
    from collections import deque
    n = len(g)
    level[:] = [-1] * n
    q = deque([s])
    level[s] = 0
    while q:
        v = q.popleft()
        for e in g[v]:
            if e.cap > 0 and level[e.to] < 0:
                level[e.to] = level[v] + 1
                q.append(e.to)
    return level[t] >= 0

def dfs(v, t, f, level, it, g):
    if v == t:
        return f
    for i in range(it[v], len(g[v])):
        it[v] = i
        e = g[v][i]
        if e.cap > 0 and level[v] < level[e.to]:
            ret = dfs(e.to, t, min(f, e.cap), level, it, g)
            if ret:
                e.cap -= ret
                g[e.to][e.rev].cap += ret
                return ret
    return 0

def max_flow(g, s, t):
    flow = 0
    n = len(g)
    level = [-1] * n
    INF = 10**18
    while bfs(level, g, s, t):
        it = [0] * n
        while True:
            f = dfs(s, t, INF, level, it, g)
            if not f:
                break
            flow += f
    return flow

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); s = int(next(it))-1; t = int(next(it))-1; B = int(next(it))
    edges = []
    g = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it))-1; v = int(next(it))-1; w = int(next(it))
        edges.append((u, v, w))
        add_edge(g, u, v, w)
    min_cut = max_flow(g, s, t)
    if min_cut > B:
        print("NO")
        return
    # find reachable vertices in residual graph
    from collections import deque
    reachable = [False]*n
    q = deque([s])
    reachable[s] = True
    while q:
        v = q.popleft()
        for e in g[v]:
            if e.cap > 0 and not reachable[e.to]:
                reachable[e.to] = True
                q.append(e.to)
    cut_edges = []
    total = 0
    for u, v, w in edges:
        if reachable[u] != reachable[v]:
            cut_edges.append((u+1, v+1))
            total += w
    # total should equal min_cut
    print("YES")
    print(len(cut_edges))
    for u, v in cut_edges:
        print(u, v)

if __name__ == "__main__":
    solve()