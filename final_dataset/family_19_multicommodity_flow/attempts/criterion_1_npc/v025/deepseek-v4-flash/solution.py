import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    rituals = []
    for _ in range(k):
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        d = int(next(it))
        rituals.append((s, t, d))
    
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        cap = int(next(it))
        edges.append((u, v, cap))
    
    # We'll keep residual capacities for each edge
    residual = [cap for _ in range(m)]
    
    # Store flows per ritual
    flows = [[0]*m for _ in range(k)]
    
    # For each ritual, run max flow with current residual capacities
    for idx, (s, t, d) in enumerate(rituals):
        # Build adjacency list for this ritual's flow
        adj = [[] for _ in range(n)]
        for eid, (u, v, cap) in enumerate(edges):
            if residual[eid] > 0:
                adj[u].append((v, eid, residual[eid]))
                adj[v].append((u, eid, 0))  # reverse edge with 0 capacity initially
        
        # We'll use Edmonds-Karp (BFS) for simplicity
        total_flow = 0
        while total_flow < d:
            # BFS to find augmenting path
            parent = [-1]*n
            parent_edge = [-1]*n
            q = deque([s])
            parent[s] = s
            found = False
            while q and not found:
                u = q.popleft()
                for v, eid, cap in adj[u]:
                    if parent[v] == -1 and cap > 0:
                        parent[v] = u
                        parent_edge[v] = eid
                        if v == t:
                            found = True
                            break
                        q.append(v)
            if not found:
                break
            # Find bottleneck
            v = t
            path_edges = []
            while v != s:
                eid = parent_edge[v]
                path_edges.append(eid)
                v = parent[v]
            # Bottleneck is min residual along path
            bottleneck = d - total_flow
            for eid in path_edges:
                # Need to know direction: find edge in adj
                # We'll just recompute by scanning
                pass
            # Simpler: we'll store edges with direction info
            # Let's rebuild with direction
            # Actually easier: store adjacency with (v, eid, cap, direction)
            # But for simplicity, we'll just do a direct BFS with residual matrix
            # Let's redo with residual matrix approach
        
        # Since above is messy, let's implement properly with residual matrix
        # We'll use a standard max flow with adjacency list of (to, rev, cap)
        # But we need to map edge ids to residual capacities
        
        # Let's implement Dinic for speed
        class Dinic:
            def __init__(self, N):
                self.N = N
                self.graph = [[] for _ in range(N)]
            
            def add_edge(self, fr, to, cap, eid):
                forward = [to, cap, eid, None]
                backward = [fr, 0, eid, None]
                forward[3] = backward
                backward[3] = forward
                self.graph[fr].append(forward)
                self.graph[to].append(backward)
            
            def bfs(self, s, t):
                level = [-1]*self.N
                q = deque([s])
                level[s] = 0
                while q:
                    v = q.popleft()
                    for to, cap, eid, rev in self.graph[v]:
                        if cap > 0 and level[to] < 0:
                            level[to] = level[v] + 1
                            q.append(to)
                self.level = level
                return level[t] >= 0
            
            def dfs(self, v, t, f):
                if v == t:
                    return f
                for i in range(self.it[v], len(self.graph[v])):
                    self.it[v] = i
                    to, cap, eid, rev = self.graph[v][i]
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
                    self.it = [0]*self.N
                    while True:
                        f = self.dfs(s, t, INF)
                        if f == 0:
                            break
                        flow += f
                return flow
        
        dinic = Dinic(n)
        for eid, (u, v, cap) in enumerate(edges):
            if residual[eid] > 0:
                dinic.add_edge(u, v, residual[eid], eid)
        
        # Run max flow
        f = dinic.max_flow(s, t)
        if f < d:
            print("NO")
            return
        
        # Now we need to extract the flow per edge for this ritual
        # We can look at the residual graph: original cap - residual cap = flow
        # But we need to map back to edge ids
        # We'll store flow on each edge by checking the forward edges
        for u in range(n):
            for to, cap, eid, rev in dinic.graph[u]:
                # cap is residual capacity after flow
                # original capacity was residual[eid] before this ritual
                # flow = original - cap
                # But we need to know direction: if u is the source of the original edge
                # We'll check if u == edges[eid][0]
                if u == edges[eid][0]:
                    flow_used = residual[eid] - cap
                    flows[idx][eid] = flow_used
                    residual[eid] = cap  # update residual for next rituals
                # else it's reverse edge, ignore
        
        # Actually the above might double count; better: after max flow, for each edge,
        # flow = original_cap - residual_cap (where residual_cap is in the forward edge)
        # We'll just compute from the graph
        
        # Let's do it cleanly:
        for eid, (u, v, cap) in enumerate(edges):
            # Find forward edge in dinic graph from u to v
            for to, cap_res, eid2, rev in dinic.graph[u]:
                if to == v and eid2 == eid:
                    flow_used = residual[eid] - cap_res
                    flows[idx][eid] = flow_used
                    residual[eid] = cap_res
                    break
    
    # If we got here, all rituals can be satisfied
    print("YES")
    for i in range(k):
        print(" ".join(str(flows[i][j]) for j in range(m)))

if __name__ == "__main__":
    solve()