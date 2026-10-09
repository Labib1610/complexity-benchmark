import sys
from collections import deque

class MaxFlow:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]
    
    def add_edge(self, u, v, cap):
        self.adj[u].append([v, cap, len(self.adj[v])])
        self.adj[v].append([u, 0, len(self.adj[u]) - 1])
    
    def bfs(self, s, t, level):
        for i in range(self.n):
            level[i] = -1
        q = deque()
        level[s] = 0
        q.append(s)
        while q:
            v = q.popleft()
            for to, cap, rev in self.adj[v]:
                if cap > 0 and level[to] < 0:
                    level[to] = level[v] + 1
                    q.append(to)
        return level[t] >= 0
    
    def dfs(self, v, t, f, level, it):
        if v == t:
            return f
        while it[v] < len(self.adj[v]):
            to, cap, rev = self.adj[v][it[v]]
            if cap > 0 and level[v] + 1 == level[to]:
                ret = self.dfs(to, t, min(f, cap), level, it)
                if ret > 0:
                    self.adj[v][it[v]][1] -= ret
                    self.adj[to][rev][1] += ret
                    return ret
            it[v] += 1
        return 0
    
    def max_flow(self, s, t):
        flow = 0
        INF = 10**18
        level = [-1] * self.n
        while self.bfs(s, t, level):
            it = [0] * self.n
            while True:
                f = self.dfs(s, t, INF, level, it)
                if f == 0:
                    break
                flow += f
        return flow
    
    def min_cut_edges(self, s):
        visited = [False] * self.n
        q = deque([s])
        visited[s] = True
        while q:
            v = q.popleft()
            for to, cap, rev in self.adj[v]:
                if cap > 0 and not visited[to]:
                    visited[to] = True
                    q.append(to)
        cut_edges = []
        for v in range(self.n):
            if visited[v]:
                for to, cap, rev in self.adj[v]:
                    if not visited[to] and cap == 0:
                        cut_edges.append((v, to))
        return cut_edges

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    s = int(next(it)) - 1
    t = int(next(it)) - 1
    B = int(next(it))
    
    mf = MaxFlow(n)
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        edges.append((u, v, w))
        mf.add_edge(u, v, w)
        mf.add_edge(v, u, w)  # undirected: add both directions with capacity w
    
    flow = mf.max_flow(s, t)
    if flow > B:
        print("NO")
        return
    
    cut_edges = mf.min_cut_edges(s)
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
    solve()