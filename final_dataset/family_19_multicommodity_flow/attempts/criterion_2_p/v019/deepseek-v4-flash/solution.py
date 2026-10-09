import sys
from collections import deque

input = sys.stdin.readline

class Dinic:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.edges = []

    def add_edge(self, u, v, cap):
        self.graph[u].append([v, cap, len(self.edges)])
        self.edges.append([u, v, cap])
        self.graph[v].append([u, 0, len(self.edges)])
        self.edges.append([v, u, 0])

    def bfs(self, s, t):
        self.level = [-1] * self.n
        q = deque([s])
        self.level[s] = 0
        while q:
            u = q.popleft()
            for v, cap, idx in self.graph[u]:
                if cap > 0 and self.level[v] < 0:
                    self.level[v] = self.level[u] + 1
                    q.append(v)
        return self.level[t] >= 0

    def dfs(self, u, t, f):
        if u == t:
            return f
        for i in range(self.it[u], len(self.graph[u])):
            self.it[u] = i
            v, cap, idx = self.graph[u][i]
            if cap > 0 and self.level[u] + 1 == self.level[v]:
                ret = self.dfs(v, t, min(f, cap))
                if ret > 0:
                    self.graph[u][i][1] -= ret
                    self.graph[v][idx ^ 1][1] += ret
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
    n, m, _ = map(int, input().split())
    s, t, d = map(int, input().split())
    s -= 1
    t -= 1

    dinic = Dinic(n)
    edges = []
    for _ in range(m):
        u, v, cap = map(int, input().split())
        u -= 1
        v -= 1
        dinic.add_edge(u, v, cap)
        edges.append((u, v, cap))

    maxflow = dinic.max_flow(s, t)
    if maxflow < d:
        print("NO")
        return

    # Output flow on each original edge
    result = []
    for i in range(m):
        u, v, cap = edges[i]
        # The forward edge is at index 2*i in dinic.edges
        # Its residual capacity is dinic.graph[u][?][1]
        # Easier: store flow from the reverse edge's capacity
        # Reverse edge index is 2*i+1
        rev_cap = dinic.edges[2*i + 1][2]  # this is the capacity of reverse edge
        # Actually we stored edges as [u, v, cap] but not the residual.
        # Let's instead track flow by looking at the graph structure.

    # Better: store the index of the forward edge when adding
    # We'll redo with storing indices.

if __name__ == "__main__":
    main()