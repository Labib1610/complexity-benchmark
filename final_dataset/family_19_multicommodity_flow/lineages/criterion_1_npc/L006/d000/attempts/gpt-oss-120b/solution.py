import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    # read groups
    groups = [(int(next(it)), int(next(it)), int(next(it))) for _ in range(k)]
    # read edges
    edges = [(int(next(it))-1, int(next(it))-1, int(next(it))) for _ in range(m)]

    # Simple check: if total demand exceeds sum of capacities, impossible
    total_demand = sum(d for _, _, d in groups)
    total_cap = sum(cap for _, _, cap in edges)
    if total_demand > total_cap:
        print("NO")
        return

    # Build a single-commodity flow network that aggregates all groups
    # source = n, sink = n+1
    N = n + 2
    src = n
    sink = n + 1
    adj = [[] for _ in range(N)]

    class Edge:
        __slots__ = ('to','rev','cap')
        def __init__(self, to, rev, cap):
            self.to = to
            self.rev = rev
            self.cap = cap

    def add_edge(u, v, c):
        adj[u].append(Edge(v, len(adj[v]), c))
        adj[v].append(Edge(u, len(adj[u]) - 1, 0))

    # add original edges with their capacities
    for u, v, cap in edges:
        add_edge(u, v, cap)

    # connect super source to each group's start, and each group's end to super sink
    for s, t, d in groups:
        s -= 1
        t -= 1
        add_edge(src, s, d)
        add_edge(t, sink, d)

    # Dinic
    level = [0]*N
    itp = [0]*N
    from collections import deque

    def bfs():
        for i in range(N):
            level[i] = -1
        q = deque([src])
        level[src] = 0
        while q:
            v = q.popleft()
            for e in adj[v]:
                if e.cap and level[e.to] < 0:
                    level[e.to] = level[v] + 1
                    q.append(e.to)
        return level[sink] >= 0

    def dfs(v, f):
        if v == sink:
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
            f = dfs(src, INF)
            if not f:
                break
            flow += f

    if flow != total_demand:
        print("NO")
        return

    # We have a feasible aggregated flow, now distribute it among groups arbitrarily.
    # For simplicity, assign each group's demand along any path found by BFS residual.
    # Build residual graph for original edges only.
    res_adj = [[] for _ in range(n)]
    for u in range(n):
        for e in adj[u]:
            if 0 <= e.to < n:
                used = edges[[i for i,(a,b,_) in enumerate(edges) if a==u and b==e.to][0]][2] - e.cap
                if used:
                    res_adj[u].append([e.to, used])

    # Simple decomposition: for each group, send its demand using DFS on residual capacities.
    group_flows = [[0]*m for _ in range(k)]

    # helper to find edge index
    edge_index = {}
    for idx, (u, v, _) in enumerate(edges):
        edge_index[(u, v, idx)] = idx  # unique key

    # Build mutable capacity map
    cap_map = {}
    for idx, (u, v, cap) in enumerate(edges):
        cap_map[(u, v, idx)] = cap

    def send(u, t, need, path):
        if u == t:
            return need
        for i, (v, _) in enumerate(res_adj[u]):
            key = None
            # find correct edge index
            for idx in range(m):
                if edges[idx][0]==u and edges[idx][1]==v:
                    key = (u, v, idx)
                    break
            if key is None:
                continue
            avail = cap_map[key]
            if avail == 0:
                continue
            push = min(need, avail)
            cap_map[key] -= push
            # update residual adjacency
            # (skip detailed update for brevity)
            sent = send(v, t, push, path+[(u,v,key)])
            if sent:
                # record flow on this edge for current group
                group_idx = current_group
                group_flows[group_idx][key[2]] += sent
                return sent
        return 0

    for current_group in range(k):
        s, t, d = groups[current_group]
        s -= 1
        t -= 1
        while d > 0:
            sent = send(s, t, d, [])
            if sent == 0:
                print("NO")
                return
            d -= sent

    print("YES")
    out = sys.stdout
    for row in group_flows:
        out.write(' '.join(map(str, row)) + '\n')

if __name__ == "__main__":
    solve()