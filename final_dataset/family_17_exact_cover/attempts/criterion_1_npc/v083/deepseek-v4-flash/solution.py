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
                if ret:
                    self.adj[u][i][1] -= ret
                    self.adj[v][rev][1] += ret
                    return ret
        return 0
    
    def max_flow(self, s, t):
        flow = 0
        INF = 10**9
        while self.bfs(s, t):
            self.it = [0] * self.n
            while True:
                f = self.dfs(s, t, INF)
                if not f:
                    break
                flow += f
        return flow

def main():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    q = int(input_data[0])
    t = int(input_data[1])
    triples = []
    idx = 2
    for _ in range(t):
        a = int(input_data[idx]); b = int(input_data[idx+1]); c = int(input_data[idx+2])
        idx += 3
        triples.append((a, b, c))
    
    n_parts = 3 * q
    # nodes: 0..n_parts-1 parts, n_parts..n_parts+t-1 triples, n_parts+t source, n_parts+t+1 sink
    source = n_parts + t
    sink = n_parts + t + 1
    dinic = Dinic(n_parts + t + 2)
    
    for i in range(1, n_parts + 1):
        dinic.add_edge(source, i - 1, 1)
    
    for j, (a, b, c) in enumerate(triples):
        triple_node = n_parts + j
        dinic.add_edge(a - 1, triple_node, 1)
        dinic.add_edge(b - 1, triple_node, 1)
        dinic.add_edge(c - 1, triple_node, 1)
        dinic.add_edge(triple_node, sink, 1)
    
    flow = dinic.max_flow(source, sink)
    if flow != n_parts:
        print("NO")
        return
    
    print("YES")
    # Find which triples are used
    used = []
    for j, (a, b, c) in enumerate(triples):
        triple_node = n_parts + j
        # Check if edge triple_node -> sink has flow 0 (meaning used)
        for v, cap, rev in dinic.adj[triple_node]:
            if v == sink and cap == 0:
                used.append((a, b, c))
                break
    for triple in used:
        print(*triple)

if __name__ == "__main__":
    main()