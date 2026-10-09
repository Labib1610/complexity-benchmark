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
    n = int(next(it)); m = int(next(it)); _ = next(it)  # the 1 is irrelevant
    s = int(next(it)) - 1
    t = int(next(it)) - 1
    d = int(next(it))

    dinic = Dinic(n)
    edge_refs = []          # store forward edge reference for each original edge
    caps0 = []              # original capacities

    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        cap = int(next(it))
        caps0.append(cap)
        # store reference to forward edge list element
        dinic.add_edge(u, v, cap, len(edge_refs))
        edge_refs.append((u, len(dinic.g[u]) - 1))   # (from, index in adjacency)

    maxf = dinic.max_flow(s, t)
    if maxf < d:
        print("NO")
        return

    # Reduce flow from f to d by sending back (maxf - d) from t to s
    need = maxf - d
    if need > 0:
        dinic.max_flow(t, s, need)

    # Extract flows
    ans = [0] * m
    for idx, (u, pos) in enumerate(edge_refs):
        edge = dinic.g[u][pos]
        flow = caps0[idx] - edge[1]   # original cap - remaining cap
        ans[idx] = flow

    print("YES")
    print(' '.join(map(str, ans)))

if __name__ == "__main__":
    solve()