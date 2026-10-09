import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    # possible extra number on the first line, ignore if present
    # peek next token: if remaining tokens count matches expected, we assume it's part of first line
    # but safest: if there are more than 2 + 3*m tokens, treat next as extra and skip
    # however problem statement suggests a stray '1', we just ignore any non‑edge token before s t d
    # We'll read s,t,d next.
    s = int(next(it))
    t = int(next(it))
    d = int(next(it))

    # store edges
    edges_input = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        edges_input.append((u, v, w))

    # Dinic implementation
    class Edge:
        __slots__ = ('to', 'rev', 'cap', 'orig_cap')
        def __init__(self, to, rev, cap):
            self.to = to
            self.rev = rev
            self.cap = cap
            self.orig_cap = cap

    graph = [[] for _ in range(n)]

    # keep reference to forward edges for output
    forward_refs = []

    def add_edge(fr, to, cap):
        fwd = Edge(to, len(graph[to]), cap)
        rev = Edge(fr, len(graph[fr]), 0)
        graph[fr].append(fwd)
        graph[to].append(rev)
        return fwd

    for u, v, w in edges_input:
        fwd = add_edge(u, v, w)
        forward_refs.append(fwd)

    INF = 10**18

    level = [0]*n
    it_ptr = [0]*n

    def bfs():
        for i in range(n):
            level[i] = -1
        q = deque()
        level[s] = 0
        q.append(s)
        while q:
            v = q.popleft()
            for e in graph[v]:
                if e.cap > 0 and level[e.to] < 0:
                    level[e.to] = level[v] + 1
                    q.append(e.to)
        return level[t] >= 0

    def dfs(v, f):
        if v == t:
            return f
        for i in range(it_ptr[v], len(graph[v])):
            e = graph[v][i]
            if e.cap > 0 and level[v] < level[e.to]:
                ret = dfs(e.to, min(f, e.cap))
                if ret:
                    e.cap -= ret
                    graph[e.to][e.rev].cap += ret
                    return ret
            it_ptr[v] += 1
        return 0

    flow = 0
    while flow < d and bfs():
        it_ptr = [0]*n
        while flow < d:
            pushed = dfs(s, d - flow)
            if not pushed:
                break
            flow += pushed

    if flow < d:
        print("NO")
        return

    # construct answer flows per original edge order
    ans = []
    for e in forward_refs:
        used = e.orig_cap - e.cap
        ans.append(str(used))

    print("YES")
    print(' '.join(ans))

if __name__ == "__main__":
    solve()