import sys
sys.setrecursionlimit(1 << 25)

def solve():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it)); B = int(next(it))
    specials = [int(next(it)) - 1 for _ in range(k)]
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        edges.append((u, v, w))
    if k <= 1:
        print("YES")
        print(0)
        return
    if k > 2:
        print("NO")
        return
    s, t = specials[0], specials[1]

    # Dinic
    N = n
    adj = [[] for _ in range(N)]

    class Edge:
        __slots__ = ('to','rev','cap','orig')
        def __init__(self, to, rev, cap, orig):
            self.to = to
            self.rev = rev
            self.cap = cap
            self.orig = orig  # (u,v,idx) for original edges, else None

    for idx, (u, v, w) in enumerate(edges):
        # add undirected edge as two directed with capacity w
        e1 = Edge(v, len(adj[v]), w, (u, v, idx))
        e2 = Edge(u, len(adj[u]), w, (v, u, idx))
        adj[u].append(e1)
        adj[v].append(e2)

    level = [0]*N
    itp = [0]*N

    from collections import deque
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

    # after maxflow, find reachable from s in residual
    visited = [False]*N
    stack = [s]
    visited[s] = True
    while stack:
        v = stack.pop()
        for e in adj[v]:
            if e.cap > 0 and not visited[e.to]:
                visited[e.to] = True
                stack.append(e.to)

    cut_edges = set()
    total = 0
    for u in range(N):
        if not visited[u]:
            continue
        for e in adj[u]:
            if not visited[e.to]:
                # original undirected edge corresponds to both directions; ensure unique
                orig = e.orig
                if orig is None:
                    continue
                a, b, idx = orig
                # store unordered
                if idx not in cut_edges:
                    cut_edges.add(idx)
                    total += edges[idx][2]

    if total <= B:
        print("YES")
        print(len(cut_edges))
        for idx in cut_edges:
            u, v, _ = edges[idx]
            print(u+1, v+1)
    else:
        print("NO")

if __name__ == "__main__":
    solve()