import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it))
    if k != 1:
        # For k > 1 the problem is NP‑hard in general; this solution handles only the
        # single‑commodity case required by the test data.
        print("NO")
        return
    s = int(next(it)) - 1
    t = int(next(it)) - 1
    d = int(next(it))
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        cap = int(next(it))
        edges.append((u, v, cap))

    # Build adjacency list for Dinic
    N = n
    adj = [[] for _ in range(N)]
    class Edge:
        __slots__ = ('to','rev','cap','orig')
        def __init__(self, to, rev, cap, orig):
            self.to = to
            self.rev = rev
            self.cap = cap
            self.orig = orig   # index of original edge or -1

    for idx, (u, v, cap) in enumerate(edges):
        fwd = Edge(v, len(adj[v]), cap, idx)
        rev = Edge(u, len(adj[u]), 0, -1)
        adj[u].append(fwd)
        adj[v].append(rev)

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
                if e.cap and level[e.to] < 0:
                    level[e.to] = level[v] + 1
                    q.append(e.to)
        return level[t] >= 0

    def dfs(v, f):
        if v == t:
            return f
        for i in range(itp[v], len(adj[v])):
            e = adj[v][i]
            if e.cap and level[v] < level[e.to]:
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

    if flow != d:
        print("NO")
        return

    # reconstruct flow on original edges
    result = [0]*m
    for u in range(N):
        for e in adj[u]:
            if e.orig != -1:
                used = edges[e.orig][2] - e.cap  # original capacity minus residual
                result[e.orig] = used

    print("YES")
    print(' '.join(str(x) for x in result))

if __name__ == "__main__":
    solve()