import sys
from collections import deque

input = sys.stdin.readline

class MaxFlow:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]
        self.cap = {}
    
    def add_edge(self, u, v, c):
        self.adj[u].append((v, len(self.adj[v]), c))
        self.adj[v].append((u, len(self.adj[u]) - 1, 0))
    
    def bfs(self, s, t, level):
        q = deque([s])
        level[s] = 0
        while q:
            u = q.popleft()
            for v, rev, c in self.adj[u]:
                if c > 0 and level[v] < 0:
                    level[v] = level[u] + 1
                    q.append(v)
        return level[t] >= 0
    
    def dfs(self, u, t, f, level, it):
        if u == t:
            return f
        for i in range(it[u], len(self.adj[u])):
            it[u] = i
            v, rev, c = self.adj[u][i]
            if c > 0 and level[v] == level[u] + 1:
                ret = self.dfs(v, t, min(f, c), level, it)
                if ret:
                    self.adj[u][i] = (v, rev, c - ret)
                    self.adj[v][rev] = (u, i, self.adj[v][rev][2] + ret)
                    return ret
        return 0
    
    def max_flow(self, s, t):
        flow = 0
        level = [-1] * self.n
        while self.bfs(s, t, level):
            it = [0] * self.n
            while True:
                f = self.dfs(s, t, 10**18, level, it)
                if not f:
                    break
                flow += f
        return flow

def solve():
    n, m, _ = map(int, input().split())
    s, t, d = map(int, input().split())
    s -= 1
    t -= 1
    
    edges = []
    for _ in range(m):
        u, v, cap = map(int, input().split())
        u -= 1
        v -= 1
        edges.append((u, v, cap))
    
    # We need to check if there is a flow of exactly d from s to t
    # with all other nodes balanced.
    # Add super source and sink for lower bound feasibility.
    S = n
    T = n + 1
    mf = MaxFlow(n + 2)
    
    # For each node, we track net flow: out - in
    balance = [0] * n
    
    # Add edges with capacity cap, lower bound 0
    for u, v, cap in edges:
        mf.add_edge(u, v, cap)
        # no lower bound, so balance unchanged
    
    # To force exactly d from s to t, we add edge t -> s with capacity d
    # and check if we can satisfy all balances.
    # But simpler: add super source to s with capacity d, t to super sink with capacity d,
    # and check if max flow == d.
    
    mf.add_edge(S, s, d)
    mf.add_edge(t, T, d)
    
    flow = mf.max_flow(S, T)
    
    if flow != d:
        print("NO")
        return
    
    # Now we need to output the flow on each original edge.
    # The flow on edge i is cap - remaining_capacity.
    # We need to retrieve from mf.adj.
    # But we added extra edges, so we need to track original edges.
    
    # Rebuild flow network to extract values
    # We'll store original edge indices.
    mf2 = MaxFlow(n + 2)
    edge_indices = []
    for u, v, cap in edges:
        idx = len(mf2.adj[u])
        mf2.add_edge(u, v, cap)
        edge_indices.append((u, idx))
    
    # Add same super edges
    mf2.add_edge(S, s, d)
    mf2.add_edge(t, T, d)
    
    mf2.max_flow(S, T)
    
    result = []
    for u, idx in edge_indices:
        # The reverse edge is idx ^ 1
        rev = mf2.adj[u][idx][1]
        # capacity used = original cap - current cap
        used = mf2.adj[u][idx][2]
        # Actually, in our representation, we store (v, rev, cap)
        # cap is remaining capacity. So used = original_cap - remaining_cap
        # But we didn't store original cap. We can compute from reverse edge.
        # Reverse edge's cap is the flow.
        flow_val = mf2.adj[u][idx][2]  # remaining cap
        # original cap = flow_val + remaining cap? No.
        # Let's just store original cap in a dict.
        pass
    
    # Easier: store original caps and compute flow as cap - remaining
    mf3 = MaxFlow(n + 2)
    edge_info = []  # (u, idx_in_adj, original_cap)
    for u, v, cap in edges:
        idx = len(mf3.adj[u])
        mf3.add_edge(u, v, cap)
        edge_info.append((u, idx, cap))
    
    mf3.add_edge(S, s, d)
    mf3.add_edge(t, T, d)
    mf3.max_flow(S, T)
    
    result = []
    for u, idx, cap in edge_info:
        # remaining capacity
        remaining = mf3.adj[u][idx][2]
        result.append(cap - remaining)
    
    print("YES")
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    solve()