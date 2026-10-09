import sys
sys.setrecursionlimit(1 << 25)

class Edge:
    __slots__ = ('to', 'rev', 'cap', 'orig_cap', 'idx')
    def __init__(self, to, rev, cap, idx=-1):
        self.to = to          # target vertex
        self.rev = rev        # index of reverse edge in graph[to]
        self.cap = cap        # residual capacity
        self.orig_cap = cap   # original capacity (only for original edges)
        self.idx = idx        # original edge index, -1 for auxiliary edges

def add_edge(g, fr, to, cap, idx=-1):
    fwd = Edge(to, len(g[to]), cap, idx)
    rev = Edge(fr, len(g[fr]), 0, -1)
    g[fr].append(fwd)
    g[to].append(rev)
    return fwd, rev

def dinic(g, s, t):
    n = len(g)
    level = [0]*n
    it = [0]*n
    INF = 10**18

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
    while bfs():
        it = [0]*n
        while True:
            f = dfs(s, INF)
            if not f:
                break
            flow += f
    return flow

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it))
    mandates = []
    balance = [0]* (n+1)
    for _ in range(k):
        s = int(next(it)); t = int(next(it)); d = int(next(it))
        mandates.append((s, t, d))
        balance[s] += d
        balance[t] -= d
    edges = []
    for idx in range(m):
        u = int(next(it)); v = int(next(it)); cap = int(next(it))
        edges.append((u, v, cap))

    S = 0
    T = n + 1
    G = [[] for _ in range(n+2)]
    edge_objs = []          # forward edge objects of original edges, in input order
    for idx, (u, v, cap) in enumerate(edges):
        fwd, rev = add_edge(G, u, v, cap, idx)
        edge_objs.append(fwd)

    total_pos = 0
    for v in range(1, n+1):
        if balance[v] > 0:
            add_edge(G, S, v, balance[v])
            total_pos += balance[v]
        elif balance[v] < 0:
            add_edge(G, v, T, -balance[v])

    maxflow = dinic(G, S, T)
    if maxflow != total_pos:
        print("NO")
        return

    # remaining flow on original edges = original capacity - residual capacity
    rem = [e.orig_cap - e.cap for e in edge_objs]   # list of ints, length m

    # adjacency for decomposition (only original edges, with mutable remaining flow)
    adj = [[] for _ in range(n+1)]
    for idx, (u, v, _) in enumerate(edges):
        if rem[idx]:
            adj[u].append((v, idx))

    # answer matrix
    ans = [[0]*m for _ in range(k)]

    from collections import deque
    for i, (src, dst, need) in enumerate(mandates):
        while need:
            # BFS to find any path with remaining flow
            prev_v = [-1]*(n+1)
            prev_e = [-1]*(n+1)
            q = deque([src])
            prev_v[src] = src
            while q and prev_v[dst] == -1:
                v = q.popleft()
                for to, eidx in adj[v]:
                    if rem[eidx] > 0 and prev_v[to] == -1:
                        prev_v[to] = v
                        prev_e[to] = eidx
                        q.append(to)
            # reconstruct path
            path = []
            v = dst
            bottleneck = need
            while v != src:
                eidx = prev_e[v]
                bottleneck = min(bottleneck, rem[eidx])
                path.append(eidx)
                v = prev_v[v]
            delta = bottleneck
            # apply delta
            for eidx in path:
                rem[eidx] -= delta
                ans[i][eidx] += delta
                if rem[eidx] == 0:
                    # remove edge from adjacency to speed up later searches
                    u = edges[eidx][0]
                    # lazy removal: we keep it, BFS will just skip because rem==0
                    pass
            need -= delta

    print("YES")
    out_lines = []
    for i in range(k):
        out_lines.append(' '.join(str(x) for x in ans[i]))
    sys.stdout.write('\n'.join(out_lines))

if __name__ == "__main__":
    solve()