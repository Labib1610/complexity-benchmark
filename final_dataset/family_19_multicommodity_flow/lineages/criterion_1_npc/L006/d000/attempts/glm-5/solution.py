import sys

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    k = int(data[idx]); idx += 1

    groups = []
    for _ in range(k):
        s = int(data[idx]) - 1; idx += 1
        t = int(data[idx]) - 1; idx += 1
        d = int(data[idx]); idx += 1
        groups.append((s, t, d))

    edges = []
    for _ in range(m):
        u = int(data[idx]) - 1; idx += 1
        v = int(data[idx]) - 1; idx += 1
        cap = int(data[idx]); idx += 1
        edges.append((u, v, cap))

    # Build a single commodity flow network.
    # Node layout:
    # 0 .. n-1 : zones
    # n .. n+k-1 : group source nodes
    # n+k .. n+2k-1 : group sink nodes
    # n+2k : super source
    # n+2k+1 : super sink

    N = n + 2 * k + 2
    S = n + 2 * k
    T = n + 2 * k + 1

    graph = [[] for _ in range(N)]

    def add_edge(u, v, cap):
        graph[u].append([v, cap, len(graph[v])])
        graph[v].append([u, 0, len(graph[u]) - 1])

    # Turnstile banks with shared capacities.
    edge_id = {}
    for j, (u, v, cap) in enumerate(edges):
        add_edge(u, v, cap)
        edge_id[j] = (len(graph[u]) - 1, u)

    # Group sources and sinks.
    for i, (s, t, d) in enumerate(groups):
        add_edge(S, n + i, d)
        add_edge(n + i, s, d)
        add_edge(t, n + k + i, d)
        add_edge(n + k + i, T, d)

    # Dinic's max flow.
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
            v, cap, rev = e
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

    total_demand = sum(d for _, _, d in groups)
    if flow < total_demand:
        print("NO")
        return

    print("YES")
    out_lines = []
    for i in range(k):
        row = []
        for j in range(m):
            eid, u = edge_id[j]
            # The edge from u to v is graph[u][eid].
            # Residual capacity = unused capacity.
            # Used = original cap - residual cap.
            used = edges[j][2] - graph[u][eid][1]
            row.append(str(used))
        out_lines.append(" ".join(row))
    sys.stdout.write("\n".join(out_lines) + "\n")

solve()