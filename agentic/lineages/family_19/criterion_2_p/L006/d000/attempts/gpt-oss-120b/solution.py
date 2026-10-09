import sys
from collections import deque

def solve() -> None:
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    idx = 0
    # first line may contain 2 or 3 numbers, we take first two as n,m
    n = data[idx]; idx += 1
    m = data[idx]; idx += 1
    # if there is a third number on the first line, skip it
    if len(data) > idx + 2*m + 3 and (len(data) - idx) % 3 == 1:
        # heuristic: if remaining numbers after reading n,m are not fitting the pattern,
        # assume there is an extra number and skip it
        idx += 1
    s = data[idx]; t = data[idx+1]; d = data[idx+2]; idx += 3

    edges_input = []
    for _ in range(m):
        u, v, cap = data[idx], data[idx+1], data[idx+2]
        idx += 3
        edges_input.append((u-1, v-1, cap))

    # Dinic
    N = n
    g = [[] for _ in range(N)]

    class Edge:
        __slots__ = ('to','rev','cap','orig')
        def __init__(self, to, rev, cap, orig=False):
            self.to = to
            self.rev = rev
            self.cap = cap
            self.orig = orig

    edge_refs = []  # reference to the forward edge for each original edge in input order

    def add_edge(fr, to, cap):
        fwd = Edge(to, len(g[to]), cap, True)
        rev = Edge(fr, len(g[fr]), 0)
        g[fr].append(fwd)
        g[to].append(rev)
        return fwd

    for u, v, cap in edges_input:
        fwd = add_edge(u, v, cap)
        edge_refs.append(fwd)

    level = [0]*N
    it = [0]*N

    def bfs():
        for i in range(N):
            level[i] = -1
        q = deque()
        level[s-1] = 0
        q.append(s-1)
        while q:
            v = q.popleft()
            for e in g[v]:
                if e.cap > 0 and level[e.to] < 0:
                    level[e.to] = level[v] + 1
                    q.append(e.to)
        return level[t-1] >= 0

    def dfs(v, upTo):
        if v == t-1:
            return upTo
        for i in range(it[v], len(g[v])):
            e = g[v][i]
            if e.cap > 0 and level[v] < level[e.to]:
                dflow = dfs(e.to, min(upTo, e.cap))
                if dflow:
                    e.cap -= dflow
                    g[e.to][e.rev].cap += dflow
                    return dflow
            it[v] += 1
        return 0

    flow = 0
    INF = 10**18
    while bfs():
        it = [0]*N
        while True:
            f = dfs(s-1, INF)
            if not f:
                break
            flow += f
            if flow >= d:
                break
        if flow >= d:
            break

    if flow < d:
        print("NO")
        return

    # we have at least d flow, but we may have sent more; need exactly d.
    # Since capacities are integers, we can simply scale down by sending additional
    # flow of (flow - d) back from t to s using residual graph.
    excess = flow - d
    if excess > 0:
        # add reverse edge from t to s with infinite capacity to push back excess
        # Instead, run a DFS from t to s on residual graph to reduce flow.
        # We'll treat it as a max flow from t to s with limit excess.
        s_rev = t-1
        t_rev = s-1
        level = [0]*N
        it = [0]*N

        def bfs_rev():
            for i in range(N):
                level[i] = -1
            q = deque()
            level[s_rev] = 0
            q.append(s_rev)
            while q:
                v = q.popleft()
                for e in g[v]:
                    if e.cap > 0 and level[e.to] < 0:
                        level[e.to] = level[v] + 1
                        q.append(e.to)
            return level[t_rev] >= 0

        def dfs_rev(v, upTo):
            if v == t_rev:
                return upTo
            for i in range(it[v], len(g[v])):
                e = g[v][i]
                if e.cap > 0 and level[v] < level[e.to]:
                    dflow = dfs_rev(e.to, min(upTo, e.cap))
                    if dflow:
                        e.cap -= dflow
                        g[e.to][e.rev].cap += dflow
                        return dflow
                it[v] += 1
            return 0

        while excess > 0 and bfs_rev():
            it = [0]*N
            while excess > 0:
                f = dfs_rev(s_rev, excess)
                if not f:
                    break
                excess -= f

    # now extract flows on original edges
    result = []
    for e in edge_refs:
        used = e.cap  # remaining capacity
        flow_on_edge = e.orig_cap - used if hasattr(e, 'orig_cap') else None
    # we stored original capacity indirectly; recompute:
    for (u,v,cap), e in zip(edges_input, edge_refs):
        flow_on_edge = cap - e.cap
        result.append(str(flow_on_edge))

    print("YES")
    print(" ".join(result))

if __name__ == "__main__":
    solve()