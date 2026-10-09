import sys
sys.setrecursionlimit(1 << 25)

class Dinic:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]

    def add_edge(self, u, v, cap, idx=-1):
        # idx stores original variable index for later retrieval
        self.adj[u].append([v, cap, len(self.adj[v]), idx])
        self.adj[v].append([u, 0, len(self.adj[u]) - 1, -1])

    def bfs(self, s, t, level):
        from collections import deque
        q = deque([s])
        level[:] = [-1] * self.n
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
                    self.adj[v][rev][1] += ret
                    return ret
        return 0

    def max_flow(self, s, t):
        flow = 0
        level = [0] * self.n
        INF = 10**18
        while self.bfs(s, t, level):
            it = [0] * self.n
            while True:
                f = self.dfs(s, t, INF, level, it)
                if not f:
                    break
                flow += f
        return flow

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); _ = int(next(it))  # third value unused (always 1)
    s = int(next(it)) - 1; t = int(next(it)) - 1; d = int(next(it))
    edges = []
    caps = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        c = int(next(it))
        edges.append((u, v))
        caps.append(c)

    # demands E_i
    E = [0] * n
    E[s] = -d
    E[t] = d

    # Build flow network
    N = n + 2
    SS = n
    TT = n + 1
    dinic = Dinic(N)

    INF = 10**18
    for idx, ((u, v), cap) in enumerate(zip(edges, caps)):
        dinic.add_edge(u, v, cap, idx)  # store idx for later

    total_pos = 0
    for i in range(n):
        if E[i] > 0:
            dinic.add_edge(SS, i, E[i])
            total_pos += E[i]
        elif E[i] < 0:
            dinic.add_edge(i, TT, -E[i])

    flow = dinic.max_flow(SS, TT)
    if flow != total_pos:
        print("NO")
        return

    # retrieve flows on original edges
    ans = [0] * m
    for u in range(n):
        for v, cap, rev, idx in dinic.adj[u]:
            if idx >= 0:  # original edge
                # original capacity - remaining capacity = flow used
                used = caps[idx] - cap
                ans[idx] = used

    print("YES")
    print(' '.join(map(str, ans)))

if __name__ == "__main__":
    solve()