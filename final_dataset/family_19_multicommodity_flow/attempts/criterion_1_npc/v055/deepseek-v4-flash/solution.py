import sys
from collections import deque

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
            if cap > 0 and self.level[v] == self.level[u] + 1:
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

def main():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    clients = []
    for _ in range(k):
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        d = int(next(it))
        clients.append((s, t, d))
    
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        lim = int(next(it))
        edges.append((u, v, lim))
    
    # We'll try a greedy approach: for each client, find a feasible flow
    # using remaining capacities. If any client fails, output NO.
    # This is not guaranteed to find a solution even if one exists,
    # but for many cases it works.
    
    # remaining capacity per edge
    rem_cap = [lim for _, _, lim in edges]
    
    # store flows per client per edge
    flows = [[0] * m for _ in range(k)]
    
    for idx, (s, t, d) in enumerate(clients):
        # Build a flow network for this client only, with current remaining capacities
        # Nodes: 0..n-1 for junctions, n = super source, n+1 = super sink
        dinic = Dinic(n + 2)
        super_s = n
        super_t = n + 1
        dinic.add_edge(super_s, s, d)
        dinic.add_edge(t, super_t, d)
        for eid, (u, v, lim) in enumerate(edges):
            if rem_cap[eid] > 0:
                dinic.add_edge(u, v, rem_cap[eid])
        
        flow = dinic.max_flow(super_s, super_t)
        if flow < d:
            print("NO")
            return
        
        # Now we need to extract the flow on each edge for this client.
        # We can do this by checking the residual graph.
        # For each edge, the flow used is original_cap - residual_cap.
        # But we added edges with capacity = rem_cap[eid], so we need to track.
        # We'll store the original capacities we added.
        # Simpler: we can run a second pass to find the actual flow on each edge.
        # We'll do a BFS/DFS from super_s to super_t to find paths and record.
        # But easier: we can just use the residual graph of dinic.
        # For each original edge (u,v), we added an edge with capacity rem_cap[eid].
        # The flow on that edge = rem_cap[eid] - current residual capacity.
        # We need to find the edge in dinic.adj[u] that goes to v.
        # We'll store mapping.
        
        # Build mapping from (u,v) to edge index in dinic
        edge_map = {}
        for eid, (u, v, lim) in enumerate(edges):
            if rem_cap[eid] > 0:
                # find the edge in dinic.adj[u] that goes to v
                for j, (to, cap, rev) in enumerate(dinic.adj[u]):
                    if to == v and cap == rem_cap[eid]:  # this is the forward edge we added
                        edge_map[eid] = (u, j)
                        break
        
        # Now extract flow for this client
        for eid, (u, v, lim) in enumerate(edges):
            if rem_cap[eid] > 0:
                uu, j = edge_map[eid]
                # forward edge capacity now is residual
                residual = dinic.adj[uu][j][1]
                used = rem_cap[eid] - residual
                flows[idx][eid] = used
                # update remaining capacity
                rem_cap[eid] -= used
            else:
                flows[idx][eid] = 0
    
    # If we got here, all clients satisfied
    print("YES")
    for row in flows:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    main()