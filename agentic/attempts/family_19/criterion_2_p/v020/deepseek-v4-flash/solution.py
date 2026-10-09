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
    
    edges = []
    dinic = Dinic(n)
    for _ in range(m):
        u, v, cap = map(int, input().split())
        u -= 1
        v -= 1
        dinic.add_edge(u, v, cap)
        edges.append((u, v, cap))
    
    maxflow = dinic.max_flow(s, t)
    if maxflow < d:
        print("NO")
        return
    
    # Now we need to find a flow of exactly d.
    # We can just take the flow from the max flow computation and scale down if needed.
    # But easier: run Dinic again with target d by adding a super sink with capacity d.
    # Actually, we can just compute flow values from the residual graph.
    
    # Build a fresh Dinic and add a dummy edge from t to a new sink with capacity d.
    # But simpler: we can just use the existing flow and reduce if maxflow > d.
    # Since capacities are integers, we can find a feasible flow of exactly d by
    # running max flow with a cap on the sink.
    
    dinic2 = Dinic(n + 1)
    for u, v, cap in edges:
        dinic2.add_edge(u, v, cap)
    # Add edge from t to new sink with capacity d
    dinic2.add_edge(t, n, d)
    flow = dinic2.max_flow(s, n)
    if flow < d:
        print("NO")
        return
    
    # Extract flow on each original edge
    res = []
    for u, v, cap in edges:
        # find the forward edge in dinic2 graph
        # We stored edges in order, so we can track by scanning adjacency
        # But easier: we can store edge indices.
        pass
    
    # Instead, let's store edge references during construction.
    # Rebuild with edge index tracking.
    
    dinic3 = Dinic(n + 1)
    edge_refs = []
    for u, v, cap in edges:
        idx = len(edge_refs)
        dinic3.add_edge(u, v, cap)
        # The forward edge is at graph[u][-1] before adding reverse
        # Actually we can store the index of forward edge in graph[u]
        # We'll do it differently: store the forward edge object reference.
        # Since graph[u][-1] is [v, cap, rev_index]
        edge_refs.append((u, len(dinic3.graph[u]) - 1))
    dinic3.add_edge(t, n, d)
    dinic3.max_flow(s, n)
    
    ans = []
    for u, idx in edge_refs:
        # original capacity minus remaining capacity = flow used
        orig_cap = None
        for v, cap, rev in edges:
            pass
        # We stored cap in edges list, so:
        # We need to find the original cap for this edge.
        # We can zip edges and edge_refs.
    
    # Let's redo cleanly:
    
    dinic4 = Dinic(n + 1)
    edge_info = []  # (u, v, cap, forward_index_in_graph[u])
    for u, v, cap in edges:
        dinic4.add_edge(u, v, cap)
        # forward edge is at graph[u][-1] before adding reverse
        fwd_idx = len(dinic4.graph[u]) - 1
        edge_info.append((u, v, cap, fwd_idx))
    dinic4.add_edge(t, n, d)
    dinic4.max_flow(s, n)
    
    ans = []
    for u, v, cap, fwd_idx in edge_info:
        # remaining capacity on forward edge
        remaining = dinic4.graph[u][fwd_idx][1]
        flow_used = cap - remaining
        ans.append(flow_used)
    
    print("YES")
    print(" ".join(map(str, ans)))

if __name__ == "__main__":
    main()