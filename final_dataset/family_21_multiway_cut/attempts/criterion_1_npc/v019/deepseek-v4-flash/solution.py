import sys
from collections import deque

input = sys.stdin.readline

class Dinic:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
    
    def add_edge(self, u, v, cap):
        self.graph[u].append([v, cap, len(self.graph[v])])
        self.graph[v].append([u, 0, len(self.graph[u]) - 1])
    
    def bfs(self, s, t):
        self.level = [-1] * self.n
        q = deque([s])
        self.level[s] = 0
        while q:
            u = q.popleft()
            for v, cap, rev in self.graph[u]:
                if cap > 0 and self.level[v] < 0:
                    self.level[v] = self.level[u] + 1
                    q.append(v)
        return self.level[t] >= 0
    
    def dfs(self, u, t, f):
        if u == t:
            return f
        for i in range(self.it[u], len(self.graph[u])):
            self.it[u] = i
            v, cap, rev = self.graph[u][i]
            if cap > 0 and self.level[u] + 1 == self.level[v]:
                ret = self.dfs(v, t, min(f, cap))
                if ret > 0:
                    self.graph[u][i][1] -= ret
                    self.graph[v][rev][1] += ret
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
    n, m, k, B = map(int, input().split())
    anchors = list(map(int, input().split()))
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((u-1, v-1, w))
    
    # If k <= 1, no need to cut anything
    if k <= 1:
        print("YES")
        print(0)
        return
    
    # Try all partitions of anchors into two non-empty sets
    # For each partition, compute min cut between the two groups
    # Combine cuts to separate all anchors
    best_cut = None
    best_cost = float('inf')
    
    # We'll use a simple approach: for each pair of anchors, compute min cut
    # Then take union of cuts for all pairs? That might be too large.
    # Instead, we try all ways to separate anchors into two groups and take min cut.
    
    # Since k is small (likely <= 5 or so), we can try all 2^(k-1) partitions
    import itertools
    anchors_idx = list(range(k))
    for mask in range(1, (1 << (k-1))):
        groupA = []
        groupB = []
        for i in range(k):
            if mask & (1 << i):
                groupA.append(anchors[i])
            else:
                groupB.append(anchors[i])
        if not groupA or not groupB:
            continue
        
        # Build flow network with super source and sink
        dinic = Dinic(n + 2)
        s = n
        t = n + 1
        for u, v, w in edges:
            dinic.add_edge(u, v, w)
            dinic.add_edge(v, u, w)
        for a in groupA:
            dinic.add_edge(s, a-1, 10**18)
        for b in groupB:
            dinic.add_edge(b-1, t, 10**18)
        
        flow = dinic.max_flow(s, t)
        if flow < best_cost:
            best_cost = flow
            # Find cut edges
            visited = [False] * (n+2)
            q = deque([s])
            visited[s] = True
            while q:
                u = q.popleft()
                for v, cap, rev in dinic.graph[u]:
                    if cap > 0 and not visited[v]:
                        visited[v] = True
                        q.append(v)
            cut_edges = []
            for u, v, w in edges:
                if visited[u] and not visited[v]:
                    cut_edges.append((u+1, v+1))
                elif visited[v] and not visited[u]:
                    cut_edges.append((u+1, v+1))
            best_cut = cut_edges
    
    if best_cost <= B:
        print("YES")
        print(len(best_cut))
        for u, v in best_cut:
            print(u, v)
    else:
        print("NO")

if __name__ == "__main__":
    solve()