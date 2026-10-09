import sys
from collections import deque

class Dinic:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]

    def add_edge(self, u, v, cap):
        self.adj[u].append([v, cap, len(self.adj[v])])
        self.adj[v].append([u, 0, len(self.adj[u]) - 1])

    def bfs(self, s, t):
        self.level = [-1] * self.n
        q = deque([s])
        self.level[s] = 0
        while q:
            v = q.popleft()
            for to, cap, rev in self.adj[v]:
                if cap > 0 and self.level[to] < 0:
                    self.level[to] = self.level[v] + 1
                    q.append(to)
        return self.level[t] >= 0

    def dfs(self, v, t, f):
        if v == t:
            return f
        for i in range(self.it[v], len(self.adj[v])):
            self.it[v] = i
            to, cap, rev = self.adj[v][i]
            if cap > 0 and self.level[v] + 1 == self.level[to]:
                ret = self.dfs(to, t, min(f, cap))
                if ret > 0:
                    self.adj[v][i][1] -= ret
                    self.adj[to][rev][1] += ret
                    return ret
        return 0

    def max_flow(self, s, t):
        flow = 0
        INF = 10**18
        while self.bfs(s, t):
            self.it = [0] * self.n
            while True:
                f = self.dfs(s, t, INF)
                if not f:
                    break
                flow += f
        return flow


def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))

    orders = []
    for _ in range(k):
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        d = int(next(it))
        orders.append((s, t, d))

    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        c = int(next(it))
        edges.append((u, v, c))

    # Build expanded network
    # Node indices:
    # (commodity i, center u) -> i*n + u
    # edge node for j-th original edge -> k*n + j
    # super source -> k*n + m
    # super sink -> k*n + m + 1
    N = k * n + m + 2
    S = k * n + m
    T = k * n + m + 1

    dinic = Dinic(N)

    total_demand = 0
    for idx, (s, t, d) in enumerate(orders):
        total_demand += d
        dinic.add_edge(S, idx * n + s, d)
        dinic.add_edge(idx * n + t, T, d)

    # For each original edge (u,v,c):
    # For each commodity i: add (i,u)->edge_node_j->(i,v)
    for j, (u, v, c) in enumerate(edges):
        edge_node = k * n + j
        for i in range(k):
            from_node = i * n + u
            to_node = i * n + v
            dinic.add_edge(from_node, edge_node, c)
            dinic.add_edge(edge_node, to_node, c)

    flow = dinic.max_flow(S, T)
    if flow != total_demand:
        print("NO")
        return

    # Extract flows per commodity per edge
    res = [[0] * m for _ in range(k)]
    for j in range(m):
        edge_node = k * n + j
        for i in range(k):
            from_node = i * n + edges[j][0]
            # find reverse edge from edge_node to from_node to get flow
            for to, cap, rev in dinic.adj[edge_node]:
                if to == from_node:
                    # flow sent = capacity of reverse edge
                    flow_sent = dinic.adj[from_node][rev][1]
                    res[i][j] = flow_sent
                    break

    print("YES")
    for row in res:
        print(" ".join(map(str, row)))


if __name__ == "__main__":
    solve()