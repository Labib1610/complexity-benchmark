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
        q = deque()
        q.append(s)
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
                        # This edge is saturated and goes from reachable to non-reachable
                        # But we need original edge info; we stored reverse index.
                        # We'll reconstruct from original edges later.
                        pass
        return visited

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
        edges.append((u, v, w))
        dinic.add_edge(u, v, w)
        dinic.add_edge(v, u, w)  # undirected
    
    maxflow = dinic.max_flow(s, t)
    if maxflow > B:
        print("NO")
        return
    
    # Find min cut edges
    visited = [False] * n
    q = deque([s])
    visited[s] = True
    while q:
        u = q.popleft()
        for v, cap, rev in dinic.graph[u]:
            if cap > 0 and not visited[v]:
                visited[v] = True
                q.append(v)
    
    removed = []
    for u, v, w in edges:
        if visited[u] != visited[v]:
            removed.append((u+1, v+1))
    
    print("YES")
    print(len(removed))
    for u, v in removed:
        print(u, v)

if __name__ == "__main__":
    main()