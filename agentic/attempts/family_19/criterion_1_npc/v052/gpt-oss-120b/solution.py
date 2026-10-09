import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it))
    orders = []
    for i in range(k):
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        d = int(next(it))
        orders.append((s, t, d, i))
    edges = []
    for j in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        cap = int(next(it))
        edges.append((u, v, cap))

    # sort orders for better pruning (larger demand first)
    orders.sort(key=lambda x: -x[2])

    # answer matrix
    ans = [[0]*m for _ in range(k)]

    # Dinic implementation
    class Dinic:
        __slots__ = ('n','g','level','it')
        def __init__(self, n):
            self.n = n
            self.g = [[] for _ in range(n)]

        def add_edge(self, fr, to, cap, idx):
            fwd = [to, cap, None, idx]   # to, cap, rev, orig_idx
            rev = [fr, 0, fwd, -1]
            fwd[2] = rev
            self.g[fr].append(fwd)
            self.g[to].append(rev)

        def bfs(self, s, t):
            level = [-1]*self.n
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

    def try_assign(idx, caps):
        if idx == len(orders):
            return True
        s, t, d, orig_i = orders[idx]
        din = Dinic(n)
        for j, (u, v, _) in enumerate(edges):
            if caps[j]:
                din.add_edge(u, v, caps[j], j)
        flow = din.max_flow(s, t)
        if flow < d:
            return False
        # retrieve flow per original edge (could be more than needed, but we need exactly d)
        # Since max flow may send more than d, we need to extract a flow of exactly d.
        # We'll run a second Dinic limited to d by adding a super source/sink trick:
        # Instead, we redo with capacity d limit by adding edge from s to t with extra capacity.
        # Simpler: run Dinic again on a copy with edge caps and stop after d units.
        # We'll implement a flow that stops when d reached.
        # Rebuild with same caps and run augmentations manually.
        din = Dinic(n)
        edge_refs = []
        for j, (u, v, _) in enumerate(edges):
            e = [u, v, caps[j], j]  # placeholder
            # we'll store forward edge reference
            forward = [v, caps[j], None, j]
            rev = [u, 0, forward, -1]
            forward[2] = rev
            din.g[u].append(forward)
            din.g[v].append(rev)
            edge_refs.append(forward)
        # augment until d
        need = d
        while need:
            if not din.bfs(s, t):
                return False
            din.it = [0]*n
            while need:
                f = din.dfs(s, t, need)
                if not f:
                    break
                need -= f
        used = [0]*m
        for j, fwd in enumerate(edge_refs):
            used[j] = caps[j] - fwd[1]  # original cap minus residual
        # store
        ans[orig_i] = used
        new_caps = [caps[j] - used[j] for j in range(m)]
        return try_assign(idx+1, new_caps)

    init_caps = [c for _,_,c in edges]
    if try_assign(0, init_caps):
        out = ["YES"]
        # reorder answers to original order
        ordered = [None]*k
        for s,t,d,i in orders:
            ordered[i] = ans[i]
        for row in ordered:
            out.append(" ".join(map(str, row)))
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()