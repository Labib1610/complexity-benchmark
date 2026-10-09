import sys
from collections import deque

class Edge:
    __slots__ = ('to', 'rev', 'cap', 'flow', 'orig_idx')
    def __init__(self, to, rev, cap, orig_idx=-1):
        self.to = to
        self.rev = rev
        self.cap = cap
        self.flow = 0
        self.orig_idx = orig_idx

def add_edge(adj, fr, to, cap, orig_idx=-1):
    fwd = Edge(to, len(adj[to]), cap, orig_idx)
    rev = Edge(fr, len(adj[fr]), 0, -1)
    adj[fr].append(fwd)
    adj[to].append(rev)

def bfs_level(adj, s, t, level):
    for i in range(len(level)):
        level[i] = -1
    q = deque([s])
    level[s] = 0
    while q:
        u = q.popleft()
        for e in adj[u]:
            if e.cap - e.flow > 0 and level[e.to] == -1:
                level[e.to] = level[u] + 1
                q.append(e.to)
    return level[t] != -1

def dfs_flow(adj, u, t, f, level, it):
    if u == t:
        return f
    while it[u] < len(adj[u]):
        e = adj[u][it[u]]
        if e.cap - e.flow > 0 and level[e.to] == level[u] + 1:
            ret = dfs_flow(adj, e.to, t, min(f, e.cap - e.flow), level, it)
            if ret > 0:
                e.flow += ret
                adj[e.to][e.rev].flow -= ret
                return ret
        it[u] += 1
    return 0

def max_flow(adj, s, t, n):
    flow = 0
    level = [-1] * n
    INF = 10**18
    while bfs_level(adj, s, t, level):
        it = [0] * n
        while True:
            f = dfs_flow(adj, s, t, INF, level, it)
            if f == 0:
                break
            flow += f
    return flow

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))

    species = []
    for _ in range(k):
        s = int(next(it))
        t = int(next(it))
        d = int(next(it))
        species.append((s, t, d))

    corridors = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        cap = int(next(it))
        corridors.append((u, v, cap))

    S = 0
    T = n + 1
    N = n + 2
    adj = [[] for _ in range(N)]

    # super source to species starts
    for i, (s, t, d) in enumerate(species):
        add_edge(adj, S, s, d)
    # species targets to super sink
    for i, (s, t, d) in enumerate(species):
        add_edge(adj, t, T, d)
    # original corridors
    for idx, (u, v, cap) in enumerate(corridors):
        add_edge(adj, u, v, cap, idx)

    total_demand = sum(d for _, _, d in species)
    flow = max_flow(adj, S, T, N)

    if flow < total_demand:
        print("NO")
        return

    # Decompose flow into per-species paths
    remaining = [d for _, _, d in species]
    ans = [[0] * m for _ in range(k)]

    # Helper to find an S-T path using edges with flow > 0
    def find_path():
        parent = [-1] * N
        parent_edge = [-1] * N
        visited = [False] * N
        stack = [S]
        visited[S] = True
        while stack:
            u = stack.pop()
            for ei, e in enumerate(adj[u]):
                if e.flow > 0 and not visited[e.to]:
                    visited[e.to] = True
                    parent[e.to] = u
                    parent_edge[e.to] = ei
                    if e.to == T:
                        # reconstruct
                        path = []
                        v = T
                        while v != S:
                            u = parent[v]
                            ei = parent_edge[v]
                            path.append((u, ei, v))
                            v = u
                        path.reverse()
                        return path
                    stack.append(e.to)
        return None

    while True:
        path = find_path()
        if path is None:
            break
        # bottleneck
        bottleneck = min(adj[u][ei].flow for u, ei, v in path)
        # identify start and target
        u0, ei0, v0 = path[0]  # u0 == S, v0 is start
        start = v0
        u_last, ei_last, v_last = path[-1]  # v_last == T, u_last is target
        target = u_last

        # find a species with matching start/target and remaining demand
        chosen = -1
        for i in range(k):
            if species[i][0] == start and species[i][1] == target and remaining[i] > 0:
                chosen = i
                break
        if chosen == -1:
            # Should not happen if flow is feasible
            print("NO")
            return

        amount = min(bottleneck, remaining[chosen])
        # subtract flow along path
        for u, ei, v in path:
            adj[u][ei].flow -= amount
            # reverse edge flow adjust
            rev_e = adj[v][adj[u][ei].rev]
            rev_e.flow += amount
        # record usage
        for u, ei, v in path:
            e = adj[u][ei]
            if e.orig_idx != -1:
                ans[chosen][e.orig_idx] += amount
        remaining[chosen] -= amount

    # Output
    print("YES")
    for i in range(k):
        print(' '.join(str(x) for x in ans[i]))

if __name__ == "__main__":
    main()