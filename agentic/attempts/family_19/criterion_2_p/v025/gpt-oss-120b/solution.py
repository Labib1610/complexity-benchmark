import sys
from collections import deque

def solve() -> None:
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    it = iter(data)
    n = next(it); m = next(it); _ = next(it)  # the third value is always 1 per statement, ignore
    s = next(it); t = next(it); d = next(it)

    edges_input = []
    for _ in range(m):
        u = next(it); v = next(it); cap = next(it)
        edges_input.append((u-1, v-1, cap))

    # Dinic with edge indexing to retrieve flows
    N = n
    g = [[] for _ in range(N)]

    class Edge:
        __slots__ = ('to','rev','cap','orig_cap','idx')
        def __init__(self, to, rev, cap, orig_cap, idx):
            self.to = to
            self.rev = rev
            self.cap = cap
            self.orig_cap = orig_cap
            self.idx = idx  # original edge index or -1 for added edges

    def add_edge(fr, to, cap, idx):
        fwd = Edge(to, len(g[to]), cap, cap, idx)
        rev = Edge(fr, len(g[fr]), 0, 0, -1)
        g[fr].append(fwd)
        g[to].append(rev)

    for i, (u, v, c) in enumerate(edges_input):
        add_edge(u, v, c, i)

    level = [0]*N
    it_ptr = [0]*N

    def bfs():
        for i in range(N):
            level[i] = -1
        q = deque([s-1])
        level[s-1] = 0
        while q:
            v = q.popleft()
            for e in g[v]:
                if e.cap and level[e.to] < 0:
                    level[e.to] = level[v] + 1
                    q.append(e.to)
        return level[t-1] >= 0

    def dfs(v, f):
        if v == t-1:
            return f
        for i in range(it_ptr[v], len(g[v])):
            e = g[v][i]
            if e.cap and level[v] < level[e.to]:
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
        it_ptr = [0]*N
        while True:
            f = dfs(s-1, INF)
            if not f:
                break
            flow += f

    if flow != d:
        print("NO")
        return

    # retrieve flows on original edges
    res = [0]*m
    for u in range(N):
        for e in g[u]:
            if e.idx != -1:
                used = e.orig_cap - e.cap
                res[e.idx] = used

    print("YES")
    print(' '.join(map(str, res)))

if __name__ == "__main__":
    solve()