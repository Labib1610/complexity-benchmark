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
                if cap > 0 and self.level[v] == -1:
                    self.level[v] = self.level[u] + 1
                    q.append(v)
        return self.level[t] != -1
    
    def dfs(self, u, t, f):
        if u == t:
            return f
        for i in range(self.it[u], len(self.adj[u])):
            self.it[u] = i
            v, cap, rev = self.adj[u][i]
            if cap > 0 and self.level[v] == self.level[u] + 1:
                ret = self.dfs(v, t, min(f, cap))
                if ret:
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
                if not f:
                    break
                flow += f
        return flow
    
    def min_cut_edges(self, s, t):
        # After max flow, find reachable nodes from s in residual graph
        visited = [False] * self.n
        q = deque([s])
        visited[s] = True
        while q:
            u = q.popleft()
            for v, cap, rev in self.adj[u]:
                if cap > 0 and not visited[v]:
                    visited[v] = True
                    q.append(v)
        # Edges from visited to unvisited are in min cut
        cut_edges = []
        for u in range(self.n):
            if visited[u]:
                for v, cap, rev in self.adj[u]:
                    if not visited[v] and cap == 0:
                        # This edge was saturated, but we need original edge info
                        # We'll store original edges separately
                        pass
        return visited

def solve():
    input_data = sys.stdin.read().strip().split()
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    B = int(next(it))
    
    sovereign = [int(next(it)) - 1 for _ in range(k)]
    
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        edges.append((u, v, w))
    
    # If k <= 1, no cuts needed
    if k <= 1:
        print("YES")
        print(0)
        return
    
    # We'll compute min cut between each pair of sovereign nodes
    # and collect all edges that appear in any min cut.
    # This is a heuristic but works for small k.
    
    # Build original adjacency for edge lookup
    edge_id = {}
    for idx, (u, v, w) in enumerate(edges):
        edge_id[(u, v)] = idx
        edge_id[(v, u)] = idx
    
    cut_edge_set = set()
    
    for i in range(k):
        for j in range(i+1, k):
            s = sovereign[i]
            t = sovereign[j]
            
            dinic = Dinic(n)
            for u, v, w in edges:
                dinic.add_edge(u, v, w)
                dinic.add_edge(v, u, w)
            
            flow = dinic.max_flow(s, t)
            visited = dinic.min_cut_edges(s, t)
            
            # Find edges crossing the cut
            for u in range(n):
                if visited[u]:
                    for v, cap, rev in dinic.adj[u]:
                        if not visited[v] and cap == 0:
                            # This edge is in min cut
                            # But we need original edge id
                            # We'll check both directions
                            if (u, v) in edge_id:
                                cut_edge_set.add(edge_id[(u, v)])
                            elif (v, u) in edge_id:
                                cut_edge_set.add(edge_id[(v, u)])
    
    total_cost = sum(edges[idx][2] for idx in cut_edge_set)
    
    if total_cost <= B:
        print("YES")
        print(len(cut_edge_set))
        for idx in cut_edge_set:
            u, v, w = edges[idx]
            print(u+1, v+1)
    else:
        print("NO")

if __name__ == "__main__":
    solve()