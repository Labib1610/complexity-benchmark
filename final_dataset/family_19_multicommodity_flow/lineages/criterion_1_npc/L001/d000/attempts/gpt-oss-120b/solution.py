import sys
sys.setrecursionlimit(1 << 25)

INF = 10 ** 18

class Dinic:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]

    def add_edge(self, u, v, cap):
        fwd = [v, cap, None]          # to, cap, rev
        rev = [u, 0, fwd]
        fwd[2] = rev
        self.adj[u].append(fwd)
        self.adj[v].append(rev)
        return fwd                     # return forward edge for later inspection

    def bfs_level(self, s, t):
        level = [-1] * self.n
        q = [s]
        level[s] = 0
        for u in q:
            for v, cap, _ in self.adj[u]:
                if cap and level[v] == -1:
                    level[v] = level[u] + 1
                    q.append(v)
        self.level = level
        return level[t] != -1

    def dfs(self, u, t, f):
        if u == t:
            return f
        for i in range(self.it[u], len(self.adj[u])):
            self.it[u] = i
            v, cap, rev = self.adj[u][i]
            if cap and self.level[v] == self.level[u] + 1:
                ret = self.dfs(v, t, min(f, cap))
                if ret:
                    self.adj[u][i][1] -= ret
                    rev[1] += ret
                    return ret
        return 0

    def max_flow(self, s, t):
        flow = 0
        while self.bfs_level(s, t):
            self.it = [0] * self.n
            while True:
                pushed = self.dfs(s, t, INF)
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
    k = int(next(it))

    s = []
    t = []
    d = []
    for _ in range(k):
        s.append(int(next(it)) - 1)
        t.append(int(next(it)) - 1)
        d.append(int(next(it)))

    u = []
    v = []
    cap = []
    for _ in range(m):
        u.append(int(next(it)) - 1)
        v.append(int(next(it)) - 1)
        cap.append(int(next(it)))

    # node ids
    def copy_id(vv, ii):
        return ii * n + vv

    base = k * n
    e_in = [base + 2 * j for j in range(m)]
    e_out = [base + 2 * j + 1 for j in range(m)]
    S = base + 2 * m
    T = S + 1
    N = T + 1

    dinic = Dinic(N)

    # source / sink edges
    total_need = 0
    for i in range(k):
        dinic.add_edge(S, copy_id(s[i], i), d[i])
        dinic.add_edge(copy_id(t[i], i), T, d[i])
        total_need += d[i]

    # remember edges for answer
    edge_ref = [[None] * m for _ in range(k)]

    for j in range(m):
        # capacity node
        dinic.add_edge(e_in[j], e_out[j], cap[j])
        for i in range(k):
            # copy(u,i) -> e_in
            fwd = dinic.add_edge(copy_id(u[j], i), e_in[j], INF)
            edge_ref[i][j] = fwd
            # e_out -> copy(v,i)
            dinic.add_edge(e_out[j], copy_id(v[j], i), INF)

    flow = dinic.max_flow(S, T)
    if flow != total_need:
        print("NO")
        return

    print("YES")
    out_lines = []
    for i in range(k):
        line = []
        for j in range(m):
            fwd = edge_ref[i][j]
            used = fwd[1] ^ INF  # not correct, need original cap - residual
            # we stored original cap as INF, so flow = INF - residual
            used = INF - fwd[1]
            line.append(str(used))
        out_lines.append(' '.join(line))
    sys.stdout.write('\n'.join(out_lines))

if __name__ == "__main__":
    solve()