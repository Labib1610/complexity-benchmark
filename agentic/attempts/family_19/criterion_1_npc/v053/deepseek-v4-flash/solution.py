import sys
from collections import deque

input = sys.stdin.readline

class MaxFlow:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
    
    def add_edge(self, u, v, cap):
        self.graph[u].append([v, cap, len(self.graph[v])])
        self.graph[v].append([u, 0, len(self.graph[u]) - 1])
    
    def bfs(self, s, t, level):
        for i in range(self.n):
            level[i] = -1
        q = deque([s])
        level[s] = 0
        while q:
            u = q.popleft()
            for v, cap, rev in self.graph[u]:
                if cap > 0 and level[v] < 0:
                    level[v] = level[u] + 1
                    q.append(v)
        return level[t] >= 0
    
    def dfs(self, u, t, f, level, iter):
        if u == t:
            return f
        for i in range(iter[u], len(self.graph[u])):
            iter[u] = i
            v, cap, rev = self.graph[u][i]
            if cap > 0 and level[v] == level[u] + 1:
                d = self.dfs(v, t, min(f, cap), level, iter)
                if d > 0:
                    self.graph[u][i][1] -= d
                    self.graph[v][rev][1] += d
                    return d
        return 0
    
    def max_flow(self, s, t):
        flow = 0
        level = [-1] * self.n
        INF = 10**18
        while self.bfs(s, t, level):
            iter = [0] * self.n
            while True:
                f = self.dfs(s, t, INF, level, iter)
                if f == 0:
                    break
                flow += f
        return flow

def solve():
    n, m, k = map(int, input().split())
    compounds = []
    for _ in range(k):
        s, t, d = map(int, input().split())
        compounds.append((s-1, t-1, d))
    
    edges = []
    for _ in range(m):
        u, v, cap = map(int, input().split())
        edges.append((u-1, v-1, cap))
    
    # We'll try to route each compound one by one, updating residual capacities
    residual = [cap for _, _, cap in edges]
    result = [[0]*m for _ in range(k)]
    
    for idx, (s, t, d) in enumerate(compounds):
        # Build flow network for this compound with current residual capacities
        mf = MaxFlow(n)
        for i, (u, v, _) in enumerate(edges):
            mf.add_edge(u, v, residual[i])
        # Add super source/sink? Actually we just need s->t flow of d
        flow = mf.max_flow(s, t)
        if flow < d:
            print("NO")
            return
        # Now we need to extract the flow on each edge for this compound
        # We can do a BFS/DFS from s to t to find paths and assign flow
        # Simpler: use the residual graph to find how much went through each edge
        # We'll do a flow decomposition:
        # For each edge, flow = original_cap - residual_cap_after_flow
        # But we need per-compound, so we track by building a new graph with only this compound's flow
        # Instead, we can do a max-flow with path recording.
        # Let's do a simple approach: run max-flow and record flows.
        # We'll modify MaxFlow to record flows.
        # For simplicity, we'll do a DFS to find d units of flow.
        # But easier: use the residual graph to compute flow on each edge.
        # We'll store original capacities and after max-flow, flow = original - residual.
        # But we need to know which edges were used by this compound.
        # We'll rebuild the graph and record.
        
        # Let's implement a flow recorder:
        flow_edges = [0]*m
        # We'll do a simple DFS from s to t, sending flow along paths
        # But we already have max flow, so we can extract from residual.
        # We'll store the original graph capacities before max flow.
        orig_caps = [residual[i] for i in range(m)]
        # After max flow, residual[i] is reduced by the flow of this compound.
        # So flow on edge i = orig_caps[i] - residual[i]
        # But residual is updated globally, so we need to capture before/after.
        # We'll do it inside the loop.
        
        # Actually, we can just run max flow and then compute flow per edge
        # by comparing residual before and after.
        # But we already updated residual? No, we haven't yet.
        # We'll build a fresh MaxFlow with current residual, run max_flow,
        # then compute flow on each edge as orig - current_residual_in_that_graph.
        # Then update global residual.
        
        mf2 = MaxFlow(n)
        edge_indices = []
        for i, (u, v, _) in enumerate(edges):
            edge_indices.append(len(mf2.graph[u]))
            mf2.add_edge(u, v, residual[i])
        
        flow_val = mf2.max_flow(s, t)
        if flow_val < d:
            print("NO")
            return
        
        # Extract flow on each edge
        for i, (u, v, _) in enumerate(edges):
            # The forward edge is at index edge_indices[i] in mf2.graph[u]
            # Its residual capacity after flow is mf2.graph[u][edge_indices[i]][1]
            used = residual[i] - mf2.graph[u][edge_indices[i]][1]
            result[idx][i] = used
            residual[i] -= used
        
        # Ensure we used exactly d
        # (flow_val should be d if possible, but we already checked)
    
    print("YES")
    for row in result:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    solve()