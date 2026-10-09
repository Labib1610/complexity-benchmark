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
        q = deque([s])
        self.level[s] = 0
        while q:
            u = q.popleft()
            for v, cap, _ in self.adj[u]:
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
                pushed = self.dfs(s, t, INF)
                if not pushed:
                    break
                flow += pushed
        return flow

def main():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    q = int(next(it))
    t = int(next(it))
    
    triples = []
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        c = int(next(it))
        triples.append((a, b, c))
    
    # Node indices:
    # source = 0
    # config nodes: 1..t
    # badge nodes: t+1 .. t+3q
    # sink = t + 3q + 1
    source = 0
    sink = t + 3*q + 1
    dinic = Dinic(sink + 1)
    
    # source -> config
    for i in range(t):
        dinic.add_edge(source, 1 + i, 1)
    
    # config -> badges
    for i, (a, b, c) in enumerate(triples):
        u = 1 + i
        for badge in (a, b, c):
            v = t + badge
            dinic.add_edge(u, v, 1)
    
    # badge -> sink
    for badge in range(1, 3*q + 1):
        v = t + badge
        dinic.add_edge(v, sink, 1)
    
    flow = dinic.max_flow(source, sink)
    
    if flow != 3*q:
        print("NO")
        return
    
    # Reconstruct chosen configs
    chosen = []
    for i, (a, b, c) in enumerate(triples):
        u = 1 + i
        used = True
        for badge in (a, b, c):
            v = t + badge
            # find edge u->v in adjacency
            found = False
            for edge in dinic.adj[u]:
                if edge[0] == v and edge[1] == 0:
                    found = True
                    break
            if not found:
                used = False
                break
        if used:
            chosen.append((a, b, c))
    
    # The flow guarantees exactly q chosen, but let's sort by first badge for neatness
    chosen.sort()
    print("YES")
    for a, b, c in chosen:
        print(a, b, c)

if __name__ == "__main__":
    main()