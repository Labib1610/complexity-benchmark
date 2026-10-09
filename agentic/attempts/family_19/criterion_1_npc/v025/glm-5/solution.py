import sys
from collections import deque
import random

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    k = int(input_data[idx]); idx += 1
    
    rituals = []
    for i in range(k):
        s = int(input_data[idx]) - 1; idx += 1
        t = int(input_data[idx]) - 1; idx += 1
        d = int(input_data[idx]); idx += 1
        rituals.append((s, t, d))
    
    edges = []
    for i in range(m):
        u = int(input_data[idx]) - 1; idx += 1
        v = int(input_data[idx]) - 1; idx += 1
        cap = int(input_data[idx]); idx += 1
        edges.append((u, v, cap))
    
    # Greedy multi-commodity flow using Dinic's
    # Try multiple orderings
    
    class Dinic:
        def __init__(self, n, edges, caps):
            self.n = n
            self.graph = [[] for _ in range(n)]
            self.caps = list(caps)
            for i, (u, v, _) in enumerate(edges):
                self.graph[u].append([v, self.caps[i], i])
                self.graph[v].append([u, 0, -1])  # reverse edge
        
        def bfs(self, s, t):
            self.level = [-1] * self.n
            self.level[s] = 0
            q = deque([s])
            while q:
                u = q.popleft()
                for e in self.graph[u]:
                    v, cap, _ = e
                    if cap > 0 and self.level[v] < 0:
                        self.level[v] = self.level[u] + 1
                        q.append(v)
            return self.level[t] >= 0
        
        def dfs(self, u, t, f):
            if u == t:
                return f
            while self.it[u] < len(self.graph[u]):
                e = self.graph[u][self.it[u]]
                v, cap, eid = e
                if cap > 0 and self.level[v] == self.level[u] + 1:
                    d = self.dfs(v, t, min(f, cap))
                    if d > 0:
                        e[1] -= d
                        # find reverse edge
                        for re in self.graph[v]:
                            if re[2] == -1 and re[0] == u:
                                re[1] += d
                                break
                        return d
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
        
        def get_edge_flows(self, edges):
            result = [0] * len(edges)
            for u in range(self.n):
                for e in self.graph[u]:
                    v, cap, eid = e
                    if eid >= 0:
                        result[eid] = self.caps[eid] - cap
            return result
    
    best_result = None
    
    orderings = [list(range(k))]
    # Try reverse order
    orderings.append(list(range(k))[::-1])
    # Try some random orderings
    for _ in range(20):
        perm = list(range(k))
        random.shuffle(perm)
        orderings.append(perm)
    
    for order in orderings:
        caps = [e[2] for e in edges]
        dinic = Dinic(n, edges, caps)
        all_flows = [[0] * m for _ in range(k)]
        success = True
        
        for ri in order:
            s, t, d = rituals[ri]
            if s == t:
                if d != 0:
                    success = False
                continue
            flow = dinic.max_flow(s, t)
            if flow < d:
                success = False
                break
            # Get the flow on each edge for this commodity
            edge_flows = dinic.get_edge_flows(edges)
            for i in range(m):
                all_flows[ri][i] = edge_flows[i]
                # Reduce capacity
                dinic.caps[i] -= edge_flows[i]
            # Rebuild graph with updated caps
            dinic = Dinic(n, edges, dinic.caps)
        
        if success:
            # Verify
            valid = True
            for i in range(m):
                total = sum(all_flows[j][i] for j in range(k))
                if total > edges[i][2]:
                    valid = False
                    break
            if valid:
                # Check flow conservation
                for ri in range(k):
                    s, t, d = rituals[ri]
                    net = [0] * n
                    for i in range(m):
                        u, v, _ = edges[i]
                        net[u] -= all_flows[ri][i]
                        net[v] += all_flows[ri][i]
                    if net[s] != -d or net[t] != d:
                        valid = False
                        break
                    for j in range(n):
                        if j != s and j != t and net[j] != 0:
                            valid = False
                            break
                if valid:
                    best_result = all_flows
                    break
    
    if best_result is not None:
        print("YES")
        for row in best_result:
            print(' '.join(map(str, row)))
    else:
        print("NO")

solve()