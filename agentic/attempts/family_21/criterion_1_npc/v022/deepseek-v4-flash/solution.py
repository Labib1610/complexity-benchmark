import sys
from collections import deque

INF = 10**15

class Dinic:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]
    
    def add_edge(self, u, v, cap):
        self.adj[u].append([v, cap, len(self.adj[v])])
        self.adj[v].append([u, 0, len(self.adj[u])-1])
    
    def bfs(self, s, t):
        self.level = [-1]*self.n
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
                if ret > 0:
                    self.adj[u][i][1] -= ret
                    self.adj[v][rev][1] += ret
                    return ret
        return 0
    
    def max_flow(self, s, t):
        flow = 0
        while self.bfs(s, t):
            self.it = [0]*self.n
            while True:
                f = self.dfs(s, t, INF)
                if f == 0:
                    break
                flow += f
        return flow

def gomory_hu(n, edges):
    # edges: list of (u, v, w)
    parent = [0]*n
    capacity = [0]*n
    tree_edges = []
    for s in range(1, n):
        t = parent[s]
        dinic = Dinic(n)
        for u, v, w in edges:
            dinic.add_edge(u, v, w)
            dinic.add_edge(v, u, w)
        flow = dinic.max_flow(s, t)
        # find reachable nodes from s in residual graph
        visited = [False]*n
        q = deque([s])
        visited[s] = True
        while q:
            u = q.popleft()
            for v, cap, rev in dinic.adj[u]:
                if cap > 0 and not visited[v]:
                    visited[v] = True
                    q.append(v)
        # update parent for nodes in visited side
        for i in range(n):
            if i != s and visited[i] and parent[i] == t:
                parent[i] = s
        if visited[parent[t]]:
            parent[s] = parent[t]
            parent[t] = s
            capacity[s] = capacity[t]
            capacity[t] = flow
        else:
            capacity[s] = flow
        tree_edges.append((s, t, flow))
    # build tree adjacency
    tree = [[] for _ in range(n)]
    for u, v, w in tree_edges:
        tree[u].append((v, w))
        tree[v].append((u, w))
    return tree

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    B = int(next(it))
    roots = [int(next(it))-1 for _ in range(k)]
    edges = []
    for _ in range(m):
        u = int(next(it))-1
        v = int(next(it))-1
        w = int(next(it))
        edges.append((u, v, w))
    
    # Build Gomory-Hu tree
    tree = gomory_hu(n, edges)
    
    # Now solve multiway cut on tree
    # Root the tree at 0
    parent = [-1]*n
    children = [[] for _ in range(n)]
    order = [0]
    parent[0] = 0
    for u in order:
        for v, w in tree[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            children[u].append((v, w))
            order.append(v)
    
    # term_mask for each node
    term_mask = [0]*n
    for idx, r in enumerate(roots):
        term_mask[r] |= (1 << idx)
    
    # DP
    # dp[u] = dict mapping mask -> (cost, decisions)
    # decisions: list of edges to cut in subtree
    dp = [None]*n
    
    # process in reverse order
    for u in reversed(order):
        # start with term_mask[u]
        cur = {term_mask[u]: (0, [])}
        for v, w in children[u]:
            new_cur = {}
            for mask_u, (cost_u, cuts_u) in cur.items():
                for mask_v, (cost_v, cuts_v) in dp[v].items():
                    # option 1: cut edge (u,v)
                    if mask_u & mask_v == 0:
                        new_mask = mask_u
                        new_cost = cost_u + cost_v + w
                        new_cuts = cuts_u + cuts_v + [(u, v)]
                        if new_mask not in new_cur or new_cost < new_cur[new_mask][0]:
                            new_cur[new_mask] = (new_cost, new_cuts)
                    # option 2: keep edge (u,v)
                    if mask_u & mask_v == 0:
                        new_mask = mask_u | mask_v
                        new_cost = cost_u + cost_v
                        new_cuts = cuts_u + cuts_v
                        if new_mask not in new_cur or new_cost < new_cur[new_mask][0]:
                            new_cur[new_mask] = (new_cost, new_cuts)
            cur = new_cur
        dp[u] = cur
    
    # find best at root
    best_cost = INF
    best_cuts = None
    for mask, (cost, cuts) in dp[0].items():
        if bin(mask).count('1') <= 1 and cost < best_cost:
            best_cost = cost
            best_cuts = cuts
    
    if best_cost > B:
        print("NO")
    else:
        print("YES")
        print(len(best_cuts))
        for u, v in best_cuts:
            print(u+1, v+1)

if __name__ == "__main__":
    solve()