import sys
from collections import deque

input = sys.stdin.readline

class Dinic:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
    
    def add_edge(self, fr, to, cap):
        forward = [to, cap, None]
        backward = [fr, 0, forward]
        forward[2] = backward
        self.graph[fr].append(forward)
        self.graph[to].append(backward)
    
    def bfs(self, s, t):
        self.level = [-1] * self.n
        q = deque([s])
        self.level[s] = 0
        while q:
            v = q.popleft()
            for to, cap, rev in self.graph[v]:
                if cap > 0 and self.level[to] < 0:
                    self.level[to] = self.level[v] + 1
                    q.append(to)
        return self.level[t] >= 0
    
    def dfs(self, v, t, f):
        if v == t:
            return f
        for i in range(self.it[v], len(self.graph[v])):
            self.it[v] = i
            to, cap, rev = self.graph[v][i]
            if cap > 0 and self.level[v] + 1 == self.level[to]:
                ret = self.dfs(to, t, min(f, cap))
                if ret > 0:
                    self.graph[v][i][1] -= ret
                    rev[1] += ret
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
    
    edges = []
    dinic = Dinic(n)
    for idx in range(m):
        u, v, C = map(int, input().split())
        u -= 1
        v -= 1
        dinic.add_edge(u, v, C)
        edges.append((u, v, C))
    
    flow = dinic.max_flow(s, t)
    if flow < d:
        print("NO")
        return
    
    # Extract flow values
    result = []
    for u, v, C in edges:
        # find the forward edge in graph
        for to, cap, rev in dinic.graph[u]:
            if to == v and rev[1] > 0:  # rev is backward edge, its cap is flow
                # flow on this edge = rev[1]
                result.append(rev[1])
                break
    
    print("YES")
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()