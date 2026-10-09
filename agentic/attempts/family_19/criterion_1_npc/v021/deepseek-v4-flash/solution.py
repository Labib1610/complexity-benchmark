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
            for v, cap, _ in self.graph[u]:
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
            if cap > 0 and self.level[v] == self.level[u] + 1:
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

def solve():
    n, m, k = map(int, input().split())
    sigs = []
    for _ in range(k):
        s, t, d = map(int, input().split())
        sigs.append((s-1, t-1, d))
    
    edges = []
    for _ in range(m):
        u, v, cap = map(int, input().split())
        edges.append((u-1, v-1, cap))
    
    # residual capacities
    residual = [cap for _, _, cap in edges]
    
    all_flows = []
    
    for s, t, d in sigs:
        # build graph with current residual capacities
        dinic = Dinic(n)
        for i, (u, v, _) in enumerate(edges):
            if residual[i] > 0:
                dinic.add_edge(u, v, residual[i])
        
        flow = dinic.max_flow(s, t)
        if flow < d:
            print("NO")
            return
        
        # record flow on each edge for this signature
        flow_on_edge = [0] * m
        # We need to extract flow from the Dinic graph
        # The graph has edges in order: original edges first, then reverse edges.
        # We'll map original edge index to the forward edge in Dinic.
        # In Dinic, for each original edge i, we added edge (u,v,residual[i]).
        # The forward edge is at graph[u][some index].
        # We'll store the index of the forward edge.
        
        # Rebuild mapping: for each original edge, find the forward edge in dinic.graph[u]
        # But easier: we can just run a DFS from s to t to find a flow of d, but that's complex.
        # Instead, we can use the fact that Dinic's graph stores edges in order.
        # We'll store the forward edge index when adding.
        
        # Let's redo: we'll store the forward edge index for each original edge.
        dinic2 = Dinic(n)
        edge_idx = []
        for i, (u, v, _) in enumerate(edges):
            if residual[i] > 0:
                idx = len(dinic2.graph[u])
                dinic2.add_edge(u, v, residual[i])
                edge_idx.append((u, idx, i))
        
        # Now run max flow
        flow2 = dinic2.max_flow(s, t)
        # flow2 should be >= d, but we only need d.
        # We'll extract the flow on each original edge by looking at the reverse edge's capacity.
        # In Dinic, after max flow, the flow on an edge is the capacity of the reverse edge.
        # The reverse edge is at graph[v][rev_idx].
        
        # But we need to map back to original edge index.
        # We stored (u, idx, i) where idx is the index in graph[u] of the forward edge.
        # The reverse edge is at graph[v][rev_idx] where rev_idx = graph[u][idx][2].
        
        for u, idx, orig_i in edge_idx:
            v, cap, rev = dinic2.graph[u][idx]
            # flow = original capacity - current capacity
            # original capacity was residual[orig_i]
            flow_val = residual[orig_i] - dinic2.graph[u][idx][1]
            flow_on_edge[orig_i] = flow_val
        
        # Now we need to ensure we only take d flow, not more.
        # Since we ran max flow, it might send more than d if possible.
        # But we only need d. We can reduce flows proportionally? No, we need exact.
        # Actually, we can just take the flow we got, but we must ensure total = d.
        # Since max flow >= d, we can find a flow of exactly d by taking a subflow.
        # But easier: we can set the sink demand to d by adding a dummy edge from t to s with capacity d? No.
        # Simpler: we can run max flow with a limit: add a super source to s with capacity d, and t to super sink with capacity d.
        # But we already have s and t.
        # Let's do: add edge from s to t with capacity d? No.
        # Actually, we can just run max flow and if it's > d, we can reduce by finding a path and reducing.
        # But that's messy.
        
        # Better approach: use a max flow with lower bound? No.
        # Since we only need to check feasibility and output, we can just run max flow and if it's >= d, we can take any d flow.
        # But we need to output the exact flow for this signature.
        # We can do: run max flow, then find a flow of exactly d by using BFS/DFS to find d units.
        # But that's also messy.
        
        # Simpler: we can modify the graph to have a super source connected to s with capacity d, and t to super sink with capacity d.
        # Then run max flow from super source to super sink. If max flow == d, we have exactly d.
        # Let's do that.
        
        dinic3 = Dinic(n + 2)
        S = n
        T = n + 1
        dinic3.add_edge(S, s, d)
        dinic3.add_edge(t, T, d)
        for i, (u, v, _) in enumerate(edges):
            if residual[i] > 0:
                dinic3.add_edge(u, v, residual[i])
        
        flow3 = dinic3.max_flow(S, T)
        if flow3 < d:
            print("NO")
            return
        
        # Extract flow on each original edge
        # The forward edges for original edges are added after the S->s and t->T edges.
        # We'll track indices.
        # Actually, we can just look at the graph and find the flow on each original edge.
        # But we need to map.
        
        # Let's store the forward edge index for each original edge.
        # We'll add original edges first, then S->s and t->T.
        # But we need to know the order.
        
        # Let's do it cleanly:
        dinic4 = Dinic(n + 2)
        S = n
        T = n + 1
        # Add original edges
        orig_edge_forward = []
        for i, (u, v, _) in enumerate(edges):
            if residual[i] > 0:
                idx = len(dinic4.graph[u])
                dinic4.add_edge(u, v, residual[i])
                orig_edge_forward.append((u, idx, i))
        # Add super edges
        dinic4.add_edge(S, s, d)
        dinic4.add_edge(t, T, d)
        
        flow4 = dinic4.max_flow(S, T)
        if flow4 < d:
            print("NO")
            return
        
        # Extract flow on each original edge
        flow_on_edge = [0] * m
        for u, idx, orig_i in orig_edge_forward:
            # flow = original_cap - current_cap
            flow_val = residual[orig_i] - dinic4.graph[u][idx][1]
            flow_on_edge[orig_i] = flow_val
        
        all_flows.append(flow_on_edge)
        
        # Update residual capacities
        for i in range(m):
            residual[i] -= flow_on_edge[i]
    
    # Output
    print("YES")
    for flows in all_flows:
        print(' '.join(map(str, flows)))

if __name__ == "__main__":
    solve()