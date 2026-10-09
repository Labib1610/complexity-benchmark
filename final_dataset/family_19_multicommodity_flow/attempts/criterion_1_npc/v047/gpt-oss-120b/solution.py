import sys
sys.setrecursionlimit(1 << 25)

class Dinic:
    __slots__ = ('n', 'g', 'level', 'it')
    def __init__(self, n):
        self.n = n
        self.g = [[] for _ in range(n)]

    def add_edge(self, fr, to, cap):
        # forward edge stores (to, rev, cap)
        fwd = [to, len(self.g[to]), cap]
        rev = [fr, len(self.g[fr]), 0]
        self.g[fr].append(fwd)
        self.g[to].append(rev)
        return fwd  # reference to forward edge to read flow later

    def bfs(self, s, t):
        level = [-1] * self.n
        q = [s]
        level[s] = 0
        for v in q:
            for to, rev, cap in self.g[v]:
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
            to, rev, cap = self.g[v][i]
            if cap and self.level[v] + 1 == self.level[to]:
                ret = self.dfs(to, t, min(f, cap))
                if ret:
                    self.g[v][i][2] -= ret
                    self.g[to][rev][2] += ret
                    return ret
        return 0

    def max_flow(self, s, t, limit):
        flow = 0
        INF = 10**18
        while flow < limit and self.bfs(s, t):
            self.it = [0] * self.n
            while flow < limit:
                f = self.dfs(s, t, limit - flow)
                if not f:
                    break
                flow += f
        return flow


def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it))
    orders = []
    for _ in range(k):
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        d = int(next(it))
        orders.append((s, t, d))
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        c = int(next(it))
        edges.append((u, v, c))

    rem = [c for _, _, c in edges]          # remaining capacity per edge
    ans = [[0] * m for _ in range(k)]

    for idx, (src, dst, need) in enumerate(orders):
        dinic = Dinic(n)
        edge_refs = []   # reference to forward edge for each original edge
        for j, (u, v, _) in enumerate(edges):
            ref = dinic.add_edge(u, v, rem[j])
            edge_refs.append(ref)

        got = dinic.max_flow(src, dst, need)
        if got < need:
            print("NO")
            return

        # read how much flow each original edge carried
        for j, ref in enumerate(edge_refs):
            used = ref[2]  # remaining capacity after flow, original - used
            flow_on_edge = rem[j] - used
            ans[idx][j] = flow_on_edge
            rem[j] -= flow_on_edge   # update residual capacity

    # all orders satisfied
    out_lines = ["YES"]
    for i in range(k):
        out_lines.append(" ".join(str(x) for x in ans[i]))
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()