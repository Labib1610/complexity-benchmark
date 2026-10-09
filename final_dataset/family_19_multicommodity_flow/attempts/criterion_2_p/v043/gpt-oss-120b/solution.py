import sys
sys.setrecursionlimit(1 << 25)

class Edge:
    __slots__ = ('to', 'rev', 'cap', 'orig_cap', 'idx')
    def __init__(self, to, rev, cap, idx):
        self.to = to
        self.rev = rev
        self.cap = cap
        self.orig_cap = cap
        self.idx = idx  # -1 for reverse or added edges

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); _ = int(next(it))  # the third number is unused (always 1)
    s = int(next(it)) - 1
    t = int(next(it)) - 1
    d = int(next(it))
    graph = [[] for _ in range(n)]
    edge_refs = [None] * m  # reference to forward edge for each original edge

    def add_edge(fr, to, cap, idx):
        fwd = Edge(to, len(graph[to]), cap, idx)
        rev = Edge(fr, len(graph[fr]), 0, -1)
        graph[fr].append(fwd)
        graph[to].append(rev)

    for i in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        cap = int(next(it))
        add_edge(u, v, cap, i)
        edge_refs[i] = graph[u][-1]  # the forward edge just added

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
            for e in graph[v]:
                if e.cap and level[e.to] < 0:
                    level[e.to] = level[v] + 1
                    q.append(e.to)
        return level[t] >= 0

    def dfs(v, f):
        if v == t:
            return f
        for i in range(it_ptr[v], len(graph[v])):
            e = graph[v][i]
            if e.cap and level[v] < level[e.to]:
                ret = dfs(e.to, min(f, e.cap))
                if ret:
                    e.cap -= ret
                    graph[e.to][e.rev].cap += ret
                    return ret
            it_ptr[v] += 1
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

    # construct answer
    ans = [0] * m
    for i, e in enumerate(edge_refs):
        used = e.orig_cap - e.cap
        ans[i] = used
    print("YES")
    print(' '.join(map(str, ans)))

if __name__ == "__main__":
    solve()