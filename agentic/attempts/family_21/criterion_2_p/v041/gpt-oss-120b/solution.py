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
    cap_limit = int(next(it))

    edges_input = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        edges_input.append((u, v, w))

    # Dinic implementation
    N = n
    adj = [[] for _ in range(N)]

    class Edge:
        __slots__ = ('to', 'rev', 'cap')
        def __init__(self, to, rev, cap):
            self.to = to
            self.rev = rev
            self.cap = cap

    def add_edge(fr, to, cap):
        fwd = Edge(to, len(adj[to]), cap)
        rev = Edge(fr, len(adj[fr]), 0)
        adj[fr].append(fwd)
        adj[to].append(rev)

    for u, v, w in edges_input:
        add_edge(u, v, w)
        add_edge(v, u, w)   # undirected edge as two directed with same capacity

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
    INF = 10**18
    while bfs():
        it_ptr = [0]*N
        while True:
            f = dfs(s, INF)
            if not f:
                break
            flow += f

    if flow > cap_limit:
        print("NO")
        return

    # find reachable vertices in residual graph
    visited = [False]*N
    stack = [s]
    visited[s] = True
    while stack:
        v = stack.pop()
        for e in adj[v]:
            if e.cap > 0 and not visited[e.to]:
                visited[e.to] = True
                stack.append(e.to)

    cut_edges = []
    for u, v, w in edges_input:
        if visited[u] != visited[v]:
            cut_edges.append((u+1, v+1))

    print("YES")
    print(len(cut_edges))
    for a, b in cut_edges:
        print(a, b)

if __name__ == "__main__":
    solve()