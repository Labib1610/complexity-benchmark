import sys
from collections import deque

def solve() -> None:
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    it = iter(data)
    n = next(it); m = next(it); _ = next(it)  # commodity count ignored
    s = next(it) - 1
    t = next(it) - 1
    d = next(it)

    edges_input = []
    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        cap = next(it)
        edges_input.append((u, v, cap))

    # Dinic implementation
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

    INF = 10**18

    level = [0]*N
    it_ptr = [0]*N

    def bfs():
        for i in range(N):
            level[i] = -1
        q = deque([s])
        level[s] = 0
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
    while bfs():
        it_ptr = [0]*N
        while True:
            pushed = dfs(s, INF)
            if not pushed:
                break
            flow += pushed
            if flow >= d:  # early stop if we already reached required volume
                break
        if flow >= d:
            break

    if flow < d:
        print("NO")
        return

    # We have at least d flow; need exactly d. The current flow may be > d.
    # Reduce excess flow by sending back along residual network from t to s.
    excess = flow - d
    if excess > 0:
        # add a super edge from t to s with capacity excess to cancel flow
        cancel_edge = add_edge(t, s, excess)
        # run another maxflow from s to t (which will push back excess)
        while bfs():
            it_ptr = [0]*N
            while True:
                pushed = dfs(s, INF)
                if not pushed:
                    break
                excess -= pushed
                if excess == 0:
                    break
            if excess == 0:
                break
        # remove the temporary edge effects (its residual may have flow)
        # No need to explicitly remove; final flows on original edges are correct.

    # Retrieve flows on original edges
    result = []
    for e in orig_refs:
        # original capacity minus remaining capacity gives flow sent
        used = e.cap  # remaining capacity
        flow_sent = e.orig_cap - used if hasattr(e, 'orig_cap') else None
    # To get original capacities, we stored them only in input; compute:
    for (u, v, cap), e in zip(edges_input, orig_refs):
        flow_sent = cap - e.cap
        result.append(str(flow_sent))

    print("YES")
    print(' '.join(result))

if __name__ == "__main__":
    solve()