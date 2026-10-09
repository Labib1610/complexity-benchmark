import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it))
    commodities = []
    for _ in range(k):
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        d = int(next(it))
        commodities.append((s, t, d))
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        cap = int(next(it))
        edges.append((u, v, cap))

    # Dinic for single-commodity max flow
    class Dinic:
        def __init__(self, N):
            self.N = N
            self.adj = [[] for _ in range(N)]

        def add_edge(self, u, v, c):
            self.adj[u].append([v, c, len(self.adj[v])])
            self.adj[v].append([u, 0, len(self.adj[u]) - 1])

        def bfs(self, s, t, level):
            q = [s]
            level[s] = 0
            for u in q:
                for v, cap, rev in self.adj[u]:
                    if cap and level[v] < 0:
                        level[v] = level[u] + 1
                        q.append(v)
            return level[t] >= 0

        def dfs(self, u, t, f, level, it):
            if u == t:
                return f
            for i in range(it[u], len(self.adj[u])):
                it[u] = i
                v, cap, rev = self.adj[u][i]
                if cap and level[v] == level[u] + 1:
                    ret = self.dfs(v, t, min(f, cap), level, it)
                    if ret:
                        self.adj[u][i][1] -= ret
                        self.adj[v][rev][1] += ret
                        return ret
            return 0

        def max_flow(self, s, t):
            flow = 0
            N = self.N
            level = [-1] * N
            while self.bfs(s, t, level):
                it = [0] * N
                while True:
                    f = self.dfs(s, t, 10**18, level, it)
                    if not f:
                        break
                    flow += f
                level = [-1] * N
            return flow

    # Pre‑compute adjacency list for the base graph
    base_adj = [[] for _ in range(n)]
    for idx, (u, v, cap) in enumerate(edges):
        base_adj[u].append((v, cap, idx))

    # Recursive search
    assignment = [[0] * m for _ in range(k)]
    caps_left = [cap for _, _, cap in edges]

    # quick feasibility check using total capacities
    def possible():
        for ci, (s, t, d) in enumerate(commodities):
            din = Dinic(n)
            for (u, v, _), cap in zip(edges, caps_left):
                if cap:
                    din.add_edge(u, v, cap)
            if din.max_flow(s, t) < d:
                return False
        return True

    if not possible():
        print("NO")
        return

    solved = False

    def dfs_edge(eid):
        nonlocal solved
        if solved:
            return
        if eid == m:
            # all edges assigned, verify each commodity can meet demand exactly
            for ci, (s, t, d) in enumerate(commodities):
                din = Dinic(n)
                for (u, v, _), cap in zip(edges, caps_left):
                    if cap:
                        din.add_edge(u, v, cap)
                if din.max_flow(s, t) != d:
                    return
            # success
            print("YES")
            for row in assignment:
                print(' '.join(map(str, row)))
            solved = True
            return

        u, v, _ = edges[eid]
        max_cap = caps_left[eid]
        # generate all distributions of up to max_cap among k commodities
        # simple recursion over commodities
        dist = [0] * k
        def distribute(idx, remaining):
            nonlocal solved
            if solved:
                return
            if idx == k:
                # apply distribution
                for ci in range(k):
                    assignment[ci][eid] = dist[ci]
                caps_left[eid] = max_cap - sum(dist)
                # prune: each commodity must still be able to send remaining demand
                # compute remaining demand per commodity
                for ci, (s, t, d) in enumerate(commodities):
                    sent = sum(assignment[ci][j] for j, (uu, vv, _) in enumerate(edges) if uu == s)
                    # not exact, we just rely on possible() later
                if possible():
                    dfs_edge(eid + 1)
                # backtrack
                caps_left[eid] = max_cap
                for ci in range(k):
                    assignment[ci][eid] = 0
                return
            # try all possible amounts for commodity idx on this edge
            for val in range(remaining + 1):
                dist[idx] = val
                distribute(idx + 1, remaining - val)

        distribute(0, max_cap)

    dfs_edge(0)
    if not solved:
        print("NO")

if __name__ == "__main__":
    solve()