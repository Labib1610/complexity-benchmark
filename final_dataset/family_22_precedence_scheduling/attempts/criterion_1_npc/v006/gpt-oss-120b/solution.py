import sys
sys.setrecursionlimit(1 << 25)

# ---------- Dinic ----------
class Dinic:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]

    def add_edge(self, u, v, cap):
        self.adj[u].append([v, cap, len(self.adj[v])])
        self.adj[v].append([u, 0,   len(self.adj[u]) - 1])

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
                    self.adj[v][rev][1] += ret
                    return ret
        return 0

    def max_flow(self, s, t):
        flow = 0
        INF = 10 ** 18
        while self.bfs_level(s, t):
            self.it = [0] * self.n
            while True:
                f = self.dfs(s, t, INF)
                if not f:
                    break
                flow += f
        return flow

# ---------- main ----------
def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    M = int(next(it))
    T = int(next(it))
    m = int(next(it))

    g = [[] for _ in range(n)]
    rg = [[] for _ in range(n)]
    indeg = [0] * n
    for _ in range(m):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        g[a].append(b)
        rg[b].append(a)
        indeg[b] += 1

    # topological order
    from collections import deque
    q = deque([i for i in range(n) if indeg[i] == 0])
    topo = []
    while q:
        v = q.popleft()
        topo.append(v)
        for to in g[v]:
            indeg[to] -= 1
            if indeg[to] == 0:
                q.append(to)
    if len(topo) != n:
        print("NO")
        return

    # earliest
    earliest = [1] * n
    for v in topo:
        for to in g[v]:
            if earliest[to] < earliest[v] + 1:
                earliest[to] = earliest[v] + 1

    # longest path to sink (in edges)
    longest = [0] * n
    for v in reversed(topo):
        best = 0
        for to in g[v]:
            if longest[to] + 1 > best:
                best = longest[to] + 1
        longest[v] = best
    latest = [T - longest[i] for i in range(n)]

    for i in range(n):
        if earliest[i] > latest[i]:
            print("NO")
            return

    # build flow network
    SRC = 0
    JOB0 = 1
    HOUR0 = JOB0 + n
    SNK = HOUR0 + T
    dinic = Dinic(SNK + 1)

    for i in range(n):
        dinic.add_edge(SRC, JOB0 + i, 1)
        for h in range(earliest[i], latest[i] + 1):
            dinic.add_edge(JOB0 + i, HOUR0 + (h - 1), 1)

    for h in range(T):
        dinic.add_edge(HOUR0 + h, SNK, M)

    flow = dinic.max_flow(SRC, SNK)
    if flow < n:
        print("NO")
        return

    # extract schedule
    ans = [0] * n
    for i in range(n):
        for v, cap, rev in dinic.adj[JOB0 + i]:
            if HOUR0 <= v < HOUR0 + T and cap == 0:  # used edge
                ans[i] = v - HOUR0 + 1
                break

    print("YES")
    print(' '.join(map(str, ans)))

if __name__ == "__main__":
    solve()