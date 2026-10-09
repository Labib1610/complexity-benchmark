import sys
from collections import deque

INF = 10**15

class Dinic:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]
        self.to = []
        self.cap = []
        self.rev = []

    def add_edge(self, u, v, cap):
        self.adj[u].append(len(self.to))
        self.to.append(v)
        self.cap.append(cap)
        self.rev.append(len(self.adj[v]))

        self.adj[v].append(len(self.to))
        self.to.append(u)
        self.cap.append(0)
        self.rev.append(len(self.adj[u]) - 1)

    def bfs(self, s, t):
        self.level = [-1] * self.n
        q = deque([s])
        self.level[s] = 0
        while q:
            u = q.popleft()
            for ei in self.adj[u]:
                if self.cap[ei] > 0 and self.level[self.to[ei]] == -1:
                    self.level[self.to[ei]] = self.level[u] + 1
                    q.append(self.to[ei])
        return self.level[t] != -1

    def dfs(self, u, t, f):
        if u == t:
            return f
        for i in range(self.it[u], len(self.adj[u])):
            ei = self.adj[u][i]
            v = self.to[ei]
            if self.cap[ei] > 0 and self.level[v] == self.level[u] + 1:
                ret = self.dfs(v, t, min(f, self.cap[ei]))
                if ret:
                    self.cap[ei] -= ret
                    self.cap[self.rev[ei]] += ret
                    return ret
            self.it[u] += 1
        return 0

    def max_flow(self, s, t):
        flow = 0
        while self.bfs(s, t):
            self.it = [0] * self.n
            while True:
                f = self.dfs(s, t, INF)
                if not f:
                    break
                flow += f
        return flow

    def reachable_from(self, s):
        vis = [False] * self.n
        q = deque([s])
        vis[s] = True
        while q:
            u = q.popleft()
            for ei in self.adj[u]:
                if self.cap[ei] > 0 and not vis[self.to[ei]]:
                    vis[self.to[ei]] = True
                    q.append(self.to[ei])
        return vis

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    B = int(next(it))

    hubs = [int(next(it)) for _ in range(k)]

    edges = []
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        edges.append((u, v, w))
        adj[u].append((v, w))
        adj[v].append((u, w))

    if k <= 1:
        print("YES")
        print(0)
        return

    # Precompute min cut between any two disjoint nonempty subsets of hubs
    # We'll compute on demand and cache.
    cut_cache = {}

    def min_cut_between(S_mask, T_mask):
        key = (S_mask, T_mask)
        if key in cut_cache:
            return cut_cache[key]

        # Build flow network
        dinic = Dinic(n + 2)
        src = n
        sink = n + 1

        for u, v, w in edges:
            dinic.add_edge(u, v, w)
            dinic.add_edge(v, u, w)

        for i in range(k):
            if (S_mask >> i) & 1:
                dinic.add_edge(src, hubs[i], INF)
            if (T_mask >> i) & 1:
                dinic.add_edge(hubs[i], sink, INF)

        flow = dinic.max_flow(src, sink)

        # Find cut edges
        reach = dinic.reachable_from(src)
        cut_edges = []
        for u, v, w in edges:
            if reach[u] != reach[v]:
                cut_edges.append((u, v))

        cut_cache[key] = (flow, cut_edges)
        return cut_cache[key]

    full_mask = (1 << k) - 1
    dp = [INF] * (1 << k)
    choice = [None] * (1 << k)

    for i in range(k):
        dp[1 << i] = 0

    for mask in range(1, 1 << k):
        if dp[mask] == INF:
            continue
        # find lowest set bit
        low = mask & -mask
        i = (low.bit_length() - 1)
        # enumerate submasks of mask that contain i and are not full mask
        sub = mask
        while sub:
            if (sub & low) and sub != mask:
                other = mask ^ sub
                cost, _ = min_cut_between(sub, other)
                new_cost = dp[other] + cost
                if new_cost < dp[mask]:
                    dp[mask] = new_cost
                    choice[mask] = (sub, other)
            sub = (sub - 1) & mask

    if dp[full_mask] > B:
        print("NO")
        return

    # Reconstruct edges
    removed_edges = []
    def reconstruct(mask):
        if mask & (mask - 1) == 0:
            return
        sub, other = choice[mask]
        _, cut_edges = min_cut_between(sub, other)
        removed_edges.extend(cut_edges)
        reconstruct(sub)
        reconstruct(other)

    reconstruct(full_mask)

    # Remove duplicates (an edge might appear in multiple cuts)
    seen = set()
    unique_edges = []
    for u, v in removed_edges:
        if u > v:
            u, v = v, u
        if (u, v) not in seen:
            seen.add((u, v))
            unique_edges.append((u, v))

    print("YES")
    print(len(unique_edges))
    for u, v in unique_edges:
        print(u + 1, v + 1)

if __name__ == "__main__":
    solve()