import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); _ = int(next(it))  # the trailing 1 is ignored
    s = int(next(it)) - 1
    t = int(next(it)) - 1
    d = int(next(it))
    edges_input = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        cap = int(next(it))
        edges_input.append((u, v, cap))

    # Dinic
    class Edge:
        __slots__ = ('to', 'rev', 'cap', 'orig_cap', 'idx')
        def __init__(self, to, rev, cap, orig_cap=-1, idx=-1):
            self.to = to
            self.rev = rev
            self.cap = cap
            self.orig_cap = orig_cap
            self.idx = idx

    g = [[] for _ in range(n)]

    def add_edge(fr, to, cap, idx=-1):
        fwd = Edge(to, len(g[to]), cap, cap, idx)
        rev = Edge(fr, len(g[fr]), 0, 0, -1)
        g[fr].append(fwd)
        g[to].append(rev)

    for i, (u, v, cap) in enumerate(edges_input):
        add_edge(u, v, cap, i)

    level = [0]*n
    it_ptr = [0]*n

    from collections import deque

    def bfs():
        for i in range(n):
            level[i] = -1
        q = deque()
        level[s] = 0
        q.append(s)
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
        for i in range(it_ptr[v], len(g[v])):
            e = g[v][i]
            if e.cap and level[v] < level[e.to]:
                ret = dfs(e.to, min(f, e.cap))
                if ret:
                    e.cap -= ret
                    g[e.to][e.rev].cap += ret
                    return ret
            it_ptr[v] += 1
        return 0

    flow = 0
    INF = 10**18
    while flow < d and bfs():
        it_ptr = [0]*n
        while flow < d:
            pushed = dfs(s, d - flow)
            if not pushed:
                break
            flow += pushed

    if flow < d:
        print("NO")
        return

    # retrieve flows for original edges
    res = [0]*m
    for u in range(n):
        for e in g[u]:
            if e.idx != -1:
                used = e.orig_cap - e.cap
                res[e.idx] = used

    print("YES")
    print(' '.join(map(str, res)))

if __name__ == "__main__":
    solve()