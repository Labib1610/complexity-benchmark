import sys
from collections import deque

class Dinic:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
    
    def add_edge(self, u, v, cap):
        self.graph[u].append([v, cap, len(self.graph[v])])
        self.graph[v].append([u, 0, len(self.graph[u]) - 1])
    
    def bfs(self, s, t):
        self.level = [-1] * self.n
        q = deque([s])
        self.level[s] = 0
        while q:
            u = q.popleft()
            for v, cap, rev in self.graph[u]:
                if cap > 0 and self.level[v] < 0:
                    self.level[v] = self.level[u] + 1
                    q.append(v)
        return self.level[t] >= 0
    
    def dfs(self, u, t, f):
        if u == t:
            return f
        for i in range(self.it[u], len(self.graph[u])):
            v, cap, rev = self.graph[u][i]
            if cap > 0 and self.level[v] == self.level[u] + 1:
                ret = self.dfs(v, t, min(f, cap))
                if ret > 0:
                    self.graph[u][i][1] -= ret
                    self.graph[v][rev][1] += ret
                    return ret
            self.it[u] += 1
        return 0
    
    def max_flow(self, s, t):
        flow = 0
        INF = 10**18
        while self.bfs(s, t):
            self.it = [0] * self.n
            while True:
                f = self.dfs(s, t, INF)
                if f == 0:
                    break
                flow += f
        return flow
    
    def min_cut_edges(self, s):
        # BFS from source in residual graph
        visited = [False] * self.n
        q = deque([s])
        visited[s] = True
        while q:
            u = q.popleft()
            for v, cap, rev in self.graph[u]:
                if cap > 0 and not visited[v]:
                    visited[v] = True
                    q.append(v)
        # Edges from visited to unvisited
        cut = []
        for u in range(self.n):
            if visited[u]:
                for v, cap, rev in self.graph[u]:
                    if not visited[v] and cap == 0:
                        # original edge u->v with cap 0 means it's saturated
                        # but we need original undirected edge; we stored both directions
                        # We'll reconstruct from original edge list later
                        cut.append((u, v))
        return cut

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it)); B = int(next(it))
    terminals = [int(next(it)) - 1 for _ in range(k)]
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        edges.append((u, v, w))
    
    if k <= 1:
        print("YES")
        print(0)
        return
    
    INF = 10**15
    best_cost = INF
    best_cut_edges = None
    
    # Try each terminal as source
    for src in terminals:
        # Build graph: original nodes + super sink (n)
        S = src
        T = n
        dinic = Dinic(n + 1)
        # Add original edges (undirected)
        for u, v, w in edges:
            dinic.add_edge(u, v, w)
            dinic.add_edge(v, u, w)
        # Connect all other terminals to super sink with INF
        for t in terminals:
            if t != S:
                dinic.add_edge(t, T, INF)
        # Compute min cut
        flow = dinic.max_flow(S, T)
        if flow < best_cost:
            best_cost = flow
            # Get cut edges
            visited = [False] * (n + 1)
            q = deque([S])
            visited[S] = True
            while q:
                u = q.popleft()
                for v, cap, rev in dinic.graph[u]:
                    if cap > 0 and not visited[v]:
                        visited[v] = True
                        q.append(v)
            cut = []
            for u in range(n):
                if visited[u]:
                    for v, cap, rev in dinic.graph[u]:
                        if v < n and not visited[v] and cap == 0:
                            # This edge is saturated; but we need original undirected edge
                            # Check both directions: if either direction is saturated, it's in cut
                            # We'll just check original edges
                            pass
            # Reconstruct from original edges
            cut_edges = []
            for u, v, w in edges:
                if visited[u] != visited[v]:
                    cut_edges.append((u+1, v+1))
            best_cut_edges = cut_edges
    
    if best_cost <= B:
        print("YES")
        print(len(best_cut_edges))
        for u, v in best_cut_edges:
            print(u, v)
    else:
        print("NO")

if __name__ == "__main__":
    solve()