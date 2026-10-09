from collections import deque
import sys

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
        q = deque()
        level[s] = 0
        q.append(s)
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

def solve():
    input_data = sys.stdin.read().strip().split()
    n, m, _ = map(int, input_data[:3])
    s, t, d = map(int, input_data[3:6])
    s -= 1
    t -= 1
    edges = []
    idx = 6
    for _ in range(m):
        u, v, limit = map(int, input_data[idx:idx+3])
        idx += 3
        edges.append((u-1, v-1, limit))
    
    # Node indices: 0..n-1 original, n = super source, n+1 = super sink
    S = n
    T = n + 1
    mf = MaxFlow(n + 2)
    
    balance = [0] * n
    balance[s] -= d
    balance[t] += d
    
    total_required = 0
    for i in range(n):
        if balance[i] > 0:
            mf.add_edge(S, i, balance[i])
            total_required += balance[i]
        elif balance[i] < 0:
            mf.add_edge(i, T, -balance[i])
    
    for u, v, limit in edges:
        mf.add_edge(u, v, limit)
    
    flow = mf.max_flow(S, T)
    if flow != total_required:
        print("NO")
        return
    
    print("YES")
    # Recover flow on original edges
    # Original edges were added after balance edges, so we can track them
    # We'll store the edge indices in the adjacency list
    # Simpler: rebuild with tracking
    # Let's redo with tracking
    mf2 = MaxFlow(n + 2)
    edge_refs = []
    for i in range(n):
        if balance[i] > 0:
            mf2.add_edge(S, i, balance[i])
        elif balance[i] < 0:
            mf2.add_edge(i, T, -balance[i])
    for u, v, limit in edges:
        edge_refs.append(mf2.add_edge(u, v, limit))
    
    mf2.max_flow(S, T)
    result = []
    for u, v, limit in edges:
        # find the forward edge in mf2.adj[u]
        for e in mf2.adj[u]:
            if e[0] == v and e[1] < limit:
                result.append(limit - e[1])
                break
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    solve()