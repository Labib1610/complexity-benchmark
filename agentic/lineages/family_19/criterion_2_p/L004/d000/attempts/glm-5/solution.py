import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    _ = int(input_data[idx]); idx += 1
    s = int(input_data[idx]) - 1; idx += 1
    t = int(input_data[idx]) - 1; idx += 1
    d = int(input_data[idx]); idx += 1

    edges = []
    adj = [[] for _ in range(n)]
    for i in range(m):
        u = int(input_data[idx]) - 1; idx += 1
        v = int(input_data[idx]) - 1; idx += 1
        cap = int(input_data[idx]); idx += 1
        edges.append((u, v, cap))
        adj[u].append((v, i))
        adj[v].append((u, i))

    # Dinic's max flow
    class Dinic:
        def __init__(self, n, edges, m):
            self.n = n
            self.m = m
            self.graph = [[] for _ in range(n)]
            for i, (u, v, cap) in enumerate(edges):
                self.graph[u].append([v, cap, len(self.graph[v])])
                self.graph[v].append([u, 0, len(self.graph[u]) - 1])

        def bfs(self, s, t):
            self.level = [-1] * self.n
            self.level[s] = 0
            q = deque([s])
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
            while self.it[u] < len(self.graph[u]):
                e = self.graph[u][self.it[u]]
                v, cap, rev = e
                if cap > 0 and self.level[v] == self.level[u] + 1:
                    ret = self.dfs(v, t, min(f, cap))
                    if ret > 0:
                        e[1] -= ret
                        self.graph[v][rev][1] += ret
                        return ret
                self.it[u] += 1
            return 0

        def max_flow(self, s, t):
            flow = 0
            while self.bfs(s, t):
                self.it = [0] * self.n
                while True:
                    f = self.dfs(s, t, float('inf'))
                    if f == 0:
                        break
                    flow += f
            return flow

        def get_flow_on_edges(self, edges):
            res = []
            for u, v, cap in edges:
                # forward edge is at some position in graph[u]
                # find it by checking reverse edge in graph[v]
                # Actually we stored: forward edge [v, cap, rev], reverse edge [u, 0, rev2]
                # After flow, forward cap decreased, reverse cap increased.
                # Flow on edge = original cap - remaining cap = reverse edge's cap.
                # But we need to find the reverse edge.
                # Since we know the structure, for edge i:
                # It was added as: graph[u].append([v, cap, len(graph[v])])
                #                  graph[v].append([u, 0, len(graph[u])-1])
                # So reverse of edge i is in graph[v] at the index stored in forward edge's rev.
                pass
            # Simpler: just track during construction
            return res

    # We need to track flow on original edges
    # Let's modify to track
    class MaxFlow:
        def __init__(self, n, edges, m):
            self.n = n
            self.m = m
            self.graph = [[] for _ in range(n)]
            self.edge_flow = [0] * m
            self.edge_info = []  # (u, v, cap, forward_index_in_u, reverse_index_in_v)
            for i, (u, v, cap) in enumerate(edges):
                fwd_idx = len(self.graph[u])
                rev_idx = len(self.graph[v])
                self.graph[u].append([v, cap, rev_idx, i, True])
                self.graph[v].append([u, 0, fwd_idx, i, False])
                self.edge_info.append((u, v, cap, fwd_idx, rev_idx))

        def bfs(self, s, t):
            self.level = [-1] * self.n
            self.level[s] = 0
            q = deque([s])
            while q:
                u = q.popleft()
                for v, cap, _, _, _ in self.graph[u]:
                    if cap > 0 and self.level[v] < 0:
                        self.level[v] = self.level[u] + 1
                        q.append(v)
            return self.level[t] >= 0

        def dfs(self, u, t, f):
            if u == t:
                return f
            while self.it[u] < len(self.graph[u]):
                e = self.graph[u][self.it[u]]
                v, cap, rev, edge_id, is_fwd = e
                if cap > 0 and self.level[v] == self.level[u] + 1:
                    ret = self.dfs(v, t, min(f, cap))
                    if ret > 0:
                        e[1] -= ret
                        self.graph[v][rev][1] += ret
                        return ret
                self.it[u] += 1
            return 0

        def max_flow(self, s, t):
            flow = 0
            while self.bfs(s, t):
                self.it = [0] * self.n
                while True:
                    f = self.dfs(s, t, float('inf'))
                    if f == 0:
                        break
                    flow += f
            return flow

        def get_flows(self):
            res = [0] * self.m
            for i, (u, v, cap, fwd_idx, rev_idx) in enumerate(self.edge_info):
                # flow = cap - remaining capacity of forward edge
                remaining = self.graph[u][fwd_idx][1]
                res[i] = cap - remaining
            return res

    mf = MaxFlow(n, edges, m)
    maxflow = mf.max_flow(s, t)

    if maxflow >= d:
        flows = mf.get_flows()
        # We need to reduce excess flow (maxflow - d) by finding cycles or paths
        # Standard approach: run DFS to cancel flow on cycles, then reduce s-t path flow
        excess = maxflow - d
        if excess > 0:
            # Build residual graph adjacency for DFS
            # We want to find paths from s to t in residual and reduce flow
            # Actually, to reduce flow by 'excess', we can push flow from t to s in residual graph
            # (i.e., cancel some s-t flow)
            # Push 'excess' units from t to s in residual graph
            # Residual graph: for each edge with flow f, we can reduce by up to f (reverse edge capacity = f)
            # and increase by up to cap-f (forward edge capacity = cap-f)
            # To reduce s-t flow, we push from t to s using reverse edges (which have capacity = current flow)
            
            # Let's just do DFS/BFS to find augmenting paths from t to s in residual graph
            # and push flow to cancel
            # But we need to update the graph structure
            # Actually, our graph already IS the residual graph!
            # graph[u] contains edges with remaining capacity.
            # For original forward edge: remaining cap = cap - flow
            # For reverse edge: remaining cap = flow
            # So pushing from t to s in this residual graph reduces the s-t flow.
            
            # Let's do DFS from t to s
            def reduce_flow(amount):
                # BFS to find path from t to s
                while amount > 0:
                    parent = [-1] * n
                    parent_edge = [-1] * n
                    visited = [False] * n
                    visited[t] = True
                    q = deque([t])
                    found = False
                    while q and not found:
                        u = q.popleft()
                        for idx, e in enumerate(mf.graph[u]):
                            v, cap, rev, edge_id, is_fwd = e
                            if cap > 0 and not visited[v]:
                                visited[v] = True
                                parent[v] = u
                                parent_edge[v] = idx
                                if v == s:
                                    found = True
                                    break
                        if found:
                            break
                    if not visited[s]:
                        break
                    # Find bottleneck
                    path = []
                    cur = s
                    bottleneck = float('inf')
                    while cur != t:
                        p = parent[cur]
                        e_idx = parent_edge[cur]
                        e = mf.graph[p][e_idx]
                        bottleneck = min(bottleneck, e[1])
                        path.append((p, e_idx))
                        cur = p
                    # Wait, we went from t to s, so to trace back from s to t we need parent pointers
                    # parent[v] = u means we went u -> v in the BFS from t
                    # So path from t to s is: t -> ... -> s
                    # To reduce, we push flow along t -> ... -> s
                    # This means for each edge u -> v on this path, we decrease its capacity and increase reverse
                    # But our edges are stored as residual edges already
                    # Let me re-trace: BFS from t, parent[s] = some node, etc.
                    # Path from t to s: t -> parent[t]? No, parent[v] = u means edge u->v
                    # So to go from t to s: we need to follow parent pointers from s back to t
                    # s's parent is some node p1, p1's parent is p2, ..., until we reach t
                    # The edges are p1->s, p2->p1, ..., t->pk
                    # So the path from t to s is: t -> pk -> ... -> p1 -> s
                    # Each edge on this path is stored in graph[parent] at parent_edge[child]
                    
                    cur = s
                    path_edges = []
                    while cur != t:
                        p = parent[cur]
                        e_idx = parent_edge[cur]
                        path_edges.append((p, e_idx))
                        cur = p
                    
                    bottleneck = min(mf.graph[p][e_idx][1] for p, e_idx in path_edges)
                    push = min(bottleneck, amount)
                    for p, e_idx in path_edges:
                        e = mf.graph[p][e_idx]
                        v, cap, rev, edge_id, is_fwd = e
                        e[1] -= push
                        mf.graph[v][rev][1] += push
                    amount -= push
            
            reduce_flow(excess)
            flows = mf.get_flows()
        
        print("YES")
        print(" ".join(map(str, flows)))
    else:
        print("NO")

solve()