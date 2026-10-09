import sys
sys.setrecursionlimit(1 << 25)

class Dinic:
    __slots__ = ('n', 'g', 'level', 'it')
    def __init__(self, n):
        self.n = n
        self.g = [[] for _ in range(n)]

    def add_edge(self, fr, to, cap, idx=-1):
        # forward edge stores idx of original edge or -1
        f = [to, cap, None, idx]
        b = [fr, 0, f, -1]
        f[2] = b
        self.g[fr].append(f)
        self.g[to].append(b)

    def bfs(self, s, t):
        level = [-1]*self.n
        q = [s]
        level[s]=0
        for v in q:
            for to, cap, rev, _ in self.g[v]:
                if cap and level[to]==-1:
                    level[to]=level[v]+1
                    q.append(to)
        self.level=level
        return level[t]!=-1

    def dfs(self, v, t, f):
        if v==t:
            return f
        for i in range(self.it[v], len(self.g[v])):
            self.it[v]=i
            to, cap, rev, _ = self.g[v][i]
            if cap and self.level[v]+1==self.level[to]:
                ret=self.dfs(to, t, min(f, cap))
                if ret:
                    self.g[v][i][1]-=ret
                    rev[1]+=ret
                    return ret
        return 0

    def max_flow(self, s, t):
        flow=0
        INF=10**18
        while self.bfs(s,t):
            self.it=[0]*self.n
            while True:
                f=self.dfs(s,t,INF)
                if not f: break
                flow+=f
        return flow

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); K = int(next(it))
    s = int(next(it))-1; t = int(next(it))-1; d = int(next(it))
    edges = []
    dinic = Dinic(n)
    for idx in range(m):
        u = int(next(it))-1; v = int(next(it))-1; c = int(next(it))
        edges.append((u, v, c))
        dinic.add_edge(u, v, c, idx)
    flow = dinic.max_flow(s, t)
    if flow < d:
        print("NO")
        return
    # we have at least d flow; we may need to reduce to exactly d.
    # Perform a second pass: send extra flow (flow-d) back from t to s using residual graph.
    excess = flow - d
    if excess:
        # add reverse infinite edge to allow canceling flow
        dinic.add_edge(t, s, excess)  # capacity excess enough
        dinic.max_flow(t, s)  # cancel excess
    # retrieve flows on original edges
    res = [0]*m
    for u in range(n):
        for to, cap, rev, idx in dinic.g[u]:
            if idx!=-1:
                # original forward edge: flow = original capacity - remaining cap
                orig_cap = edges[idx][2]
                used = orig_cap - cap
                res[idx] = used
    print("YES")
    print(' '.join(map(str, res)))

if __name__ == "__main__":
    solve()