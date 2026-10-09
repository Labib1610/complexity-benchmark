import sys
from collections import deque

input = sys.stdin.readline

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
    q, t = map(int, input().split())
    triples = []
    for _ in range(t):
        a, b, c = map(int, input().split())
        triples.append((a, b, c))
    
    # Node indices:
    # 0: source
    # 1..t: triple nodes
    # t+1 .. t+3q: personnel nodes
    # t+3q+1: sink
    source = 0
    triple_start = 1
    person_start = triple_start + t
    sink = person_start + 3*q
    
    dinic = Dinic(sink + 1)
    
    for i in range(t):
        dinic.add_edge(source, triple_start + i, 1)
        a, b, c = triples[i]
        dinic.add_edge(triple_start + i, person_start + (a-1), 1)
        dinic.add_edge(triple_start + i, person_start + (b-1), 1)
        dinic.add_edge(triple_start + i, person_start + (c-1), 1)
    
    for i in range(3*q):
        dinic.add_edge(person_start + i, sink, 1)
    
    flow = dinic.max_flow(source, sink)
    
    if flow < q:
        print("NO")
        return
    
    print("YES")
    used = [False] * t
    for i in range(t):
        if used[i]:
            continue
        # Check if this triple is used in the flow
        # The edge source -> triple has capacity 0 if used
        edge = dinic.adj[source][i]
        if edge[1] == 0:  # capacity consumed
            used[i] = True
            print(*triples[i])
    
if __name__ == "__main__":
    main()