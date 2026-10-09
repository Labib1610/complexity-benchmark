import sys
sys.setrecursionlimit(1 << 25)

# ---------- Dinic ----------
class Edge:
    __slots__ = ('to', 'rev', 'cap')
    def __init__(self, to, rev, cap):
        self.to = to
        self.rev = rev
        self.cap = cap

class Dinic:
    def __init__(self, n):
        self.n = n
        self.g = [[] for _ in range(n)]

    def add_edge(self, fr, to, cap):
        f = Edge(to, len(self.g[to]), cap)
        b = Edge(fr, len(self.g[fr]), 0)
        self.g[fr].append(f)
        self.g[to].append(b)

    def bfs_level(self, s, t):
        level = [-1] * self.n
        q = [s]
        level[s] = 0
        for v in q:
            for e in self.g[v]:
                if e.cap and level[e.to] < 0:
                    level[e.to] = level[v] + 1
                    q.append(e.to)
        self.level = level
        return level[t] >= 0

    def dfs(self, v, t, f):
        if v == t:
            return f
        for i in range(self.it[v], len(self.g[v])):
            e = self.g[v][i]
            if e.cap and self.level[v] < self.level[e.to]:
                ret = self.dfs(e.to, t, min(f, e.cap))
                if ret:
                    e.cap -= ret
                    self.g[e.to][e.rev].cap += ret
                    return ret
            self.it[v] += 1
        return 0

    def max_flow(self, s, t):
        flow = 0
        INF = 10 ** 18
        while self.bfs_level(s, t):
            self.it = [0] * self.n
            while True:
                f = self.dfs(s, t, INF)
                if not f:
                    break
                flow += f
        return flow

# ---------- main ----------
def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); M = int(next(it)); T = int(next(it)); m = int(next(it))
    adj = [[] for _ in range(n)]
    radj = [[] for _ in range(n)]
    indeg = [0]*n
    for _ in range(m):
        a = int(next(it))-1
        b = int(next(it))-1
        adj[a].append(b)
        radj[b].append(a)
        indeg[b] += 1

    # topological order
    from collections import deque
    q = deque([i for i in range(n) if indeg[i]==0])
    topo = []
    while q:
        v = q.popleft()
        topo.append(v)
        for to in adj[v]:
            indeg[to] -= 1
            if indeg[to]==0:
                q.append(to)
    if len(topo)!=n:
        print("NO")
        return

    earliest = [1]*n
    for v in topo:
        for to in adj[v]:
            if earliest[to] < earliest[v] + 1:
                earliest[to] = earliest[v] + 1

    latest = [T]*n
    for v in reversed(topo):
        for pre in radj[v]:
            if latest[pre] > latest[v] - 1:
                latest[pre] = latest[v] - 1

    for i in range(n):
        if earliest[i] > latest[i]:
            print("NO")
            return

    # segment tree nodes
    # we will number nodes:
    # 0 ... n-1          : operation vertices
    # n ... n+seg_cnt-1  : segment tree internal + leaves
    # last two nodes: source, sink
    seg_offset = n
    # build segment tree
    size = 1
    while size < T:
        size <<= 1
    seg_cnt = 2*size
    total_nodes = n + seg_cnt + 2
    SRC = total_nodes - 2
    SNK = total_nodes - 1
    dinic = Dinic(total_nodes)

    # edges source -> operation
    for v in range(n):
        dinic.add_edge(SRC, v, 1)

    # leaf to sink (capacity M)
    for leaf in range(size, size+T):
        dinic.add_edge(seg_offset + leaf, SNK, M)

    INF = 10**9
    # internal edges (parent -> child) infinite capacity
    for node in range(1, size):
        dinic.add_edge(seg_offset + node, seg_offset + node*2, INF)
        dinic.add_edge(seg_offset + node, seg_offset + node*2+1, INF)

    # helper to add edges from operation to interval [l,r] (1‑based)
    def add_interval(v, l, r):
        l += size-1
        r += size-1
        while l <= r:
            if l & 1:
                dinic.add_edge(v, seg_offset + l, 1)
                l += 1
            if not (r & 1):
                dinic.add_edge(v, seg_offset + r, 1)
                r -= 1
            l >>= 1
            r >>= 1

    for v in range(n):
        add_interval(v, earliest[v], latest[v])

    flow = dinic.max_flow(SRC, SNK)
    if flow != n:
        print("NO")
        return

    # retrieve assignment
    ans = [0]*n
    for v in range(n):
        for e in dinic.g[v]:
            if e.to >= seg_offset and e.cap == 0:   # used edge
                node = e.to - seg_offset
                # go down to leaf
                while node < size:
                    # which child has flow?
                    left = node*2
                    right = left+1
                    # check edges from current node
                    for ee in dinic.g[seg_offset + node]:
                        if ee.to == seg_offset + left and ee.cap == 0:
                            node = left
                            break
                        if ee.to == seg_offset + right and ee.cap == 0:
                            node = right
                            break
                    else:
                        # should not happen
                        break
                # leaf index to time
                time = node - size + 1
                ans[v] = time
                break

    print("YES")
    print(' '.join(map(str, ans)))

if __name__ == "__main__":
    solve()