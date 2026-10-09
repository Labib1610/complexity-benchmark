import sys
from collections import deque

input = sys.stdin.readline

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
            self.it[u] = i
            v, cap, rev = self.graph[u][i]
            if cap > 0 and self.level[u] + 1 == self.level[v]:
                ret = self.dfs(v, t, min(f, cap))
                if ret > 0:
                    self.graph[u][i][1] -= ret
                    self.graph[v][rev][1] += ret
                    return ret
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
        visited = [False] * self.n
        q = deque([s])
        visited[s] = True
        while q:
            u = q.popleft()
            for v, cap, rev in self.graph[u]:
                if cap > 0 and not visited[v]:
                    visited[v] = True
                    q.append(v)
        cut_edges = []
        for u in range(self.n):
            if visited[u]:
                for v, cap, rev in self.graph[u]:
                    if not visited[v] and cap == 0:
                        cut_edges.append((u, v))
        return cut_edges

def solve():
    n, m, k, B = map(int, input().split())
    terminals = list(map(int, input().split()))
    terminals = [t - 1 for t in terminals]
    
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        edges.append((u, v, w))
    
    # Try isolating each terminal
    best_cost = float('inf')
    best_edges = None
    
    for term in terminals:
        # Build graph with super source = term, super sink = all other terminals connected to a dummy sink
        # We'll create a dummy sink node n
        dinic = Dinic(n + 1)
        sink = n
        for u, v, w in edges:
            dinic.add_edge(u, v, w)
            dinic.add_edge(v, u, w)
        # Connect all other terminals to sink with INF
        INF = 10**15
        for t in terminals:
            if t != term:
                dinic.add_edge(t, sink, INF)
        
        cost = dinic.max_flow(term, sink)
        if cost < best_cost:
            best_cost = cost
            cut_edges = dinic.min_cut_edges(term)
            # Filter out edges to sink (they are artificial)
            real_cut = [(u+1, v+1) for u, v in cut_edges if u < n and v < n]
            best_edges = real_cut
    
    if best_cost <= B:
        print("YES")
        print(len(best_edges))
        for u, v in best_edges:
            print(u, v)
    else:
        print("NO")

if __name__ == "__main__":
    solve()