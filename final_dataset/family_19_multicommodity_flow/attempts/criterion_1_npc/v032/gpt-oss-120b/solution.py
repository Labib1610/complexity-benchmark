import sys
sys.setrecursionlimit(1 << 25)

class Dinic:
    __slots__ = ('n', 'g', 'level', 'it')
    def __init__(self, n):
        self.n = n
        self.g = [[] for _ in range(n)]

    def add_edge(self, fr, to, cap, idx=-1):
        # idx is the original edge index, -1 for auxiliary edges
        f = [to, cap, None, idx]
        b = [fr, 0, f, -1]
        f[2] = b
        self.g[fr].append(f)
        self.g[to].append(b)

    def bfs(self, s, t):
        level = [-1]*self.n
        q = [s]
        level[s] = 0
        for v in q:
            for to, cap, rev, _ in self.g[v]:
                if cap and level[to] < 0:
                    level[to] = level[v]+1
                    q.append(to)
        self.level = level
        return level[t] >= 0

    def dfs(self, v, t, f):
        if v == t:
            return f
        for i in range(self.it[v], len(self.g[v])):
            self.it[v] = i
            to, cap, rev, _ = self.g[v][i]
            if cap and self.level[v]+1 == self.level[to]:
                ret = self.dfs(to, t, min(f, cap))
                if ret:
                    self.g[v][i][1] -= ret
                    rev[1] += ret
                    return ret
        return 0

    def max_flow(self, s, t):
        flow = 0
        INF = 10**18
        while self.bfs(s, t):
            self.it = [0]*self.n
            while True:
                f = self.dfs(s, t, INF)
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
    cats = []
    supply = [0]*n
    demand = [0]*n
    for _ in range(k):
        s = int(next(it))-1
        t = int(next(it))-1
        d = int(next(it))
        cats.append((s, t, d))
        supply[s] += d
        demand[t] += d
    edges = []
    for _ in range(m):
        u = int(next(it))-1
        v = int(next(it))-1
        cap = int(next(it))
        edges.append((u, v, cap))

    # ---------- Phase 1 ----------
    S = n
    T = n+1
    dinic = Dinic(n+2)
    for idx, (u, v, cap) in enumerate(edges):
        dinic.add_edge(u, v, cap, idx)
    total_demand = 0
    for v in range(n):
        if supply[v]:
            dinic.add_edge(S, v, supply[v])
        if demand[v]:
            dinic.add_edge(v, T, demand[v])
            total_demand += demand[v]
    flow = dinic.max_flow(S, T)
    if flow != total_demand:
        print("NO")
        return

    # retrieve total used capacity on each original edge
    used_total = [0]*m
    for u in range(n):
        for to, cap, rev, idx in dinic.g[u]:
            if idx >= 0:  # original edge
                used = rev[1]  # flow sent forward = reverse edge capacity
                used_total[idx] = used

    # ---------- Phase 2 ----------
    remaining = [edges[i][2] for i in range(m)]
    answer = [[0]*m for _ in range(k)]

    for ci, (src, dst, need) in enumerate(cats):
        din = Dinic(n)
        for idx, (u, v, _) in enumerate(edges):
            if remaining[idx]:
                din.add_edge(u, v, remaining[idx], idx)
        got = din.max_flow(src, dst)
        if got != need:
            print("NO")
            return
        # extract flows
        for u in range(n):
            for to, cap, rev, idx in din.g[u]:
                if idx >= 0:
                    f = rev[1]  # flow sent forward
                    if f:
                        answer[ci][idx] = f
                        remaining[idx] -= f

    # ---------- Output ----------
    print("YES")
    out_lines = []
    for i in range(k):
        out_lines.append(' '.join(str(x) for x in answer[i]))
    sys.stdout.write('\n'.join(out_lines))

if __name__ == "__main__":
    solve()