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
    
    def bfs(self, s, t, level):
        for i in range(self.n):
            level[i] = -1
        q = deque([s])
        level[s] = 0
        while q:
            u = q.popleft()
            for v, cap, _ in self.adj[u]:
                if cap > 0 and level[v] < 0:
                    level[v] = level[u] + 1
                    q.append(v)
        return level[t] >= 0
    
    def dfs(self, u, t, f, level, it):
        if u == t:
            return f
        while it[u] < len(self.adj[u]):
            v, cap, rev = self.adj[u][it[u]]
            if cap > 0 and level[v] == level[u] + 1:
                ret = self.dfs(v, t, min(f, cap), level, it)
                if ret > 0:
                    self.adj[u][it[u]][1] -= ret
                    self.adj[v][rev][1] += ret
                    return ret
            it[u] += 1
        return 0
    
    def max_flow(self, s, t):
        flow = 0
        level = [-1] * self.n
        INF = 10**18
        while self.bfs(s, t, level):
            it = [0] * self.n
            while True:
                f = self.dfs(s, t, INF, level, it)
                if f == 0:
                    break
                flow += f
        return flow
    
    def min_cut_edges(self, s):
        visited = [False] * self.n
        q = deque([s])
        visited[s] = True
        while q:
            u = q.popleft()
            for v, cap, _ in self.adj[u]:
                if cap > 0 and not visited[v]:
                    visited[v] = True
                    q.append(v)
        cut_edges = []
        for u in range(self.n):
            if visited[u]:
                for v, cap, _ in self.adj[u]:
                    if not visited[v] and cap == 0:
                        # original edge direction? We need original edges.
                        # We'll store original edges separately.
                        pass
        return visited

def solve():
    n, m, k, B = map(int, input().split())
    reactive = list(map(int, input().split()))
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((u-1, v-1, w))
    
    # Build Gomory-Hu tree
    parent = [0] * n
    gomory_hu = [[] for _ in range(n)]
    flow_net = MaxFlow(n)
    for u, v, w in edges:
        flow_net.add_edge(u, v, w)
        flow_net.add_edge(v, u, w)
    
    # We'll compute min cut between each reactive site and others using Gomory-Hu
    # But simpler: For each pair of reactive sites, compute min cut and take the smallest.
    # Since k is small, we can do k-1 maxflow computations.
    
    best_cut = None
    best_cost = float('inf')
    
    for i in range(k):
        s = reactive[i] - 1
        for j in range(i+1, k):
            t = reactive[j] - 1
            mf = MaxFlow(n)
            for u, v, w in edges:
                mf.add_edge(u, v, w)
                mf.add_edge(v, u, w)
            cost = mf.max_flow(s, t)
            if cost < best_cost:
                best_cost = cost
                visited = mf.min_cut_edges(s)
                cut_edges = []
                for u, v, w in edges:
                    if visited[u] and not visited[v]:
                        cut_edges.append((u+1, v+1))
                    elif visited[v] and not visited[u]:
                        cut_edges.append((u+1, v+1))
                best_cut = cut_edges
    
    if best_cost <= B:
        print("YES")
        print(len(best_cut))
        for u, v in best_cut:
            print(u, v)
    else:
        print("NO")

if __name__ == "__main__":
    solve()