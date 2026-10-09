import sys
from collections import deque

input = sys.stdin.readline

class Dinic:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
    
    def add_edge(self, fr, to, cap):
        forward = [to, cap, None]
        backward = [fr, 0, forward]
        forward[2] = backward
        self.graph[fr].append(forward)
        self.graph[to].append(backward)
    
    def bfs(self, s, t):
        self.level = [-1] * self.n
        q = deque([s])
        self.level[s] = 0
        while q:
            v = q.popleft()
            for to, cap, rev in self.graph[v]:
                if cap > 0 and self.level[to] < 0:
                    self.level[to] = self.level[v] + 1
                    q.append(to)
        return self.level[t] >= 0
    
    def dfs(self, v, t, f):
        if v == t:
            return f
        for i in range(self.it[v], len(self.graph[v])):
            self.it[v] = i
            to, cap, rev = self.graph[v][i]
            if cap > 0 and self.level[v] + 1 == self.level[to]:
                ret = self.dfs(to, t, min(f, cap))
                if ret > 0:
                    self.graph[v][i][1] -= ret
                    rev[1] += ret
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
    categories = []
    for _ in range(k):
        s, t, d = map(int, input().split())
        categories.append((s-1, t-1, d))
    
    edges = []
    for _ in range(m):
        u, v, cap = map(int, input().split())
        edges.append((u-1, v-1, cap))
    
    # Node indexing:
    # 0..n-1: original stations
    # n: super source
    # n+1: super sink
    S = n
    T = n+1
    N = n+2
    
    dinic = Dinic(N)
    
    total_demand = 0
    # Add edges from super source to induction stations and from fulfillment stations to super sink
    for s, t, d in categories:
        total_demand += d
        dinic.add_edge(S, s, d)
        dinic.add_edge(t, T, d)
    
    # Add original chute edges
    for u, v, cap in edges:
        dinic.add_edge(u, v, cap)
    
    # Check if max flow equals total demand
    flow = dinic.max_flow(S, T)
    if flow != total_demand:
        print("NO")
        return
    
    # Recover flows per category
    # We need to know which edges correspond to which category
    # We'll store the edge indices for each category's source edge and sink edge
    # But easier: we can run flow per category separately on the residual graph? 
    # Actually we can decompose the flow by looking at the edges from S to s_i and t_i to T.
    
    # We'll store the edge objects for each category's S->s and t->T edges
    cat_source_edges = []
    cat_sink_edges = []
    for s, t, d in categories:
        # Add edge S->s
        forward = [s, d, None]
        backward = [S, 0, forward]
        forward[2] = backward
        dinic.graph[S].append(forward)
        dinic.graph[s].append(backward)
        cat_source_edges.append(forward)
        
        # Add edge t->T
        forward2 = [T, d, None]
        backward2 = [t, 0, forward2]
        forward2[2] = backward2
        dinic.graph[t].append(forward2)
        dinic.graph[T].append(backward2)
        cat_sink_edges.append(forward2)
    
    # But we already added them above, so we need to redo this properly.
    # Let's restructure: we'll add them once and store references.
    
    # Actually, let's redo the graph building with references.
    
    # Rebuild
    dinic = Dinic(N)
    cat_source_edges = []
    cat_sink_edges = []
    for s, t, d in categories:
        total_demand += d
        e1 = [s, d, None]
        e1_rev = [S, 0, e1]
        e1[2] = e1_rev
        dinic.graph[S].append(e1)
        dinic.graph[s].append(e1_rev)
        cat_source_edges.append(e1)
        
        e2 = [T, d, None]
        e2_rev = [t, 0, e2]
        e2[2] = e2_rev
        dinic.graph[t].append(e2)
        dinic.graph[T].append(e2_rev)
        cat_sink_edges.append(e2)
    
    # Add original chute edges
    chute_edges = []
    for u, v, cap in edges:
        e = [v, cap, None]
        e_rev = [u, 0, e]
        e[2] = e_rev
        dinic.graph[u].append(e)
        dinic.graph[v].append(e_rev)
        chute_edges.append(e)
    
    flow = dinic.max_flow(S, T)
    if flow != total_demand:
        print("NO")
        return
    
    # Now decompose flow per category
    # For each category, we know the flow on its S->s edge is d (since max flow = total_demand)
    # We can trace from s to t using the residual graph.
    
    # We'll do BFS/DFS per category to find the paths and amounts.
    # But since capacities are integers and flow is integral, we can decompose.
    
    # We'll create a copy of the flow on each chute edge for each category.
    # We'll use the residual graph to find paths.
    
    # For each category, we need to find d units from s to t.
    # We'll use the current residual graph after max flow.
    # We can repeatedly find a path from s to t in the residual graph with positive capacity,
    # send min capacity along it, and record.
    
    ans = [[0]*m for _ in range(k)]
    
    for idx, (s, t, d) in enumerate(categories):
        remaining = d
        while remaining > 0:
            # BFS to find path from s to t in residual graph
            parent = [-1]*N
            parent_edge = [None]*N
            q = deque([s])
            parent[s] = s
            while q and parent[t] == -1:
                v = q.popleft()
                for e in dinic.graph[v]:
                    to, cap, rev = e
                    if cap > 0 and parent[to] == -1:
                        parent[to] = v
                        parent_edge[to] = e
                        q.append(to)
            if parent[t] == -1:
                print("NO")
                return
            # Find bottleneck
            f = remaining
            v = t
            while v != s:
                e = parent_edge[v]
                f = min(f, e[1])
                v = parent[v]
            # Apply flow
            v = t
            while v != s:
                e = parent_edge[v]
                e[1] -= f
                e[2][1] += f
                v = parent[v]
            remaining -= f
            # Record flow on chute edges
            # We need to know which chute edge this is.
            # We'll map edge object to chute index.
            # But we didn't store mapping. Let's do it now.
            # We'll store mapping before.
    
    # Actually we need to map each chute edge object to its index.
    # Let's rebuild with mapping.
    
    # Rebuild again with mapping
    dinic = Dinic(N)
    cat_source_edges = []
    cat_sink_edges = []
    for s, t, d in categories:
        e1 = [s, d, None]
        e1_rev = [S, 0, e1]
        e1[2] = e1_rev
        dinic.graph[S].append(e1)
        dinic.graph[s].append(e1_rev)
        cat_source_edges.append(e1)
        
        e2 = [T, d, None]
        e2_rev = [t, 0, e2]
        e2[2] = e2_rev
        dinic.graph[t].append(e2)
        dinic.graph[T].append(e2_rev)
        cat_sink_edges.append(e2)
    
    chute_edge_to_idx = {}
    chute_edges = []
    for i, (u, v, cap) in enumerate(edges):
        e = [v, cap, None]
        e_rev = [u, 0, e]
        e[2] = e_rev
        dinic.graph[u].append(e)
        dinic.graph[v].append(e_rev)
        chute_edges.append(e)
        chute_edge_to_idx[id(e)] = i
    
    flow = dinic.max_flow(S, T)
    if flow != total_demand:
        print("NO")
        return
    
    ans = [[0]*m for _ in range(k)]
    
    for idx, (s, t, d) in enumerate(categories):
        remaining = d
        while remaining > 0:
            parent = [-1]*N
            parent_edge = [None]*N
            q = deque([s])
            parent[s] = s
            while q and parent[t] == -1:
                v = q.popleft()
                for e in dinic.graph[v]:
                    to, cap, rev = e
                    if cap > 0 and parent[to] == -1:
                        parent[to] = v
                        parent_edge[to] = e
                        q.append(to)
            if parent[t] == -1:
                print("NO")
                return
            f = remaining
            v = t
            while v != s:
                e = parent_edge[v]
                f = min(f, e[1])
                v = parent[v]
            v = t
            while v != s:
                e = parent_edge[v]
                e[1] -= f
                e[2][1] += f
                # If this edge is a chute edge, record
                if id(e) in chute_edge_to_idx:
                    ans[idx][chute_edge_to_idx[id(e)]] += f
                v = parent[v]
            remaining -= f
    
    print("YES")
    for row in ans:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    solve()