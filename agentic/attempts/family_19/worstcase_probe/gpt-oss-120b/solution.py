import sys
from collections import deque

sys.setrecursionlimit(1 << 25)

class Dinic:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]

    def add_edge(self, u, v, cap):
        self.adj[u].append([v, cap, len(self.adj[v])])
        self.adj[v].append([u, 0,   len(self.adj[u]) - 1])

    def bfs(self, s, t, level):
        q = deque([s])
        level[:] = [-1] * self.n
        level[s] = 0
        while q:
            v = q.popleft()
            for to, cap, rev in self.adj[v]:
                if cap and level[to] == -1:
                    level[to] = level[v] + 1
                    q.append(to)
        return level[t] != -1

    def dfs(self, v, t, f, level, it):
        if v == t:
            return f
        for i in range(it[v], len(self.adj[v])):
            it[v] = i
            to, cap, rev = self.adj[v][i]
            if cap and level[v] + 1 == level[to]:
                ret = self.dfs(to, t, min(f, cap), level, it)
                if ret:
                    self.adj[v][i][1] -= ret
                    self.adj[to][rev][1] += ret
                    return ret
        return 0

    def max_flow(self, s, t, limit=None):
        flow = 0
        level = [0] * self.n
        INF = 10 ** 18
        while self.bfs(s, t, level):
            it = [0] * self.n
            while True:
                pushed = self.dfs(s, t, INF if limit is None else limit - flow,
                                  level, it)
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
    n = int(next(it)); m = int(next(it)); k = int(next(it))
    s = []; t = []; d = []
    for _ in range(k):
        s.append(int(next(it)) - 1)
        t.append(int(next(it)) - 1)
        d.append(int(next(it)))
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        cap = int(next(it))
        edges.append((u, v, cap))

    # compute node supplies
    b = [0] * n
    for i in range(k):
        b[s[i]] += d[i]
        b[t[i]] -= d[i]

    S = n
    T = n + 1
    dinic = Dinic(n + 2)
    total_supply = 0
    for v in range(n):
        if b[v] > 0:
            dinic.add_edge(S, v, b[v])
            total_supply += b[v]
        elif b[v] < 0:
            dinic.add_edge(v, T, -b[v])
    for idx, (u, v, cap) in enumerate(edges):
        dinic.add_edge(u, v, cap)

    flow = dinic.max_flow(S, T)
    if flow != total_supply:
        print("NO")
        return

    # retrieve total flow on original edges
    total_on_edge = [0] * m
    # edges were added after the S/T edges, in the same order
    # we need to locate them in dinic.adj
    # We'll store a reference while adding
    edge_refs = []
    dinic2 = Dinic(n + 2)  # rebuild to keep references clean
    # add S/T again
    for v in range(n):
        if b[v] > 0:
            dinic2.add_edge(S, v, b[v])
        elif b[v] < 0:
            dinic2.add_edge(v, T, -b[v])
    for idx, (u, v, cap) in enumerate(edges):
        # store position
        pos = len(dinic2.adj[u])
        dinic2.add_edge(u, v, cap)
        edge_refs.append((u, pos))  # forward edge index in adj[u]

    dinic2.max_flow(S, T)  # now flows are stored

    for idx, (u, pos) in enumerate(edge_refs):
        to, cap, rev = dinic2.adj[u][pos]
        used = cap  # original capacity minus remaining capacity
        total_on_edge[idx] = used

    # per‑commodity decomposition
    answer = [[0] * m for _ in range(k)]

    # residual capacities equal to current total_on_edge
    for i in range(k):
        # build Dinic on residual of total_on_edge
        dinc = Dinic(n)
        for idx, (u, v, _) in enumerate(edges):
            if total_on_edge[idx]:
                dinc.add_edge(u, v, total_on_edge[idx])
        need = d[i]
        got = dinc.max_flow(s[i], t[i], need)
        if got != need:
            # should never happen
            print("NO")
            return
        # read how much was sent on each original edge
        for idx, (u, pos) in enumerate(edge_refs):
            # forward edge in dinc.adj[u] has same order as we added
            to, cap, rev = dinc.adj[u][pos]
            used = dinc.adj[to][rev][1]  # flow that went forward = reverse edge capacity
            if used:
                answer[i][idx] = used
                total_on_edge[idx] -= used

    # output
    out = ["YES"]
    for i in range(k):
        out.append(" ".join(str(x) for x in answer[i]))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()