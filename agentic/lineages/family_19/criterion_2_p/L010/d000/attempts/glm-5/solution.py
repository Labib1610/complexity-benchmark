import sys

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    _ = int(data[idx]); idx += 1  # product type, always 1

    s = int(data[idx]); idx += 1
    t = int(data[idx]); idx += 1
    d = int(data[idx]); idx += 1

    edges = []
    for _ in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        c = int(data[idx]); idx += 1
        edges.append((u, v, c))

    # Build graph for max flow
    # Nodes: 1..n
    # We'll use Dinic's algorithm

    class Dinic:
        def __init__(self, n):
            self.n = n
            self.graph = [[] for _ in range(n + 1)]

        def add_edge(self, u, v, cap):
            self.graph[u].append([v, cap, len(self.graph[v])])
            self.graph[v].append([u, 0, len(self.graph[u]) - 1])

        def bfs(self, s, t):
            self.level = [-1] * (self.n + 1)
            self.level[s] = 0
            q = [s]
            head = 0
            while head < len(q):
                u = q[head]; head += 1
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
                v, cap, rev = e
                if cap > 0 and self.level[v] == self.level[u] + 1:
                    ret = self.dfs(v, t, min(f, cap))
                    if ret > 0:
                        self.graph[u][self.it[u]][1] -= ret
                        self.graph[v][rev][1] += ret
                        return ret
                self.it[u] += 1
            return 0

        def max_flow(self, s, t):
            flow = 0
            while self.bfs(s, t):
                self.it = [0] * (self.n + 1)
                while True:
                    f = self.dfs(s, t, float('inf'))
                    if f == 0:
                        break
                    flow += f
            return flow

    dinic = Dinic(n)
    for u, v, c in edges:
        dinic.add_edge(u, v, c)

    flow = dinic.max_flow(s, t)

    if flow < d:
        print("NO")
        return

    # Extract flow values
    # For each original edge, the flow is cap - remaining cap
    # We stored edges in order; need to track which graph edges correspond
    # Rebuild to extract
    # Actually we can track: when we added edge i, it was added to graph[u] at some position
    # Let's redo with tracking

    # Rebuild with tracking
    dinic2 = Dinic(n)
    edge_indices = []
    for u, v, c in edges:
        pos = len(dinic2.graph[u])
        dinic2.add_edge(u, v, c)
        edge_indices.append(pos)

    dinic2.max_flow(s, t)

    result = []
    for i, (u, v, c) in enumerate(edges):
        pos = edge_indices[i]
        # The edge is dinic2.graph[u][pos], original cap was c
        # remaining cap is dinic2.graph[u][pos][1]
        remaining = dinic2.graph[u][pos][1]
        flow_val = c - remaining
        result.append(flow_val)

    # Verify: net out of s should be >= d, but we need exactly d
    # If flow > d, we need to reduce some flows
    # Actually the problem says "exactly equal to d"
    # Max flow gives us flow >= d, we need to reduce to exactly d

    if flow > d:
        # Need to reduce flow by (flow - d)
        # We can do a DFS from s to t along edges with positive flow and reduce
        excess = flow - d

        # Build residual-like graph using current flow assignment
        # We'll reduce flow along s-t paths
        # Use the flow values in result[]

        # Build adjacency: for each edge with flow > 0, we can reduce it
        adj = [[] for _ in range(n + 1)]
        for i, (u, v, c) in enumerate(edges):
            if result[i] > 0:
                adj[u].append((v, i))  # can push flow reduction forward

        # Actually reducing flow on edge u->v means we send less from u to v
        # This is like finding paths from s to t in the flow graph and reducing

        # We need to reduce total out-flow from s by 'excess'
        # Find augmenting paths in reverse? No.
        # Reducing flow on a path s->...->t by delta reduces net flow by delta

        # DFS to find paths and reduce
        def find_and_reduce(u, t, delta):
            if u == t:
                return delta
            for j in range(len(adj[u])):
                v, ei = adj[u][j]
                if result[ei] > 0:
                    reduce = min(delta, result[ei])
                    ret = find_and_reduce(v, t, reduce)
                    if ret > 0:
                        result[ei] -= ret
                        return ret
            return 0

        remaining_excess = excess
        while remaining_excess > 0:
            reduced = find_and_reduce(s, t, remaining_excess)
            if reduced == 0:
                break
            remaining_excess -= reduced

    print("YES")
    print(' '.join(map(str, result)))

solve()