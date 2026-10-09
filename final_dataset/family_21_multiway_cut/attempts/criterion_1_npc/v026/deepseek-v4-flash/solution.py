import sys
from collections import deque

input = sys.stdin.readline

class Dinic:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.edges = []  # (u, v, cap, idx)

    def add_edge(self, u, v, cap, idx):
        self.graph[u].append([v, cap, len(self.edges)])
        self.edges.append((u, v, cap, idx))
        self.graph[v].append([u, 0, len(self.edges)])
        self.edges.append((v, u, 0, idx))

    def bfs(self, s, t):
        self.level = [-1] * self.n
        q = deque([s])
        self.level[s] = 0
        while q:
            u = q.popleft()
            for v, cap, _ in self.graph[u]:
                if cap > 0 and self.level[v] == -1:
                    self.level[v] = self.level[u] + 1
                    q.append(v)
        return self.level[t] != -1

    def dfs(self, u, t, f):
        if u == t:
            return f
        for i in range(self.it[u], len(self.graph[u])):
            v, cap, eid = self.graph[u][i]
            if cap > 0 and self.level[v] == self.level[u] + 1:
                ret = self.dfs(v, t, min(f, cap))
                if ret:
                    self.graph[u][i][1] -= ret
                    self.edges[eid ^ 1] = (v, u, self.edges[eid ^ 1][2] + ret, self.edges[eid ^ 1][3])
                    self.edges[eid] = (u, v, self.edges[eid][2] - ret, self.edges[eid][3])
                    return ret
            self.it[u] += 1
        return 0

    def max_flow(self, s, t):
        flow = 0
        INF = 10**18
        while self.bfs(s, t):
            self.it = [0] * self.n
            while True:
                pushed = self.dfs(s, t, INF)
                if not pushed:
                    break
                flow += pushed
        return flow

    def min_cut_edges(self, s):
        visited = [False] * self.n
        q = deque([s])
        visited[s] = True
        while q:
            u = q.popleft()
            for v, cap, _ in self.graph[u]:
                if cap > 0 and not visited[v]:
                    visited[v] = True
                    q.append(v)
        cut_edges = []
        for u in range(self.n):
            if visited[u]:
                for v, cap, eid in self.graph[u]:
                    if not visited[v] and self.edges[eid][2] == 0:
                        # original edge was (u,v)
                        orig_idx = self.edges[eid][3]
                        cut_edges.append(orig_idx)
        return cut_edges


def solve():
    n, m, k, B = map(int, input().split())
    licensed = list(map(int, input().split()))
    licensed = [x-1 for x in licensed]

    edges = []
    adj = [[] for _ in range(n)]
    for idx in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        edges.append((u, v, w, idx))
        adj[u].append((v, w, idx))
        adj[v].append((u, w, idx))

    # Build Dinic graph
    dinic = Dinic(n)
    for u, v, w, idx in edges:
        dinic.add_edge(u, v, w, idx)
        dinic.add_edge(v, u, w, idx)  # undirected

    removed = set()
    total_cost = 0

    # We'll attempt to separate each pair among licensed
    for i in range(k):
        for j in range(i+1, k):
            s = licensed[i]
            t = licensed[j]
            # reset edge capacities
            dinic2 = Dinic(n)
            for u, v, w, idx in edges:
                if idx not in removed:
                    dinic2.add_edge(u, v, w, idx)
                    dinic2.add_edge(v, u, w, idx)
            cut_cost = dinic2.max_flow(s, t)
            if total_cost + cut_cost > B:
                print("NO")
                return
            # find cut edges
            cut_idx = dinic2.min_cut_edges(s)
            for idx in cut_idx:
                if idx not in removed:
                    removed.add(idx)
                    total_cost += edges[idx][2]
    if total_cost > B:
        print("NO")
        return
    print("YES")
    print(len(removed))
    for idx in removed:
        u, v, w, _ = edges[idx]
        print(u+1, v+1)

if __name__ == "__main__":
    solve()