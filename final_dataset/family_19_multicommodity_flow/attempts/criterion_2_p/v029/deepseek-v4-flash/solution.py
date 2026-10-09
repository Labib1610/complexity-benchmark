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
            self.it[u] = i
            v, cap, rev = self.graph[u][i]
            if cap > 0 and self.level[u] < self.level[v]:
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
    _ = int(next(it))  # the "1" on first line
    s = int(next(it)) - 1
    t = int(next(it)) - 1
    d = int(next(it))
    
    edges = []
    dinic = Dinic(n)
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        c = int(next(it))
        edges.append((u, v, c))
        dinic.add_edge(u, v, c)
    
    maxflow = dinic.max_flow(s, t)
    if maxflow < d:
        print("NO")
        return
    
    # Extract flow on each original edge
    flow_values = []
    for u, v, c in edges:
        # find the forward edge in dinic.graph[u]
        for idx, (to, cap, rev) in enumerate(dinic.graph[u]):
            if to == v and cap <= c:  # forward edge has cap reduced from original
                # original cap - current cap = flow
                flow = c - cap
                flow_values.append(flow)
                break
    
    print("YES")
    print(" ".join(map(str, flow_values)))

if __name__ == "__main__":
    main()