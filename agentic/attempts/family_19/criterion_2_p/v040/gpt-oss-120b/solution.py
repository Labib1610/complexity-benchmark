import sys
sys.setrecursionlimit(1 << 25)

class Dinic:
    __slots__ = ('n', 'g', 'level', 'it')
    def __init__(self, n):
        self.n = n
        self.g = [[] for _ in range(n)]

    def add_edge(self, fr, to, cap):
        fwd = [to, cap, None]          # to, cap, rev will be set later
        rev = [fr, 0, fwd]
        fwd[2] = rev
        self.g[fr].append(fwd)
        self.g[to].append(rev)
        return fwd                     # return forward edge object

    def bfs(self, s, t):
        level = [-1] * self.n
        q = [s]
        level[s] = 0
        for v in q:
            for to, cap, rev in self.g[v]:
                if cap and level[to] == -1:
                    level[to] = level[v] + 1
                    q.append(to)
        self.level = level
        return level[t] != -1

    def dfs(self, v, t, f):
        if v == t:
            return f
        for i in range(self.it[v], len(self.g[v])):
            self.it[v] = i
            to, cap, rev = self.g[v][i]
            if cap and self.level[v] + 1 == self.level[to]:
                ret = self.dfs(to, t, f if f < cap else cap)
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
    n = int(next(it))
    m = int(next(it))
    _ = next(it)          # the problem statement had a stray '1', ignore
    s = int(next(it)) - 1
    t = int(next(it)) - 1
    d = int(next(it))

    dinic = Dinic(n)
    edge_refs = []          # forward edge objects in input order
    caps = []               # original capacities for later output

    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        c = int(next(it))
        fwd = dinic.add_edge(u, v, c)
        edge_refs.append(fwd)
        caps.append(c)

    flow = dinic.max_flow(s, t, d)

    if flow != d:
        print("NO")
        return

    # compute flow on each original edge
    ans = []
    for fwd, cap in zip(edge_refs, caps):
        used = cap - fwd[1]   # original capacity minus remaining capacity
        ans.append(str(used))

    print("YES")
    print(" ".join(ans))


if __name__ == "__main__":
    solve()