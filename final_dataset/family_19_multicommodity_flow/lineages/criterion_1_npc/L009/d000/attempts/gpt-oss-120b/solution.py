import sys
sys.setrecursionlimit(1 << 25)

class Dinic:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]

    def add_edge(self, u, v, cap):
        # forward edge
        self.adj[u].append([v, cap, len(self.adj[v])])
        # backward edge
        self.adj[v].append([u, 0, len(self.adj[u]) - 1])

    def bfs_level(self, s, t):
        level = [-1] * self.n
        q = [s]
        level[s] = 0
        for u in q:
            for v, cap, rev in self.adj[u]:
                if cap and level[v] == -1:
                    level[v] = level[u] + 1
                    q.append(v)
        self.level = level
        return level[t] != -1

    def dfs_flow(self, u, t, f, it):
        if u == t:
            return f
        for i in range(it[u], len(self.adj[u])):
            it[u] = i
            v, cap, rev = self.adj[u][i]
            if cap and self.level[v] == self.level[u] + 1:
                ret = self.dfs_flow(v, t, min(f, cap), it)
                if ret:
                    self.adj[u][i][1] -= ret
                    self.adj[v][rev][1] += ret
                    return ret
        return 0

    def max_flow(self, s, t):
        flow = 0
        INF = 10 ** 18
        while self.bfs_level(s, t):
            it = [0] * self.n
            while True:
                pushed = self.dfs_flow(s, t, INF, it)
                if not pushed:
                    break
                flow += pushed
        return flow

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it))
    s = [0]*k; t = [0]*k; d = [0]*k
    for i in range(k):
        s[i] = int(next(it))-1
        t[i] = int(next(it))-1
        d[i] = int(next(it))
    edges = []
    for _ in range(m):
        u = int(next(it))-1
        v = int(next(it))-1
        cap = int(next(it))
        edges.append((u, v, cap))

    S = n
    T = n+1
    dinic = Dinic(n+2)

    # store index of edge in original list for later reference
    edge_idx = []          # (u, position in adj[u]) for each original edge
    for idx, (u, v, cap) in enumerate(edges):
        pos = len(dinic.adj[u])
        dinic.add_edge(u, v, cap)
        edge_idx.append((u, pos))

    for i in range(k):
        dinic.add_edge(S, s[i], d[i])
        dinic.add_edge(t[i], T, d[i])

    total_d = sum(d)
    flow = dinic.max_flow(S, T)
    if flow != total_d:
        print("NO")
        return

    # retrieve flow on original edges
    flow_on_edge = [0]*m
    for idx, (u, pos) in enumerate(edge_idx):
        v, cap, rev = dinic.adj[u][pos]
        # original capacity - remaining capacity = used flow
        used = edges[idx][2] - cap
        flow_on_edge[idx] = used

    # build adjacency for decomposition (only original edges)
    adj = [[] for _ in range(n)]
    for idx, (u, v, _) in enumerate(edges):
        if flow_on_edge[idx]:
            adj[u].append([v, flow_on_edge[idx], idx])   # store idx for answer

    # answer matrix
    ans = [[0]*m for _ in range(k)]

    # decomposition per commodity
    sys.setrecursionlimit(1 << 25)
    def dfs(u, need, target, path):
        if u == target:
            return need
        for e in adj[u]:
            v, cap, eid = e
            if cap == 0:
                continue
            pushed = dfs(v, min(need, cap), target, path)
            if pushed:
                e[1] -= pushed          # decrease remaining flow
                path.append((eid, pushed))
                return pushed
        return 0

    for i in range(k):
        need = d[i]
        while need:
            path = []
            pushed = dfs(s[i], need, t[i], path)
            if not pushed:
                # should not happen
                print("NO")
                return
            need -= pushed
            for eid, amt in path:
                ans[i][eid] += amt

    # output
    out = ["YES"]
    for i in range(k):
        out.append(" ".join(str(x) for x in ans[i]))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()