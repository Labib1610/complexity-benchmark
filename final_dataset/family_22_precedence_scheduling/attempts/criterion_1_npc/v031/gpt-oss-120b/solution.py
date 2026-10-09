import sys
sys.setrecursionlimit(1 << 25)

# ---------- Dinic ----------
class Dinic:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]

    def add_edge(self, u, v, cap):
        self.adj[u].append([v, cap, len(self.adj[v])])
        self.adj[v].append([u, 0,   len(self.adj[u]) - 1])

    def bfs_level(self, s, t):
        level = [-1] * self.n
        q = [s]
        level[s] = 0
        for v in q:
            for to, cap, rev in self.adj[v]:
                if cap and level[to] == -1:
                    level[to] = level[v] + 1
                    q.append(to)
        self.level = level
        return level[t] != -1

    def dfs(self, v, t, f):
        if v == t:
            return f
        for i in range(self.it[v], len(self.adj[v])):
            self.it[v] = i
            to, cap, rev = self.adj[v][i]
            if cap and self.level[v] + 1 == self.level[to]:
                ret = self.dfs(to, t, min(f, cap))
                if ret:
                    self.adj[v][i][1] -= ret
                    self.adj[to][rev][1] += ret
                    return ret
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
    n = int(next(it))
    M = int(next(it))
    T = int(next(it))
    m = int(next(it))

    g = [[] for _ in range(n)]
    indeg = [0] * n
    for _ in range(m):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        g[a].append(b)
        indeg[b] += 1

    # topological order
    from collections import deque
    q = deque([i for i in range(n) if indeg[i] == 0])
    topo = []
    while q:
        v = q.popleft()
        topo.append(v)
        for to in g[v]:
            indeg[to] -= 1
            if indeg[to] == 0:
                q.append(to)
    if len(topo) != n:
        print("NO")
        return

    # earliest times
    earliest = [1] * n
    for v in topo:
        ev = earliest[v]
        for to in g[v]:
            if earliest[to] < ev + 1:
                earliest[to] = ev + 1
    if any(e > T for e in earliest):
        print("NO")
        return

    # segment tree over [1, T]
    size = 1
    while size < T:
        size <<= 1
    seg_start = n  # first index of segment tree nodes
    total_nodes = seg_start + 2 * size
    dinic = Dinic(total_nodes + 2)
    SRC = total_nodes
    SNK = total_nodes + 1

    # edges source -> jobs
    for i in range(n):
        dinic.add_edge(SRC, i, 1)

    # build tree edges
    # node indices: seg_start + idx, where idx in [1, 2*size)
    def node(idx):
        return seg_start + idx

    for idx in range(1, size):
        left = idx << 1
        right = left | 1
        dinic.add_edge(node(idx), node(left), 10 ** 9)
        dinic.add_edge(node(idx), node(right), 10 ** 9)

    # leaves to sink with capacity M
    for pos in range(1, T + 1):
        leaf = node(size + pos - 1)
        dinic.add_edge(leaf, SNK, M)

    # connect jobs to segment tree covering [earliest[i], T]
    def add_job_interval(job, l, r, idx, seg_l, seg_r):
        if l > seg_r or r < seg_l:
            return
        if l <= seg_l and seg_r <= r:
            dinic.add_edge(job, node(idx), 1)
            return
        mid = (seg_l + seg_r) // 2
        add_job_interval(job, l, r, idx * 2, seg_l, mid)
        add_job_interval(job, l, r, idx * 2 + 1, mid + 1, seg_r)

    for i in range(n):
        add_job_interval(i, earliest[i], T, 1, 1, size)

    flow = dinic.max_flow(SRC, SNK)
    if flow != n:
        print("NO")
        return

    # retrieve rooms
    room = [0] * n

    # for each job, follow the edge with flow 1 down the tree
    for i in range(n):
        for to, cap, rev in dinic.adj[i]:
            if cap == 0:  # original capacity 1, now used
                cur = to
                # descend until leaf
                while cur < seg_start + size:  # not a leaf
                    # find child with used flow
                    for nxt, c2, rev2 in dinic.adj[cur]:
                        if c2 == 0:  # flow used
                            cur = nxt
                            break
                # leaf corresponds to position
                pos = cur - (seg_start + size) + 1
                room[i] = pos
                break

    print("YES")
    print(' '.join(str(room[i]) for i in range(n)))

if __name__ == "__main__":
    solve()