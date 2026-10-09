from collections import deque
import sys

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
            for v, cap, _ in self.graph[u]:
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

def main():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    s = int(next(it)) - 1
    t = int(next(it)) - 1
    budget = int(next(it))

    edges = []
    dinic = Dinic(n)
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        edges.append((u, v, w))
        dinic.add_edge(u, v, w)
        dinic.add_edge(v, u, w)

    min_cut_cost = dinic.max_flow(s, t)

    if min_cut_cost > budget:
        print("NO")
        return

    # Find reachable nodes from source in residual graph
    reachable = [False] * n
    q = deque([s])
    reachable[s] = True
    while q:
        u = q.popleft()
        for v, cap, _ in dinic.graph[u]:
            if cap > 0 and not reachable[v]:
                reachable[v] = True
                q.append(v)

    # Edges crossing the cut
    cut_edges = []
    for i, (u, v, w) in enumerate(edges):
        if reachable[u] != reachable[v]:
            cut_edges.append(i + 1)

    print("YES")
    print(len(cut_edges))
    for idx in cut_edges:
        u, v, _ = edges[idx - 1]
        print(u + 1, v + 1)

if __name__ == "__main__":
    main()