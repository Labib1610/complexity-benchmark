import sys
sys.setrecursionlimit(1 << 25)

class Dinic:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]

    def add_edge(self, u, v, c, idx=-1):
        # forward edge
        f = [v, c, None, idx]   # to, cap, rev, idx
        # backward edge
        b = [u, 0, f, -1]
        f[2] = b
        self.adj[u].append(f)
        self.adj[v].append(b)

    def bfs(self, s, t, level):
        from collections import deque
        q = deque([s])
        level[:] = [-1]*self.n
        level[s] = 0
        while q:
            u = q.popleft()
            for v, cap, rev, _ in self.adj[u]:
                if cap and level[v] == -1:
                    level[v] = level[u] + 1
                    q.append(v)
        return level[t] != -1

    def dfs(self, u, t, f, level, it):
        if u == t:
            return f
        for i in range(it[u], len(self.adj[u])):
            it[u] = i
            v, cap, rev, _ = self.adj[u][i]
            if cap and level[v] == level[u] + 1:
                ret = self.dfs(v, t, min(f, cap), level, it)
                if ret:
                    self.adj[u][i][1] -= ret
                    rev[1] += ret
                    return ret
        return 0

    def max_flow(self, s, t, limit):
        flow = 0
        level = [0]*self.n
        while flow < limit and self.bfs(s, t, level):
            it = [0]*self.n
            while flow < limit:
                pushed = self.dfs(s, t, limit - flow, level, it)
                if not pushed:
                    break
                flow += pushed
        return flow

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); _ = int(next(it))  # third value unused (type count)
    s = int(next(it)) - 1
    t = int(next(it)) - 1
    d = int(next(it))
    edges = []
    caps = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        cap = int(next(it))
        edges.append((u, v))
        caps.append(cap)

    dinic = Dinic(n)
    for idx, (u, v) in enumerate(edges):
        dinic.add_edge(u, v, caps[idx], idx)

    flow = dinic.max_flow(s, t, d)
    if flow < d:
        print("NO")
        return

    # retrieve flows on original edges
    res = [0]*m
    for u in range(n):
        for v, cap, rev, idx in dinic.adj[u]:
            if idx >= 0:  # original edge
                used = caps[idx] - cap
                res[idx] = used

    print("YES")
    print(' '.join(map(str, res)))

if __name__ == "__main__":
    solve()