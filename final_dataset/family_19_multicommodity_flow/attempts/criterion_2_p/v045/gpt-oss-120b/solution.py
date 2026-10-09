import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it))  # k is always 1
    s = int(next(it)) - 1
    t = int(next(it)) - 1
    d = int(next(it))
    edges_input = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        cap = int(next(it))
        edges_input.append((u, v, cap))

    # Dinic with edge indexing to retrieve flows
    N = n
    adj = [[] for _ in range(N)]
    class Edge:
        __slots__ = ('to','rev','cap','orig_cap','idx')
        def __init__(self, to, rev, cap, orig_cap, idx):
            self.to = to
            self.rev = rev
            self.cap = cap
            self.orig_cap = orig_cap
            self.idx = idx  # original edge index or -1 for added edges

    def add_edge(fr, to, cap, idx):
        fwd = Edge(to, len(adj[to]), cap, cap, idx)
        rev = Edge(fr, len(adj[fr]), 0, 0, -1)
        adj[fr].append(fwd)
        adj[to].append(rev)

    for idx, (u, v, cap) in enumerate(edges_input):
        add_edge(u, v, cap, idx)

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
            if flow >= d:  # early stop if we already have enough
                break
        if flow >= d:
            break

    if flow < d:
        print("NO")
        return

    # We have at least d flow; we may have sent more, need exactly d.
    # If flow > d, we can reduce excess by sending back along residual paths.
    excess = flow - d
    if excess > 0:
        # try to push back excess from t to s
        # temporarily treat t as source, s as sink, capacities are residual forward edges.
        # We'll run a flow of size excess from t to s.
        s_orig, t_orig = s, t
        s, t = t_orig, s_orig  # swap
        while excess > 0 and bfs():
            it_ptr = [0]*N
            while excess > 0:
                f = dfs(s, excess)
                if not f:
                    break
                excess -= f
        # restore original order (not needed further)
        s, t = s_orig, t_orig

    # collect flows for original edges
    result = [0]*m
    for u in range(N):
        for e in adj[u]:
            if e.idx >= 0:
                used = e.orig_cap - e.cap
                result[e.idx] = used

    print("YES")
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    solve()