import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it))
    s = int(next(it)) - 1
    t = int(next(it)) - 1
    d = int(next(it))
    edges_input = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        L = int(next(it))
        edges_input.append((u, v, L))

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

    # store reference to original edges to retrieve flow later
    orig_refs = [None] * m

    def add_edge(fr, to, cap, orig_idx=None):
        fwd = Edge(to, len(adj[to]), cap, orig_idx is not None)
        rev = Edge(fr, len(adj[fr]), 0, False)
        adj[fr].append(fwd)
        adj[to].append(rev)
        if orig_idx is not None:
            orig_refs[orig_idx] = (fr, len(adj[fr]) - 1)  # store position of forward edge

    for idx, (u, v, L) in enumerate(edges_input):
        add_edge(u, v, L, idx)

    level = [0] * N
    it_ptr = [0] * N

    def bfs() -> bool:
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
        it_ptr = [0] * N
        while True:
            pushed = dfs(s, INF)
            if not pushed:
                break
            flow += pushed
            if flow >= d:
                break
        if flow >= d:
            break

    if flow < d:
        print("NO")
        return

    # We have at least d flow; we may have sent more, need to reduce to exactly d.
    # Since capacities are integral, we can simply run another DFS to push back excess.
    excess = flow - d
    if excess > 0:
        # Build residual graph again and try to send excess from t to s (i.e., cancel flow)
        # We'll treat t as source and s as sink.
        # Reuse bfs/dfs with swapped roles.
        s2, t2 = t, s
        while excess > 0 and bfs():
            it_ptr = [0] * N
            while excess > 0:
                pushed = dfs(s2, excess)
                if not pushed:
                    break
                excess -= pushed
        # after this, flow equals d

    # Retrieve flows on original edges
    result = []
    for idx in range(m):
        fr, pos = orig_refs[idx]
        e = adj[fr][pos]
        used = edges_input[idx][2] - e.cap  # original capacity minus remaining capacity
        result.append(str(used))

    print("YES")
    print(" ".join(result))

if __name__ == "__main__":
    solve()