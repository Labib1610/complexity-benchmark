import sys
from collections import deque

def solve() -> None:
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    it = iter(data)
    n = next(it); m = next(it); _ = next(it)  # the third value is always 1 per statement
    s = next(it); t = next(it); d = next(it)
    edges_input = []
    for _ in range(m):
        u = next(it); v = next(it); c = next(it)
        edges_input.append((u-1, v-1, c))  # zero‑based

    # Dinic
    N = n
    g = [[] for _ in range(N)]

    class Edge:
        __slots__ = ('to','rev','cap','orig_cap','idx')
        def __init__(self, to, rev, cap, idx=-1):
            self.to = to
            self.rev = rev
            self.cap = cap
            self.orig_cap = cap
            self.idx = idx  # original edge index for output, -1 for added edges

    def add_edge(fr, to, cap, idx=-1):
        fwd = Edge(to, len(g[to]), cap, idx)
        rev = Edge(fr, len(g[fr]), 0)
        g[fr].append(fwd)
        g[to].append(rev)

    for i, (u, v, c) in enumerate(edges_input):
        add_edge(u, v, c, i)

    level = [0]*N
    it_ptr = [0]*N

    def bfs():
        for i in range(N):
            level[i] = -1
        q = deque([s-1])
        level[s-1] = 0
        while q:
            v = q.popleft()
            for e in g[v]:
                if e.cap and level[e.to] < 0:
                    level[e.to] = level[v] + 1
                    q.append(e.to)
        return level[t-1] >= 0

    def dfs(v, f):
        if v == t-1:
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
    while bfs():
        it_ptr = [0]*N
        while True:
            f = dfs(s-1, INF)
            if not f:
                break
            flow += f
            if flow >= d:  # we can stop early once we have enough
                break
        if flow >= d:
            break

    if flow < d:
        print("NO")
        return

    # we have sent at least d flow; if more, we need to reduce excess.
    # Perform a second flow to cancel extra flow (flow - d) from s to t.
    excess = flow - d
    if excess:
        # add reverse edge with infinite capacity to allow sending back excess
        # simpler: run another maxflow from t to s on the residual graph to push back excess.
        # We'll treat t as source, s as sink.
        s_src = t-1
        t_sink = s-1
        # reuse bfs/dfs with new source/sink
        def bfs2():
            for i in range(N):
                level[i] = -1
            q = deque([s_src])
            level[s_src] = 0
            while q:
                v = q.popleft()
                for e in g[v]:
                    if e.cap and level[e.to] < 0:
                        level[e.to] = level[v] + 1
                        q.append(e.to)
            return level[t_sink] >= 0

        def dfs2(v, f):
            if v == t_sink:
                return f
            for i in range(it_ptr[v], len(g[v])):
                e = g[v][i]
                if e.cap and level[v] < level[e.to]:
                    ret = dfs2(e.to, min(f, e.cap))
                    if ret:
                        e.cap -= ret
                        g[e.to][e.rev].cap += ret
                        return ret
                it_ptr[v] += 1
            return 0

        while excess and bfs2():
            it_ptr = [0]*N
            while excess:
                f = dfs2(s_src, excess)
                if not f:
                    break
                excess -= f

    # collect flows on original edges
    ans = [0]*m
    for u in range(N):
        for e in g[u]:
            if e.idx != -1:
                used = e.orig_cap - e.cap
                ans[e.idx] = used

    print("YES")
    print(' '.join(map(str, ans)))

if __name__ == "__main__":
    solve()