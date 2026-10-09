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
        q = deque([s])
        level[s] = 0
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

def min_cut_edges(n, edges, s, t):
    mf = MaxFlow(n)
    for u, v, w in edges:
        mf.add_edge(u, v, w)
        mf.add_edge(v, u, w)
    flow = mf.max_flow(s, t)
    # find reachable from s in residual graph
    visited = [False] * n
    q = deque([s])
    visited[s] = True
    while q:
        u = q.popleft()
        for v, cap, rev in mf.adj[u]:
            if cap > 0 and not visited[v]:
                visited[v] = True
                q.append(v)
    cut_edges = []
    for u, v, w in edges:
        if visited[u] != visited[v]:
            cut_edges.append((u, v))
    return flow, cut_edges

def solve():
    n, m, k, B = map(int, input().split())
    hubs = list(map(int, input().split()))
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((u-1, v-1, w))
    
    if k == 1:
        print("YES")
        print(0)
        return
    
    # Build Gomory-Hu tree
    # We'll compute min-cut between all pairs of hubs
    # But for simplicity, we can just try to find a cut that separates all hubs
    # using a greedy approach: for each hub, find min cut to the rest.
    
    # We'll use a simple approach: try to find a cut that separates all hubs
    # by using a minimum spanning tree on hubs with weights = min-cut between them.
    
    # Compute min-cut between each pair of hubs
    hub_set = set(hubs)
    hub_list = hubs
    k = len(hub_list)
    mincut = [[0]*k for _ in range(k)]
    cut_edges_between = [[None]*k for _ in range(k)]
    
    for i in range(k):
        for j in range(i+1, k):
            flow, ce = min_cut_edges(n, edges, hub_list[i]-1, hub_list[j]-1)
            mincut[i][j] = mincut[j][i] = flow
            cut_edges_between[i][j] = cut_edges_between[j][i] = ce
    
    # Build MST on hubs using mincut as weights
    parent = list(range(k))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(x, y):
        rx, ry = find(x), find(y)
        if rx != ry:
            parent[ry] = rx
    
    edges_mst = []
    for i in range(k):
        for j in range(i+1, k):
            edges_mst.append((mincut[i][j], i, j))
    edges_mst.sort()
    
    mst_edges = []
    total_cost = 0
    for w, i, j in edges_mst:
        if find(i) != find(j):
            union(i, j)
            mst_edges.append((i, j))
            total_cost += w
    
    if total_cost > B:
        print("NO")
        return
    
    # Collect all cut edges from MST
    chosen_edges = set()
    for i, j in mst_edges:
        for u, v in cut_edges_between[i][j]:
            chosen_edges.add((min(u,v), max(u,v)))
    
    print("YES")
    print(len(chosen_edges))
    for u, v in chosen_edges:
        print(u+1, v+1)

if __name__ == "__main__":
    solve()