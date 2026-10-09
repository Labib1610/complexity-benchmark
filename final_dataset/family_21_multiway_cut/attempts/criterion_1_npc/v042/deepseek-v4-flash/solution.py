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
    
    def min_cut(self, s):
        visited = [False] * self.n
        q = deque([s])
        visited[s] = True
        while q:
            u = q.popleft()
            for v, cap, rev in self.adj[u]:
                if cap > 0 and not visited[v]:
                    visited[v] = True
                    q.append(v)
        return visited

def solve():
    n, m, k, B = map(int, input().split())
    terminals = list(map(int, input().split()))
    terminals = [t-1 for t in terminals]
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        edges.append((u, v, w))
    
    if k == 1:
        print("YES")
        print(0)
        return
    
    # Build graph for min cut
    def build_graph():
        dinic = Dinic(n)
        for u, v, w in edges:
            dinic.add_edge(u, v, w)
            dinic.add_edge(v, u, w)
        return dinic
    
    # Recursive multiway cut
    cut_edges = set()
    total_cost = 0
    
    def multiway_cut(term_set):
        nonlocal total_cost
        if len(term_set) <= 1:
            return
        # pick two terminals
        s = term_set[0]
        t = term_set[1]
        dinic = build_graph()
        flow = dinic.max_flow(s, t)
        if flow > B - total_cost:
            return False
        # find min cut edges
        reachable = dinic.min_cut(s)
        # collect cut edges
        cut_now = []
        for idx, (u, v, w) in enumerate(edges):
            if reachable[u] != reachable[v]:
                cut_now.append((u, v, w))
        # add to global cut
        for u, v, w in cut_now:
            cut_edges.add((min(u,v), max(u,v)))
        total_cost += flow
        if total_cost > B:
            return False
        # partition terminals
        left = [x for x in term_set if reachable[x]]
        right = [x for x in term_set if not reachable[x]]
        if not left or not right:
            return False
        return multiway_cut(left) and multiway_cut(right)
    
    if not multiway_cut(terminals):
        print("NO")
        return
    
    if total_cost > B:
        print("NO")
        return
    
    print("YES")
    print(len(cut_edges))
    for u, v in sorted(cut_edges):
        print(u+1, v+1)

if __name__ == "__main__":
    solve()