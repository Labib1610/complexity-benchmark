import sys

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    k = int(data[idx]); idx += 1

    streams = []
    for _ in range(k):
        s = int(data[idx]) - 1; idx += 1
        t = int(data[idx]) - 1; idx += 1
        d = int(data[idx]); idx += 1
        streams.append((s, t, d))

    edges = []
    for _ in range(m):
        u = int(data[idx]) - 1; idx += 1
        v = int(data[idx]) - 1; idx += 1
        cap = int(data[idx]); idx += 1
        edges.append((u, v, cap))

    # Build super source / super sink flow network.
    # Node indexing:
    #   0 .. n-1 : original servers
    #   n        : super source
    #   n+1      : super sink
    #   n+2 ..   : edge nodes (one per original link)
    S = n
    T = n + 1
    base = n + 2
    N = base + m

    graph = [[] for _ in range(N)]

    def add_edge(u, v, cap):
        graph[u].append([v, cap, len(graph[v])])
        graph[v].append([u, 0, len(graph[u]) - 1])

    # Edge node structure: link j has node base+j.
    # We store the index of the forward residual arc inside graph[base+j]
    # so that after maxflow we can recover flow on link j.
    edge_arc = [0] * m
    for j, (u, v, cap) in enumerate(edges):
        add_edge(u, base + j, cap)
        add_edge(base + j, v, cap)
        # forward residual arc of link u->(base+j) is graph[u][-1]
        # but we want the arc from base+j back to u in graph[base+j],
        # which is graph[base+j][0] (added first when u->base+j was added).
        edge_arc[j] = 0

    total_demand = 0
    for i, (s, t, d) in enumerate(streams):
        add_edge(S, s, d)
        add_edge(t, T, d)
        total_demand += d

    # Dinic max flow
    level = [0] * N
    it = [0] * N

    from collections import deque

    def bfs():
        for i in range(N):
            level[i] = -1
        level[S] = 0
        q = deque([S])
        while q:
            u = q.popleft()
            for e in graph[u]:
                v, cap, _ = e
                if cap > 0 and level[v] < 0:
                    level[v] = level[u] + 1
                    q.append(v)
        return level[T] >= 0

    def dfs(u, f):
        if u == T:
            return f
        while it[u] < len(graph[u]):
            e = graph[u][it[u]]
            v, cap, rev = e[0], e[1], e[2]
            if cap > 0 and level[v] == level[u] + 1:
                ret = dfs(v, min(f, cap))
                if ret > 0:
                    e[1] -= ret
                    graph[v][rev][1] += ret
                    return ret
            it[u] += 1
        return 0

    flow = 0
    while bfs():
        it = [0] * N
        while True:
            f = dfs(S, 10**18)
            if f == 0:
                break
            flow += f

    if flow < total_demand:
        print("NO")
        return

    # Recover per-link total flow.
    link_flow = [0] * m
    for j in range(m):
        # graph[base+j][0] is the residual arc back to u.
        # Its capacity equals flow sent on u->(base+j), which equals flow on link j.
        link_flow[j] = graph[base + j][edge_arc[j]][1]

    # Now decompose per-stream flows using flow decomposition on the
    # per-stream residual paths in the original graph with link capacities
    # equal to the per-link total flows we just found.
    # We build a per-stream network: source s_i, sink t_i, demand d_i,
    # link capacities = link_flow[j].
    # Then decompose paths.

    # Build adjacency for per-stream decomposition.
    # We will mutate capacities, so keep a copy.
    cap_copy = link_flow[:]

    # adjacency list: for each node, list of (edge_index)
    # We need reverse lookup for residual.
    # Simpler: build graph with explicit arcs.
    class Arc:
        __slots__ = ('to', 'cap', 'rev')
        def __init__(self, to, cap, rev):
            self.to = to
            self.cap = cap
            self.rev = rev

    g = [[] for _ in range(n)]
    for j, (u, v, _) in enumerate(edges):
        g[u].append([j, v, cap_copy[j], len(g[v])])
        g[v].append([-1, u, 0, len(g[u]) - 1])

    # For each stream, push d_i units from s to t, recording per-edge usage.
    ans = [[0] * m for _ in range(k)]

    for i, (s, t, d) in enumerate(streams):
        remaining = d
        # We use DFS-based augmentation with path recording.
        # Since graph is small enough (Dinic already ran), we can do
        # repeated DFS finding any path with positive capacity.
        while remaining > 0:
            # find path s->t
            visited = [False] * n
            parent_arc = [None] * n  # (node, arc_index_in_g[node])
            stack = [s]
            visited[s] = True
            found = False
            while stack:
                u = stack.pop()
                if u == t:
                    found = True
                    break
                for ai, (j, v, c, rev) in enumerate(g[u]):
                    if c > 0 and not visited[v]:
                        visited[v] = True
                        parent_arc[v] = (u, ai)
                        stack.append(v)
            if not found:
                # Should not happen if total flow matches demand.
                print("NO")
                return
            # find bottleneck
            path = []
            cur = t
            bottleneck = remaining
            while cur != s:
                pu, ai = parent_arc[cur]
                arc = g[pu][ai]
                path.append((pu, ai))
                if arc[2] < bottleneck:
                    bottleneck = arc[2]
                cur = pu
            # apply
            for (pu, ai) in path:
                arc = g[pu][ai]
                j = arc[0]
                v = arc[1]
                arc[2] -= bottleneck
                g[v][arc[3]][2] += bottleneck
                if j >= 0:
                    ans[i][j] += bottleneck
            remaining -= bottleneck

    print("YES")
    out = []
    for i in range(k):
        out.append(" ".join(str(ans[i][j]) for j in range(m)))
    sys.stdout.write("\n".join(out) + "\n")

solve()