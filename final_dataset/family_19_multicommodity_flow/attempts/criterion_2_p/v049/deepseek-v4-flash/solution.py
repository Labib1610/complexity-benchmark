from collections import deque

class MaxFlow:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]
        self.cap = {}
    
    def add_edge(self, u, v, c):
        self.adj[u].append(v)
        self.adj[v].append(u)
        self.cap[(u, v)] = self.cap.get((u, v), 0) + c
        self.cap[(v, u)] = self.cap.get((v, u), 0)
    
    def bfs(self, s, t, parent):
        visited = [False] * self.n
        q = deque([s])
        visited[s] = True
        while q:
            u = q.popleft()
            for v in self.adj[u]:
                if not visited[v] and self.cap[(u, v)] > 0:
                    visited[v] = True
                    parent[v] = u
                    if v == t:
                        return True
                    q.append(v)
        return False
    
    def max_flow(self, s, t):
        flow = 0
        parent = [-1] * self.n
        while self.bfs(s, t, parent):
            # find bottleneck
            v = t
            bottleneck = float('inf')
            while v != s:
                u = parent[v]
                bottleneck = min(bottleneck, self.cap[(u, v)])
                v = u
            # augment
            v = t
            while v != s:
                u = parent[v]
                self.cap[(u, v)] -= bottleneck
                self.cap[(v, u)] += bottleneck
                v = u
            flow += bottleneck
        return flow

def solve():
    import sys
    input = sys.stdin.readline

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

    # We'll build a flow network with n+2 nodes: 0..n-1 original, n = S, n+1 = T
    S = n
    T = n + 1
    mf = MaxFlow(n + 2)

    # Add original edges
    for u, v, cap in edges:
        mf.add_edge(u, v, cap)

    # Add edge t -> s with lower bound = d, capacity = d (exact)
    # In flow terms: add edge with capacity d, and we force flow d through it
    # We'll add it as normal edge with capacity d, and also adjust demands
    mf.add_edge(t, s, d)

    # Compute demands
    demand = [0] * n
    # For each original edge, out from u, in to v
    for u, v, cap in edges:
        demand[u] -= cap
        demand[v] += cap
    # For the t->s edge with flow exactly d:
    demand[t] -= d
    demand[s] += d

    # Add super source/sink edges
    total_demand = 0
    for i in range(n):
        if demand[i] > 0:
            mf.add_edge(S, i, demand[i])
            total_demand += demand[i]
        elif demand[i] < 0:
            mf.add_edge(i, T, -demand[i])

    # Run max flow from S to T
    flow = mf.max_flow(S, T)

    if flow != total_demand:
        print("NO")
        return

    # Recover flow on original edges
    # The flow on original edge (u,v) is cap_original - residual_cap[(u,v)]
    # But we need to be careful: we added t->s edge too.
    # We'll store original capacities for edges.
    original_cap = {}
    for idx, (u, v, cap) in enumerate(edges):
        original_cap[(u, v)] = cap

    # For each original edge, flow = original_cap - residual_cap[(u,v)]
    result = []
    for u, v, cap in edges:
        # residual capacity from u to v
        residual = mf.cap[(u, v)]
        flow_on_edge = cap - residual
        result.append(flow_on_edge)

    print("YES")
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    solve()