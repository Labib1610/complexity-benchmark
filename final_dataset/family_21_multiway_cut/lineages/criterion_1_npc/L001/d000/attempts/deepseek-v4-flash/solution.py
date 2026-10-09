import sys
from collections import deque

class Dinic:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]
        self.edges = []
    
    def add_edge(self, u, v, cap, idx):
        # We'll store forward edge and reverse
        self.adj[u].append(len(self.edges))
        self.edges.append([v, cap, idx, len(self.edges)+1])
        self.adj[v].append(len(self.edges))
        self.edges.append([u, 0, idx, len(self.edges)-1])
    
    def bfs(self, s, t):
        self.level = [-1]*self.n
        q = deque()
        q.append(s)
        self.level[s] = 0
        while q:
            u = q.popleft()
            for eid in self.adj[u]:
                v, cap, _, _ = self.edges[eid]
                if cap > 0 and self.level[v] < 0:
                    self.level[v] = self.level[u]+1
                    q.append(v)
        return self.level[t] >= 0
    
    def dfs(self, u, t, f):
        if u == t:
            return f
        for i in range(self.it[u], len(self.adj[u])):
            self.it[u] = i
            eid = self.adj[u][i]
            v, cap, _, rev = self.edges[eid]
            if cap > 0 and self.level[v] == self.level[u]+1:
                ret = self.dfs(v, t, min(f, cap))
                if ret > 0:
                    self.edges[eid][1] -= ret
                    self.edges[rev][1] += ret
                    return ret
        return 0
    
    def max_flow(self, s, t):
        flow = 0
        INF = 10**9
        while self.bfs(s, t):
            self.it = [0]*self.n
            while True:
                f = self.dfs(s, t, INF)
                if f == 0:
                    break
                flow += f
        return flow
    
    def min_cut_edges(self, s):
        # After max_flow, find reachable nodes from s
        visited = [False]*self.n
        q = deque([s])
        visited[s] = True
        while q:
            u = q.popleft()
            for eid in self.adj[u]:
                v, cap, _, _ = self.edges[eid]
                if cap > 0 and not visited[v]:
                    visited[v] = True
                    q.append(v)
        # Edges from visited to unvisited are cut edges
        cut_edges = []
        for eid in range(0, len(self.edges), 2):
            u, v, cap, idx, rev = self.edges[eid][0], self.edges[eid][1], self.edges[eid][2], self.edges[eid][3], self.edges[eid][4] if len(self.edges[eid]) == 5 else None
            # Actually careful: each entry is [v, cap, idx, rev]
            # Our structure: [v, cap, idx, rev]
            u_node = self.edges[eid][0]  # not stored, need track from reverse
        # Let's store original endpoints when adding edge; modify add_edge to store in separate list
        return []

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it)); B = int(next(it))
    terminals = [int(next(it))-1 for _ in range(k)]
    
    edges = []
    for i in range(m):
        u = int(next(it))-1
        v = int(next(it))-1
        w = int(next(it))
        edges.append((u,v,w))
    
    # Data structure to store cut edges per pair
    cut_union = {}
    
    for i in range(k):
        for j in range(i+1, k):
            s = terminals[i]
            t = terminals[j]
            dinic = Dinic(n)
            # Add edges with original index
            for idx, (u,v,w) in enumerate(edges):
                dinic.add_edge(u, v, w, idx)
                dinic.add_edge(v, u, w, idx)  # undirected -> add both directions
            # Actually undirected in Dinic: add both forward in one direction? 
            # For undirected, we can add edge with capacity w in both directions.
            # But Dinic add_edge already adds reverse with cap 0, so we can input capacity w for both directions separately.
            # So we need to add two edges each direction with capacity w.
            # Let's adjust.
    
    # Because the above approach not complete — we'll re-implement carefully.
    
    # Redo with proper Dinic for undirected
    
    class Dinic2:
        def __init__(self, n):
            self.n = n
            self.adj = [[] for _ in range(n)]
            self.edges = []
        
        def add_edge(self, u, v, cap):
            self.adj[u].append(len(self.edges))
            self.edges.append([v, cap, len(self.edges)+1])
            self.adj[v].append(len(self.edges))
            self.edges.append([u, 0, len(self.edges)-1])
        
        def bfs(self, s, t):
            self.level = [-1]*self.n
            q = deque([s])
            self.level[s] = 0
            while q:
                u = q.popleft()
                for eid in self.adj[u]:
                    v, cap, _ = self.edges[eid]
                    if cap > 0 and self.level[v] < 0:
                        self.level[v] = self.level[u]+1
                        q.append(v)
            return self.level[t] >= 0
        
        def dfs(self, u, t, f):
            if u == t:
                return f
            for i in range(self.it[u], len(self.adj[u])):
                self.it[u] = i
                eid = self.adj[u][i]
                v, cap, rev = self.edges[eid]
                if cap > 0 and self.level[v] == self.level[u]+1:
                    ret = self.dfs(v, t, min(f, cap))
                    if ret:
                        self.edges[eid][1] -= ret
                        self.edges[rev][1] += ret
                        return ret
            return 0
        
        def max_flow(self, s, t):
            flow = 0
            INF = 10**9
            while self.bfs(s, t):
                self.it = [0]*self.n
                while True:
                    f = self.dfs(s, t, INF)
                    if not f:
                        break
                    flow += f
            return flow
        
        def min_cut_edges(self, s):
            visited = [False]*self.n
            q = deque([s])
            visited[s] = True
            while q:
                u = q.popleft()
                for eid in self.adj[u]:
                    v, cap, _ = self.edges[eid]
                    if cap > 0 and not visited[v]:
                        visited[v] = True
                        q.append(v)
            cut_idx = set()
            for eid in range(0, len(self.edges), 2):
                u = self.edges[eid+1][0]  # reverse edge's v is original u
                v = self.edges[eid][0]    # forward edge's v
                cap = self.edges[eid][1]
                # Actually reverse edge's v is u, so:
                u_node = self.edges[eid+1][0]
                v_node = self.edges[eid][0]
                if visited[u_node] and not visited[v_node]:
                    cut_idx.add(eid//2)
            return cut_idx
    
    # Now build pair cuts
    pair_cut_edges = set()
    for i in range(k):
        for j in range(i+1, k):
            s = terminals[i]
            t = terminals[j]
            dinic = Dinic2(n)
            for u,v,w in edges:
                dinic.add_edge(u, v, w)
                dinic.add_edge(v, u, w)
            dinic.max_flow(s, t)
            cut = dinic.min_cut_edges(s)
            for idx in cut:
                pair_cut_edges.add(idx)
    
    total_cost = sum(edges[idx][2] for idx in pair_cut_edges)
    if total_cost > B:
        print("NO")
    else:
        print("YES")
        print(len(pair_cut_edges))
        for idx in sorted(pair_cut_edges):
            u,v,w = edges[idx]
            print(u+1, v+1)

if __name__ == "__main__":
    solve()