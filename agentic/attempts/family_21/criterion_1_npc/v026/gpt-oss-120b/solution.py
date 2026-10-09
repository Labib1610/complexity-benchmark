import sys
sys.setrecursionlimit(1 << 25)

INF = 10 ** 18

class Dinic:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]

    def add_edge(self, u, v, cap, idx=-1):
        # idx stores original edge id for later identification (if needed)
        self.adj[u].append([v, cap, len(self.adj[v]), idx])
        self.adj[v].append([u, 0,   len(self.adj[u]) - 1, -1])

    def bfs_level(self, s, t):
        self.level = [-1] * self.n
        q = [s]
        self.level[s] = 0
        for u in q:
            for v, cap, rev, _ in self.adj[u]:
                if cap and self.level[v] == -1:
                    self.level[v] = self.level[u] + 1
                    q.append(v)
        return self.level[t] != -1

    def dfs(self, u, t, f):
        if u == t:
            return f
        for i in range(self.it[u], len(self.adj[u])):
            self.it[u] = i
            v, cap, rev, _ = self.adj[u][i]
            if cap and self.level[v] == self.level[u] + 1:
                ret = self.dfs(v, t, min(f, cap))
                if ret:
                    self.adj[u][i][1] -= ret
                    self.adj[v][rev][1] += ret
                    return ret
        return 0

    def max_flow(self, s, t):
        flow = 0
        while self.bfs_level(s, t):
            self.it = [0] * self.n
            while True:
                pushed = self.dfs(s, t, INF)
                if not pushed:
                    break
                flow += pushed
        return flow

    def min_cut_edges(self, s):
        """return list of original edge ids that cross the cut (source side reachable)"""
        visited = [False] * self.n
        stack = [s]
        visited[s] = True
        while stack:
            u = stack.pop()
            for v, cap, rev, _ in self.adj[u]:
                if cap and not visited[v]:
                    visited[v] = True
                    stack.append(v)
        cut_edges = []
        for u in range(self.n):
            for v, cap, rev, idx in self.adj[u]:
                if idx >= 0:          # original edge
                    if visited[u] != visited[v]:
                        cut_edges.append(idx)
        return cut_edges


def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it)); B = int(next(it))
    specials = [int(next(it)) - 1 for _ in range(k)]
    edges = []
    for i in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        edges.append((u, v, w))

    # map terminal index -> vertex id
    term_to_vertex = specials

    # pre‑compute cut cost and cut edge list for every pair of disjoint masks
    maxmask = 1 << k
    cut_cost = [[INF] * maxmask for _ in range(maxmask)]
    cut_edges = [[None] * maxmask for _ in range(maxmask)]

    # helper to build flow graph for a given pair of masks
    def compute(mask_a, mask_b):
        dinic = Dinic(n + 2)
        S = n
        T = n + 1
        # original edges
        for idx, (u, v, w) in enumerate(edges):
            dinic.add_edge(u, v, w, idx)
            dinic.add_edge(v, u, w, idx)   # because graph is undirected, add both directions
        # connect terminals
        for i in range(k):
            if (mask_a >> i) & 1:
                dinic.add_edge(S, term_to_vertex[i], INF)
            if (mask_b >> i) & 1:
                dinic.add_edge(term_to_vertex[i], T, INF)
        flow = dinic.max_flow(S, T)
        cut = dinic.min_cut_edges(S)
        return flow, cut

    # compute for all disjoint non‑empty masks
    for mask_a in range(1, maxmask):
        for mask_b in range(1, maxmask):
            if mask_a & mask_b:
                continue
            if mask_a > mask_b:   # compute each unordered pair once
                continue
            cost, edgelist = compute(mask_a, mask_b)
            cut_cost[mask_a][mask_b] = cut_cost[mask_b][mask_a] = cost
            cut_edges[mask_a][mask_b] = cut_edges[mask_b][mask_a] = edgelist

    # DP
    dp = [INF] * maxmask
    best_sub = [0] * maxmask
    for mask in range(1, maxmask):
        if mask & (mask - 1) == 0:   # single bit
            dp[mask] = 0
            continue
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if other:
                cur = dp[sub] + dp[other] + cut_cost[sub][other]
                if cur < dp[mask]:
                    dp[mask] = cur
                    best_sub[mask] = sub
            sub = (sub - 1) & mask

    full = maxmask - 1
    if dp[full] > B:
        print("NO")
        return

    # reconstruction
    answer_edges = set()

    def recon(mask):
        if mask & (mask - 1) == 0:
            return
        sub = best_sub[mask]
        other = mask ^ sub
        for eid in cut_edges[sub][other]:
            answer_edges.add(eid)
        recon(sub)
        recon(other)

    recon(full)

    print("YES")
    print(len(answer_edges))
    for eid in answer_edges:
        u, v, _ = edges[eid]
        print(u + 1, v + 1)


if __name__ == "__main__":
    solve()