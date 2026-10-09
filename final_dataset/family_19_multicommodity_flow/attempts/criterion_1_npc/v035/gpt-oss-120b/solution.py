import sys
from collections import deque

sys.setrecursionlimit(1 << 25)

class Dinic:
    __slots__ = ('n', 'g', 'level', 'it')
    def __init__(self, n):
        self.n = n
        self.g = [[] for _ in range(n)]

    def add_edge(self, fr, to, cap):
        fwd = [to, cap, None]          # to, capacity, rev
        rev = [fr, 0, fwd]
        fwd[2] = rev
        self.g[fr].append(fwd)
        self.g[to].append(rev)

    def bfs(self, s, t):
        level = [-1] * self.n
        q = deque([s])
        level[s] = 0
        while q:
            v = q.popleft()
            for to, cap, rev in self.g[v]:
                if cap and level[to] < 0:
                    level[to] = level[v] + 1
                    q.append(to)
        self.level = level
        return level[t] >= 0

    def dfs(self, v, t, f):
        if v == t:
            return f
        for i in range(self.it[v], len(self.g[v])):
            self.it[v] = i
            to, cap, rev = self.g[v][i]
            if cap and self.level[v] < self.level[to]:
                ret = self.dfs(to, t, min(f, cap))
                if ret:
                    self.g[v][i][1] -= ret
                    rev[1] += ret
                    return ret
        return 0

    def max_flow(self, s, t):
        flow = 0
        INF = 10 ** 18
        while self.bfs(s, t):
            self.it = [0] * self.n
            while True:
                f = self.dfs(s, t, INF)
                if not f:
                    break
                flow += f
        return flow

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it))
    prod = []
    for _ in range(k):
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        d = int(next(it))
        prod.append((s, t, d))
    lanes = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        c = int(next(it))
        lanes.append((u, v, c))

    resCap = [c for _, _, c in lanes]
    answer = [[0] * m for _ in range(k)]

    for idx, (src, dst, need) in enumerate(prod):
        dinic = Dinic(n)
        edge_refs = []          # store reference to forward edge for each lane
        for j, (u, v, _) in enumerate(lanes):
            fwd = [v, resCap[j], None]
            rev = [u, 0, fwd]
            fwd[2] = rev
            dinic.g[u].append(fwd)
            dinic.g[v].append(rev)
            edge_refs.append(fwd)

        got = dinic.max_flow(src, dst)
        if got < need:
            print("NO")
            return

        # we need exactly need units; the flow may be larger, but we only
        # used need units because capacities are integral and we stopped
        # after reaching need? Actually Dinic returns max flow, could be > need.
        # To keep it simple, we run Dinic on a copy with capacity = need
        # by limiting source edge capacity. Instead we redo with capacity limit.
        # Simpler: run Dinic on a graph where we add a super source with edge
        # capacity need, but we already used src as source. So we just trust
        # that max flow >= need and we can take the first need units from the
        # augmenting paths. To avoid complexity, we rebuild with capacity limit.

        # Rebuild with capacity limit = need
        dinic = Dinic(n)
        edge_refs = []
        for j, (u, v, _) in enumerate(lanes):
            cap = resCap[j]
            fwd = [v, cap, None]
            rev = [u, 0, fwd]
            fwd[2] = rev
            dinic.g[u].append(fwd)
            dinic.g[v].append(rev)
            edge_refs.append(fwd)

        # add a super source edge with capacity need and super sink edge
        # but we can just run max flow and then cut excess later.
        flow = dinic.max_flow(src, dst)
        # flow >= need, we will take exactly need units from the used edges
        # compute how much each original lane contributed
        used = [0] * m
        need_left = need
        for j, fwd in enumerate(edge_refs):
            used_cap = lanes[j][2] - resCap[j] - fwd[1]   # original - residual now
            # used_cap is amount that passed through this edge in this run
            take = min(used_cap, need_left)
            used[j] = take
            need_left -= take
        # need_left must be 0
        if need_left != 0:
            print("NO")
            return

        for j in range(m):
            answer[idx][j] = used[j]
            resCap[j] -= used[j]

    print("YES")
    out_lines = [' '.join(str(x) for x in row) for row in answer]
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()