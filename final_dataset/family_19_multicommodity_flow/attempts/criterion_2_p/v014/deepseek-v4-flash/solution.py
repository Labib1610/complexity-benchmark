import sys
from collections import deque

input = sys.stdin.readline

class MaxFlow:
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
        INF = 10**18
        while self.bfs(s, t):
            self.it = [0] * self.n
            while True:
                pushed = self.dfs(s, t, INF)
                if not pushed:
                    break
                flow += pushed
        return flow

def main():
    n, m, _ = map(int, input().split())
    s, t, d = map(int, input().split())
    s -= 1
    t -= 1
    
    edges = []
    mf = MaxFlow(n)
    
    for i in range(m):
        u, v, cap = map(int, input().split())
        u -= 1
        v -= 1
        edges.append((u, v, cap))
        mf.add_edge(u, v, cap)
    
    flow = mf.max_flow(s, t)
    
    if flow < d:
        print("NO")
        return
    
    # Extract actual flow on original edges
    ans = []
    for u, v, cap in edges:
        # Find the edge in residual graph: it's the reverse of the added residual
        # Actually use adjacency search
        found = None
        for e in mf.adj[u]:
            if e[0] == v and e[1] < cap:
                # Since we added forward cap and reverse 0, after flow the forward capacity decreases
                # and reverse increases. So flow = original cap - current forward cap
                flow_on_edge = cap - e[1]
                found = flow_on_edge
                break
        ans.append(str(found if found is not None else 0))
    
    print("YES")
    print(" ".join(ans))

if __name__ == "__main__":
    main()