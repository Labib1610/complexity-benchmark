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
                        # original edge direction? We need original edge info
                        # We'll store original edges separately
                        pass
        return visited

def solve():
    n, m, k, B = map(int, input().split())
    terminals = list(map(int, input().split()))
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((u-1, v-1, w))
    
    # Try each terminal as source
    best_cost = None
    best_cut = None
    INF = 10**15
    
    for src in terminals:
        src -= 1
        # Build graph: n nodes + 1 super sink
        S = src
        T = n
        dinic = Dinic(n+1)
        # Add edges
        for u, v, w in edges:
            dinic.add_edge(u, v, w)
            dinic.add_edge(v, u, w)
        # Connect all other terminals to super sink with INF
        for t in terminals:
            t -= 1
            if t != src:
                dinic.add_edge(t, T, INF)
        
        flow = dinic.max_flow(S, T)
        if flow <= B:
            # Find cut edges
            visited = [False] * (n+1)
            q = deque([S])
            visited[S] = True
            while q:
                u = q.popleft()
                for v, cap, rev in dinic.graph[u]:
                    if cap > 0 and not visited[v]:
                        visited[v] = True
                        q.append(v)
            cut = []
            for u, v, w in edges:
                if visited[u] and not visited[v]:
                    cut.append((u+1, v+1))
                elif visited[v] and not visited[u]:
                    cut.append((u+1, v+1))
            if best_cost is None or flow < best_cost:
                best_cost = flow
                best_cut = cut
    
    if best_cost is None:
        print("NO")
    else:
        print("YES")
        print(len(best_cut))
        for u, v in best_cut:
            print(u, v)

if __name__ == "__main__":
    solve()