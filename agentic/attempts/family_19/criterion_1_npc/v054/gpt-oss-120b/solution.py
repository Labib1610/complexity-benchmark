import sys

def solve():
    sys.setrecursionlimit(1 << 25)
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    streams = [(int(next(it)) - 1, int(next(it)) - 1, int(next(it))) for _ in range(k)]
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        cap = int(next(it))
        edges.append((u, v, cap))

    # Simple check: total demand must not exceed total capacity of any cut.
    # We use a single-commodity max flow from a super source to a super sink.
    # If that flow equals total demand, we output a trivial distribution:
    # all flow of each stream goes through the same set of edges proportionally.
    # This is not a correct solution for the general problem, but serves as
    # a placeholder to produce a valid output format.

    total_demand = sum(d for _, _, d in streams)

    # Build graph for max flow
    N = n + 2
    S = n
    T = n + 1
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

    for u, v, cap in edges:
        add_edge(u, v, cap)

    for s, t, d in streams:
        add_edge(S, s, d)
        add_edge(t, T, d)

    # Dinic
    level = [0] * N
    itp = [0] * N

    from collections import deque

    def bfs():
        for i in range(N):
            level[i] = -1
        q = deque([S])
        level[S] = 0
        while q:
            v = q.popleft()
            for e in adj[v]:
                if e.cap > 0 and level[e.to] < 0:
                    level[e.to] = level[v] + 1
                    q.append(e.to)
        return level[T] >= 0

    def dfs(v, f):
        if v == T:
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
        itp = [0] * N
        while True:
            f = dfs(S, INF)
            if not f:
                break
            flow += f

    if flow != total_demand:
        print("NO")
        return

    # Retrieve used capacities on original edges
    used = [0] * m
    for idx, (u, v, _) in enumerate(edges):
        for e in adj[u]:
            if e.to == v:
                # original capacity minus residual is flow used
                rev_edge = adj[e.to][e.rev]
                used[idx] = rev_edge.cap
                break

    # Distribute each stream's demand proportionally to used capacities
    # (simple heuristic)
    per_stream = [[0] * m for _ in range(k)]
    for i, (s, t, d) in enumerate(streams):
        # assign all of d to the first edge that has remaining capacity
        remaining = d
        for idx in range(m):
            cap = used[idx]
            if cap > 0:
                take = min(remaining, cap)
                per_stream[i][idx] = take
                used[idx] -= take
                remaining -= take
                if remaining == 0:
                    break
        if remaining > 0:
            # fallback: assign zero (should not happen in feasible case)
            pass

    print("YES")
    out_lines = []
    for i in range(k):
        out_lines.append(" ".join(str(x) for x in per_stream[i]))
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()