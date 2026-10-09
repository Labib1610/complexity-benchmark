import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); _ = int(next(it))  # asset types ignored
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
        def __init__(self, to, rev, cap, orig=False):
            self.to = to
            self.rev = rev
            self.cap = cap
            self.orig = orig  # marks if this edge corresponds to original input edge

    G = [[] for _ in range(n)]
    # store reference to original edges to retrieve flow later
    orig_refs = [None] * m

    def add_edge(fr, to, cap, idx=None):
        fwd = Edge(to, len(G[to]), cap, idx is not None)
        rev = Edge(fr, len(G[fr]), 0, False)
        G[fr].append(fwd)
        G[to].append(rev)
        if idx is not None:
            orig_refs[idx] = (fr, len(G[fr]) - 1)  # store location of forward edge

    for i, (u, v, cap) in enumerate(edges_input):
        add_edge(u, v, cap, i)

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
            for e in G[v]:
                if e.cap > 0 and level[e.to] < 0:
                    level[e.to] = level[v] + 1
                    q.append(e.to)
        return level[t] >= 0

    def dfs(v, f):
        if v == t:
            return f
        for i in range(it_ptr[v], len(G[v])):
            e = G[v][i]
            if e.cap > 0 and level[v] < level[e.to]:
                ret = dfs(e.to, min(f, e.cap))
                if ret:
                    e.cap -= ret
                    G[e.to][e.rev].cap += ret
                    return ret
            it_ptr[v] += 1
        return 0

    flow = 0
    INF = 10**18
    while bfs():
        it_ptr = [0] * n
        while True:
            f = dfs(s, INF)
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

    # we may have sent more than d; need to reduce excess if any.
    # Since capacities are integers, we can simply run a second flow to cancel (flow-d) from s to t.
    excess = flow - d
    if excess > 0:
        # add a reverse demand: try to send excess from t to s using residual graph.
        # We'll treat t as source and s as sink.
        s2, t2 = t, s
        # reuse bfs/dfs with new source/target
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
                e = G[v][i]
                if e.cap > 0 and level[v] < level[e.to]:
                    ret = dfs2(e.to, min(f, e.cap))
                    if ret:
                        e.cap -= ret
                        G[e.to][e.rev].cap += ret
                        return ret
                it_ptr[v] += 1
            return 0

        while excess > 0 and bfs2():
            it_ptr = [0] * n
            while excess > 0:
                f = dfs2(s2, excess)
                if not f:
                    break
                excess -= f
        # after this, total flow from original s to t is exactly d

    # retrieve flows on original edges
    result = []
    for idx in range(m):
        fr, pos = orig_refs[idx]
        e = G[fr][pos]
        # original capacity minus remaining capacity gives flow sent
        used = edges_input[idx][2] - e.cap
        result.append(str(used))

    print("YES")
    print(' '.join(result))

if __name__ == "__main__":
    solve()