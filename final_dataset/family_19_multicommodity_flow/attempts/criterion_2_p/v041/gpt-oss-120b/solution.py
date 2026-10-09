import sys
sys.setrecursionlimit(1 << 25)

class Dinic:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]

    def add_edge(self, u, v, c, idx=-1):
        # forward edge
        f = [v, c, None, idx]   # to, cap, rev, idx
        # backward edge
        b = [u, 0, f, -1]
        f[2] = b
        self.adj[u].append(f)
        self.adj[v].append(b)
        return f  # return forward edge reference

    def bfs(self, s, t, level):
        from collections import deque
        q = deque([s])
        level[:] = [-1]*self.n
        level[s] = 0
        while q:
            u = q.popleft()
            for e in self.adj[u]:
                if e[1] > 0 and level[e[0]] == -1:
                    level[e[0]] = level[u] + 1
                    q.append(e[0])
        return level[t] != -1

    def dfs(self, u, t, f, level, it):
        if u == t:
            return f
        for i in range(it[u], len(self.adj[u])):
            it[u] = i
            v, cap, rev, _ = self.adj[u][i]
            if cap > 0 and level[v] == level[u] + 1:
                ret = self.dfs(v, t, min(f, cap), level, it)
                if ret:
                    self.adj[u][i][1] -= ret
                    rev[1] += ret
                    return ret
        return 0

    def max_flow(self, s, t, limit=float('inf')):
        flow = 0
        level = [0]*self.n
        while flow < limit and self.bfs(s, t, level):
            it = [0]*self.n
            while flow < limit:
                pushed = self.dfs(s, t, limit - flow, level, it)
                if not pushed:
                    break
                flow += pushed
        return flow

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); _ = next(it)  # the constant 1, ignored
    s = int(next(it))-1; t = int(next(it))-1; d = int(next(it))
    edges_input = []
    for _ in range(m):
        u = int(next(it))-1; v = int(next(it))-1; cap = int(next(it))
        edges_input.append((u, v, cap))

    dinic = Dinic(n)
    edge_refs = []
    for idx, (u, v, cap) in enumerate(edges_input):
        e = dinic.add_edge(u, v, cap, idx)
        edge_refs.append(e)

    maxf = dinic.max_flow(s, t)
    if maxf < d:
        print("NO")
        return

    # Reduce excess flow if any
    excess = maxf - d
    if excess > 0:
        # send flow from t back to s in residual graph
        dinic.max_flow(t, s, excess)

    # retrieve flows
    res = [0]*m
    for idx, e in enumerate(edge_refs):
        orig_cap = edges_input[idx][2]
        flow = orig_cap - e[1]  # forward edge remaining capacity
        res[idx] = flow

    print("YES")
    print(' '.join(map(str, res)))

if __name__ == "__main__":
    solve()