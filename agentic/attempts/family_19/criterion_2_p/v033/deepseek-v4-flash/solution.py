import sys
from collections import deque

input_data = sys.stdin.read().strip().split()
n, m, _ = map(int, input_data[:3])
s, t, d = map(int, input_data[3:6])
edges_input = []
idx = 6
for j in range(m):
    u = int(input_data[idx]) - 1
    v = int(input_data[idx+1]) - 1
    cap = int(input_data[idx+2])
    idx += 3
    edges_input.append((u, v, cap))

class Dinic:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]
    
    def add_edge(self, u, v, cap):
        self.adj[u].append([v, cap, len(self.adj[v])])
        self.adj[v].append([u, 0, len(self.adj[u]) - 1])
    
    def bfs(self, s, t):
        self.level = [-1]*self.n
        q = deque()
        q.append(s)
        self.level[s] = 0
        while q:
            u = q.popleft()
            for v, cap, rev in self.adj[u]:
                if cap > 0 and self.level[v] < 0:
                    self.level[v] = self.level[u] + 1
                    q.append(v)
        return self.level[t] >= 0
    
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
            self.it = [0]*self.n
            while True:
                f = self.dfs(s, t, INF)
                if f == 0:
                    break
                flow += f
        return flow

# Build flow network
dinic = Dinic(n)
edge_indices = []
for u, v, cap in edges_input:
    dinic.add_edge(u, v, cap)
    edge_indices.append((u, len(dinic.adj[u]) - 1))  # forward edge index in adj[u]

maxflow = dinic.max_flow(s-1, t-1)
if maxflow < d:
    print("NO")
else:
    print("YES")
    res = []
    for (u, eidx), (_, _, cap_orig) in zip(edge_indices, edges_input):
        # The remaining capacity on forward edge is cap_orig - flow
        flow_val = cap_orig - dinic.adj[u][eidx][1]
        res.append(str(flow_val))
    print(" ".join(res))