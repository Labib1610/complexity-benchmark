import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it))
    orders = []
    for _ in range(k):
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        d = int(next(it))
        orders.append((s, t, d))
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        cap = int(next(it))
        edges.append([u, v, cap])

    # Build adjacency for Dinic with edge indices reference
    class Dinic:
        __slots__ = ('n','g','level','it')
        def __init__(self, n):
            self.n = n
            self.g = [[] for _ in range(n)]
        def add_edge(self, fr, to, cap, idx):
            # store idx of original edge for recording flow
            fwd = [to, cap, None, idx]   # to, cap, rev, idx
            rev = [fr, 0, fwd, -1]
            fwd[2] = rev
            self.g[fr].append(fwd)
            self.g[to].append(rev)
        def bfs(self, s, t):
            level = [-1]*self.n
            q = deque([s])
            level[s]=0
            while q:
                v=q.popleft()
                for e in self.g[v]:
                    if e[1]>0 and level[e[0]]<0:
                        level[e[0]]=level[v]+1
                        q.append(e[0])
            self.level=level
            return level[t]>=0
        def dfs(self, v, t, f):
            if v==t:
                return f
            for i in range(self.it[v], len(self.g[v])):
                self.it[v]=i
                e=self.g[v][i]
                if e[1]>0 and self.level[v]<self.level[e[0]]:
                    ret=self.dfs(e[0], t, min(f, e[1]))
                    if ret:
                        e[1]-=ret
                        e[2][1]+=ret
                        return ret
            return 0
        def max_flow(self, s, t):
            flow=0
            INF=10**18
            while self.bfs(s,t):
                self.it=[0]*self.n
                while True:
                    f=self.dfs(s,t,INF)
                    if not f: break
                    flow+=f
            return flow

    # residual capacities per original edge
    residual = [cap for _,_,cap in edges]
    per_order_flow = [[0]*m for _ in range(k)]

    for oi, (src, dst, demand) in enumerate(orders):
        dinic = Dinic(n)
        for idx, (u,v,_) in enumerate(edges):
            if residual[idx]>0:
                dinic.add_edge(u, v, residual[idx], idx)
        sent = dinic.max_flow(src, dst)
        if sent < demand:
            print("NO")
            return
        # we need exactly demand flow; the max flow may exceed demand, but we only need to extract demand.
        # To get exact flows, we run again with capacity limited to demand.
        # Simpler: run with capacity = demand by limiting source edge.
        # Rebuild with capacity = demand on a super source edge.
        # Instead, we can augment only demand amount by limiting total flow.
        # We'll redo with capacity = demand.
        dinic = Dinic(n)
        for idx, (u,v,_) in enumerate(edges):
            cap = residual[idx]
            dinic.add_edge(u, v, cap, idx)
        # add super source/sink trick not needed; just run max flow and stop after demand.
        # modify max_flow to stop when flow reaches demand.
        flow=0
        INF=10**18
        while flow<demand and dinic.bfs(src, dst):
            dinic.it=[0]*n
            while flow<demand:
                f=dinic.dfs(src, dst, demand-flow)
                if not f: break
                flow+=f
        # record flows on original edges
        for u in range(n):
            for e in dinic.g[u]:
                idx = e[3]
                if idx!=-1:
                    used = edges[idx][2] - e[1]  # original cap - remaining
                    per_order_flow[oi][idx] = used
                    residual[idx] -= used
        # after fulfilling demand, residual already updated
    print("YES")
    out_lines = []
    for i in range(k):
        out_lines.append(' '.join(str(per_order_flow[i][j]) for j in range(m)))
    sys.stdout.write('\n'.join(out_lines))

if __name__ == "__main__":
    solve()