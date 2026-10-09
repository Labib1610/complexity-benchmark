import sys
sys.setrecursionlimit(1 << 25)

class Edge:
    __slots__ = ('to', 'rev', 'cap', 'orig')
    def __init__(self, to, rev, cap, orig=False):
        self.to = to          # target vertex
        self.rev = rev        # index of reverse edge in adjacency list of 'to'
        self.cap = cap        # residual capacity
        self.orig = orig      # True for original graph edges (not super source/sink)

def add_edge(g, fr, to, cap, orig=False):
    g[fr].append(Edge(to, len(g[to]), cap, orig))
    g[to].append(Edge(fr, len(g[fr]) - 1, 0, False))

def dinic(g, s, t):
    n = len(g)
    level = [0] * n
    it = [0] * n

    from collections import deque
    def bfs():
        for i in range(n):
            level[i] = -1
        q = deque([s])
        level[s] = 0
        while q:
            v = q.popleft()
            for e in g[v]:
                if e.cap and level[e.to] < 0:
                    level[e.to] = level[v] + 1
                    q.append(e.to)
        return level[t] >= 0

    def dfs(v, f):
        if v == t:
            return f
        for i in range(it[v], len(g[v])):
            e = g[v][i]
            if e.cap and level[v] < level[e.to]:
                ret = dfs(e.to, min(f, e.cap))
                if ret:
                    e.cap -= ret
                    g[e.to][e.rev].cap += ret
                    return ret
            it[v] += 1
        return 0

    flow = 0
    INF = 10**18
    while bfs():
        it = [0] * n
        while True:
            f = dfs(s, INF)
            if not f:
                break
            flow += f
    return flow

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it))
    streams = []
    for _ in range(k):
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        d = int(next(it))
        streams.append((s, t, d))
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        cap = int(next(it))
        edges.append((u, v, cap))

    S = n
    T = n + 1
    G = [[] for _ in range(n + 2)]

    # original edges, remember their order
    edge_refs = []          # (from, index in G[from]) for each original edge
    for idx, (u, v, cap) in enumerate(edges):
        add_edge(G, u, v, cap, orig=True)
        edge_refs.append( (u, len(G[u]) - 1) )   # last added edge

    total_d = 0
    for i, (s, t, d) in enumerate(streams):
        total_d += d
        add_edge(G, S, s, d)          # super source to s_i
        add_edge(G, t, T, d)          # t_i to super sink

    maxflow = dinic(G, S, T)
    if maxflow != total_d:
        print("NO")
        return

    # Build a structure that stores the *actual* flow on original edges
    # after maxflow, the residual capacities are in G, but we need the flow value.
    # For each original edge we can compute flow = original_cap - residual_cap
    flow_on_edge = [0] * m
    for idx, (u, edge_idx) in enumerate(edge_refs):
        e = G[u][edge_idx]
        rev = G[e.to][e.rev]
        used = rev.cap          # reverse edge capacity equals flow sent forward
        flow_on_edge[idx] = used

    # Now decompose the flow into per‑stream paths.
    # We'll work on a copy of the flow values on all edges (including super edges).
    # For simplicity we keep a separate adjacency list with mutable capacities.
    # We'll reuse G but interpret capacities as *remaining flow* (not residual).
    # First, set each edge's 'cap' to the amount of flow that currently passes
    # through it (i.e. forward flow). For original edges we already have it.
    # For super source/sink edges, the forward flow equals the original capacity
    # (they are saturated in a feasible solution).
    # Build a list of all edges that may carry flow.
    flow_adj = [[] for _ in range(n + 2)]
    # original edges
    for idx, (u, edge_idx) in enumerate(edge_refs):
        e = G[u][edge_idx]
        f = flow_on_edge[idx]
        if f:
            # store mutable copy
            flow_adj[u].append([e.to, f, idx])   # idx is original edge index
    # super source edges
    for e in G[S]:
        if e.cap == 0:   # saturated, flow = original capacity
            # find original capacity from reverse edge
            rev = G[e.to][e.rev]
            f = rev.cap
            if f:
                flow_adj[S].append([e.to, f, -1])   # -1 marks super edge
    # edges from t_i to T
    for v in range(n):
        for e in G[v]:
            if e.to == T:
                if e.cap == 0:
                    rev = G[T][e.rev]
                    f = rev.cap
                    if f:
                        flow_adj[v].append([T, f, -2])   # -2 marks sink edge

    # answer matrix
    ans = [[0] * m for _ in range(k)]

    # helper to find a path with DFS
    def dfs_path(v, target, visited, path):
        if v == target:
            return True
        visited[v] = True
        for i, (to, cap, eid) in enumerate(flow_adj[v]):
            if cap and not visited[to]:
                path.append((v, i))   # store vertex and index in its list
                if dfs_path(to, target, visited, path):
                    return True
                path.pop()
        return False

    # decompose
    while True:
        visited = [False] * (n + 2)
        path = []
        if not dfs_path(S, T, visited, path):
            break
        # determine minimal flow on this path
        delta = min(flow_adj[v][idx][1] for v, idx in path)
        # first edge tells the stream
        first_v, first_idx = path[0]
        to, _, eid = flow_adj[first_v][first_idx]
        # eid is -1 (super edge) -> need to know which stream it is.
        # The edge S->s_i corresponds to stream i; we can find i by matching to.
        stream_i = None
        for i, (s, t, d) in enumerate(streams):
            if s == to:
                stream_i = i
                break
        # subtract delta and record on original edges
        for v, idx in path:
            edge = flow_adj[v][idx]
            edge[1] -= delta
            if edge[2] >= 0:          # original edge
                ans[stream_i][edge[2]] += delta
        # remove zero‑capacity entries to keep DFS fast (optional)
        for v in range(n + 2):
            flow_adj[v] = [e for e in flow_adj[v] if e[1] > 0]

    # output
    out = ["YES"]
    for i in range(k):
        out.append(" ".join(str(x) for x in ans[i]))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()