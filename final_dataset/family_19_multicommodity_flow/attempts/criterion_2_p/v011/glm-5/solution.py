import sys
from collections import deque

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    _ = int(next(it))  # egg type, always 1
    s = int(next(it))
    t = int(next(it))
    d = int(next(it))

    edges = []
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        u = int(next(it))
        v = int(next(it))
        cap = int(next(it))
        edges.append((u, v, cap))
        adj[u].append(i)
        adj[v].append(i)

    # Build flow network with edge indices
    # We'll use Dinic's algorithm
    # Edge storage: to, rev, cap, flow, id
    
    class Edge:
        __slots__ = ('to', 'rev', 'cap', 'flow', 'id')
        def __init__(self, to, rev, cap, id):
            self.to = to
            self.rev = rev
            self.cap = cap
            self.flow = 0
            self.id = id

    graph = [[] for _ in range(n + 1)]
    for idx, (u, v, cap) in enumerate(edges):
        # Forward edge
        fwd = Edge(v, len(graph[v]), cap, idx)
        # Backward edge
        rev = Edge(u, len(graph[u]), 0, idx)
        graph[u].append(fwd)
        graph[v].append(rev)

    level = [0] * (n + 1)
    ptr = [0] * (n + 1)

    def bfs():
        for i in range(1, n + 1):
            level[i] = -1
        level[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for e in graph[u]:
                if e.cap - e.flow > 0 and level[e.to] < 0:
                    level[e.to] = level[u] + 1
                    q.append(e.to)
        return level[t] >= 0

    def dfs(u, f):
        if u == t:
            return f
        for i in range(ptr[u], len(graph[u])):
            e = graph[u][i]
            if e.cap - e.flow > 0 and level[e.to] == level[u] + 1:
                pushed = dfs(e.to, min(f, e.cap - e.flow))
                if pushed > 0:
                    e.flow += pushed
                    graph[e.to][e.rev].flow -= pushed
                    return pushed
            ptr[u] += 1
        return 0

    flow = 0
    while flow < d and bfs():
        ptr = [0] * (n + 1)
        while True:
            pushed = dfs(s, d - flow)
            if pushed == 0:
                break
            flow += pushed
            if flow >= d:
                break

    if flow < d:
        print("NO")
        return

    # Extract flows for original edges
    ans = [0] * m
    for u in range(1, n + 1):
        for e in graph[u]:
            if e.id >= 0 and e.cap > 0:  # Original forward edge
                ans[e.id] = e.flow

    print("YES")
    print(' '.join(map(str, ans)))

if __name__ == "__main__":
    solve()