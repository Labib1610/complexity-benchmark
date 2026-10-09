import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); _ = int(next(it))  # the third number is always 1, ignore
    s = int(next(it)) - 1
    t = int(next(it)) - 1
    d = int(next(it))
    edges_input = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        cap = int(next(it))
        edges_input.append((u, v, cap))

    # Dinic
    N = n
    adj = [[] for _ in range(N)]

    class Edge:
        __slots__ = ('to', 'rev', 'cap', 'orig_idx')
        def __init__(self, to, rev, cap, orig_idx=-1):
            self.to = to
            self.rev = rev
            self.cap = cap
            self.orig_idx = orig_idx

    def add_edge(fr, to, cap, orig_idx=-1):
        fwd = Edge(to, len(adj[to]), cap, orig_idx)
        rev = Edge(fr, len(adj[fr]), 0)
        adj[fr].append(fwd)
        adj[to].append(rev)

    # add original edges, remember index
    for idx, (u, v, cap) in enumerate(edges_input):
        add_edge(u, v, cap, idx)

    level = [0]*N
    it_ptr = [0]*N

    from collections import deque
    def bfs():
        for i in range(N):
            level[i] = -1
        q = deque()
        level[s] = 0
        q.append(s)
        while q:
            v = q.popleft()
            for e in adj[v]:
                if e.cap and level[e.to] < 0:
                    level[e.to] = level[v] + 1
                    q.append(e.to)
        return level[t] >= 0

    def dfs(v, f):
        if v == t:
            return f
        for i in range(it_ptr[v], len(adj[v])):
            e = adj[v][i]
            if e.cap and level[v] < level[e.to]:
                ret = dfs(e.to, min(f, e.cap))
                if ret:
                    e.cap -= ret
                    adj[e.to][e.rev].cap += ret
                    return ret
            it_ptr[v] += 1
        return 0

    flow = 0
    while flow < d and bfs():
        it_ptr = [0]*N
        while flow < d:
            pushed = dfs(s, d - flow)
            if not pushed:
                break
            flow += pushed

    if flow < d:
        print("NO")
        return

    # retrieve flows on original edges
    result = [0]*m
    for u in range(N):
        for e in adj[u]:
            if e.orig_idx != -1:
                # original forward edge: flow = original capacity - remaining capacity
                # we need original capacity, which is stored as (remaining + reverse cap)
                rev_edge = adj[e.to][e.rev]
                used = rev_edge.cap  # amount sent forward
                result[e.orig_idx] = used

    print("YES")
    print(' '.join(str(x) for x in result))

if __name__ == "__main__":
    solve()