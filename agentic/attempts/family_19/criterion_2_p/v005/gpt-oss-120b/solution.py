import sys
sys.setrecursionlimit(1 << 25)

class Edge:
    __slots__ = ('to', 'rev', 'cap')
    def __init__(self, to, rev, cap):
        self.to = to          # target vertex
        self.rev = rev        # index of reverse edge in graph[to]
        self.cap = cap        # residual capacity

def add_edge(g, fr, to, cap):
    fwd = Edge(to, len(g[to]), cap)
    rev = Edge(fr, len(g[fr]), 0)
    g[fr].append(fwd)
    g[to].append(rev)
    return fwd  # reference to forward edge

def dinic(g, s, t, limit):
    n = len(g)
    level = [0] * n
    it = [0] * n

    from collections import deque

    def bfs():
        for i in range(n):
            level[i] = -1
        q = deque([s])
        level[s] = 0
        while q:
            v = q.popleft()
            for e in g[v]:
                if e.cap and level[e.to] < 0:
                    level[e.to] = level[v] + 1
                    q.append(e.to)
        return level[t] >= 0

    def dfs(v, f):
        if v == t:
            return f
        for i in range(it[v], len(g[v])):
            e = g[v][i]
            if e.cap and level[v] < level[e.to]:
                ret = dfs(e.to, f if f < e.cap else e.cap)
                if ret:
                    e.cap -= ret
                    g[e.to][e.rev].cap += ret
                    return ret
            it[v] += 1
        return 0

    flow = 0
    INF = 10**18
    while flow < limit and bfs():
        it = [0] * n
        while flow < limit:
            pushed = dfs(s, limit - flow)
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
    _ = next(it)  # the third number on line 1 is unused in statement (maybe version)
    s = int(next(it)) - 1
    t = int(next(it)) - 1
    d = int(next(it))

    g = [[] for _ in range(n)]
    orig_edges = []          # (forward_edge_ref, capacity)
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        cap = int(next(it))
        fwd = add_edge(g, u, v, cap)
        orig_edges.append((fwd, cap))

    maxflow = dinic(g, s, t, d)
    if maxflow < d:
        sys.stdout.write("NO")
        return

    # retrieve flows
    flows = []
    for fwd, cap in orig_edges:
        used = cap - fwd.cap
        flows.append(str(used))
    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(flows))

if __name__ == "__main__":
    solve()