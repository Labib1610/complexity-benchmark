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

def main():
    n, m, s, t, B = map(int, input().split())
    s -= 1
    t -= 1
    dinic = Dinic(n)
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        dinic.add_edge(u, v, w)
        dinic.add_edge(v, u, w)  # undirected
        edges.append((u, v, w))
    
    min_cut_cost = dinic.max_flow(s, t)
    if min_cut_cost > B:
        print("NO")
        return
    
    cut_edges = dinic.min_cut_edges(s)
    # Map back to original edge indices
    edge_set = set()
    for u, v in cut_edges:
        # find original edge
        for idx, (a, b, w) in enumerate(edges):
            if (a == u and b == v) or (a == v and b == u):
                edge_set.add((a+1, b+1))
                break
    
    print("YES")
    print(len(edge_set))
    for u, v in edge_set:
        print(u, v)

if __name__ == "__main__":
    main()