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
        cap = int(next(it))
        edges_input.append((u, v, cap))

    # Dinic with edge indexing to retrieve original order flows
    N = n
    adj = [[] for _ in range(N)]

    class Edge:
        __slots__ = ('to', 'rev', 'cap', 'orig_cap')
        def __init__(self, to, rev, cap):
            self.to = to
            self.rev = rev
            self.cap = cap
            self.orig_cap = cap

    # store reference to edge objects for original edges
    edge_refs = []

    def add_edge(fr, to, cap):
        fwd = Edge(to, len(adj[to]), cap)
        rev = Edge(fr, len(adj[fr]), 0)
        adj[fr].append(fwd)
        adj[to].append(rev)
        return fwd

    for (u, v, cap) in edges_input:
        e = add_edge(u, v, cap)
        edge_refs.append(e)

    INF = 10**18

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
            it_ptr[v] = i
            e = adj[v][i]
            if e.cap > 0 and level[v] < level[e.to]:
                ret = dfs(e.to, min(f, e.cap))
                if ret:
                    e.cap -= ret
                    adj[e.to][e.rev].cap += ret
                    return ret
        return 0

    flow = 0
    while bfs():
        it_ptr = [0]*N
        while True:
            pushed = dfs(s, INF)
            if not pushed:
                break
            flow += pushed
            if flow >= d:  # early stop if enough
                break
        if flow >= d:
            break

    if flow < d:
        print("NO")
        return

    # we have at least d flow, but may have sent more; need exactly d.
    # Since capacities are integers, we can trim excess by reducing flow on any path.
    # Simplest: we have residual network with flow = flow. We need to push back (flow-d) units from t to s.
    excess = flow - d
    if excess > 0:
        # add reverse edge from t to s with infinite capacity to allow sending back flow
        # Actually we can just run a maxflow from t to s on the residual graph to cancel excess.
        s2, t2 = t, s
        # reuse bfs/dfs with same structures but source=t, sink=s
        while excess > 0 and bfs():
            it_ptr = [0]*N
            while excess > 0:
                pushed = dfs(s2, excess)
                if not pushed:
                    break
                excess -= pushed
        # after this, flow reduced to d
    # Now extract flows on original edges: original capacity - remaining capacity
    result = []
    for e in edge_refs:
        used = e.orig_cap - e.cap
        result.append(str(used))
    print("YES")
    print(' '.join(result))

if __name__ == "__main__":
    solve()