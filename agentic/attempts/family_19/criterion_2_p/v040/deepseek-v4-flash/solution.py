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

def main():
    n, m, _ = map(int, input().split())
    s, t, d = map(int, input().split())
    s -= 1
    t -= 1
    
    dinic = Dinic(n)
    edges = []
    for _ in range(m):
        u, v, c = map(int, input().split())
        u -= 1
        v -= 1
        dinic.add_edge(u, v, c)
        edges.append((u, v, c, len(dinic.graph[u]) - 1))
    
    flow = dinic.max_flow(s, t)
    if flow < d:
        print("NO")
        return
    
    # We need to output allocation for each edge
    result = []
    for u, v, c, rev_idx in edges:
        # Find the forward edge in graph[u]
        for idx, (to, cap, rev) in enumerate(dinic.graph[u]):
            if to == v and idx == rev_idx:
                # original capacity - remaining capacity = flow used
                used = c - cap
                result.append(str(used))
                break
    
    print("YES")
    print(" ".join(result))

if __name__ == "__main__":
    main()