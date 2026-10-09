import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); _ = next(it)  # the third number is always 1, ignore
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
            self.orig = orig  # marks if this edge corresponds to original input edge

    # store reference to original edges to retrieve flow later
    orig_edges = []

    def add_edge(fr, to, cap, orig=False):
        fwd = Edge(to, len(adj[to]), cap, orig)
        rev = Edge(fr, len(adj[fr]), 0, False)
        adj[fr].append(fwd)
        adj[to].append(rev)
        return fwd

    for idx, (u, v, cap) in enumerate(edges_input):
        e = add_edge(u, v, cap, True)
        orig_edges.append(e)

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

    def dfs(v, upTo):
        if v == t:
            return upTo
        for i in range(it_ptr[v], len(adj[v])):
            e = adj[v][i]
            if e.cap > 0 and level[v] < level[e.to]:
                ret = dfs(e.to, min(upTo, e.cap))
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
    # Since capacities are integral, we can simply run a second flow to reduce excess.
    # Build residual graph from current state and push back (flow - d) from t to s.

    excess = flow - d
    if excess > 0:
        # add a super source = t, super sink = s, and try to send excess back.
        # We'll reuse same structure: just run bfs/dfs from t to s on residual graph.
        # Temporarily swap s and t.
        orig_s, orig_t = s, t
        s, t = orig_t, orig_s
        while excess > 0 and bfs():
            it_ptr = [0]*N
            while excess > 0:
                f = dfs(s, excess)
                if not f:
                    break
                excess -= f
        # restore original s,t (not needed further)
        s, t = orig_s, orig_t

    # Now extract flows on original edges: flow = original capacity - residual cap
    result = []
    for e, (u, v, cap) in zip(orig_edges, edges_input):
        used = cap - e.cap
        result.append(str(used))

    print("YES")
    print(' '.join(result))

if __name__ == "__main__":
    solve()