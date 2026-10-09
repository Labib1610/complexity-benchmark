import sys
sys.setrecursionlimit(1 << 25)

class Edge:
    __slots__ = ('to', 'rev', 'cap', 'orig_cap', 'idx')
    def __init__(self, to, rev, cap, idx=-1):
        self.to = to          # target vertex
        self.rev = rev        # index of reverse edge in graph[to]
        self.cap = cap        # residual capacity
        self.orig_cap = cap   # original capacity (only for forward edges)
        self.idx = idx        # input index for original edges, -1 otherwise

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); _ = next(it)  # third number unused
    s = int(next(it)) - 1
    t = int(next(it)) - 1
    d = int(next(it))

    graph = [[] for _ in range(n)]
    edge_refs = [None] * m          # will store forward Edge objects

    def add_edge(fr, to, cap, idx=-1):
        fwd = Edge(to, len(graph[to]), cap, idx)
        rev = Edge(fr, len(graph[fr]), 0)
        graph[fr].append(fwd)
        graph[to].append(rev)
        return fwd

    for i in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        c = int(next(it))
        e = add_edge(u, v, c, i)
        edge_refs[i] = e

    # Dinic
    INF = 10**18
    level = [0] * n
    it_ptr = [0] * n

    from collections import deque

    def bfs():
        for i in range(n):
            level[i] = -1
        q = deque()
        level[s] = 0
        q.append(s)
        while q:
            v = q.popleft()
            for e in graph[v]:
                if e.cap > 0 and level[e.to] < 0:
                    level[e.to] = level[v] + 1
                    q.append(e.to)
        return level[t] >= 0

    def dfs(v, upTo):
        if v == t:
            return upTo
        for i in range(it_ptr[v], len(graph[v])):
            it_ptr[v] = i
            e = graph[v][i]
            if e.cap > 0 and level[e.to] == level[v] + 1:
                pushed = dfs(e.to, min(upTo, e.cap))
                if pushed:
                    e.cap -= pushed
                    graph[e.to][e.rev].cap += pushed
                    return pushed
        return 0

    flow = 0
    limit = d
    while flow < limit and bfs():
        it_ptr = [0] * n
        while flow < limit:
            pushed = dfs(s, limit - flow)
            if not pushed:
                break
            flow += pushed

    if flow < d:
        print("NO")
        return

    # retrieve flows on original edges
    res = [0] * m
    for i, e in enumerate(edge_refs):
        used = e.orig_cap - e.cap
        res[i] = used

    print("YES")
    print(' '.join(map(str, res)))

if __name__ == "__main__":
    solve()