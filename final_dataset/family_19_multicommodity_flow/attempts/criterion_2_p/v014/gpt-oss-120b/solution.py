import sys
sys.setrecursionlimit(1 << 25)

class Dinic:
    __slots__ = ('n', 'g', 'level', 'it')
    def __init__(self, n):
        self.n = n
        self.g = [[] for _ in range(n)]

    def add_edge(self, fr, to, cap, idx=-1):
        # forward edge
        fwd = [to, cap, None, idx]   # to, cap, rev, idx
        # backward edge
        rev = [fr, 0, fwd, -1]
        fwd[2] = rev
        self.g[fr].append(fwd)
        self.g[to].append(rev)

    def bfs(self, s, t):
        level = [-1] * self.n
        q = [s]
        level[s] = 0
        for v in q:
            for to, cap, rev, _ in self.g[v]:
                if cap and level[to] < 0:
                    level[to] = level[v] + 1
                    q.append(to)
        self.level = level
        return level[t] >= 0

    def dfs(self, v, t, f):
        if v == t:
            return f
        for i in range(self.it[v], len(self.g[v])):
            self.it[v] = i
            to, cap, rev, _ = self.g[v][i]
            if cap and self.level[v] + 1 == self.level[to]:
                ret = self.dfs(to, t, min(f, cap))
                if ret:
                    self.g[v][i][1] -= ret
                    rev[1] += ret
                    return ret
        return 0

    def max_flow(self, s, t, limit):
        flow = 0
        INF = 10**18
        while flow < limit and self.bfs(s, t):
            self.it = [0] * self.n
            while flow < limit:
                pushed = self.dfs(s, t, limit - flow)
                if not pushed:
                    break
                flow += pushed
        return flow

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); _ = next(it)  # the third number is always 1
    s = int(next(it)) - 1
    t = int(next(it)) - 1
    d = int(next(it))

    dinic = Dinic(n)
    # store reference to the forward edge for each original edge
    edge_refs = [None] * m
    caps = [0] * m

    for idx in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        cap = int(next(it))
        caps[idx] = cap
        # add edge and keep reference to forward edge list object
        dinic.add_edge(u, v, cap, idx)
        edge_refs[idx] = dinic.g[u][-1]   # the forward edge just added

    flow = dinic.max_flow(s, t, d)
    if flow < d:
        print("NO")
        return

    # retrieve flows
    res = []
    for idx in range(m):
        fwd = edge_refs[idx]
        used = caps[idx] - fwd[1]   # original capacity minus remaining capacity
        res.append(str(used))

    print("YES")
    print(' '.join(res))

if __name__ == "__main__":
    solve()