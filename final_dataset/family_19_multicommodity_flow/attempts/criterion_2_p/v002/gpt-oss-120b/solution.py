import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    s = int(next(it)) - 1
    t = int(next(it)) - 1
    d = int(next(it))
    edges_input = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        cap = int(next(it))
        edges_input.append((u, v, cap))

    # Dinic implementation with edge indexing to retrieve flows
    N = n
    adj = [[] for _ in range(N)]

    class Edge:
        __slots__ = ('to', 'rev', 'cap', 'orig_cap')
        def __init__(self, to, rev, cap):
            self.to = to
            self.rev = rev
            self.cap = cap
            self.orig_cap = cap

    def add_edge(fr, to, cap):
        fwd = Edge(to, len(adj[to]), cap)
        rev = Edge(fr, len(adj[fr]), 0)
        adj[fr].append(fwd)
        adj[to].append(rev)
        return fwd, rev

    # keep reference to forward edges in input order
    forward_refs = []
    for u, v, cap in edges_input:
        fwd, rev = add_edge(u, v, cap)
        forward_refs.append(fwd)

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
    INF = 10**18
    while bfs():
        it_ptr = [0]*N
        while True:
            pushed = dfs(s, INF)
            if not pushed:
                break
            flow += pushed
            if flow >= d:  # early stop if we already reached required amount
                break
        if flow >= d:
            break

    if flow < d:
        print("NO")
        return

    # we have at least d flow, but maybe more; we need exactly d on each edge.
    # Since we may have sent more, we can simply scale down by reducing flow along augmenting paths.
    # Simpler: run Dinic again but stop when flow reaches d, using same graph (capacities already reduced).
    # However current residual graph already has flow = flow. We need to extract actual flow values on original edges.
    # The forward edge's original capacity minus remaining capacity equals flow sent.
    result = []
    for e in forward_refs:
        used = e.orig_cap - e.cap
        result.append(str(used))

    # If flow > d, we need to reduce excess. Since capacities are integral and we only need any feasible routing of exactly d,
    # we can just output the current used values but they sum to flow > d, which violates requirement.
    # To handle this, we redo the max flow with a limit d from scratch.

    # Rebuild graph with limit d
    adj = [[] for _ in range(N)]
    forward_refs = []
    for u, v, cap in edges_input:
        fwd, rev = add_edge(u, v, cap)
        forward_refs.append(fwd)

    flow = 0
    while bfs():
        it_ptr = [0]*N
        while True:
            pushed = dfs(s, d - flow)
            if not pushed:
                break
            flow += pushed
            if flow == d:
                break
        if flow == d:
            break

    if flow < d:
        print("NO")
        return

    print("YES")
    out = [str(e.orig_cap - e.cap) for e in forward_refs]
    print(' '.join(out))

if __name__ == "__main__":
    solve()