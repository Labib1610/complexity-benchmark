import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it))
    comps = []
    for _ in range(k):
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        d = int(next(it))
        comps.append((s, t, d))
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        c = int(next(it))
        edges.append([u, v, c])

    # Build adjacency for Dinic with edge indices
    class Dinic:
        __slots__ = ('n','g','level','it')
        def __init__(self, n):
            self.n = n
            self.g = [[] for _ in range(n)]
        def add_edge(self, fr, to, cap, idx=None):
            f = [to, cap, None]
            b = [fr, 0, f]
            f[2] = b
            self.g[fr].append(f)
            self.g[to].append(b)
            return f  # return forward edge reference
        def bfs(self, s, t):
            level = [-1]*self.n
            q = deque([s])
            level[s]=0
            while q:
                v=q.popleft()
                for to,cap,rev in self.g[v]:
                    if cap and level[to]==-1:
                        level[to]=level[v]+1
                        q.append(to)
            self.level=level
            return level[t]!=-1
        def dfs(self, v, t, f):
            if v==t:
                return f
            for i in range(self.it[v], len(self.g[v])):
                self.it[v]=i
                to,cap,rev=self.g[v][i]
                if cap and self.level[v]+1==self.level[to]:
                    ret=self.dfs(to,t,min(f,cap))
                    if ret:
                        self.g[v][i][1]-=ret
                        rev[1]+=ret
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

    # residual capacities per edge
    residual = [c for _,_,c in edges]
    per_comp_flow = [[0]*m for _ in range(k)]

    for idx, (s,t,d) in enumerate(comps):
        din = Dinic(n)
        edge_refs = []
        for i,(u,v,_) in enumerate(edges):
            cap = residual[i]
            ref = din.add_edge(u, v, cap, i)
            edge_refs.append(ref)
        flow = din.max_flow(s, t)
        if flow < d:
            print("NO")
            return
        # retrieve flow amounts on each original edge
        # run another bfs to push exactly d units and record used edges
        # Simple approach: repeat augmentations until d reached, recording usage
        need = d
        used = [0]*m
        # reuse dinic structure, but we need to know which edges got flow.
        # We'll perform DFS augmentations manually.
        # Since Dinic already sent max flow, we can look at reverse edges to see flow sent.
        for i, ref in enumerate(edge_refs):
            used[i] = edges[i][2] - ref[1]  # original cap - remaining = flow sent
        # If total used > d (because max flow may exceed), we need to trim.
        total_used = sum(used)
        if total_used > d:
            # scale down proportionally (since integer, just reduce arbitrarily)
            excess = total_used - d
            for i in range(m):
                if excess==0: break
                dec = min(used[i], excess)
                used[i] -= dec
                excess -= dec
        # apply
        for i in range(m):
            per_comp_flow[idx][i] = used[i]
            residual[i] -= used[i]
            if residual[i] < 0:
                print("NO")
                return

    print("YES")
    out_lines = []
    for i in range(k):
        out_lines.append(' '.join(str(x) for x in per_comp_flow[i]))
    sys.stdout.write('\n'.join(out_lines))

if __name__ == "__main__":
    solve()