import sys
sys.setrecursionlimit(1 << 25)

class Dinic:
    __slots__ = ('n', 'g', 'level', 'it')
    def __init__(self, n):
        self.n = n
        self.g = [[] for _ in range(n)]

    def add_edge(self, fr, to, cap):
        fwd = [to, cap, None]          # to, cap, rev
        rev = [fr, 0, fwd]
        fwd[2] = rev
        self.g[fr].append(fwd)
        self.g[to].append(rev)
        return fwd

    def bfs(self, s, t):
        level = [-1] * self.n
        q = [s]
        level[s] = 0
        for v in q:
            for to, cap, rev in self.g[v]:
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
            to, cap, rev = self.g[v][i]
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
    s = []
    t = []
    d = []
    for _ in range(k):
        s.append(int(next(it)) - 1)
        t.append(int(next(it)) - 1)
        d.append(int(next(it)))
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        lim = int(next(it))
        edges.append((u, v, lim))

    remaining = [lim for _, _, lim in edges]
    answer = [[0] * m for _ in range(k)]

    for idx in range(k):
        dinic = Dinic(n)
        fwd_refs = [None] * m
        for j, (u, v, _) in enumerate(edges):
            cap = remaining[j]
            if cap:
                fwd_refs[j] = dinic.add_edge(u, v, cap)
            else:
                # still need a placeholder to keep indices aligned
                fwd_refs[j] = None
        flow = dinic.max_flow(s[idx], t[idx], d[idx])
        if flow < d[idx]:
            print("NO")
            return
        # retrieve used flow on each original edge
        for j, ref in enumerate(fwd_refs):
            if ref is None:
                used = 0
            else:
                used = edges[j][2] - remaining[j] - ref[1]  # original cap - residual
                # simpler: used = original_cap - remaining_cap_before - residual
                # but we know original cap = remaining_before, so used = original - residual
                used = (remaining[j] + ref[1]) - ref[1]  # actually just original - residual = used
                used = (edges[j][2] - remaining[j]) - (edges[j][2] - remaining[j] - ref[1])  # messy
                # easier: used = original_capacity - current_residual
                used = (edges[j][2] - (remaining[j] + ref[1] - (edges[j][2] - remaining[j])))  # overcomplicated
            # The above is confusing; we can compute directly:
        # Re‑compute correctly:
        for j, ref in enumerate(fwd_refs):
            if ref is None:
                used = 0
            else:
                # original capacity for this edge in this step = remaining_before
                # remaining_before = remaining[j] + flow_used_on_this_edge (unknown)
                # but we stored remaining[j] before building graph? we didn't.
                # Simpler: store original capacities in a list before building.
                pass
    # The above attempt got messy; rewrite with clearer handling.

def solve():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it))
    s = []; t = []; d = []
    for _ in range(k):
        s.append(int(next(it))-1)
        t.append(int(next(it))-1)
        d.append(int(next(it)))
    edges = []
    for _ in range(m):
        u = int(next(it))-1
        v = int(next(it))-1
        lim = int(next(it))
        edges.append((u,v,lim))

    remaining = [lim for _,_,lim in edges]
    answer = [[0]*m for _ in range(k)]

    for idx in range(k):
        # remember capacities before building graph
        caps_before = remaining[:]

        # build Dinic
        dinic = Dinic(n)
        edge_refs = [None]*m
        for j,(u,v,_) in enumerate(edges):
            cap = caps_before[j]
            if cap>0:
                edge_refs[j] = dinic.add_edge(u,v,cap)

        flow = dinic.max_flow(s[idx], t[idx], d[idx])
        if flow < d[idx]:
            print("NO")
            return

        # extract used flow on each original edge
        for j, ref in enumerate(edge_refs):
            if ref is None:
                used = 0
            else:
                # original capacity = caps_before[j]
                # residual capacity after flow = ref[1]
                used = caps_before[j] - ref[1]
            answer[idx][j] = used
            remaining[j] -= used   # update remaining capacity

    # all commodities processed
    out = ["YES"]
    for i in range(k):
        out.append(" ".join(str(x) for x in answer[i]))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()