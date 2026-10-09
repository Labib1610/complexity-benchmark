import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); _ = int(next(it))  # product count ignored
    s = int(next(it)) - 1
    t = int(next(it)) - 1
    d = int(next(it))
    edges_input = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        c = int(next(it))
        edges_input.append((u, v, c))

    # Dinic
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

    # store references to forward edges for output
    edge_refs = []
    for u, v, c in edges_input:
        fwd, rev = add_edge(u, v, c)
        edge_refs.append(fwd)

    level = [0]*N
    itp = [0]*N

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
        for i in range(itp[v], len(adj[v])):
            e = adj[v][i]
            if e.cap > 0 and level[v] < level[e.to]:
                ret = dfs(e.to, min(f, e.cap))
                if ret:
                    e.cap -= ret
                    adj[e.to][e.rev].cap += ret
                    return ret
            itp[v] += 1
        return 0

    flow = 0
    INF = 10**18
    while bfs():
        itp = [0]*N
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

    # we have at least d flow, but maybe more. Need to reduce to exactly d.
    # Since capacities are integers, we can simply run another flow reduction:
    # Build residual graph with current flow, and try to push back (flow - d) from t to s.
    excess = flow - d
    if excess > 0:
        # add reverse edge from t to s with capacity excess and try to send that back
        # Actually we can just run a maxflow from t to s on the residual network.
        s2, t2 = t, s
        # reuse bfs/dfs with swapped source/sink
        while excess > 0 and bfs():
            itp = [0]*N
            while True:
                f = dfs(s2, excess)
                if not f:
                    break
                excess -= f
                if excess == 0:
                    break
        # after this, total flow from original s to t is exactly d

    # collect flows on original edges
    result = []
    for e in edge_refs:
        used = e.orig_cap - e.cap
        result.append(str(used))

    print("YES")
    print(" ".join(result))

if __name__ == "__main__":
    solve()