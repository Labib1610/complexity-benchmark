import sys
from collections import deque

input = sys.stdin.readline

class Dinic:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]

    def add_edge(self, u, v, cap):
        self.adj[u].append([v, cap, len(self.adj[v])])
        self.adj[v].append([u, 0, len(self.adj[u]) - 1])

    def bfs(self, s, t):
        self.level = [-1] * self.n
        q = deque([s])
        self.level[s] = 0
        while q:
            u = q.popleft()
            for v, cap, rev in self.adj[u]:
                if cap > 0 and self.level[v] < 0:
                    self.level[v] = self.level[u] + 1
                    q.append(v)
        return self.level[t] >= 0

    def dfs(self, u, t, f):
        if u == t:
            return f
        for i in range(self.it[u], len(self.adj[u])):
            self.it[u] = i
            v, cap, rev = self.adj[u][i]
            if cap > 0 and self.level[u] + 1 == self.level[v]:
                ret = self.dfs(v, t, min(f, cap))
                if ret > 0:
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
                f = self.dfs(s, t, INF)
                if f == 0:
                    break
                flow += f
        return flow

def solve():
    n, m, k = map(int, input().split())
    requests = []
    for _ in range(k):
        s, t, d = map(int, input().split())
        requests.append((s-1, t-1, d))
    edges = []
    for _ in range(m):
        u, v, cap = map(int, input().split())
        edges.append((u-1, v-1, cap))

    # Node indexing:
    # 0..n-1: stations
    # n..n+k-1: request source nodes
    # n+k..n+2k-1: request sink nodes
    # n+2k: super source
    # n+2k+1: super sink
    S = n + 2*k
    T = n + 2*k + 1
    dinic = Dinic(n + 2*k + 2)

    # Connect super source to each request source
    for i, (s, t, d) in enumerate(requests):
        req_src = n + i
        req_snk = n + k + i
        dinic.add_edge(S, req_src, d)
        dinic.add_edge(req_snk, T, d)
        # request source -> start station
        dinic.add_edge(req_src, s, d)
        # end station -> request sink
        dinic.add_edge(t, req_snk, d)

    # Add tube edges with capacity
    for u, v, cap in edges:
        dinic.add_edge(u, v, cap)

    total_demand = sum(d for _, _, d in requests)
    flow = dinic.max_flow(S, T)

    if flow != total_demand:
        print("NO")
        return

    # Extract flows per request per edge
    # We need to know which edge index in dinic corresponds to each original edge
    # We'll store the edge indices when adding
    edge_flow_indices = []
    for idx, (u, v, cap) in enumerate(edges):
        # The edge added in dinic is at position len(adj[u])-1 after adding
        # But we need to track it: we'll store the forward edge index
        # We'll add edges again to track indices
        pass

    # Rebuild with tracking
    dinic2 = Dinic(n + 2*k + 2)
    edge_refs = []
    for i, (s, t, d) in enumerate(requests):
        req_src = n + i
        req_snk = n + k + i
        dinic2.add_edge(S, req_src, d)
        dinic2.add_edge(req_snk, T, d)
        dinic2.add_edge(req_src, s, d)
        dinic2.add_edge(t, req_snk, d)

    for u, v, cap in edges:
        dinic2.add_edge(u, v, cap)
        # The forward edge is at index len(dinic2.adj[u])-1
        edge_refs.append((u, len(dinic2.adj[u]) - 1))

    dinic2.max_flow(S, T)

    # For each request, we need to find how much flows through each original edge
    # We can do a BFS/DFS from each request source to its sink, but easier:
    # We can compute flow on each edge by looking at the residual graph.
    # For each original edge (u,v), the flow = original_cap - residual_cap
    # But we need per-request breakdown. We can do a flow decomposition.

    # Flow decomposition: for each request, send flow from its source to its sink
    # along the residual network of the original capacities.
    # We'll use the original capacities and the flows we found.

    # Build a flow matrix per request per edge
    result = [[0]*m for _ in range(k)]

    # We'll do a simple approach: for each request, run a DFS from its start station
    # to its end station using the remaining capacities, subtracting the flow we send.
    # But we need to know how much of each edge's flow belongs to which request.
    # Since the problem guarantees a solution, we can decompose.

    # We'll use the residual graph from dinic2 to find paths for each request.
    # For each request i, we need to send d_i units from s_i to t_i.
    # We'll use the flow values on edges: flow_on_edge = cap - residual_cap

    # First, compute flow on each original edge
    flow_on_edge = []
    for idx, (u, v, cap) in enumerate(edges):
        # find the forward edge in dinic2.adj[u]
        # We stored edge_refs[idx] = (u, index_in_adj)
        u_idx, e_idx = edge_refs[idx]
        # residual capacity is dinic2.adj[u_idx][e_idx][1]
        residual = dinic2.adj[u_idx][e_idx][1]
        flow_on_edge.append(cap - residual)

    # Now decompose per request using DFS on the flow network
    # We'll create a copy of flow_on_edge to subtract as we assign
    remaining_flow = flow_on_edge[:]

    # For each request, find paths from s_i to t_i using edges with remaining_flow > 0
    for i, (s, t, d) in enumerate(requests):
        need = d
        # DFS to find a path
        while need > 0:
            # find any path from s to t using remaining_flow
            parent = [-1]*n
            q = deque([s])
            parent[s] = s
            while q and parent[t] == -1:
                u = q.popleft()
                for idx, (u2, v2, cap) in enumerate(edges):
                    if u2 == u and remaining_flow[idx] > 0 and parent[v2] == -1:
                        parent[v2] = u
                        q.append(v2)
            if parent[t] == -1:
                # shouldn't happen if flow is valid
                break
            # find bottleneck
            path_edges = []
            v = t
            while v != s:
                u = parent[v]
                # find edge index from u to v
                for idx, (u2, v2, cap) in enumerate(edges):
                    if u2 == u and v2 == v and remaining_flow[idx] > 0:
                        path_edges.append(idx)
                        break
                v = u
            path_edges.reverse()
            bottleneck = min(remaining_flow[idx] for idx in path_edges)
            bottleneck = min(bottleneck, need)
            for idx in path_edges:
                remaining_flow[idx] -= bottleneck
                result[i][idx] += bottleneck
            need -= bottleneck

    print("YES")
    for row in result:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    solve()