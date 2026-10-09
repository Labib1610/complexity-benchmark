import sys
from collections import deque

INF = 10**15

class Dinic:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]
    
    def add_edge(self, u, v, cap):
        self.adj[u].append([v, cap, len(self.adj[v])])
        self.adj[v].append([u, 0, len(self.adj[u]) - 1])
    
    def bfs(self, s, t):
        self.level = [-1] * self.n
        q = deque([s])
        self.level[s] = 0
        while q:
            u = q.popleft()
            for v, cap, rev in self.adj[u]:
                if cap > 0 and self.level[v] == -1:
                    self.level[v] = self.level[u] + 1
                    q.append(v)
        return self.level[t] != -1
    
    def dfs(self, u, t, f):
        if u == t:
            return f
        for i in range(self.it[u], len(self.adj[u])):
            self.it[u] = i
            v, cap, rev = self.adj[u][i]
            if cap > 0 and self.level[v] == self.level[u] + 1:
                ret = self.dfs(v, t, min(f, cap))
                if ret:
                    self.adj[u][i][1] -= ret
                    self.adj[v][rev][1] += ret
                    return ret
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
    
    def min_cut_edges(self, s):
        visited = [False] * self.n
        q = deque([s])
        visited[s] = True
        while q:
            u = q.popleft()
            for v, cap, rev in self.adj[u]:
                if cap > 0 and not visited[v]:
                    visited[v] = True
                    q.append(v)
        cut_edges = []
        for u in range(self.n):
            if visited[u]:
                for v, cap, rev in self.adj[u]:
                    if not visited[v] and cap == 0:
                        # original edge u->v was cut
                        cut_edges.append((u, v))
        return cut_edges

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    B = int(next(it))
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
    
    # Build graph for min cut
    # We'll run isolating cut for each terminal
    chosen_edges = set()
    total_cost = 0
    
    for term in terminals:
        # Build Dinic graph
        dinic = Dinic(n + 2)
        S = n
        T = n + 1
        # super source to terminal
        dinic.add_edge(S, term, INF)
        # super sink from all other terminals
        for t in terminals:
            if t != term:
                dinic.add_edge(t, T, INF)
        # add original edges
        for u, v, w in edges:
            dinic.add_edge(u, v, w)
            dinic.add_edge(v, u, w)
        
        flow = dinic.max_flow(S, T)
        cut_edges = dinic.min_cut_edges(S)
        # cut_edges are (u,v) where u in S-side, v in T-side
        # map back to original edge
        for u, v in cut_edges:
            if u == S or v == T:
                continue
            # find original edge with this pair (u,v) or (v,u)
            for (a, b, w) in edges:
                if (a == u and b == v) or (a == v and b == u):
                    if (min(a,b), max(a,b)) not in chosen_edges:
                        chosen_edges.add((min(a,b), max(a,b)))
                        total_cost += w
                    break
    
    if total_cost <= B:
        print("YES")
        print(len(chosen_edges))
        for u, v in chosen_edges:
            print(u+1, v+1)
    else:
        print("NO")

if __name__ == "__main__":
    solve()