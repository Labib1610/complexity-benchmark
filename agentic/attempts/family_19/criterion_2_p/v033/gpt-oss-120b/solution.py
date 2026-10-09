import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    _ = next(it)  # the extra '1' in statement, ignore
    s = int(next(it)) - 1
    t = int(next(it)) - 1
    d = int(next(it))

    edges_input = []
    graph = [[] for _ in range(n)]

    class Edge:
        __slots__ = ('to', 'rev', 'cap', 'orig_cap')
        def __init__(self, to, rev, cap):
            self.to = to
            self.rev = rev
            self.cap = cap
            self.orig_cap = cap

    def add_edge(fr, to, cap):
        fwd = Edge(to, len(graph[to]), cap)
        rev = Edge(fr, len(graph[fr]), 0)
        graph[fr].append(fwd)
        graph[to].append(rev)
        return fwd, rev

    # store reference to forward edges for output
    forward_refs = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        cap = int(next(it))
        fwd, rev = add_edge(u, v, cap)
        forward_refs.append(fwd)

    INF = 10**18

    def bfs(level):
        q = deque([s])
        level[s] = 0
        while q:
            v = q.popleft()
            for e in graph[v]:
                if e.cap > 0 and level[e.to] < 0:
                    level[e.to] = level[v] + 1
                    q.append(e.to)
        return level[t] >= 0

    def dfs(v, upTo, level, it_idx):
        if v == t:
            return upTo
        for i in range(it_idx[v], len(graph[v])):
            e = graph[v][i]
            if e.cap > 0 and level[v] + 1 == level[e.to]:
                ret = dfs(e.to, min(upTo, e.cap), level, it_idx)
                if ret:
                    e.cap -= ret
                    graph[e.to][e.rev].cap += ret
                    return ret
            it_idx[v] += 1
        return 0

    flow = 0
    while True:
        level = [-1] * n
        if not bfs(level):
            break
        it_idx = [0] * n
        while True:
            pushed = dfs(s, INF, level, it_idx)
            if not pushed:
                break
            flow += pushed
            if flow >= d:
                break
        if flow >= d:
            break

    if flow < d:
        print("NO")
        return

    # we have possibly more flow than needed; need to adjust to exactly d.
    # Since capacities are integral and we stopped when flow >= d,
    # the excess is flow - d, we can push back along any augmenting path from t to s.
    excess = flow - d
    if excess > 0:
        # Build residual graph for reverse flow
        # We'll repeatedly find a path from s to t with positive flow to reduce.
        # Simpler: run another maxflow from t to s on the current residual with limit excess.
        # Add reverse edge from t to s with capacity excess and try to send excess flow.
        # Actually we can just run a DFS to send excess back.
        def bfs_rev(level):
            q = deque([t])
            level[t] = 0
            while q:
                v = q.popleft()
                for e in graph[v]:
                    # e is forward edge in residual; we need edges with cap>0 that go towards s
                    if e.cap > 0 and level[e.to] < 0:
                        level[e.to] = level[v] + 1
                        q.append(e.to)
            return level[s] >= 0

        def dfs_rev(v, upTo, level, it_idx):
            if v == s:
                return upTo
            for i in range(it_idx[v], len(graph[v])):
                e = graph[v][i]
                if e.cap > 0 and level[v] + 1 == level[e.to]:
                    ret = dfs_rev(e.to, min(upTo, e.cap), level, it_idx)
                    if ret:
                        e.cap -= ret
                        graph[e.to][e.rev].cap += ret
                        return ret
                it_idx[v] += 1
            return 0

        while excess > 0:
            level = [-1] * n
            if not bfs_rev(level):
                break
            it_idx = [0] * n
            while excess > 0:
                pushed = dfs_rev(t, excess, level, it_idx)
                if not pushed:
                    break
                excess -= pushed

    # Now extract flows on original edges
    result = []
    for e in forward_refs:
        used = e.orig_cap - e.cap
        result.append(str(used))

    print("YES")
    print(' '.join(result))

if __name__ == "__main__":
    solve()