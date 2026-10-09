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
        q = deque()
        q.append(s)
        self.level[s] = 0
        while q:
            u = q.popleft()
            for v, cap, _ in self.adj[u]:
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
        self.bfs(s, t)
        cut_edges = []
        for u in range(self.n):
            if self.level[u] != -1:
                for v, cap, rev in self.adj[u]:
                    if cap == 0 and self.level[v] == -1:
                        # original edge u->v was saturated
                        # but we need to know original direction
                        # We'll store original edges separately
                        pass
        # We'll instead collect edges by checking original capacities
        return cut_edges

def main():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    B = int(next(it))
    anchors = [int(next(it)) - 1 for _ in range(k)]
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        edges.append((u, v, w))
    
    # Build graph for Dinic
    # We'll run max flow for each pair of anchors
    # To get min cut edges, we need to know which original edges are cut.
    # We'll store original edge indices.
    
    # For each pair, we run Dinic on a fresh graph with capacities = weights
    # After max flow, we find reachable nodes from source in residual graph.
    # An original edge (u,v) is in the min cut if exactly one endpoint is reachable.
    
    cut_edge_set = set()
    total_cost = 0
    
    for i in range(k):
        for j in range(i+1, k):
            s = anchors[i]
            t = anchors[j]
            dinic = Dinic(n)
            # add edges with original weights
            for idx, (u, v, w) in enumerate(edges):
                dinic.add_edge(u, v, w)
                dinic.add_edge(v, u, w)  # undirected: add both directions with same cap
            # Actually Dinic's add_edge adds directed edge with reverse 0 cap.
            # For undirected, we add two directed edges with full capacity each.
            # But that doubles capacity? No, we need to model undirected edge as two directed edges each with capacity w.
            # However, in max flow, that's correct: flow can go either way.
            # But for min cut, the cut capacity counts each undirected edge once.
            # If we add two directed edges with capacity w, the cut will count both directions if both are cut? Actually min cut will cut at most one direction.
            # Standard approach: add one edge with capacity w and reverse with capacity w (i.e., both directions have capacity w).
            # Dinic's add_edge adds reverse with 0, so we need to add two separate edges.
            # Let's fix: we'll add edge u->v with cap w and v->u with cap w separately.
            # But that creates two parallel edges in each direction? Actually we can just add two directed edges.
            # For min cut, the capacity of the cut is sum of capacities of edges from S to T.
            # If we have both u->v and v->u with cap w, and u in S, v in T, then u->v contributes w, v->u is from T to S so not counted.
            # So it's fine.
            
            # Rebuild properly:
            dinic = Dinic(n)
            for u, v, w in edges:
                dinic.add_edge(u, v, w)
                dinic.add_edge(v, u, w)
            
            dinic.max_flow(s, t)
            # Find reachable nodes from s in residual graph
            reachable = [False] * n
            q = deque([s])
            reachable[s] = True
            while q:
                u = q.popleft()
                for v, cap, _ in dinic.adj[u]:
                    if cap > 0 and not reachable[v]:
                        reachable[v] = True
                        q.append(v)
            # Now find original edges crossing the cut
            for idx, (u, v, w) in enumerate(edges):
                if reachable[u] != reachable[v]:
                    # This edge is in the min cut
                    if idx not in cut_edge_set:
                        cut_edge_set.add(idx)
                        total_cost += w
    
    if total_cost <= B:
        print("YES")
        print(len(cut_edge_set))
        for idx in cut_edge_set:
            u, v, _ = edges[idx]
            print(u+1, v+1)
    else:
        print("NO")

if __name__ == "__main__":
    main()