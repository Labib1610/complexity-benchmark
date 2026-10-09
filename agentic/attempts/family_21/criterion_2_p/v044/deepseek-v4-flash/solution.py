import sys
from collections import deque

class Dinic:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]
    
    def add_edge(self, u, v, cap):
        self.adj[u].append([v, cap, len(self.adj[v])])
        self.adj[v].append([u, 0, len(self.adj[u]) - 1])
    
    def bfs(self, s, t):
        self.level = [-1] * self.n
        q = deque()
        q.append(s)
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
                if ret > 0:
                    self.adj[u][i][1] -= ret
                    self.adj[v][rev][1] += ret
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

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    s = int(next(it)) - 1
    t = int(next(it)) - 1
    B = int(next(it))
    
    edges = []
    dinic = Dinic(n)
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        edges.append((u, v, w))
        dinic.add_edge(u, v, w)
        dinic.add_edge(v, u, w)  # bidirectional
    
    maxflow = dinic.max_flow(s, t)
    if maxflow > B:
        print("NO")
        return
    
    # Find min cut edges: reachable from s in residual graph
    reachable = [False] * n
    q = deque([s])
    reachable[s] = True
    while q:
        u = q.popleft()
        for v, cap, rev in dinic.adj[u]:
            if cap > 0 and not reachable[v]:
                reachable[v] = True
                q.append(v)
    
    cut_edges = []
    for u, v, w in edges:
        if reachable[u] and not reachable[v]:
            cut_edges.append((u+1, v+1))
        elif reachable[v] and not reachable[u]:
            cut_edges.append((u+1, v+1))
    
    print("YES")
    print(len(cut_edges))
    for u, v in cut_edges:
        print(u, v)

if __name__ == "__main__":
    main()