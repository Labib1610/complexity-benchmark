import sys
sys.setrecursionlimit(1 << 25)

class Dinic:
    __slots__ = ('n', 'g', 'level', 'it')
    def __init__(self, n):
        self.n = n
        self.g = [[] for _ in range(n)]

    def add_edge(self, fr, to, cap):
        # forward edge stores: to, rev index, capacity, flow
        fwd = [to, len(self.g[to]), cap, 0]
        rev = [fr, len(self.g[fr]), 0, 0]
        self.g[fr].append(fwd)
        self.g[to].append(rev)
        return fwd  # reference to forward edge for later flow reading

    def bfs(self, s, t):
        level = [-1] * self.n
        q = [s]
        level[s] = 0
        for v in q:
            for to, rev, cap, flow in self.g[v]:
                if cap - flow > 0 and level[to] < 0:
                    level[to] = level[v] + 1
                    q.append(to)
        self.level = level
        return level[t] >= 0

    def dfs(self, v, t, f):
        if v == t:
            return f
        for i in range(self.it[v], len(self.g[v])):
            self.it[v] = i
            to, rev, cap, flow = self.g[v][i]
            if cap - flow > 0 and self.level[v] + 1 == self.level[to]:
                ret = self.dfs(to, t, min(f, cap - flow))
                if ret:
                    # augment
                    self.g[v][i][3] += ret
                    self.g[to][rev][3] -= ret
                    return ret
        return 0

    def max_flow(self, s, t, limit=None):
        flow = 0
        INF = 10**18
        while self.bfs(s, t):
            self.it = [0] * self.n
            while True:
                pushed = self.dfs(s, t, INF if limit is None else limit - flow)
                if not pushed:
                    break
                flow += pushed
                if limit is not None and flow >= limit:
                    return flow
        return flow

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); _ = next(it)  # third number ignored
    s = int(next(it)) - 1
    t = int(next(it)) - 1
    d = int(next(it))
    dinic = Dinic(n)
    edge_refs = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        cap = int(next(it))
        ref = dinic.add_edge(u, v, cap)
        edge_refs.append(ref)

    flow = dinic.max_flow(s, t, limit=d)
    if flow < d:
        print("NO")
        return
    print("YES")
    out = [str(e[3]) for e in edge_refs]   # e[3] is the flow on forward edge
    print(' '.join(out))

if __name__ == "__main__":
    solve()