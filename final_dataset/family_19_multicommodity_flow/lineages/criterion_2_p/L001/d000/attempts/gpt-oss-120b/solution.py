import sys
sys.setrecursionlimit(1 << 25)

class Edge:
    __slots__ = ('to', 'rev', 'cap', 'orig')
    def __init__(self, to, rev, cap):
        self.to = to
        self.rev = rev
        self.cap = cap
        self.orig = cap

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); _ = int(next(it))  # third value unused (always 1)
    s = int(next(it)) - 1
    t = int(next(it)) - 1
    d = int(next(it))
    g = [[] for _ in range(n)]
    edge_refs = []  # (forward_edge, backward_edge) for each input edge

    def add_edge(u, v, c):
        fwd = Edge(v, len(g[v]), c)
        rev = Edge(u, len(g[u]), 0)
        g[u].append(fwd)
        g[v].append(rev)
        return fwd, rev

    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        c = int(next(it))
        fwd, rev = add_edge(u, v, c)
        edge_refs.append(fwd)

    level = [0] * n
    it_ptr = [0] * n

    from collections import deque

    def bfs():
        for i in range(n):
            level[i] = -1
        q = deque([s])
        level[s] = 0
        while q:
            v = q.popleft()
            for e in g[v]:
                if e.cap and level[e.to] == -1:
                    level[e.to] = level[v] + 1
                    q.append(e.to)
        return level[t] != -1

    def dfs(v, f):
        if v == t:
            return f
        for i in range(it_ptr[v], len(g[v])):
            it_ptr[v] = i
            e = g[v][i]
            if e.cap and level[e.to] == level[v] + 1:
                ret = dfs(e.to, min(f, e.cap))
                if ret:
                    e.cap -= ret
                    g[e.to][e.rev].cap += ret
                    return ret
        return 0

    flow = 0
    INF = 10**18
    while flow < d and bfs():
        it_ptr = [0] * n
        while flow < d:
            pushed = dfs(s, d - flow)
            if not pushed:
                break
            flow += pushed

    if flow != d:
        print("NO")
        return

    print("YES")
    res = []
    for e in edge_refs:
        used = e.orig - e.cap
        res.append(str(used))
    print(' '.join(res))

if __name__ == "__main__":
    solve()