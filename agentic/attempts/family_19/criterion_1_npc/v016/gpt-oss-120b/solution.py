import sys
from collections import deque

sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it))

    contracts = []
    balance = [0] * (n + 1)
    for _ in range(k):
        s = int(next(it)); t = int(next(it)); d = int(next(it))
        contracts.append((s, t, d))
        balance[s] += d
        balance[t] -= d

    edges = []                     # (u,v,cap)
    for _ in range(m):
        u = int(next(it)); v = int(next(it)); cap = int(next(it))
        edges.append((u, v, cap))

    # ---------- Dinic ----------
    N = n + 2
    S = 0
    T = n + 1

    class Edge:
        __slots__ = ('to', 'rev', 'cap', 'idx')
        def __init__(self, to, rev, cap, idx=-1):
            self.to = to
            self.rev = rev
            self.cap = cap
            self.idx = idx          # original edge index, -1 for super edges

    graph = [[] for _ in range(N)]

    def add_edge(fr, to, cap, idx=-1):
        fwd = Edge(to, len(graph[to]), cap, idx)
        rev = Edge(fr, len(graph[fr]), 0, -1)
        graph[fr].append(fwd)
        graph[to].append(rev)

    total_need = 0
    for v in range(1, n + 1):
        if balance[v] > 0:
            add_edge(S, v, balance[v])
            total_need += balance[v]
        elif balance[v] < 0:
            add_edge(v, T, -balance[v])

    for idx, (u, v, cap) in enumerate(edges):
        add_edge(u, v, cap, idx)

    level = [0] * N
    it_ptr = [0] * N

    def bfs():
        for i in range(N):
            level[i] = -1
        q = deque([S])
        level[S] = 0
        while q:
            v = q.popleft()
            for e in graph[v]:
                if e.cap and level[e.to] < 0:
                    level[e.to] = level[v] + 1
                    q.append(e.to)
        return level[T] >= 0

    def dfs(v, f):
        if v == T:
            return f
        for i in range(it_ptr[v], len(graph[v])):
            e = graph[v][i]
            if e.cap and level[v] < level[e.to]:
                ret = dfs(e.to, min(f, e.cap))
                if ret:
                    e.cap -= ret
                    graph[e.to][e.rev].cap += ret
                    return ret
            it_ptr[v] += 1
        return 0

    flow = 0
    INF = 10 ** 18
    while bfs():
        it_ptr = [0] * N
        while True:
            pushed = dfs(S, INF)
            if not pushed:
                break
            flow += pushed

    if flow != total_need:
        print("NO")
        return

    # retrieve flow on original edges
    flow_on_edge = [0] * m
    for u in range(N):
        for e in graph[u]:
            if e.idx >= 0:          # original edge
                used = graph[e.to][e.rev].cap   # reverse edge holds the flow sent
                flow_on_edge[e.idx] = used

    # ---------- decomposition ----------
    # adjacency list of edges that still have remaining flow
    adj = [[] for _ in range(n + 1)]
    for idx, (u, v, _) in enumerate(edges):
        if flow_on_edge[idx] > 0:
            adj[u].append([v, idx])   # mutable list to allow updating remaining

    remaining = flow_on_edge[:]          # mutable copy
    answer = [[0] * m for _ in range(k)]

    for ci, (s, t, d) in enumerate(contracts):
        need = d
        while need:
            # BFS to find any path with remaining >0
            prev = [-1] * (n + 1)
            prev_edge = [-1] * (n + 1)
            q = deque([s])
            prev[s] = s
            while q and prev[t] == -1:
                v = q.popleft()
                for nb, eidx in adj[v]:
                    if remaining[eidx] > 0 and prev[nb] == -1:
                        prev[nb] = v
                        prev_edge[nb] = eidx
                        q.append(nb)
            if prev[t] == -1:
                # should never happen
                print("NO")
                return
            # reconstruct path
            path = []
            cur = t
            bottleneck = need
            while cur != s:
                eidx = prev_edge[cur]
                bottleneck = min(bottleneck, remaining[eidx])
                path.append((prev[cur], cur, eidx))
                cur = prev[cur]
            push = bottleneck
            # apply push
            for u, v, eidx in path:
                remaining[eidx] -= push
                answer[ci][eidx] += push
            need -= push

    # output
    out_lines = ["YES"]
    for i in range(k):
        out_lines.append(" ".join(str(x) for x in answer[i]))
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()