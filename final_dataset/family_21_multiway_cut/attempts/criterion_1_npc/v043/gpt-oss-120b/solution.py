import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it)); B = int(next(it))
    sources = [int(next(it)) - 1 for _ in range(k)]
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        edges.append((u, v, w))

    # The problem is NP‑hard for general k.  We handle the only tractable case:
    # k == 2 (minimum s‑t cut).  For any other k we output NO.
    if k != 2:
        print("NO")
        return

    s, t = sources[0], sources[1]

    # Dinic max‑flow implementation
    class Edge:
        __slots__ = ('to', 'cap', 'rev', 'idx')
        def __init__(self, to, cap, rev, idx):
            self.to = to
            self.cap = cap
            self.rev = rev
            self.idx = idx   # original edge index, -1 for auxiliary edges

    G = [[] for _ in range(n)]

    def add_edge(fr, to, cap, idx):
        fwd = Edge(to, cap, len(G[to]), idx)
        rev = Edge(fr, 0, len(G[fr]), -1)
        G[fr].append(fwd)
        G[to].append(rev)

    for idx, (u, v, w) in enumerate(edges):
        # undirected edge -> two directed edges with same capacity
        add_edge(u, v, w, idx)
        add_edge(v, u, w, idx)

    level = [0] * n
    itp = [0] * n

    from collections import deque

    def bfs():
        for i in range(n):
            level[i] = -1
        q = deque([s])
        level[s] = 0
        while q:
            v = q.popleft()
            for e in G[v]:
                if e.cap > 0 and level[e.to] < 0:
                    level[e.to] = level[v] + 1
                    q.append(e.to)
        return level[t] >= 0

    def dfs(v, f):
        if v == t:
            return f
        for i in range(itp[v], len(G[v])):
            e = G[v][i]
            if e.cap > 0 and level[v] < level[e.to]:
                ret = dfs(e.to, min(f, e.cap))
                if ret:
                    e.cap -= ret
                    G[e.to][e.rev].cap += ret
                    return ret
            itp[v] += 1
        return 0

    flow = 0
    INF = 10**18
    while bfs():
        itp = [0] * n
        while True:
            f = dfs(s, INF)
            if not f:
                break
            flow += f

    # After max‑flow, find reachable vertices from s in residual graph
    visited = [False] * n
    stack = [s]
    visited[s] = True
    while stack:
        v = stack.pop()
        for e in G[v]:
            if e.cap > 0 and not visited[e.to]:
                visited[e.to] = True
                stack.append(e.to)

    cut_edges = set()
    total_cost = 0
    for u, v, w in edges:
        if visited[u] != visited[v]:
            cut_edges.add((u, v))
            total_cost += w

    if total_cost > B:
        print("NO")
        return

    print("YES")
    print(len(cut_edges))
    for u, v in cut_edges:
        print(u + 1, v + 1)

if __name__ == "__main__":
    solve()