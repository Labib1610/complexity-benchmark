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

def solve():
    n, m, k, B = map(int, input().split())
    anchors = list(map(int, input().split()))
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((u-1, v-1, w))
    
    # We'll try to separate each anchor from the rest
    best_cost = float('inf')
    best_cut = None
    
    for anchor in anchors:
        # Build flow network: source = anchor, sink = super sink connected to all other anchors
        source = anchor - 1
        sink = n
        dinic = Dinic(n + 1)
        for u, v, w in edges:
            dinic.add_edge(u, v, w)
            dinic.add_edge(v, u, w)
        # connect all other anchors to sink with INF
        INF = 10**15
        for a in anchors:
            if a != anchor:
                dinic.add_edge(a - 1, sink, INF)
        
        cost = dinic.max_flow(source, sink)
        if cost < best_cost:
            best_cost = cost
            # find cut edges
            visited = [False] * (n + 1)
            q = deque([source])
            visited[source] = True
            while q:
                u = q.popleft()
                for v, cap, rev in dinic.graph[u]:
                    if cap > 0 and not visited[v]:
                        visited[v] = True
                        q.append(v)
            cut_edges = []
            for u, v, w in edges:
                if visited[u] != visited[v]:
                    cut_edges.append((u+1, v+1))
            best_cut = cut_edges
    
    if best_cost <= B:
        print("YES")
        print(len(best_cut))
        for u, v in best_cut:
            print(u, v)
    else:
        print("NO")

if __name__ == "__main__":
    solve()