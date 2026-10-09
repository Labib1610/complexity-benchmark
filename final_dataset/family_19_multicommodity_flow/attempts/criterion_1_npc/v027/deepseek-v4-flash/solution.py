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
        q = deque()
        level[s] = 0
        q.append(s)
        while q:
            u = q.popleft()
            for v, cap, rev in self.adj[u]:
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

def main():
    n, m, k = map(int, input().split())
    syndicates = []
    for _ in range(k):
        s, t, d = map(int, input().split())
        syndicates.append((s-1, t-1, d))
    
    edges = []
    for _ in range(m):
        u, v, cap = map(int, input().split())
        edges.append((u-1, v-1, cap))
    
    S = n
    T = n + 1
    mf = MaxFlow(n + 2)
    
    total_demand = 0
    for i, (s, t, d) in enumerate(syndicates):
        mf.add_edge(S, s, d)
        mf.add_edge(t, T, d)
        total_demand += d
    
    for u, v, cap in edges:
        mf.add_edge(u, v, cap)
    
    flow = mf.max_flow(S, T)
    if flow != total_demand:
        print("NO")
        return
    
    # Now decompose flow per syndicate
    # We'll run separate max flows for each syndicate on residual capacities
    # First, get the original capacities
    orig_cap = [cap for _, _, cap in edges]
    
    # We'll store the flow per syndicate per edge
    result = [[0]*m for _ in range(k)]
    
    # For each syndicate, we need to find a feasible flow of its quota
    # We'll use the residual graph after previous assignments
    # Build a fresh max flow for each syndicate with only its source/sink and current residual capacities
    for idx, (s, t, d) in enumerate(syndicates):
        # Build a new flow network for this syndicate
        mf2 = MaxFlow(n)
        # Add edges with current residual capacities
        for e_idx, (u, v, cap) in enumerate(edges):
            # residual capacity = original cap - sum of flows already assigned on this edge
            used = sum(result[i][e_idx] for i in range(k))
            mf2.add_edge(u, v, cap - used)
        # Add super source/sink for this syndicate
        SS = n
        TT = n + 1
        mf2 = MaxFlow(n + 2)
        mf2.add_edge(SS, s, d)
        mf2.add_edge(t, TT, d)
        for e_idx, (u, v, cap) in enumerate(edges):
            used = sum(result[i][e_idx] for i in range(k))
            mf2.add_edge(u, v, cap - used)
        
        f = mf2.max_flow(SS, TT)
        if f != d:
            print("NO")
            return
        
        # Now extract the flow on each edge for this syndicate
        # We need to look at the forward edges in mf2's adjacency
        # The edges are added in order: first the super source/sink edges, then the original edges
        # We'll map them
        edge_flow = [0]*m
        # The original edges are added after the two super edges
        # In mf2.adj, for each original edge (u,v,cap), the forward edge is at some index
        # We'll track by scanning adjacency
        # Easier: we can store the edge indices when adding
        # Let's rebuild with tracking
        mf3 = MaxFlow(n + 2)
        mf3.add_edge(SS, s, d)
        mf3.add_edge(t, TT, d)
        edge_refs = []
        for e_idx, (u, v, cap) in enumerate(edges):
            used = sum(result[i][e_idx] for i in range(k))
            mf3.add_edge(u, v, cap - used)
            # The forward edge is the last added in adj[u]
            edge_refs.append((u, len(mf3.adj[u]) - 1))
        
        f = mf3.max_flow(SS, TT)
        # Now extract flow on each original edge
        for e_idx, (u, idx) in enumerate(edge_refs):
            # The forward edge capacity was reduced by flow
            # The flow on this edge = original residual cap - current cap
            # But we need the flow sent by this syndicate
            # The forward edge's original cap (before this syndicate) was (cap - used)
            # After max flow, the remaining cap is mf3.adj[u][idx][1]
            # So flow = (cap - used) - remaining
            orig_residual = edges[e_idx][2] - sum(result[i][e_idx] for i in range(k))
            remaining = mf3.adj[u][idx][1]
            flow_on_edge = orig_residual - remaining
            result[idx][e_idx] = flow_on_edge
    
    print("YES")
    for row in result:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    main()