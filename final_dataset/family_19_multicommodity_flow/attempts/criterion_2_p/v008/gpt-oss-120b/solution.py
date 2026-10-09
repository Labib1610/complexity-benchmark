import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); _ = int(next(it))  # the third number is always 1, ignore
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
        __slots__ = ('to', 'rev', 'cap', 'orig')
        def __init__(self, to, rev, cap):
            self.to = to
            self.rev = rev
            self.cap = cap
            self.orig = cap

    G = [[] for _ in range(n)]
    edge_refs = []  # forward edge reference for each original edge

    def add_edge(fr, to, cap):
        fwd = Edge(to, len(G[to]), cap)
        rev = Edge(fr, len(G[fr]), 0)
        G[fr].append(fwd)
        G[to].append(rev)
        return fwd

    for u, v, cap in edges_input:
        e = add_edge(u, v, cap)
        edge_refs.append(e)

    level = [0]*n
    it_ptr = [0]*n

    from collections import deque
    def bfs():
        for i in range(n):
            level[i] = -1
        q = deque([s])
        level[s] = 0
        while q:
            v = q.popleft()
            for e in G[v]:
                if e.cap > 0 and level[e.to] < 0:
                    level[e.to] = level[v] + 1
                    q.append(e.to)
        return level[t] >= 0

    def dfs(v, f):
        if v == t:
            return f
        for i in range(it_ptr[v], len(G[v])):
            it_ptr[v] = i
            e = G[v][i]
            if e.cap > 0 and level[v] < level[e.to]:
                ret = dfs(e.to, min(f, e.cap))
                if ret:
                    e.cap -= ret
                    G[e.to][e.rev].cap += ret
                    return ret
        return 0

    flow = 0
    INF = 10**18
    while bfs():
        it_ptr = [0]*n
        while True:
            f = dfs(s, INF)
            if not f:
                break
            flow += f
            if flow >= d:  # early stop if we already have enough
                break
        if flow >= d:
            break

    if flow < d:
        print("NO")
        return

    # we have at least d flow, but maybe more; we need exactly d on each edge.
    # Since we may have sent more than d, we can reduce excess by pushing back along any augmenting path.
    # Simpler: run another maxflow from s to t on residual graph with capacity = flow - d to cancel excess.
    excess = flow - d
    if excess > 0:
        # add a super sink to pull back excess flow
        # Instead, we can just run a flow from t to s of amount excess on the residual graph.
        # Implement a DFS augmenting from t to s.
        # Reuse Dinic with swapped source/sink.
        s2, t2 = t, s
        # adjust global variables for second run
        def bfs2():
            for i in range(n):
                level[i] = -1
            q = deque([s2])
            level[s2] = 0
            while q:
                v = q.popleft()
                for e in G[v]:
                    if e.cap > 0 and level[e.to] < 0:
                        level[e.to] = level[v] + 1
                        q.append(e.to)
            return level[t2] >= 0

        def dfs2(v, f):
            if v == t2:
                return f
            for i in range(it_ptr[v], len(G[v])):
                it_ptr[v] = i
                e = G[v][i]
                if e.cap > 0 and level[v] < level[e.to]:
                    ret = dfs2(e.to, min(f, e.cap))
                    if ret:
                        e.cap -= ret
                        G[e.to][e.rev].cap += ret
                        return ret
            return 0

        while excess > 0 and bfs2():
            it_ptr = [0]*n
            while excess > 0:
                f = dfs2(s2, excess)
                if not f:
                    break
                excess -= f

    # Now total flow from s to t is exactly d.
    result = []
    for e in edge_refs:
        used = e.orig - e.cap
        result.append(str(used))
    print("YES")
    print(' '.join(result))

if __name__ == "__main__":
    solve()