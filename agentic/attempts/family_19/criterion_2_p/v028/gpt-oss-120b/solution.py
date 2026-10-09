import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    _ = next(it)  # the extra '1' in description, ignore
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
    N = n
    adj = [[] for _ in range(N)]

    class Edge:
        __slots__ = ('to', 'rev', 'cap', 'orig')
        def __init__(self, to, rev, cap, orig=False):
            self.to = to
            self.rev = rev
            self.cap = cap
            self.orig = orig  # marks if this edge corresponds to original input

    # store reference to original edges for output
    orig_refs = []

    def add_edge(fr, to, cap, orig=False):
        fwd = Edge(to, len(adj[to]), cap, orig)
        rev = Edge(fr, len(adj[fr]), 0, False)
        adj[fr].append(fwd)
        adj[to].append(rev)
        return fwd

    for idx, (u, v, cap) in enumerate(edges_input):
        e = add_edge(u, v, cap, True)
        orig_refs.append(e)

    level = [0]*N
    it_ptr = [0]*N

    def bfs():
        for i in range(N):
            level[i] = -1
        q = deque()
        level[s] = 0
        q.append(s)
        while q:
            v = q.popleft()
            for e in adj[v]:
                if e.cap > 0 and level[e.to] < 0:
                    level[e.to] = level[v] + 1
                    q.append(e.to)
        return level[t] >= 0

    def dfs(v, f):
        if v == t:
            return f
        for i in range(it_ptr[v], len(adj[v])):
            e = adj[v][i]
            if e.cap > 0 and level[v] < level[e.to]:
                ret = dfs(e.to, min(f, e.cap))
                if ret:
                    e.cap -= ret
                    adj[e.to][e.rev].cap += ret
                    return ret
            it_ptr[v] += 1
        return 0

    flow = 0
    INF = 10**18
    while bfs():
        it_ptr = [0]*N
        while True:
            f = dfs(s, INF)
            if not f:
                break
            flow += f

    if flow < d:
        print("NO")
        return

    # We have a flow of at least d, but we may have sent more than needed.
    # Need to adjust to exactly d while respecting capacities.
    # Since capacities are integral, we can simply run a second flow reduction:
    # Build residual graph with current flow, and try to push back (flow - d) from t to s.
    excess = flow - d
    if excess > 0:
        # reset level/it for another maxflow from t to s on residual
        s2, t2 = t, s
        def bfs2():
            for i in range(N):
                level[i] = -1
            q = deque()
            level[s2] = 0
            q.append(s2)
            while q:
                v = q.popleft()
                for e in adj[v]:
                    if e.cap > 0 and level[e.to] < 0:
                        level[e.to] = level[v] + 1
                        q.append(e.to)
            return level[t2] >= 0

        def dfs2(v, f):
            if v == t2:
                return f
            for i in range(it_ptr[v], len(adj[v])):
                e = adj[v][i]
                if e.cap > 0 and level[v] < level[e.to]:
                    ret = dfs2(e.to, min(f, e.cap))
                    if ret:
                        e.cap -= ret
                        adj[e.to][e.rev].cap += ret
                        return ret
                it_ptr[v] += 1
            return 0

        while excess > 0 and bfs2():
            it_ptr = [0]*N
            while excess > 0:
                pushed = dfs2(s2, excess)
                if not pushed:
                    break
                excess -= pushed

    # Now extract flows on original edges: original capacity - remaining capacity
    result = []
    for e, (u, v, cap) in zip(orig_refs, edges_input):
        used = cap - e.cap
        result.append(str(used))

    print("YES")
    print(' '.join(result))

if __name__ == "__main__":
    solve()