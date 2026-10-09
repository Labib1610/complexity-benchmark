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
        q = deque()
        q.append(s)
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

def main():
    input_data = sys.stdin.read().strip().split()
    n, m, _ = map(int, input_data[:3])
    s, t, d = map(int, input_data[3:6])
    edges = []
    idx = 6
    for _ in range(m):
        u, v, c = map(int, input_data[idx:idx+3])
        idx += 3
        edges.append((u-1, v-1, c))
    
    dinic = Dinic(n)
    for u, v, c in edges:
        dinic.add_edge(u, v, c)
    
    flow = dinic.max_flow(s-1, t-1)
    if flow < d:
        print("NO")
        return
    
    # Extract flow on each original edge
    result = []
    for u, v, c in edges:
        # find the forward edge in graph
        for e in dinic.graph[u]:
            if e[0] == v and e[1] < c:
                # flow = original cap - remaining cap
                result.append(c - e[1])
                break
        else:
            result.append(0)
    
    print("YES")
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()