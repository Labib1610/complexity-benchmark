import sys
sys.setrecursionlimit(1 << 25)

class Edge:
    __slots__ = ('to', 'rev', 'cap', 'orig')
    def __init__(self, to, rev, cap, orig):
        self.to = to          # destination vertex
        self.rev = rev        # index of reverse edge in graph[to]
        self.cap = cap        # residual capacity
        self.orig = orig      # original capacity (0 for reverse edges)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); _ = next(it)  # commodity count ignored
    s = int(next(it)) - 1
    t = int(next(it)) - 1
    d = int(next(it))

    graph = [[] for _ in range(n)]
    orig_edges = [None] * m

    def add_edge(u, v, cap, idx):
        fwd = Edge(v, len(graph[v]), cap, cap)
        rev = Edge(u, len(graph[u]), 0, 0)
        graph[u].append(fwd)
        graph[v].append(rev)
        if idx is not None:
            orig_edges[idx] = fwd

    for i in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        cap = int(next(it))
        add_edge(u, v, cap, i)

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
                if e.cap and level[e.to] == -1:
                    level[e.to] = level[v] + 1
                    q.append(e.to)
        return level[t] != -1

    def dfs(v, f):
        if v == t:
            return f
        for i in range(it_ptr[v], len(graph[v])):
            it_ptr[v] = i
            e = graph[v][i]
            if e.cap and level[e.to] == level[v] + 1:
                ret = dfs(e.to, f if f < e.cap else e.cap)
                if ret:
                    e.cap -= ret
                    graph[e.to][e.rev].cap += ret
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

    if flow < d:
        print("NO")
        return

    # retrieve flows on original edges
    res = []
    for e in orig_edges:
        used = e.orig - e.cap
        res.append(str(used))
    print("YES")
    print(' '.join(res))

if __name__ == "__main__":
    solve()