import sys
sys.setrecursionlimit(1 << 25)

class Edge:
    __slots__ = ('to', 'rev', 'cap', 'idx')
    def __init__(self, to, rev, cap, idx):
        self.to = to          # target vertex
        self.rev = rev        # index of reverse edge in graph[to]
        self.cap = cap        # residual capacity
        self.idx = idx        # original edge index or -1 for auxiliary edges

class Dinic:
    def __init__(self, n):
        self.n = n
        self.g = [[] for _ in range(n)]

    def add_edge(self, fr, to, cap, idx=-1):
        fwd = Edge(to, len(self.g[to]), cap, idx)
        rev = Edge(fr, len(self.g[fr]), 0, -1)
        self.g[fr].append(fwd)
        self.g[to].append(rev)
        return fwd  # reference to forward edge

    def bfs(self, s, t, level):
        from collections import deque
        level[:] = [-1] * self.n
        q = deque([s])
        level[s] = 0
        while q:
            v = q.popleft()
            for e in self.g[v]:
                if e.cap and level[e.to] < 0:
                    level[e.to] = level[v] + 1
                    q.append(e.to)
        return level[t] >= 0

    def dfs(self, v, t, f, level, it):
        if v == t:
            return f
        for i in range(it[v], len(self.g[v])):
            it[v] = i
            e = self.g[v][i]
            if e.cap and level[v] + 1 == level[e.to]:
                ret = self.dfs(e.to, t, min(f, e.cap), level, it)
                if ret:
                    e.cap -= ret
                    self.g[e.to][e.rev].cap += ret
                    return ret
        return 0

    def max_flow(self, s, t, limit=None):
        flow = 0
        level = [0] * self.n
        INF = 10**18
        while self.bfs(s, t, level):
            it = [0] * self.n
            while True:
                f = self.dfs(s, t, INF if limit is None else limit - flow,
                             level, it)
                if not f:
                    break
                flow += f
                if limit is not None and flow >= limit:
                    return flow
        return flow

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); _ = int(next(it))  # third number is always 1
    s = int(next(it)) - 1
    t = int(next(it)) - 1
    d = int(next(it))

    dinic = Dinic(n)
    orig_edges = [None] * m          # store forward Edge reference
    caps = [0] * m

    for idx in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        cap = int(next(it))
        caps[idx] = cap
        e = dinic.add_edge(u, v, cap, idx)
        orig_edges[idx] = e

    f = dinic.max_flow(s, t)
    if f < d:
        print("NO")
        return

    # Reduce excess flow if needed
    excess = f - d
    if excess:
        dinic.max_flow(t, s, excess)

    # Retrieve flows
    res = []
    for idx, e in enumerate(orig_edges):
        used = caps[idx] - e.cap
        res.append(str(used))

    print("YES")
    print(' '.join(res))

if __name__ == "__main__":
    solve()